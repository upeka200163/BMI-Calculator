# BMI-Calculator
# 🧮 Pro BMI Calculator v2.0  

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)  
![SQLite](https://img.shields.io/badge/Database-SQLite-orange)  
![Status](https://img.shields.io/badge/Project-Academic-purple)

---

## 📌 Overview  

**Pro BMI Calculator v2.0** is a modern desktop application developed using Python Tkinter with SQLite database integration.  

The system includes a complete Register & Login authentication module, an interactive BMI Calculator Dashboard, and a BMI History Tracking feature with a clean dark-themed user interface.

---

## 🚀 Key Features  

### 🔐 User Authentication  
- User Registration with unique username validation  
- Secure Login system  
- Logout functionality  

### 📊 BMI Dashboard  
- Input Weight (kg) and Height (m)  
- Automatic BMI Calculation  
- BMI Category Detection:
  - Underweight  
  - Normal  
  - Overweight  
  - Obese  
- Dynamic progress indicator  
- Clear button to reset inputs  

### 📜 BMI History  
- Stores all BMI calculations in SQLite database  
- View previous records with date & time  
- Organized table view using Treeview  

---

## 🛠️ Technologies Used  

- Python 3  
- Tkinter (GUI Development)  
- SQLite3 (Database Management)  
- Pillow (Image Handling)  
- ttk (Styled Components)  

---

## 🗂️ Database Structure  

### Users Table  
| Field | Type |
|-------|------|
| id | INTEGER (Primary Key) |
| username | TEXT (Unique) |
| password | TEXT |

### BMI Results Table  
| Field | Type |
|-------|------|
| id | INTEGER (Primary Key) |
| user_id | INTEGER |
| weight | REAL |
| height | REAL |
| bmi | REAL |
| date | TIMESTAMP |

---

## 🧠 How It Works  

1. User creates an account  
2. Logs into the system  
3. Enters weight and height  
4. BMI is calculated using:

BMI = Weight (kg) / Height (m)^2  

5. Result is displayed with category & color indicator  
6. Data is saved into database  
7. User can view BMI history anytime  

---

## 🎨 UI Highlights  

- Modern Dark Theme  
- Card-Based Layout  
- Background Image Support  
- Clean & Professional Design  

---

## 📚 Academic Purpose  

This project was developed as part of an academic learning process to demonstrate:

- GUI Application Development  
- Database Connectivity  
- Event-Driven Programming  
- CRUD Operations  
- Structured OOP Design  

---

## 🔮 Future Improvements  

- Password hashing (security enhancement)  
- BMI trend graph visualization  
- Export history to PDF  
- Improved responsive layout  

---

## 🚀 Installation Guide  

### 1️⃣ Clone the Repository  

```bash
git clone :https://github.com/upeka200163/BMI-Calculator.git
```

### 2️⃣ Navigate to Project Folder  

```bash
cd pro-bmi-calculator
```

### 3️⃣ Install Required Library  

```bash
pip install pillow
```

### 4️⃣ Run the Application  

```bash
python main.py
``` 
