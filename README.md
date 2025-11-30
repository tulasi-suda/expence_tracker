## Personal Expense Tracker
## Overview:

- The Personal Expense Tracker is a Python console application that helps users manage their daily expenses. It allows you to record expenses, categorize them, view spending patterns, and generate detailed monthly reports. All data is stored in a CSV file for persistence between sessi

## Features

**Add Expenses**:

- Record expenses with date, category, description, and amount

**View Expenses**:

- Display all expenses in a tabular format

**Filter Expenses**:

- Filter by category, date range, or specif

**Edit Expenses**:

- Modify existing expense entries

**Delete Expenses**:

- Remove unwanted expense records

**Generate Reports**:

- Create monthly summaries with category breakdowns

**Data Persistence**:

- All data is automatically saved to a CSV file

## Installation

Ensure you have Python 3.6 or higher installed on your system

Download or copy the expense_tracker.py file to your desired loca

No additional dependencies are required beyond Python's standard library

USAGE Running the Application

To start the application, run the following command in your terminal or command prompt:
```sql
bash :

python expense_tracker.py
```

## Main Menu Options
Once the application is running, you'll see the following menu:
**=== Personal Expense Tracker ===**

- Add Expense
- View All Expenses
- Filter Expenses
- Delete Expense
- Edit Expense
- Generate Summary Report
- Exit



## Adding an Expense (Option 1)

- Select option 1 from the main menu

- Enter the date in YYYY-MM-DD format or press Enter for today's date

- Select a category from the list by entering the corresponding number

- Enter a description for the expense Enter the amount (must be a positive number)

- The expense will be saved with a unique ID

## Viewing Expenses (Option 2)

- Select option 2 from the main menu

- All expenses will be displayed in a tabular format with columns for ID, Date, Category, Description, and Amount

## Filtering Expenses (Option 3)

- Select option 3 from the main menu

- Choose how you want to lter expenses:

- View all expenses

- Filter by category
- 
- Filter by date range

- Filter by Specific ID The ltered results will be displayed

## Deleting an Expense (Option 4)

- Select option 4 from the main menu

- First lter the expenses to nd the one you want to delete

- Enter the ID of the expense you want to delete Con rm the deletion when prompted

## Editing an Expense (Option 5)

- Select option 5 from the main menu

- View all expenses to nd the one you want to edit

-Enter the ID of the expense you want to edit Select which eld you want to modify:

```sql
Date
Category
Description
Amount
```

- Enter the new value for the selected eld

- The changes will be saved automatically

## Generating a Summary Report (Option 6)

- Select option 6 from the main menu

- Enter the month and year in YYYY-MM format or press Enter for the current month

- The application will generate a report showing:

- Total expenses for the month

- Category breakdown with percentages

- Highest spending category

- Lowest spending category

## Exiting the Application (Option 7)

- Select option 7 from the main menu The application will exit gracefully

## Data Storage

 All expense data is stored in a CSV le named expenses.csv in the same directory as the application.
The le structure is as follows:
```sql
ID Date
Category
Description
Amount
1
2025-08-29 Food
Breakfast
$250.00
2
2025-08-29 Travel
Bus charge
$29.00
3
2025-08-29 Shopping
Cloths
$2200.00
4
2025-08-29 Bills
Recharge
$399.00
5
2025-08-29 Other
Rent
$500.00
```

## Categories

The application uses the following prede ned categories:
```sql
Food
Travel
Shopping
Bills
Other
```
## Error Handling

The application includes comprehensive error handling for:

- Invalid date formats

- Invalid numerical inputs File I/O errors

- Invalid menu selections

## Future Enhancements

Potential improvements for future versions:

- Custom category creation

- Data export to other formats (JSON, Excel)

- Graphical user interface (GUI)

- Cloud synchronization

- Budget setting and alerts

- Receipt image attachment

- Multi-currency support
