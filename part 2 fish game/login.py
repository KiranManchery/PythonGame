import tkinter as tk

class LoginScreen:
    def __init__(self, window, login_handler, signup_handler):
        # create a frame for the login screen
        self.frame = tk.Frame(window)
        self.frame.grid(row=1, column=0, sticky="nsew")
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)

        # create the widgets for the login screen
        tk.Label(self.frame, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)
        tk.Label(self.frame, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # create the buttons for the login screen
        login_button = tk.Button(self.frame, text="Login", command=login_handler)
        login_button.grid(row=2, column=0, pady=10)
        signup_button = tk.Button(self.frame, text="Signup", command=signup_handler)
        signup_button.grid(row=2, column=1, pady=10)