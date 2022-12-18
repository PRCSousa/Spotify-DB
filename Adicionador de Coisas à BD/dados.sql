-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: spotifer
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `albums`
--

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;
INSERT INTO `albums` VALUES (1,'Midnights',1,'2022-10-21'),(2,'reputation',1,'2017-11-10'),(3,'Midnights (3am Edition)',1,'2022-10-21'),(4,'Northern Anthems',2,'2018-03-23'),(5,'The Navigator',2,'2019-11-22'),(6,'Everything is Color',2,'2018-07-27'),(7,'Happier Than Ever',3,'2021-07-30'),(8,'WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?',3,'2019-03-29'),(9,'BABYMETAL',4,'2015-05-11'),(10,'METAL GALAXY',4,'2019-10-11'),(11,'METAL RESISTANCE',4,'2016-04-01'),(12,'The Lockdown Sessions',5,'2021-10-22'),(13,'In The Zone',5,'2003-11-13'),(14,'Blackout',5,'2007-10-25'),(15,'...Baby One More Time (Digital Deluxe Version)',5,'1999-01-12'),(16,'Oops!... I Did It Again',5,'2000-05-16'),(17,'Circus (Deluxe Version)',5,'2008-12-02'),(18,'Femme Fatale (Deluxe Version)',5,'2011-03-28'),(19,'Death of a Bachelor',6,'2016-01-15'),(20,'Pray for the Wicked',6,'2018-06-22'),(21,'Lover',6,'2019-08-23'),(22,'A Fever You Can\'t Sweat Out',6,'2005-09-27'),(23,'Vices & Virtues',6,'2011-03-18'),(24,'American Beauty/American Psycho',7,'2015-01-20'),(25,'From Under The Cork Tree',7,'2005-05-03'),(26,'Infinity On High',7,'2007-01-01'),(27,'Save Rock And Roll',7,'2013-01-01');
/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (1,'Taylor Swift'),(2,'Vian Izak'),(3,'Billie Eilish'),(4,'BABYMETAL'),(5,'Britney Spears'),(6,'Panic! At The Disco'),(7,'Fall Out Boy');
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `followers`
--

