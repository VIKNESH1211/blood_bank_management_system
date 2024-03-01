import tkinter as tk
from tkinter import messagebox
import mysql.connector

class BloodBankManagementApp:
    def __init__(self, root):
        self.root = root
        root.title("Blood Bank Management System")
        self.root.geometry("500x400")  # Set the window size

        # Create a frame for the main menu
        self.menu_frame = tk.Frame(root, padx=20, pady=20)
        self.menu_frame.pack(fill="both", expand=True)

        # Create and set fonts
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 14, "bold")

        # Blood Inventory Section
        blood_inventory_label = tk.Label(self.menu_frame, text="Blood Inventory", font=("Helvetica", 16, "bold"))
        blood_inventory_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

        self.blood_type_label = tk.Label(self.menu_frame, text="Blood Type:", font=label_font)
        self.blood_type_label.grid(row=1, column=0)
        self.blood_type_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.blood_type_entry.grid(row=1, column=1)

        self.quantity_label = tk.Label(self.menu_frame, text="Quantity:", font=label_font)
        self.quantity_label.grid(row=1, column=2)
        self.quantity_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.quantity_entry.grid(row=1, column=3)

        self.check_button = tk.Button(self.menu_frame, text="Check Blood Units", font=button_font, command=self.check_blood_units)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        self.update_button = tk.Button(self.menu_frame, text="Update Blood Bank", font=button_font, command=self.update_blood_bank)
        self.update_button.grid(row=2, column=2, columnspan=2, pady=(10, 0))

        # Recipient Section
        recipient_label = tk.Label(self.menu_frame, text="Recipient", font=("Helvetica", 16, "bold"))
        recipient_label.grid(row=3, column=0, columnspan=4, pady=(20, 10))

        self.recipient_name_label = tk.Label(self.menu_frame, text="Recipient Name:", font=label_font)
        self.recipient_name_label.grid(row=4, column=0)
        self.recipient_name_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.recipient_name_entry.grid(row=4, column=1)

        self.withdrawal_quantity_label = tk.Label(self.menu_frame, text="Withdrawal Quantity:", font=label_font)
        self.withdrawal_quantity_label.grid(row=4, column=2)
        self.withdrawal_quantity_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.withdrawal_quantity_entry.grid(row=4, column=3)

        self.withdraw_button = tk.Button(self.menu_frame, text="Update Withdrawal", font=button_font, command=self.update_withdrawal)
        self.withdraw_button.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        # Donor Section
        donor_label = tk.Label(self.menu_frame, text="Donor Information", font=("Helvetica", 16, "bold"))
        donor_label.grid(row=6, column=0, columnspan=4, pady=(20, 10))

        self.donor_name_label = tk.Label(self.menu_frame, text="Donor Name:", font=label_font)
        self.donor_name_label.grid(row=7, column=0)
        self.donor_name_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.donor_name_entry.grid(row=7, column=1)

        self.donor_age_label = tk.Label(self.menu_frame, text="Donor Age:", font=label_font)
        self.donor_age_label.grid(row=7, column=2)
        self.donor_age_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.donor_age_entry.grid(row=7, column=3)

        self.donor_gender_label = tk.Label(self.menu_frame, text="Donor Gender:", font=label_font)
        self.donor_gender_label.grid(row=8, column=0)
        self.donor_gender_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.donor_gender_entry.grid(row=8, column=1)

        self.donor_phone_label = tk.Label(self.menu_frame, text="Donor Phone:", font=label_font)
        self.donor_phone_label.grid(row=8, column=2)
        self.donor_phone_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.donor_phone_entry.grid(row=8, column=3)

        self.donor_date_received_label = tk.Label(self.menu_frame, text="Date Received:", font=label_font)
        self.donor_date_received_label.grid(row=9, column=0)
        self.donor_date_received_entry = tk.Entry(self.menu_frame, font=entry_font)
        self.donor_date_received_entry.grid(row=9, column=1)

        #self.add_donor_button = tk.Button(self.menu_frame, text="Add Donor", font=button_font, command=self.add_donor)
        #self.add_donor_button.grid(row=10, column=0, columnspan=4, pady=(10, 0), padx=10)  # Place the button at the bottom

    # Rest of the methods (update_blood_bank, check_blood_units, update_withdrawal, add_donor)

# Rest of the code remains the same...

