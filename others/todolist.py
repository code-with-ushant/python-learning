import customtkinter as ctk
import json
import os

TASKS_FILE = "tasks.json"


class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("500x500")
        ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
        ctk.set_default_color_theme("blue")  # You can change to "green", "dark-blue", etc.

        self.task_list = []

        # UI Components
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=20, padx=10, fill="x")

        self.task_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter new task...")
        self.task_entry.pack(side="left", expand=True, fill="x", padx=(10, 5))

        self.add_button = ctk.CTkButton(self.input_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side="left", padx=5)

        self.task_frame = ctk.CTkScrollableFrame(self, height=350)
        self.task_frame.pack(padx=10, fill="both", expand=True)

        self.theme_button = ctk.CTkButton(self, text="Toggle Theme", command=self.toggle_theme)
        self.theme_button.pack(pady=10)

        # Load saved tasks
        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            task_data = {"text": task_text, "completed": False}
            self.task_list.append(task_data)
            self.display_tasks()
            self.task_entry.delete(0, ctk.END)
            self.save_tasks()

    def display_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.task_list):
            task_row = ctk.CTkFrame(self.task_frame)
            task_row.pack(fill="x", pady=5, padx=5)

            var = ctk.BooleanVar(value=task["completed"])

            checkbox = ctk.CTkCheckBox(
                task_row, text=task["text"], variable=var,
                command=lambda i=index, v=var: self.toggle_task(i, v)
            )
            checkbox.pack(side="left", expand=True, fill="x", padx=(5, 10))

            del_button = ctk.CTkButton(task_row, text="❌", width=40,
                                       command=lambda i=index: self.delete_task(i))
            del_button.pack(side="right", padx=(0, 5))

            if task["completed"]:
                checkbox.configure(text_color="gray")
                checkbox.select()

    def toggle_task(self, index, var):
        self.task_list[index]["completed"] = var.get()
        self.save_tasks()
        self.display_tasks()

    def delete_task(self, index):
        del self.task_list[index]
        self.save_tasks()
        self.display_tasks()

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.task_list, f, indent=4)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.task_list = json.load(f)
        self.display_tasks()

    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        ctk.set_appearance_mode("Light" if current == "Dark" else "Dark")


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
