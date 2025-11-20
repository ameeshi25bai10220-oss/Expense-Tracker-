# *Expense-Tracker*
A modular Python CLI application for personal expense tracking, budgeting, and real-time calculation of the required daily spending limit.

## Project Title
Modular Expense Tracker

## Overview of the project
The Modular Expense Tracker is a command-line interface (CLI) application designed to help users manage their expenses efficiently and utilizing SQLite for persistent CRUD operations and structured modular design for financial analysis.

## Features
1. Persistent Data Storage (SQLite): All expenses are stored in an embedded expenses.db file.  

2. Full CRUD Capability: Users can Create, Read, Update, and Delete transactions by unique IDs.  

3. Actionable Budgeting Metric: Calculates the daily spending limit to meet monthly budget goals.  

4. Algorithm Highlight: Uses datetime functions to determine remaining budget divided by remaining days for real-time guidance.  

5. Real-time Overspending Alerts: Provides immediate red alerts if the user exceeds their budget.  

6. Category Analytics: Offers a spending breakdown by category with text-based visualizations like bar charts.  

7. Modular Design: The codebase consists of three functional modules (Input, Logic, Reporting) for better scalability.

## Technologies/tools used
Language: Python 3.13

Database: SQLite3

Design: Modular Architecture

Libraries: sqlite3, datetime, calendar (Standard Python libraries, avoiding external dependencies.)

## Steps to install & run the project
Clone the Repository: Navigate to your desired directory and clone the project:

1. git clone https://github.com/ameeshi25bai10220-oss/Expense-Tracker
`cd modular-expense-tracker`

2. Verify Files: Ensure all necessary files (main.py, data_model.py, expense_input_v2.py, etc.) are in the root directory.
Run the application:
`python main.py`
(The application will automatically create the expenses.db file and the necessary table structure upon its first run.)

## Instructions for testing
Follow these steps to test all primary features and data persistence:

1. Test 1: Data Creation (CRUD - Create)

Select 1. Add New Expense.

Add at least three expenses using different categories (e.g., Food, Bills, Fun) to populate the database.


2. Test 2: Reporting & Logic (CRUD - Read)

Select 2. View Summary & Analytics.

Verify that the "Total Spent," "Budget Remaining," and the "Category Breakdown" are correctly calculated.

Check the display of the Daily Budget Metric and any color-coded warnings.


3. Test 3: Data Management (CRUD - Update & Delete)

Select 3. Edit/Delete Expenses. The app will list all current records.

Test [D]elete: Enter the ID of one expense and confirm deletion.

Test [E]dit: Enter the ID of another expense, provide a new amount, and select a new category.

Return to the main menu and select 2. View Summary & Analytics to confirm the data changes have been permanently applied and reflect the new calculations.

## Screenshots

(after test 1)

<img width="750" height="795" alt="image" src="https://github.com/user-attachments/assets/4e68c977-023f-48a2-97a1-30cf361e107e" />


(after test 2)

<img width="814" height="676" alt="image" src="https://github.com/user-attachments/assets/073d478f-e22a-4177-a1b8-7e590d459333" />


(after test 3)  (ID 1 and 2 were deleted for testing previously)

<img width="801" height="462" alt="image" src="https://github.com/user-attachments/assets/aeca84c3-3709-48ba-865e-557a94bed03e" />


(after test 4)

<img width="475" height="228" alt="image" src="https://github.com/user-attachments/assets/7b8927cb-d144-407e-b9a6-057cce2475b5" />

