import tkinter as tk
from tkinter import messagebox

from action_manager import UndoRedoSystem


class App:
    def __init__(self, root):
        self.system = UndoRedoSystem()

        self.root = root
        self.root.title("Sistema Undo / Redo")
        self.root.geometry("700x500")

        title = tk.Label(
            root,
            text="Sistema de Edición con Undo/Redo",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        add_button = tk.Button(
            button_frame,
            text="Agregar Acción",
            command=self.add_action
        )
        add_button.grid(row=0, column=0, padx=5)

        undo_button = tk.Button(
            button_frame,
            text="Undo",
            command=self.undo_action
        )
        undo_button.grid(row=0, column=1, padx=5)

        redo_button = tk.Button(
            button_frame,
            text="Redo",
            command=self.redo_action
        )
        redo_button.grid(row=0, column=2, padx=5)

        self.output = tk.Text(root, height=20, width=70)
        self.output.pack(pady=10)

        self.update_display()

    def add_action(self):
        action = self.entry.get()

        try:
            self.system.add_action(action)
            self.entry.delete(0, tk.END)
            self.update_display()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def undo_action(self):
        try:
            self.system.undo()
            self.update_display()

        except Exception as e:
            messagebox.showwarning("Undo", str(e))

    def redo_action(self):
        try:
            self.system.redo()
            self.update_display()

        except Exception as e:
            messagebox.showwarning("Redo", str(e))

    def update_display(self):
        self.output.delete("1.0", tk.END)

        current = self.system.get_current_state()
        undo = self.system.get_history()
        redo = self.system.get_redo_history()

        text = "ESTADO ACTUAL:\\n"
        text += "\\n".join(current)

        text += "\\n\\nHISTORIAL UNDO:\\n"
        text += "\\n".join(undo)

        text += "\\n\\nHISTORIAL REDO:\\n"
        text += "\\n".join(redo)

        self.output.insert(tk.END, text)