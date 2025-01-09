
# Face Recogniton Attendance System

This project is a Face Recognition-based Attendance Management System designed to streamline the process of taking and managing attendance. It offers an intuitive user interface with various functionalities to ensure efficient attendance tracking.

## Table of Contents
- [About](#about)
- [Getting Started](#getting-started)
- [Features](#features)
- [Installation](#installation)
---

## About

The **Face Recognition Attendance System** is an automated solution designed to simplify attendance tracking by utilizing facial recognition technology. Users can register by providing their personal details and uploading a photo, which the system uses to train a facial recognition model. Once registered, users can mark their attendance simply by facing the camera, with the system automatically recognizing their face and recording the attendance. The app also allows administrators to view a list of registered users and their attendance records, all of which are stored securely in a MySQL database. Additionally, the system includes features for contacting the administrator and submitting complaints or feedback, making it a comprehensive and user-friendly tool for attendance management.

---

## Features

List the main features of your project:
#### 1. User Signup

    Users can register by entering personal details and uploading a photo. The system uses the photo to train a facial recognition model, and all user data is stored in a MySQL database.

#### 2. Mark Attendance

    Users can mark their attendance by opening the camera. The system uses facial recognition to identify and record attendance with a timestamp.

#### 3. View Registered Users

    Displays a list of all registered users along with their details and photos, pulled from the MySQL database.

#### 4. View Attendance Records

    Shows attendance history for all users, including the date and time, stored in the MySQL database.

#### 5. Contact Information

    Provides users with contact details for the system administrator for support or inquiries.

#### 6. Submit Complaints

    Users can submit complaints with their details, which are stored and can be reviewed by the administrator.

---

## Getting Started

### Prerequisites
Before you begin, make sure you have the following tools and dependencies installed:
- Python 3.10 or higher
- MySQL for database storage
- Face Recognition Library for face detection
- pip for installing Python packages
- Virtual Enviroment Library for venv

## Installation

### I. Setting up mysql for database

1. Login in mysql database using msql 
   ```bash
   mysql -u <username> -p

2. Create Database
    ```bash
    create database face_reco_attendance_sys;
    use face_reco_attendance_sys;

3. Make Table for Storing User data
    ```bash
    CREATE TABLE user_data (
    name VARCHAR(255),
    roll_no VARCHAR(255) PRIMARY KEY,
    reg_no INT,
    phone VARCHAR(20),
    email VARCHAR(255),
    dep VARCHAR(30),
    sem VARCHAR(10),
    day INT,
    month INT,
    year INT,
    sex VARCHAR(10),
    photo_sample TINYINT
    );
    
4. For complaint box
-   Create the database

    ```bash
     CREATE DATABASE student_complaints;

- Use the newly created database

    ```bash
     USE student_complaints;

- Create the table

    ```bash
    CREATE TABLE complaints (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255) NOT NULL, 
        roll_no VARCHAR(255) NOT NULL, 
        department VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        complaint TEXT NOT NULL 
    );


---
###  II. To Run Project and Installation of Libraries

1. Clone the repo:
   ```bash
   git clone https://github.com/risav68111/face_reco_attendance_sys.git

2. Moving to project directory
   ```bash
    cd face_reco_attendance_sys

3. Create Virtual enviroment for project seperating libraries
   ```bash
   python -m venv venv

4. Activate virtual enviroment
   ```bash
   venv\scripts\activate

5. Install Required Libraries
   ```bash 
   pip install -r requirements.txt 
   
6. Run Main friendly
   ```bash
   python main.py 
