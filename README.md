Overview:
 >The Personal Expense Tracker is a Python console application that helps users manage their dai
 expenses. It allows you to record expenses, categorize them, view spending patterns, and generate
 detailed monthly reports. All data is stored in a CSV le for persistence between session
 Features
 Add Expenses:
 Record expenses with date, category, description, and amount
 View Expenses:
 Display all expenses in a tabular format
 Filter Expenses:
 Filter by category, date range, or speci c
 Edit Expenses:
 Modify existing expense entries
 Delete Expenses:
 Remove unwanted expense records
 Generate Reports:
 Create monthly summaries with category breakdowns
 Data Persistence:
 All data is automatically saved to a CSV le
 Installation
 Ensure you have Python 3.6 or higher installed on your system
 Download or copy the expense_tracker.py le to your desired locati
 No additional dependencies are required beyond Python's standard library
 Usage
 Running the Application
 To start the application, run the following command in your terminal or command prompt:
 bash :
 python expense_tracker.py

Main Menu Options
 Once the application is running, you'll see the following
 menu:
 === Personal Expense Tracker ===
 . Add Expense
 . View All Expense
 . Filter Expense
 . Delete Expens
 . Edit Expens
 . Generate Summary Repor
 . Exit
 >Adding an Expense (Option 1)
 Select option 1 from the main menu
 Enter the date in YYYY-MM-DD format or press Enter for today's date
 Select a category from the list by entering the corresponding number
 Enter a description for the expense
 Enter the amount (must be a positive number)
 The expense will be saved with a unique ID
 >Viewing Expenses (Option 2)
 Select option 2 from the main menu
 All expenses will be displayed in a tabular format with columns for ID, Date, Category, Description, and
 Amount
 >Filtering Expenses (Option 3)
 Select option 3 from the main menu
 Choose how you want to lter expense
 View all expenses
 Filter by category
 Filter by date range
 
Filter by speci c
 The ltered results will be display
 >Deleting an Expense (Option 4)
 Select option 4 from the main menu
 First lter the expenses to nd the one you want to de
 Enter the ID of the expense you want to delete
 Con rm the deletion when prompt
 >Editing an Expense (Option 5)
 Select option 5 from the main menu
 View all expenses to nd the one you want to ed
 Enter the ID of the expense you want to edit
 Select which eld you want to modif
 Date
 Category
 Description
 Amount
 Enter the new value for the selected e
 The changes will be saved automatically
 >Generating a Summary Report (Option 6)
 Select option 6 from the main menu
 Enter the month and year in YYYY-MM format or press Enter for the current month
 The application will generate a report showing:
 Total expenses for the month
 Category breakdown with percentages
 Highest spending category
 Lowest spending category
 >Exiting the Application (Option 7)
 Select option 7 from the main menu
 The application will exit gracefully
 
 Data Storage
 All expense data is stored in a CSV le nam
 expenses.csv in the same directory as the application.
 The le structure is as follows:
 ID Date Category Description Amount
 1 2025-9-9 Food party $5000.00
 2 2025-9-16 Travel tirupati $6000.00
 3 2025-9-20 Travel return $6500.00
 4 2025-9-24 Shopping clothes $5999.00
 5 2025-10-3 Bills electricity $8967.00
 Categories
 The application uses the following prede ned categorie
 Food
 Travel
 Shopping
 Bills
 Other
 Error Handling
 The application includes comprehensive error handling for:
 Invalid date formats
 Invalid numerical inputs
 File I/O errors
 Invalid menu selections
 Future Enhancements
 Potential improvements for future versions:
 Custom category creation
 Data export to other formats (JSON, Excel)
 Graphical user interface (GUI)
 Cloud synchronization
 
Budget setting and alerts
 Receipt image attachment
 Multi-currency support
