-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: prepai
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `progress`
--

DROP TABLE IF EXISTS `progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `progress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress`
--

LOCK TABLES `progress` WRITE;
/*!40000 ALTER TABLE `progress` DISABLE KEYS */;
INSERT INTO `progress` VALUES (1,'tanyamangla2005@gmail.com','infosys','Two Sum','done');
/*!40000 ALTER TABLE `progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Tanya','tanyamangla2005@gmail.com','tanya123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viva_answers`
--

DROP TABLE IF EXISTS `viva_answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `viva_answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `question` text,
  `answer` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viva_answers`
--

LOCK TABLES `viva_answers` WRITE;
/*!40000 ALTER TABLE `viva_answers` DISABLE KEYS */;
/*!40000 ALTER TABLE `viva_answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viva_questions`
--

DROP TABLE IF EXISTS `viva_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `viva_questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) DEFAULT NULL,
  `question` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viva_questions`
--

LOCK TABLES `viva_questions` WRITE;
/*!40000 ALTER TABLE `viva_questions` DISABLE KEYS */;
INSERT INTO `viva_questions` VALUES (1,'OS','What is process and thread?'),(2,'OS','What is deadlock? Explain conditions.'),(3,'OS','Difference between paging and segmentation?'),(4,'CN','What is TCP/IP model?'),(5,'CN','Difference between TCP and UDP?'),(6,'CN','What is DNS?'),(7,'DBMS','What is normalization?'),(8,'DBMS','Difference between SQL and NoSQL?'),(9,'DBMS','What is indexing?'),(10,'C','What is pointer?'),(11,'C','Difference between malloc and calloc?'),(12,'C++','What is OOP?'),(13,'HR','Tell me about yourself'),(14,'HR','What are your strengths and weaknesses?'),(15,'HR','Why should we hire you?'),(16,'HR','Introduce yourself in 1 minute'),(17,'HR','Why do you want to join our company?'),(18,'HR','Describe a challenging situation you faced'),(19,'HR','Where do you see yourself in 5 years?'),(20,'HR','What motivates you?'),(21,'HR','Tell me about a failure and what you learned'),(22,'HR','How do you handle pressure?'),(23,'HR','Are you a team player? Give example'),(24,'HR','Why should we not hire you?'),(25,'HR','What are your career goals?'),(26,'HR','Describe your leadership experience'),(27,'HR','How do you manage time?'),(28,'HR','What is your biggest achievement?'),(29,'HR','Are you willing to relocate?'),(30,'HR','Tell me about your strengths with examples');
/*!40000 ALTER TABLE `viva_questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-06 20:51:43