# Rest of the code remains the same...
     
    def update_blood_bank(self):
        blood_type = self.blood_type_entry.get()
        quantity = int(self.quantity_entry.get())
        donor_name = self.donor_name_entry.get()
        donor_age = int(self.donor_age_entry.get())
        donor_gender = self.donor_gender_entry.get()
        donor_phone = self.donor_phone_entry.get()
        donor_date_received = self.donor_date_received_entry.get()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VikneshViknesh",
                database="user_authentication"
            )
            cursor = db.cursor()

            cursor.execute("INSERT INTO blood_bank (blood_type, donor_name, donor_age, donor_gender, donor_phone, date_received, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (blood_type, donor_name, donor_age, donor_gender, donor_phone, donor_date_received , quantity))

            db.commit()
            db.close()
            messagebox.showinfo("Success", "Donor information added to the blood bank.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")

    def check_blood_units(self):
        blood_type = self.blood_type_entry.get()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VikneshViknesh",
                database="user_authentication"
            )
            cursor = db.cursor()

            cursor.execute("SELECT SUM(quantity) FROM blood_bank WHERE blood_type = %s", ([blood_type]))
            total_quantity = cursor.fetchone()[0]

            db.close()

            if total_quantity is not None:
                messagebox.showinfo("Blood Units Available", f"Total Quantity for Blood Type {blood_type}: {total_quantity}")
            else:
                messagebox.showinfo("Blood Units Available", f"No blood units available for Blood Type {blood_type}.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")


    def update_withdrawal(self):
        recipient_name = self.recipient_name_entry.get()
        blood_type = self.blood_type_entry.get()
        quantity = int(self.withdrawal_quantity_entry.get())

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VikneshViknesh",
                database="user_authentication"
            )
            cursor = db.cursor()

            cursor.execute("INSERT INTO blood_bank (recipient_name, blood_type, quantity) VALUES (%s, %s, %s)", (recipient_name, blood_type, -quantity))

            db.commit()
            db.close()
            messagebox.showinfo("Success", "Withdrawal recorded successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")


    def add_donor(self):
        donor_name = self.donor_name_entry.get()
        donor_age = int(self.donor_age_entry.get())
        donor_gender = self.donor_gender_entry.get()
        donor_phone = self.donor_phone_entry.get()
        donor_date_received = self.donor_date_received_entry.get()

        try:
            db = mysql.connector.connect(
                host="your_host",
                user="your_username",
                password="your_password",
                database="your_database"
            )
            cursor = db.cursor()

            cursor.execute("INSERT INTO donors (name, age, gender, phone_number, date_received) VALUES (%s, %s, %s, %s, %s)",
                           (donor_name, donor_age, donor_gender, donor_phone, donor_date_received))

            db.commit()
            db.close()
            messagebox.showinfo("Success", "Donor information added successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")


class LoginPage:
    def __init__(self, root):
        self.root = root
        root.title("Login Page")
        root.geometry("300x200")  # Set the window size

        # Create a frame for login elements
        login_frame = tk.Frame(root, padx=20, pady=10)  # Add padding
        login_frame.pack(expand=True, fill="both")

        # Create and set font
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 14, "bold")

        # Username Label and Entry
        self.username_label = tk.Label(login_frame, text="Username:", font=label_font)
        self.username_label.pack(pady=(0, 5))
        self.username_entry = tk.Entry(login_frame, font=entry_font)
        self.username_entry.pack(pady=(0, 10))

        # Password Label and Entry
        self.password_label = tk.Label(login_frame, text="Password:", font=label_font)
        self.password_label.pack(pady=(0, 5))
        self.password_entry = tk.Entry(login_frame, show="*", font=entry_font)
        self.password_entry.pack(pady=(0, 10))

        # Login Button
        self.login_button = tk.Button(login_frame, text="Login", font=button_font, command=self.login)
        self.login_button.pack()

    
    def login(self):
        # Get the username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            # Connect to the MySQL database
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VikneshViknesh",
                database="user_authentication"
            )
            cursor = db.cursor()

            # Check if the provided username and password exist in the 'users' table
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user_data = cursor.fetchone()

            if user_data:
                # Authentication successful, open the Blood Bank Management app
                self.open_blood_bank_management()
            else:
                # Authentication failed, show an error message
                messagebox.showerror("Login Failed", "Invalid username or password")

            db.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")



    def open_blood_bank_management(self):
        self.root.destroy()  # Close the login window
        root = tk.Tk()
        app = BloodBankManagementApp(root)
        root.mainloop()


        

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root)
    root.mainloop()