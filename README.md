
# **Student Result Management App**

A **Python Tkinter GUI application** to manage student results with MySQL backend.
Features include: Add, View, Edit, Delete student records with automatic achievement calculation and continuous ID management.

---

## **Features**

* Add student details (Name, Subject, Marks).
* Automatic calculation of **Achievement** based on marks:

  * 90–100 → Diamond
  * 75–89 → Platinum
  * 60–74 → Silver
  * 50–59 → Bronze
  * <50 → No Achievement
* View all results in a **sortable table**.
* Edit any record from the table.
* Delete any record.
* IDs are **continuous**, automatically reordered after deletion.
* Input validation:

  * Name & Subject: letters only
  * Marks: integer 0–100

---

## **Technologies Used**

* Python 3.x
* Tkinter for GUI
* MySQL / MariaDB for database
* MySQL Connector Python (`mysql-connector-python`)

---

## **Database Setup**

Run the following SQL commands to set up your MySQL database:

```sql
-- Create database
CREATE DATABASE student_db;
USE student_db;

-- Create table
CREATE TABLE result (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    subject VARCHAR(50),
    marks INT,
    achievement VARCHAR(100)
);
```

---

## **Project Structure**

```
student_result_app/
│
├── app.py         # Main Tkinter application
├── db.py          # Database connection and CRUD operations
└── README.md      # Documentation
```

---

## **Installation**

1. Clone the repository:

```bash
git clone <your-repo-url>
cd student_result_app
```

2. Install required Python package:

```bash
pip install mysql-connector-python
```

3. Make sure MySQL server is running and database is set up as above.

---

## **How to Run**

```bash
python app.py
```

* Enter Name, Subject, and Marks.
* Click **Submit** to add the record.
* Click **Show Results** to view all records in a table.
* Use **Edit Selected** to modify a record.
* Use **Delete Selected** to delete a record.
* IDs will be automatically updated to remain continuous.

---

## **Screenshots**

*(Add screenshots of your Tkinter GUI here)*

---

## **Database Operations in Code**

* **Insert Record:**

```python
db.insert_result(name, subject, marks)
```

* **Fetch Records:**

```python
results = db.fetch_results()
```

* **Update Record:**

```python
db.update_result(record_id, name, subject, marks)
```

* **Delete Record:**

```python
db.delete_result(record_id)
```

* **ID Handling:** After deletion, IDs are reordered so there are no gaps.

---

## **Achievements Logic**

```text
Marks >= 90 : Diamond
Marks >= 75 : Platinum
Marks >= 60 : Silver
Marks >= 50 : Bronze
Marks < 50  : No Achievement
```

---

## **Future Enhancements**

* Add **Search / Filter** feature.
* Export results to CSV or PDF.
* Add **login/authentication** for multiple users.
* Graphical performance charts per student.

---

## **Author**

Anil Kumar Reddy
Email: [anil@example.com](mailto:anil@example.com)

