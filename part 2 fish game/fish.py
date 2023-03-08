import random
import tkinter as tk
from tkinter import messagebox

class Fish:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.name}, {self.weight} kg, ${self.value}"

class Game:
    def __init__(self):
        self.player_name = ""
        self.current_score = 0
        self.cast_button = None
        self.keep_button = None
        self.release_button = None
        self.bucket_button = None
        self.bucket_text = None
        self.empty_button = None
        self.score_label = None
        self.info_text = None
        self.current_fish = None
        self.bucket = []

    def update_score_label(self):
        self.score_label.config(text=f"Current Score: {self.current_score}")

    def update_info_text(self, message):
        self.info_text.insert(tk.END, f"{message}\n")
        self.info_text.see(tk.END)

    def cast_line(self):
        fish_types = ["Bream", "Carp", "Perch", "Pike", "Trout"]
        fish_weights = [random.uniform(0.1, 5) for _ in range(len(fish_types))]
        fish_values = [round(random.uniform(1, 20), 2) for _ in range(len(fish_types))]
        fish_list = [Fish(fish_types[i], fish_weights[i], fish_values[i]) for i in range(len(fish_types))]
        self.current_fish = random.choice(fish_list)
        self.update_info_text(f"You caught a {self.current_fish.name} weighing {self.current_fish.weight:.2f} kg")
        self.cast_button.config(state="disabled")
        self.keep_button.config(state="normal")
        self.release_button.config(state="normal")

    def keep_fish(self):
        self.bucket.append(self.current_fish)
        self.current_score += self.current_fish.value
        self.update_score_label()
        self.update_info_text(f"You added a {self.current_fish.name} weighing {self.current_fish.weight:.2f} kg to your bucket")
        self.cast_button.config(state="normal")
        self.keep_button.config(state="disabled")
        self.release_button.config(state="disabled")
        self.bucket_button.config(state="normal")

    def release_fish(self):
        self.update_info_text(f"You released a {self.current_fish.name} weighing {self.current_fish.weight:.2f} kg")
        self.cast_button.config(state="normal")
        self.keep_button.config(state="disabled")
        self.release_button.config(state="disabled")

    def empty_bucket(self):
        if len(self.bucket) == 0:
            messagebox.showinfo("Empty Bucket", "Your bucket is already empty!")
        else:
            bucket_info = ""
            total_value = 0
            for fish in self.bucket:
                bucket_info += f"{fish}\n"
                total_value += fish.value
            self.bucket = []
            self.current_score += total_value
            self.update_score_label()
            self.bucket_text.delete("1.0", tk.END)
            self.bucket_text.insert(tk.END, bucket_info)
            self.update_info_text("You emptied your bucket")
            self.bucket_button.config(state="disabled")

    def start_game(self):
        if not self.player_name:
            messagebox.showerror("Error", "Please enter a username before starting the game")
            return
        self.cast_button.config(state="normal")
        self.info_text.delete("1.0", tk.END)