from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"   # required for session

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqltanya123",
    database="prepai"
)

cursor = db.cursor()

import google.generativeai as genai

genai.configure(api_key="AIzaSyBg8oZB66gOd1-Ja1jK6kYJaOLyA70oHRI")

model = genai.GenerativeModel("models/gemini-flash-latest")

# Company Questions Data
company_questions = {

    "tcs": [
        ("Two Sum", "https://leetcode.com/problems/two-sum/"),
        ("Palindrome Number", "https://leetcode.com/problems/palindrome-number/"),
        ("Reverse String", "https://www.geeksforgeeks.org/reverse-a-string/"),
        ("Factorial", "https://www.geeksforgeeks.org/program-for-factorial-of-a-number/"),
        ("Fibonacci", "https://www.geeksforgeeks.org/program-for-fibonacci-numbers/"),
        ("Prime Number", "https://www.geeksforgeeks.org/check-for-prime-number/"),
        ("Array Rotation", "https://www.geeksforgeeks.org/array-rotation/"),
        ("Find Max Element", "https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/"),
        ("Binary Search", "https://leetcode.com/problems/binary-search/"),
        ("Anagram Check", "https://leetcode.com/problems/valid-anagram/")
    ],

    "infosys": [
        ("Two Sum", "https://leetcode.com/problems/two-sum/"),
        ("Merge Sorted Array", "https://leetcode.com/problems/merge-sorted-array/"),
        ("Move Zeroes", "https://leetcode.com/problems/move-zeroes/"),
        ("Missing Number", "https://leetcode.com/problems/missing-number/"),
        ("Majority Element", "https://leetcode.com/problems/majority-element/"),
        ("Longest Common Prefix", "https://leetcode.com/problems/longest-common-prefix/"),
        ("Valid Parentheses", "https://leetcode.com/problems/valid-parentheses/"),
        ("Climbing Stairs", "https://leetcode.com/problems/climbing-stairs/"),
        ("Best Time to Buy Stock", "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"),
        ("Intersection of Arrays", "https://leetcode.com/problems/intersection-of-two-arrays/")
    ],

    "amazon": [
        ("Two Sum", "https://leetcode.com/problems/two-sum/"),
        ("LRU Cache", "https://leetcode.com/problems/lru-cache/"),
        ("Product of Array Except Self", "https://leetcode.com/problems/product-of-array-except-self/"),
        ("Top K Frequent Elements", "https://leetcode.com/problems/top-k-frequent-elements/"),
        ("Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/"),
        ("3Sum", "https://leetcode.com/problems/3sum/"),
        ("Container With Most Water", "https://leetcode.com/problems/container-with-most-water/"),
        ("Search in Rotated Sorted Array", "https://leetcode.com/problems/search-in-rotated-sorted-array/"),
        ("Word Ladder", "https://leetcode.com/problems/word-ladder/"),
        ("Number of Islands", "https://leetcode.com/problems/number-of-islands/")
    ]
}


# Home
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user:
            return "User already exists ❌"

        # Insert new user
        cursor.execute(
            "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",
            (name,email,password)
        )
        db.commit()

        return redirect('/login')

    return render_template('register.html')


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email,password)
        )
        user = cursor.fetchone()

        if user:
            session['user'] = user[2]   # store email
            return redirect('/dashboard')
        else:
            return "Invalid Email or Password ❌"

    return render_template('login.html')


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' in session:

        email = session['user']

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqltanya123",
            database="prepai"
        )
        cursor = conn.cursor()

        # column name
        cursor.execute("SELECT COUNT(*) FROM progress WHERE email=%s", (email,))
        count = cursor.fetchone()[0]

        # Total questions (update if we add more)
        total_questions = 30

        # Progress %
        progress = round((count / total_questions) * 100, 2)

        # Level logic
        if count < 5:
            level = "Beginner"
        elif count < 15:
            level = "Intermediate"
        else:
            level = "Advanced"

        return render_template(
            'dashboard.html',
            user=email,
            count=count,
            level=level,
            progress=progress
        )

    return redirect('/login')
# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# ---------------- COMPANIES ----------------
@app.route('/companies')
def companies():
    if 'user' in session:
        return render_template('companies.html')
    return redirect('/login')

@app.route('/questions/<company>')
def questions(company):
    if 'user' in session:
        email = session['user']

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sqltanya123",
            database="prepai"
        )
        cursor = conn.cursor()

        cursor.execute(
            "SELECT question FROM progress WHERE email=%s AND company=%s",
            (email, company)
        )

        completed = [row[0] for row in cursor.fetchall()]

        questions = company_questions.get(company, [])

        return render_template(
            'questions.html',
            company=company,
            questions=questions,
            completed=completed
        )

    return redirect('/login')


@app.route('/mark_done', methods=['POST'])
def mark_done():
    email = request.form['email']
    company = request.form['company']
    question = request.form['question']

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sqltanya123",
        database="prepai"
    )
    cursor = conn.cursor()

    # Prevent duplicate entries
    cursor.execute(
        "SELECT * FROM progress WHERE email=%s AND company=%s AND question=%s",
        (email, company, question)
    )

    existing = cursor.fetchone()

    if not existing:
        cursor.execute(
            "INSERT INTO progress (email, company, question, status) VALUES (%s, %s, %s, %s)",
            (email, company, question, "done")
        )
        conn.commit()

    return redirect(f"/questions/{company}")
    
@app.route('/viva/<type>')
def viva_type(type):
    if 'user' not in session:
        return redirect('/login')

    if type == "hr":
        cursor.execute("SELECT * FROM viva_questions WHERE subject='HR'")
    else:
        cursor.execute("SELECT * FROM viva_questions WHERE subject!='HR'")

    questions = cursor.fetchall()
    questions = [list(q) for q in questions]

    print(questions)  # optional debug


    return render_template('viva.html', questions=questions, viva_type=type)

@app.route('/viva_select')
def viva_select():
    if 'user' not in session:
        return redirect('/login')

    return render_template('viva_select.html')




def analyze_answer(question, answer):
    try:
        prompt = f"""
You are an experienced technical interviewer and mentor.

Question: {question}
Answer: {answer}

Give feedback in a balanced way:
- Not too long, not too short
- Clear, structured, and helpful
- Easy to understand (no heavy jargon)
- Practical suggestions for improvement

Format:

Score: X/10

Strengths:
- (2-3 clear points)

Weaknesses:
- (2-3 clear points)

How to Improve:
- (actionable advice, what exactly to do better)

Keep tone:
- Professional but friendly
- Like a real interviewer guiding a student
"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"❌ AI Error: {str(e)}"


 # @app.route('/test-ai')
#def test_ai():
    try:
        response = model.generate_content("Say hello in one line")
        return response.text
    except Exception as e:
        return str(e)



    
from flask import jsonify

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    question = request.form['question']
    answer = request.form['answer']
    email = session['user']

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sqltanya123",
        database="prepai"
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO viva_answers (email, question, answer) VALUES (%s,%s,%s)",
        (email, question, answer)
    )
    conn.commit()

    # 🔥 AI ANALYSIS
    feedback = analyze_answer(question, answer)

    return jsonify({
        "status": "success",
        "feedback": feedback
    })

    #return "Answer submitted successfully"

@app.route('/models')
def list_models():
    import google.generativeai as genai

    models = genai.list_models()
    return "<br>".join([m.name for m in models])

if __name__ == '__main__':
    app.run(debug=True)
