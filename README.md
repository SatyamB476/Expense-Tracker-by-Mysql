# 📊 FinTrack: OOP-Based Personal Finance Analytics System

## 📌 Project Overview
**FinTrack** is a professional-grade personal finance management tool built to solve the practical problem of disorganized expense tracking. Unlike static spreadsheets, this system utilizes a **Client-Server Architecture** to provide a secure, scalable, and data-driven approach to financial health.

This project demonstrates a strong foundation in **Python, SQL, and Data Analytics** by integrating a live **MySQL database** with automated **Pandas** analysis and **Matplotlib** visualizations.

---

## 🚀 Key Features

* **Relational Database Management:** Uses a normalized **MySQL** schema with foreign keys to ensure data integrity.
* **Object-Oriented Design (OOP):** Built with modular Python classes for maintainable and scalable code.
* **Automated Data Analytics:** Leverages **Pandas** to perform real-time data transformation and aggregation.
* **Interactive Visualizations:** Generates spending distribution reports using **Matplotlib**.
* **Professional CLI:** A polished Command Line Interface using the `tabulate` library for structured data reporting.

---

## 🛠️ Technical Stack

* **Language:** Python (Primary)
* **Database:** MySQL (Server-based DBMS)
* **Libraries:** Pandas, NumPy, Matplotlib, MySQL-Connector, Tabulate
* **Tools:** Git, GitHub, Visual Studio Code

---

## 🏗️ System Architecture

The project follows a **3-Layer Architecture**:
1.  **Presentation Layer (`main.py`):** Interactive CLI for user input and reporting.
2.  **Logic Layer (`manager.py`):** OOP-based controller handling data processing and analytics.
3.  **Data Access Layer (`database.py`):** Automated SQL script to initialize schemas and manage persistence.

---

## 📥 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/SatyamB476/Expense-Tracker-by-Mysql.git](https://github.com/SatyamB476/Expense-Tracker-by-Mysql.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install mysql-connector-python pandas matplotlib tabulate
    ```
3.  **Configure Database:**
    * Update the `password` variable in `database.py` and `manager.py`.
4.  **Run the Application:**
    ```bash
    python main.py
    ```

---

## 👨‍💻 Author
**Satyam**
* **Email:** satyambhardwaj0391@gmail.com