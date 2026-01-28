# 🎓 EduTrack – Academic Records & Workflow Engine

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/REST_API-000000?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

<p align="center">
  <b>A role-based academic management backend implementing real-world workflows using Django REST Framework</b>
</p>

---

## 🚀 Project Overview

*EduTrack* is a backend-focused academic records management system that demonstrates  
*Role-Based Access Control (RBAC), **secure authentication, and **approval workflows*  
commonly used in real-world education platforms.

This project strictly separates responsibilities between *Students, **Faculty, and **Admins*  
and enforces access rules at the API level.

---

## 🧠 Core Concept

> 🔐 Authentication identifies the user  
> 🎭 Authorization (role) decides what the user can do

---

## 🧑‍🤝‍🧑 User Roles & Capabilities

| Role | Capabilities |
|---|---|
🎓 *Student* | View enrolled courses and approved results |
🧑‍🏫 *Faculty* | Enter marks and create academic records |
🛡 *Admin* | Approve records and manage the system |


## Screenshots

## Admin Access
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/ed260613-21dd-4129-a5f3-1f3c857c1572" />

## Faculty Access

![Image](https://github.com/user-attachments/assets/f6a45959-08bf-4063-8339-a66b1aaebd06)

## Students Course Enrollment

![Image](https://github.com/user-attachments/assets/55fb7a6b-18ba-45d2-9162-b0453a3fcdbd)

## Students Access and Show Your Mark

![Image](https://github.com/user-attachments/assets/8270db03-f17c-453b-8260-3d6639c5c11d)

## Student Only Access For Get Our Marks
![Image](https://github.com/user-attachments/assets/d9c5ec8e-9999-4976-80d5-dcd345778b63)


---

## 🔁 System Workflow

```text
Admin creates users & courses
        ↓
Student enrolls in courses
        ↓
Faculty enters marks
        ↓
Admin approves records




---





