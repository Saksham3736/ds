# outputs

### practical 10

```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

=== Sorted Singly Circular Linked List (SCLL) ===

Menu:
1. Insert
2. Delete
3. Traverse
4. Exit
Enter your choice: 1
Enter value to insert: 10
Inserted 10 successfully.

Enter your choice: 1
Enter value to insert: 5
Inserted 5 successfully.

Enter your choice: 1
Enter value to insert: 20
Inserted 20 successfully.

Enter your choice: 3
List elements: 5 10 20

Enter your choice: 2
Enter value to delete: 10
Deleted 10 successfully.

Enter your choice: 3
List elements: 5 20

Enter your choice: 2
Enter value to delete: 15
Element 15 not found.

Enter your choice: 2
Enter value to delete: 5
Deleted 5 successfully.

Enter your choice: 2
Enter value to delete: 20
Deleted 20 successfully.

Enter your choice: 3
List is empty.

Enter your choice: 4
Exiting program...

```
### 11
```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 1
Enter SSN: E101
Enter Name (single word): Alice
Enter Department: HR
Enter Designation: Manager
Enter Salary: 60000
Enter Phone Number: 9876543210
Inserted at beginning.

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 2
Enter SSN: E102
Enter Name (single word): Bob
Enter Department: Finance
Enter Designation: Analyst
Enter Salary: 50000
Enter Phone Number: 9123456789
Inserted at end.

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 3
Enter SSN after which to insert:
E101
Enter SSN: E103
Enter Name (single word): Carol
Enter Department: HR
Enter Designation: Assistant
Enter Salary: 40000
Enter Phone Number: 9988776655
Inserted after SSN E101.

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 4

Employee 1
SSN: E101
Name: Alice
Department: HR
Designation: Manager
Salary: 60000
Phone: 9876543210

Employee 2
SSN: E103
Name: Carol
Department: HR
Designation: Assistant
Salary: 40000
Phone: 9988776655

Employee 3
SSN: E102
Name: Bob
Department: Finance
Designation: Analyst
Salary: 50000
Phone: 9123456789

Total number of employees: 3

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 5
Deleted first employee.

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 4

Employee 1
SSN: E103
Name: Carol
Department: HR
Designation: Assistant
Salary: 40000
Phone: 9988776655

Employee 2
SSN: E102
Name: Bob
Department: Finance
Designation: Analyst
Salary: 50000
Phone: 9123456789

Total number of employees: 2

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 6
Deleted last employee.

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 4

Employee 1
SSN: E103
Name: Carol
Department: HR
Designation: Assistant
Salary: 40000
Phone: 9988776655

Total number of employees: 1

--- Employee DLL Menu ---
1. Insert at Beginning
2. Insert at End
3. Insert After SSN
4. Display and Count
5. Delete First
6. Delete Last
7. Exit
Enter your choice: 7
Exiting.

```
### 12
```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

=== Polynomial Addition Program (3 variables: x, y, z) ===

Menu:
1. Create POLY1(x,y,z)
2. Create POLY2(x,y,z)
3. Display POLY1, POLY2
4. Add POLY1 and POLY2 → POLYSUM
5. Display POLYSUM
6. Exit

Enter your choice: 1
Enter number of terms in POLY1: 3
Enter coefficient, powers of x, y, z: 3 2 1 0
Enter coefficient, powers of x, y, z: 5 1 1 2
Enter coefficient, powers of x, y, z: -2 0 0 1
POLY1 created successfully.

Enter your choice: 2
Enter number of terms in POLY2: 3
Enter coefficient, powers of x, y, z: 4 2 1 0
Enter coefficient, powers of x, y, z: -5 1 1 2
Enter coefficient, powers of x, y, z: 6 0 0 3
POLY2 created successfully.

Enter your choice: 3

POLY1(x,y,z): 3x^2y^1z^0 + 5x^1y^1z^2 -2x^0y^0z^1
POLY2(x,y,z): 4x^2y^1z^0 -5x^1y^1z^2 + 6x^0y^0z^3

Enter your choice: 4
Polynomials added successfully.

Enter your choice: 5

POLYSUM(x,y,z): 7x^2y^1z^0 + 0x^1y^1z^2 -2x^0y^0z^1 + 6x^0y^0z^3
(Zero coefficient term skipped internally)

Final Simplified POLYSUM(x,y,z): 7x^2y^1z^0 - 2x^0y^0z^1 + 6x^0y^0z^3

Enter your choice: 6
Exiting program...
```
### 13
```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

=== Stack Implementation using Array ===

Menu:
1. Push
2. Pop
3. Display
4. Exit

Enter your choice: 1
Enter value to push: 10
Pushed 10 onto stack successfully.

Enter your choice: 1
Enter value to push: 20
Pushed 20 onto stack successfully.

Enter your choice: 1
Enter value to push: 30
Pushed 30 onto stack successfully.

Enter your choice: 3
Stack elements (top to bottom): 30 20 10 

Enter your choice: 2
Popped element: 30

Enter your choice: 3
Stack elements (top to bottom): 20 10 

Enter your choice: 2
Popped element: 20

Enter your choice: 2
Popped element: 10

Enter your choice: 2
Stack Underflow! Stack is empty.

Enter your choice: 3
Stack is empty.

Enter your choice: 4
Exiting program...
```
### 14
```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

=== Stack Implementation using Linked List ===

Menu:
1. Push
2. Pop
3. Display
4. Exit

Enter your choice: 1
Enter value to push: 10
Pushed 10 onto stack successfully.

Enter your choice: 1
Enter value to push: 20
Pushed 20 onto stack successfully.

Enter your choice: 1
Enter value to push: 30
Pushed 30 onto stack successfully.

Enter your choice: 3
Stack elements (top to bottom): 30 20 10 

Enter your choice: 2
Popped element: 30

Enter your choice: 3
Stack elements (top to bottom): 20 10 

Enter your choice: 2
Popped element: 20

Enter your choice: 2
Popped element: 10

Enter your choice: 2
Stack Underflow! Stack is empty.

Enter your choice: 3
Stack is empty.

Enter your choice: 4
Exiting program...
```
### 15
```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

=== Palindrome Check using Stack ===

Menu:
1. Check Palindrome
2. Exit

Enter your choice: 1
Enter a number: 12321
Original number: 12321
Reversed number: 12321
The number is a Palindrome.

Enter your choice: 1
Enter a number: 14541
Original number: 14541
Reversed number: 14541
The number is a Palindrome.

Enter your choice: 1
Enter a number: 12345
Original number: 12345
Reversed number: 54321
The number is NOT a Palindrome.

Enter your choice: 1
Enter a number: 1221
Original number: 1221
Reversed number: 1221
The number is a Palindrome.

Enter your choice: 2
Exiting program...
```
### 16
```
SAKSHAM
URN: 2435157
CRN: 2415256
D2 CSE-E1
============

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 1
Enter postfix expression (single-digit operands only): 53+
Result = 8

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 1
Enter postfix expression (single-digit operands only): 82/4*
Result = 16

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 1
Enter postfix expression (single-digit operands only): 56+2*
Result = 22

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 1
Enter postfix expression (single-digit operands only): 93-2^
Result = 49

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 1
Enter postfix expression (single-digit operands only): 52+
Result = 7

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 1
Enter postfix expression (single-digit operands only): 82/4*5+
Result = 21

=== Postfix Expression Evaluation ===
1. Evaluate Postfix Expression
2. Exit
Enter your choice: 2
Exiting program...
```
