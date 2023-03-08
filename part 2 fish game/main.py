import tkinter as tk
from fish import Game
from gui import GameScreen
from login import LoginScreen
from UserBase import UserBase

def login():
    def handle_login():
        username = login_screen.username_entry.get()
        password = login_screen.password_entry.get()
        if userbase.check_password(username, password):
            login_screen.frame.destroy()
            game(userbase.get_user(username))
        else:
            login_screen.username_entry.delete(0, tk.END)
            login_screen.password_entry.delete(0, tk.END)
            login_screen.username_entry.focus()
            login_screen_error_label.config(text="Incorrect username or password")

    def handle_signup():
        login_screen.frame.destroy()
        signup()

    login_screen = LoginScreen(window, handle_login, handle_signup)
    login_screen_error_label = tk.Label(login_screen.frame, fg="red")
    login_screen_error_label.grid(row=3, column=0, columnspan=2)

def signup():
    def handle_signup():
        username = signup_screen.username_entry.get()
        password = signup_screen.password_entry.get()
        confirm_password = signup_screen.confirm_password_entry.get()
        if not username:
            signup_screen_error_label.config(text="Please enter a username")
        elif not password:
            signup_screen_error_label.config(text="Please enter a password")
        elif password != confirm_password:
            signup_screen_error_label.config(text="Passwords do not match")
        elif userbase.add_user(username, password):
            signup_screen.frame.destroy()
            game(userbase.get_user(username))
        else:
            signup_screen_error_label.config(text="Username already taken")

    def handle_cancel():
        signup_screen.frame.destroy()
        login()

    signup_screen = LoginScreen(window, handle_signup, handle_cancel)
    signup_screen.frame.grid()
    signup_screen.frame.columnconfigure(2, weight=1)
    signup_screen.frame.rowconfigure(2, minsize=20)
    tk.Label(signup_screen.frame, text="Confirm Password").grid(row=2, column=0)
    signup_screen.confirm_password_entry = tk.Entry(signup_screen.frame, show="*")
    signup_screen.confirm_password_entry.grid(row=2, column=1)
    signup_screen_error_label = tk.Label(signup_screen.frame, fg="red")
    signup_screen_error_label.grid(row=3, column=0, columnspan=3)

def game(user):
    def handle_cast():
        game.cast_line()

    def handle_keep():
        game.keep_fish()

    def handle_release():
        game.release_fish()

    def handle_bucket():
        game.empty_bucket()

    window.geometry("800x600")
    game_screen = GameScreen(window, handle_cast, handle_keep, handle_release, handle_bucket)
    game = Game()
    game.player_name = user.username
    game.cast_button = game_screen.cast_button
    game.keep_button = game_screen.keep_button
    game.release_button = game_screen.release_button
    game.bucket_button = game_screen.bucket_button
    game.bucket_text = game_screen.bucket_text
    game.empty_button = game_screen.empty_button
    game.score_label = game_screen.score_label
    game.info_text = game_screen.info_text
    game_screen.player_label.config(text=f"Player: {game.player_name}")
    game.update_score_label()
    game_screen.frame.grid()
    window.mainloop()

if __name__ == "__main__":
    userbase = UserBase()
    window = tk.Tk()
    window.title("Fishing Game")
    login()