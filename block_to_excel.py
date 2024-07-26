import openpyxl
import re

# Block of questions you can change this if you want like to digital electronics questions or dbms questions
questions = """
1. Write a program to display “INDUS UNIVERSITY” using cout statement.
2. Program which get a integer number and display "WELL DONE" that many times
3. Program to find even and odd numbers between 100 and 200
4. Program to add the digits of given integer number.
5. Program that convert the temperature from Fahrenheit to Celsius.(F-32)×5/9.
6. Write a program to evaluate the following investment equation V = P[(1+r)n
-1]
Where, V is value of compound interest.
 P is principle amount.
 r is rate per period
 n is number of period.
1. An electricity board charges the following rates to domestic users to discharge large consumption
of energy.
 For the first 100 units – 60 P per unit
 For next 200 units - 80P per unit
 Beyond 300 units - 90 P per Unit
 All users are charged a minimum of Rs.50.00. If the total amount is more
 Than Rs. 300.00 then an additional surcharge of 15% is added. Write a
 program to read the names of users and number of units consumed and
 printout the charges with names.
2. Program for Analysis of mark sheet using else if ladder.
3. Write a Program to reverse of given numbers.
4. Write a Program to read a matrix of n*n from keyboard and display the sum of two matrix.
5. Write a Program to illustrate the concept of enum.
6. Write a Program to print the following output using for loop.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
1. Program to find factorial of a given number
2. Write a program in C++ to generate Fibonacci Series by using recursion.
3. Write a Program to find out the square root of a number using inbuilt function library.
4. Write a program to find an area of circle using function with no argument and no return value.
5. Write a program to check whether the number is prime or not using 1) a function with argument
but no return value 2) a function with argument and return value.
6. Write a Program to find average of numbers using a function (no argument) which will return the
mean value of all numbers.
7. What is Default arguments in function? Explain with Example.
8. Write a Program to find out simple interest using a function with three arguments namely
amount, time and interest rate (as a default argument).
9. Write a program using a function with arguments to swap the values of a pair of integers using
call by reference.
10. Explain Call by reference and Return by Reference with suitable example.
11. Write a function power () to raise a number m to a power n. The function takes a double value for
m and int value for n, and returns the result correctly. Use a default value of 2 for n to make the
function to calculate the square when this argument is omitted. Write a main that gets the value of
m and n from the user to test the function.
12. Write a Program to demonstrate the concept of nesting of member function
13. What is inline function? Where and How it is useful in C++? Give an example of inline function
with class and without class.
14. Program for Use of Scope Resolution Operator (::).
15. Write a program that demonstrates the Static Data Member And static member function.
16. Write a Program to illustrate difference between Structure and Class.
17. Explain function overloading with an example.
18. Explain SETW manipulator with example
1. Define a class to represent a string with operations string length, compare and reverse. Show its
use by writing main()
2. Write a class called “arithmetic” having two integer and one character data members. It performs
the operation on its integer members indicated by character member (+, -, *, /). For example *
indicates multiplication on data members as d1 * d2. Write a class with all necessary constructors
and methods to perform the operation and print the operation performed in format Ans = d1 op d2.
Test your class using main().
3. Define Class named point which represents 2-D Point, i.e P(x, y). Define Default Constructor to
initialize both data member value 5. Define Necessary Function and Write a program to test class
Point.
4. Create a class Account. It has three data member account id, name and balance. Define function to
assign value and display value. Define function that search account number given by the user. If
account number exists, print detail of that account. Write a program using array of object. Declare
at least 5 account and print details.
5. Write a single C++ program to explain the concept of both constructor and destructor.
6. Write a program which include class to represent a vector(a serious of float values). Include
member functions to perform the following tasks:
 a> To create the vector
 b> To modify the value of given elements
 c> To Display the given vector in the form(10,20,30)
7. Declare a class called book_details to represent details for a book, having data members like title,
author, edition, price and no_of_copies_available. Define following functions:
 - constructor(s)
 - display to display all data members
 - find_books to find and display details of all books having price less than Rs. 250
 - main to create an array of book_details and to show usage of above functions
8. Define a class Time with hours and minutes as two data members, add necessary member functions
to initialize and display data of class. Do not use constructors in a class. Define a member function
sum() which adds two Time objects. Invoke the statements like T3.sum(T1, T2) in main ().
9. Explain friend function with suitable example. Write a program to find out sum of two private data
members x and y of two classes A and B using a common friend function. Assume that the prototype
for both the classes will be void sum (A, B);
10. Define a class matrix with an integer array of 3X3 as a data member. Define a friend function
which adds two matrix objects and returns resultant matrix object.
11. Define a class complex, having data member as X and Y, Define a friend function sum () to add
two complex numbers and display all numbers using show () friend function. Program for
Maximum number using Friend function for two classes
12. Write a C++ program to explain Objects as function arguments. Define a class name VALUE with
two data member variable, two member functions for inputting data and displaying the result.
Define third member function that takes two objects as arguments and adds the objects.
13. Create two classes DM and DB which store the value of distances. DM stores distances in meters
and centimetres and DB in feet and inches. Write a program that can read values for the class
objects and add one object of DM with another object of DB. Use a friend function to carry out the
addition operation. The object stores the results may a DM object or DB object, depending on the
units in which the results are required. The display should be in the format of feet and inches or
meters and centimeters depending on the object on display.1Feet = 0.3048Meter 1Meter = 3.28
Feet.1Inch = 2.54 Centimeter 1 Centimeter = 0.3937 Inch(June 2013)
14. Create a class student that stores roll_no, name. Create a class test that stores marks obtained in
five subjects. Class result derived from student and test contains the total marks and percentage
obtained in test. Input and display information of a student.
15. Write a program in C++ to find the sum of two entered complex numbers from different classes
and display the sum using a common friend function of both classes.
16. Create class Time that has three data members hour, minute and second and two constructors, default
constructor and parameterized constructor to initialize data member. Write a program to add two times
by overloading operator +
17. Define a class complex with real and imaginary as two data member, add necessary constructors
and member function to initialize and display data of class. Class should overload the + operator to
add two complex objects and return the results. Invoke the statements like C3=C1+C2 in main ().
18. Define a circle class with radius as data member, necessary constructors and member function to
compute area of circle. Class should overload the = = operator to compare two circle objects
whether they are equal in radius. Demonstrate its use in main ().
19. Declare a class called bird having two private data members called name and weight. Define
following functions:
- default constructor for reading data members from key board
- Overloaded constructor with two arguments to be used for initialization of data members.
- display function to display data members.
- overloaded member operator >= to compare weight of two bird objects, returning false if weight
of first bird object is less than that of second & true otherwise.
Define function main to illustrate use of above functions.
20. Declare a class called book having members like book_title, publisher and author_name. Overload
operators << and >> for class book. Define function main.
21. Program to overload a single unary Operator.
22. Define a class complex with real and imaginary as two data member with default & parameterized
constructors, function to initialize display data of class. It should overload the + operator to add
two complex objects. Write a program to demonstrate use of complex class.
23. Create one class rupees, which has one member data to store amount in rupee and create another
class paise which has member data to store amount in paise. Write a program to convert one amount
to another amount with the use of type conversion
1. Program to implement Single Inheritance
2. Program to Implement Hybrid Inheritance...
3. Student class have two derived class named as Test, Sports and both Test, Sports has a derived
class named as Result which display all the details.
4. Assume that circle is defined using radius and cylinder is defined using
radius and height. Write a circle class as base class and inherit the cylinder class from it. Develop
classes such that user can compute the area of circle objects and volume of cylinder objects. Area
of circle is radius*radius, while volume of cylinder is pie*(radius)2*height.
5. Assume that vehicle class is defined as base class with price and year of manufacturing. Derive
two classes namely bus and truck from base class with bus with seating capacity and truck with
loading capacity. Develop classes with necessary member functions to get and put data.
Demonstrate its use in main ().
7. Create a class student that stores roll_no,name. Create a class test that stores marks obtained in five
subjects. Class result derived from student and test contains the total marks and percentage obtained
in test. Input and display information of a student.
8. Create a class vehicle which stores the vehicle number and chassisno no as a data member. Define
another class for scooter, which inherits the data members of the class vehicle and has a data
member for storing price and name of company. Display the data from derived class.
9. Write a program to demonstrate the use of pure virtual function.
11. Declare a class called item having data members item_code, item_name, cost and discount.
Derive two classes from class item, namely employee and customer. The class employee has data
members like employee_id and amount. The class customer has data members like
customer_name and amount. Define following functions
- to initialize data members.
- to display the values of members.
- to compute amount to be paid for purchased item.
- main to create objects of both derived classes and to show usage of above functions.
12. Define a class publisher that stores the name of title. Derive two classes book and tape, which
inherit publisher. Book class contains member data called page no and tape class contain time for
playing. Define Functions in the appropriate classes to get and print the details.
1. Write a C++ program demonstrating use of the pure virtual function with the use of base and
derived classes.
2. Write a C++ program to overload the + operator to concatenate two strings.
3. Program to create a class THREE-D contains data members like X, Y, Z having dimensions.
Include constructor to initialize data. and overload Unary +, -, ++, -- and Binary * Operator
4. Declare a class called logic_gate to represent logic gates. The class has three data members - input1,
input2 and input3 to represent three inputs to the logic gate. The class also has a virtual function
member called get_gate_output. Derive two classes from the base class logic_gate, namely,
and_gate and or_gate to represent ‘logical and gate’ and ‘logical or gate’ respectively. Define
function get_gate_output in both of these classes to get the output of the gate. Show use of above
classes and functions to demonstrate dynamic polymorphism in function main.
5. Write a complete program to illustrate the use of this pointer
6. Declare a class called my_string having char * str_ptr as a member, used to point to a string. Define
a constructor for initializing member. Define an overloaded operator + to be applied on two
operands of type class my_string for concatenating strings pointed by str_ptr of operands. The
resultant string is placed in a new object of type class my_string which is returned. Define main to
show the usage of these functions
7. Write a C++ program that creates inventory of items by storing item_code, item name and qty.
Access the data using pointers.
8. Create a class ITEM with item_code, item_rate and quantity as a data member. Create an array of
pointers to objects of class ITEM. Write a member function which will calculate the amount of
item. Print item_code and amount of item.
1. Write a program that reads a text file and creates another file that is identical except that every
character is in upper case.
2. Write a program that reads a text file and creates another text file that is identical except that every
letter must be converted to lower case irrespective of its original case (e.g. ‘a’ or ‘A’ will become
‘a’).
3. Explain various file mode parameters in C++. Write a program to copy the contents of a source file
student1.txt to a destination file student2.txt character by character.
4. Write a program that opens two text files for reading data. It creates a third file that contains the
text of first file and then that of second file (text of second file to be appended after text of the first
file, to produce the third file).
5. Write a program to show use of manipulators. 
"""


def split_questions(text):
    questions = []
    current_question = ""
    lines = text.strip().split('\n')
    
    for line in lines:
        if re.match(r'^\d+\.\s', line) and current_question:
            questions.append(current_question.strip())
            current_question = line
        else:
            current_question += " " + line
    
    if current_question:
        questions.append(current_question.strip())
    
    return questions


split_questions = split_questions(questions)


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Questions"


for i, question in enumerate(split_questions, start=1):
    sheet[f'A{i}'] = f'Question {i}'
    sheet[f'B{i}'] = question


workbook.save("questions.xlsx") # change name if you want
