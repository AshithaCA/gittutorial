import tkinter as tk
import re

# Function to validate email using regular expression
def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

# Function to validate password using regular expression
def validate_password(password):
    regex = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{8,}$'
    return re.match(regex, password)

# Function to handle form submission
def submit():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not validate_email(email):
        result_label.config(text="Invalid email address", fg="red")
    elif not validate_password(password):
        result_label.config(text="Weak password! Must contain at least 8 characters, one lowercase, one uppercase, one digit, and one special character.", fg="red")
    else:
        result_label.config(text=f"Registration successful for {username}!", fg="green")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Email label and entry
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Register", command=submit)
submit_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()