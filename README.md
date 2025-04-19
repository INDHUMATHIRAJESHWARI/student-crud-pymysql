# student-crud-pymysql
A simple student management system console-based application demonstrating CRUD operations with Python and PyMySQL

### Prerequisites
- Python 3.8+
- MySQL Server 8.0
- PyMySQL (`pip install pymysql`)

### Setup
1. Create MySQL database:
   ~sql
   CREATE DATABASE my_db;
   USE my_db;
   CREATE TABLE student(
     id INT PRIMARY KEY,
     name VARCHAR(50),
     age INT
   );
  

-Configure credentials in database.py
 self.con = pymysql.connect(
    host='localhost',
    user='your_username',  
    password='your_password', 
    db='my_db'
)

-Install dependencies
    pip install pymysql

-Run the application
    python main.py

-Menu Options
  1. Insert   → Add new student
  2. View     → List all students
  3. Edit     → Update student age
  4. Delete   → Remove student
  0. Close    → Exit program




### Demo Output

~python main.py
Connect to db succesfull!


 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 1

 Student Registration Form
Enter id : 1020
Enter name : Sensa
Enter age : 23
Data saved!


 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 2

 Registered Student Data
1001    Ram     21

1002    Lakhman 22

1003    Lara    23

1004    Nila    20

1020    Sensa   23



 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 3

 Student Updation Form
Enter id : 1020
Enter age : 21
Data saved!


 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 2

 Registered Student Data
1001    Ram     21

1002    Lakhman 22

1003    Lara    23

1004    Nila    20

1020    Sensa   21



 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 4

Student Removal Form
Enter id : 1020
Data deleted!


 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 2

 Registered Student Data
1001    Ram     21

1002    Lakhman 22

1003    Lara    23

1004    Nila    20



 DashBoard
1. Insert
2. View
3. Edit
4. Delete
0. Close
Enter choice : 0
App closed!



