import login
import fish
import tkinter as tk
# create a tkinter window
window = tk.Tk()
window.title("Fishing Game 2023")
window.geometry("500x500")

# set up a grid for the widgets
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# create a frame for the login selection screen
login_frame = tk.Frame(window)
login_frame.grid(row=1, column=0, sticky="nsew")
login_frame.columnconfigure(0, weight=1)
login_frame.columnconfigure(1, weight=3)

# create a frame for the signup selection screen
signup_frame = tk.Frame(window)
signup_frame.grid(row=1, column=0, sticky="nsew")
signup_frame.columnconfigure(0, weight=1)
signup_frame.columnconfigure(1, weight=3)

# create a frame for the leaderboard display screen
score_frame = tk.Frame(window)
score_frame.grid(row=1, column=0, sticky="nsew")

# create a frame for the game
game_frame = tk.Frame(window)
game_frame.grid(row=1, column=0, sticky="nsew")
game_frame.columnconfigure(0, weight=1)
game_frame.rowconfigure(0, weight=1)

# create a frame for the bucket
bucket_frame = tk.Frame(window)
bucket_frame.grid(row=1, column=0, sticky="nsew")
bucket_frame.columnconfigure(0, weight=1)

# create the widgets for the login selection screen
tk.Label(login_frame, text="Username").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)
tk.Label(login_frame, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

# create the widgets for the signup selection screen
tk.Label(signup_frame, text="Username").grid(row=0, column=0)
username_entry2 = tk.Entry(signup_frame)
username_entry2.grid(row=0, column=1)
tk.Label(signup_frame, text="Password").grid(row=1, column=0)
password_entry1 = tk.Entry(signup_frame, show="*")
password_entry1.grid(row=1, column=1)
tk.Label(signup_frame, text="Re-enter Password").grid(row=2, column=0)
password_entry2 = tk.Entry(signup_frame, show="*")
password_entry2.grid(row=2, column=1)

# create the widgets for the leaderboard display screen
score_text = tk.Text(score_frame)
score_text.grid(row=0, column=0, sticky="nsew")

# create the widgets for the game
score_label = tk.Label(game_frame, text="Current Score: 0")
score_label.grid(row=0, column=0, sticky="w")
cast_button = tk.Button(game_frame, text="Cast a line!")
cast_button.grid(row=1, column=0, pady=10)
keep_button = tk.Button(game_frame, text="Keep", state="disabled")
keep_button.grid(row=1, column=1, padx=5)
release_button = tk.Button(game_frame, text="Release", state="disabled")
release_button.grid(row=1, column=2, padx=5)
bucket_button = tk.Button(game_frame, text="Bucket", state="disabled")
bucket_button.grid(row=1, column=3, padx=5)
image_label = tk.Label(game_frame)
image_label.grid(row=2, column=0, columnspan=4, pady=10)

# create the widgets for the bucket
bucket_label = tk.Label(bucket_frame, text="Bucket")
bucket_label.grid(row=0, column=0, sticky="w")
bucket_text = tk.Text(bucket_frame, height=10, width=50)
bucket_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
empty_button = tk.Button(bucket_frame, text="Empty bucket", state="disabled")
empty_button.grid(row=2, column=0, pady=10)

# create the widgets for the information display
info_label = tk.Label(window, text="Information:")
info_label.grid(row=2, column=0, sticky="w")
info_text = tk.Text(window, height=5, width=50)
info_text.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

window.mainloop()

