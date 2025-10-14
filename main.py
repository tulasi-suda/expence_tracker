import csv
import os
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def _init_(self, filename="expenses.csv"):
        self.filename = filename
        self.categories = ["Food", "Travel", "Shopping", "Bills", "Other"]
        self.expenses = []
        self.next_id = 1
        self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from CSV file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # Convert amount to float and ID to int
                        row['id'] = int(row['id'])
                        row['amount'] = float(row['amount'])
                        self.expenses.append(row)
                        
                        # Update next_id to be one more than the highest ID
                        if row['id'] >= self.next_id:
                            self.next_id = row['id'] + 1
            except (FileNotFoundError, csv.Error, ValueError) as e:
                print(f"Error loading expenses: {e}")
                print("Starting with empty expense list.")
    
    def save_all_expenses(self):
        """Save all expenses to CSV file (overwrite)"""
        try:
            with open(self.filename, 'w', newline='') as file:
                fieldnames = ['id', 'date', 'category', 'description', 'amount']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.expenses)
        except IOError as e:
            print(f"Error saving expenses: {e}")
    
    def save_expense(self, expense):
        """Save a single expense to CSV file (append)"""
        try:
            file_exists = os.path.exists(self.filename)
            
            with open(self.filename, 'a', newline='') as file:
                fieldnames = ['id', 'date', 'category', 'description', 'amount']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                writer.writerow(expense)
        except IOError as e:
            print(f"Error saving expense: {e}")
    
    def add_expense(self):
        """Add a new expense"""
        print("\n--- Add New Expense ---")
        
        # Get date
        while True:
            date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date_str:
                date_str = datetime.now().strftime("%Y-%m-%d")
                break
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        # Get category
        print("Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
        
        while True:
            try:
                cat_choice = int(input("Select category (number): "))
                if 1 <= cat_choice <= len(self.categories):
                    category = self.categories[cat_choice - 1]
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get description
        description = input("Enter description: ").strip()
        
        # Get amount
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Create expense dictionary with ID
        expense = {
            'id': self.next_id,
            'date': date_str,
            'category': category,
            'description': description,
            'amount': amount
        }
        
        # Add to list and save to file
        self.expenses.append(expense)
        self.save_expense(expense)
        
        # Increment ID for next expense
        self.next_id += 1
        
        print(f"Expense added successfully! (ID: {expense['id']})")
    
    def view_expenses(self, expenses=None):
        """View expenses with optional filtering"""
        if expenses is None:
            expenses = self.expenses
            
        if not expenses:
            print("No expenses to display.")
            return
        
        print("\n{:<5} {:<12} {:<12} {:<25} {:<10}".format("ID", "Date", "Category", "Description", "Amount"))
        print("-" * 70)
        for expense in expenses:
            print("{:<5} {:<12} {:<12} {:<25} ${:<10.2f}".format(
                expense['id'],
                expense['date'], 
                expense['category'], 
                expense['description'], 
                expense['amount']
            ))
        
        return expenses
    
    def filter_expenses(self):
        """Filter expenses by category or date range"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return None
        
        print("\n--- Filter Expenses ---")
        print("1. View all expenses")
        print("2. Filter by category")
        print("3. Filter by date range")
        print("4. Filter by ID")
        
        while True:
            try:
                choice = int(input("Select option: "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        
        filtered_expenses = self.expenses
        
        if choice == 2:
            # Filter by category
            print("Categories:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i}. {category}")
            
            while True:
                try:
                    cat_choice = int(input("Select category to filter by (number): "))
                    if 1 <= cat_choice <= len(self.categories):
                        selected_category = self.categories[cat_choice - 1]
                        filtered_expenses = [e for e in self.expenses if e['category'] == selected_category]
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == 3:
            # Filter by date range
            while True:
                try:
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    datetime.strptime(start_date, "%Y-%m-%d")
                    
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    datetime.strptime(end_date, "%Y-%m-%d")
                    
                    filtered_expenses = [
                        e for e in self.expenses 
                        if start_date <= e['date'] <= end_date
                    ]
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
        
        elif choice == 4:
            # Filter by ID
            while True:
                try:
                    expense_id = int(input("Enter expense ID: "))
                    filtered_expenses = [e for e in self.expenses if e['id'] == expense_id]
                    if not filtered_expenses:
                        print(f"No expense found with ID {expense_id}.")
                    break
                except ValueError:
                    print("Please enter a valid number.")
        
        return filtered_expenses
    
    def delete_expense(self):
        """Delete an expense from the tracker"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n--- Delete Expense ---")
        
        # First, show all expenses with IDs
        filtered_expenses = self.filter_expenses()
        if not filtered_expenses:
            return
        
        self.view_expenses(filtered_expenses)
        
        # Get the expense to delete
        while True:
            try:
                expense_id = int(input("\nEnter the ID of the expense to delete (0 to cancel): "))
                if expense_id == 0:
                    print("Deletion cancelled.")
                    return
                
                # Find the expense with the given ID
                expense_to_delete = None
                for expense in filtered_expenses:
                    if expense['id'] == expense_id:
                        expense_to_delete = expense
                        break
                
                if expense_to_delete:
                    # Confirm deletion
                    confirm = input(f"Are you sure you want to delete expense ID {expense_id}? (y/n): ").lower()
                    if confirm == 'y':
                        # Remove from main list
                        self.expenses.remove(expense_to_delete)
                        
                        # Save all expenses to file (overwrite)
                        self.save_all_expenses()
                        
                        print(f"Expense ID {expense_id} deleted successfully!")
                    else:
                        print("Deletion cancelled.")
                    return
                else:
                    print(f"Invalid ID. No expense with ID {expense_id} in the filtered list.")
            except ValueError:
                print("Please enter a valid number.")
    
    def edit_expense(self):
        """Edit an existing expense"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n--- Edit Expense ---")
        
        # First, show all expenses with IDs
        self.view_expenses(self.expenses)
        
        # Get the expense to edit
        while True:
            try:
                expense_id = int(input("\nEnter the ID of the expense to edit (0 to cancel): "))
                if expense_id == 0:
                    print("Edit cancelled.")
                    return
                
                # Find the expense with the given ID
                expense_to_edit = None
                for expense in self.expenses:
                    if expense['id'] == expense_id:
                        expense_to_edit = expense
                        break
                
                if expense_to_edit:
                    print(f"\nEditing expense ID {expense_id}:")
                    print(f"1. Date: {expense_to_edit['date']}")
                    print(f"2. Category: {expense_to_edit['category']}")
                    print(f"3. Description: {expense_to_edit['description']}")
                    print(f"4. Amount: ${expense_to_edit['amount']:.2f}")
                    print("5. Cancel")
                    
                    # Get field to edit
                    while True:
                        try:
                            field_choice = int(input("Select field to edit (1-5): "))
                            if 1 <= field_choice <= 5:
                                break
                            else:
                                print("Invalid choice.")
                        except ValueError:
                            print("Please enter a valid number.")
                    
                    if field_choice == 5:
                        print("Edit cancelled.")
                        return
                    
                    # Edit the selected field
                    if field_choice == 1:
                        # Edit date
                        while True:
                            date_str = input("Enter new date (YYYY-MM-DD): ").strip()
                            try:
                                datetime.strptime(date_str, "%Y-%m-%d")
                                expense_to_edit['date'] = date_str
                                break
                            except ValueError:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                    
                    elif field_choice == 2:
                        # Edit category
                        print("Categories:")
                        for i, category in enumerate(self.categories, 1):
                            print(f"{i}. {category}")
                        
                        while True:
                            try:
                                cat_choice = int(input("Select new category (number): "))
                                if 1 <= cat_choice <= len(self.categories):
                                    expense_to_edit['category'] = self.categories[cat_choice - 1]
                                    break
                                else:
                                    print("Invalid choice.")
                            except ValueError:
                                print("Please enter a valid number.")
                    
                    elif field_choice == 3:
                        # Edit description
                        new_description = input("Enter new description: ").strip()
                        expense_to_edit['description'] = new_description
                    
                    elif field_choice == 4:
                        # Edit amount
                        while True:
                            try:
                                new_amount = float(input("Enter new amount: "))
                                if new_amount <= 0:
                                    print("Amount must be positive.")
                                    continue
                                expense_to_edit['amount'] = new_amount
                                break
                            except ValueError:
                                print("Please enter a valid number.")
                    
                    # Save changes to file
                    self.save_all_expenses()
                    print(f"Expense ID {expense_id} updated successfully!")
                    return
                else:
                    print(f"Invalid ID. No expense with ID {expense_id}.")
            except ValueError:
                print("Please enter a valid number.")
    
    def generate_summary(self):
        """Generate monthly summary report"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n--- Monthly Summary ---")
        
        # Get month and year for summary
        while True:
            try:
                month_year = input("Enter month and year (YYYY-MM) or press Enter for current month: ").strip()
                if not month_year:
                    month_year = datetime.now().strftime("%Y-%m")
                    break
                
                # Validate format
                datetime.strptime(month_year, "%Y-%m")
                break
            except ValueError:
                print("Invalid format. Please use YYYY-MM.")
        
        # Filter expenses for the selected month
        monthly_expenses = [
            e for e in self.expenses 
            if e['date'].startswith(month_year)
        ]
        
        if not monthly_expenses:
            print(f"No expenses recorded for {month_year}.")
            return
        
        # Calculate totals
        total = sum(e['amount'] for e in monthly_expenses)
        
        # Calculate category breakdown
        category_totals = defaultdict(float)
        for expense in monthly_expenses:
            category_totals[expense['category']] += expense['amount']
        
        # Find highest and lowest categories
        highest_category = None
        lowest_category = None
        highest_amount = 0
        lowest_amount = float('inf')
        
        for category, amount in category_totals.items():
            if amount > highest_amount:
                highest_amount = amount
                highest_category = category
            if amount < lowest_amount:
                lowest_amount = amount
                lowest_category = category
        
        # Display summary
        print(f"\nSummary for {month_year}:")
        print(f"Total expenses: ${total:.2f}")
        
        print("\nCategory breakdown:")
        for category, amount in category_totals.items():
            percentage = (amount / total) * 100 if total > 0 else 0
            print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")
        
        # Display highest and lowest spending categories
        if highest_category and lowest_category:
            print(f"\nHighest spending category: {highest_category} (${highest_amount:.2f})")
            print(f"Lowest spending category: {lowest_category} (${lowest_amount:.2f})")
        else:
            print("\nNot enough data to determine highest and lowest spending categories.")
    
    def run(self):
        """Main application loop"""
        while True:
            print("\n=== Personal Expense Tracker ===")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Filter Expenses")
            print("4. Delete Expense")
            print("5. Edit Expense")
            print("6. Generate Summary Report")
            print("7. Exit")
            
            try:
                choice = int(input("Select option: "))
                
                if choice == 1:
                    self.add_expense()
                elif choice == 2:
                    self.view_expenses(self.expenses)
                elif choice == 3:
                    filtered = self.filter_expenses()
                    if filtered:
                        self.view_expenses(filtered)
                elif choice == 4:
                    self.delete_expense()
                elif choice == 5:
                    self.edit_expense()
                elif choice == 6:
                    self.generate_summary()
                elif choice == 7:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select 1-7.")
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")

# Run the application
if _name_ == "_main_":
    tracker = ExpenseTracker()
    tracker.run()