LOCK TABLES `followers` WRITE;
/*!40000 ALTER TABLE `followers` DISABLE KEYS */;
INSERT INTO `followers` VALUES (1,2),(1,4),(2,1),(2,3),(3,1),(3,2),(3,4),(5,6),(5,7),(6,1),(6,3),(7,5),(7,6);
/*!40000 ALTER TABLE `followers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `playlist_songs`
--

LOCK TABLES `playlist_songs` WRITE;
/*!40000 ALTER TABLE `playlist_songs` DISABLE KEYS */;
INSERT INTO `playlist_songs` VALUES (1,31,1),(1,19,2),(1,14,3),(2,17,1),(2,22,2),(2,8,3),(6,59,1),(6,23,2),(6,46,3),(6,70,4),(2,12,4),(2,31,5),(2,50,6),(3,3,1),(3,32,2),(3,55,3),(3,67,4),(4,1,1),(4,15,2),(4,27,3),(5,7,1),(5,29,2),(5,53,3);
/*!40000 ALTER TABLE `playlist_songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `playlists`
--

LOCK TABLES `playlists` WRITE;
/*!40000 ALTER TABLE `playlists` DISABLE KEYS */;
INSERT INTO `playlists` VALUES (1,1,'A mimir','Musicas para dormir',1),(2,2,'Inserir Nome','NULL',0),(3,4,'Workout Motivation','Upbeat tracks to get your heart rate up',1),(4,5,'Road Trip Playlist','A mix of pop and rock hits for long car rides',0),(5,6,'Study Session','Focus-boosting instrumental tracks',0),(6,7,'Summer Hits','The hottest tracks of the season',1);
/*!40000 ALTER TABLE `playlists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (1,'Anti-Hero',1,1,201),(2,'Lavender Haze',1,1,202),(3,'Midnight Rain',1,1,175),(4,'Snow On The Beach (feat. Lana Del Rey)',1,1,256),(5,'Maroon',1,1,218),(6,'You\'re On Your Own, Kid',1,1,194),(7,'Don’t Blame Me',1,2,236),(8,'Bejeweled',1,1,194),(9,'Karma',1,1,205),(10,'The Great War',1,3,240),(11,'Things Will Get Better',2,4,114),(12,'Mostly',2,4,102),(13,'Call the Nightingale',2,5,105),(14,'The London Air Raids',2,4,214),(15,'Will I Find My Home - Acoustic Version',2,6,213),(16,'Witchcraft',2,NULL,110),(17,'Song I Believe In',2,NULL,195),(18,'The London Air Raids - Michael Schawel Remix',2,NULL,173),(19,'Revolver',2,NULL,180),(20,'Revolver - I the Ai Remix',2,6,223),(21,'lovely (with Khalid)',3,NULL,200),(22,'Happier Than Ever',3,7,299),(23,'TV',3,NULL,281),(24,'everything i wanted',3,NULL,245),(25,'Bored',3,NULL,181),(26,'when the party\'s over',3,8,196),(27,'bad guy',3,8,194),(28,'Happier Than Ever - Edit',3,NULL,151),(29,'idontwannabeyouanymore',3,NULL,204),(30,'i love you',3,8,292),(31,'Monochrome',4,NULL,237),(32,'Gimme Chocolate!!',4,9,231),(33,'Divine Attack - Shingeki -',4,NULL,219),(34,'BxMxC',4,NULL,183),(35,'Headbangeeeeerrrrr!!!!!',4,9,240),(36,'PA PA YA!!',4,10,235),(37,'KARATE',4,11,263),(38,'Megitsune',4,9,248),(39,'Road of Resistance',4,9,318),(40,'Shanti Shanti Shanti',4,10,191),(41,'Hold Me Closer',5,12,202),(42,'My Only Wish (This Year)',5,NULL,255),(43,'Toxic',5,13,199),(44,'Gimme More',5,14,251),(45,'...Baby One More Time',5,15,211),(46,'Oops!...I Did It Again',5,16,211),(47,'Womanizer',5,17,224),(48,'Circus',5,17,192),(49,'Criminal',5,18,225),(50,'Toxic Pony',5,NULL,198),(51,'House of Memories',6,19,209),(52,'High Hopes',6,20,191),(53,'ME! (feat. Brendon Urie of Panic! At The Disco)',6,21,193),(54,'I Write Sins Not Tragedies',6,22,187),(55,'Death of a Bachelor',6,19,204),(56,'Emperor\'s New Clothes',6,19,159),(57,'Don\'t Threaten Me with a Good Time',6,19,213),(58,'Hey Look Ma, I Made It',6,20,170),(59,'The Ballad of Mona Lisa',6,23,227),(60,'Victorious',6,19,179),(61,'Centuries',7,24,228),(62,'Sugar, We\'re Goin Down',7,25,229),(63,'Thnks fr th Mmrs',7,26,204),(64,'Dance, Dance',7,25,180),(65,'Immortals',7,24,189),(66,'Summer Days (feat. Macklemore & Patrick Stump of Fall Out Boy)',7,NULL,164),(67,'My Songs Know What You Did In The Dark (Light Em Up)',7,27,187),(68,'This Ain\'t A Scene, It\'s An Arms Race',7,26,212),(69,'The Phoenix',7,27,245),(70,'Uma Thurman',7,24,212);
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Pedro Sousa','sussypedro@mail.com','ilovepizzarolls'),(2,'Ines Cardoso','inescardi@mail.com','lerolero24'),(3,'Rui Silva','ruisilva@mail.com','chocochips123'),(4,'Sofia Martins','sofiamartins@mail.com','bananacake567'),(5,'Joao Rodrigues','joaorodrigues@mail.com','strawberryshortcake999'),(6,'Ana Santos','anasantos@mail.com','mintchocolatechip87326'),(7,'Carlos Alberto','carlosalberto@mail.com','vanillacreamapplepie456');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-18 18:33:58
