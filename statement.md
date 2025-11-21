# Project: Expense Tracker

## 1. Problem Statement

Financial ignorance and budget overruns brought on by inadequate tracking are the main issues this project attempts to address. People frequently find it difficult to keep track of their monthly financial situation in real time, depending more on past information than on proactive advice. Current solutions are frequently too complicated or time-consuming. In order to avoid budget failure, there is a fundamental need for a straightforward, practical, and predictive budgeting tool that offers quick feedback and useful metrics.

## 2. Scope of the Project

The project is focused on delivering a robust, single-user, Command-Line Interface (CLI) application dedicated entirely to monthly expense tracking and management. 

The scope includes implementing data persistence via an embedded SQLite database, developing the core algorithm to calculate the Required Daily Budget based on real-time factors, and supporting full CRUD operations (Create, Read, Update, Delete) for expense records. It strictly adheres to a modular design principle with three distinct components. 

Excluded functionality includes multi-user support, external bank API integration, advanced forecasting, and a Graphical User Interface (GUI).

## 3. Target Users

The application is designed for users who require simplicity and actionable guidance to manage fixed monthly income. 

This primarily includes Students managing fixed monthly allowances who need to monitor their daily spending limits, and Young Professionals seeking to track basic household expenses and establish responsible saving habits without using complex financial software.

## 4. High-Level Features

The system is built around a robust, three-module architecture to ensure a clear separation of concerns. 

The Input/Persistence Module (M1) handles all user interaction, including expense addition, editing, and deletion (CRUD operations), securing the data in an embedded SQLite database. 

The Logic/Calculation Module (M2) functions as the computational brain, processing raw expense data to calculate key metrics, most notably the Required Daily Budget algorithm. 

Finally, the Reporting/Analytics Module (M3) presents this processed data to the user, generating the monthly summary report, category visualizations, and critical overspending alerts in a clear, consumable format.
