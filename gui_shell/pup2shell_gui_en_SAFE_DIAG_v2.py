
import tkinter as tk
from tkinter import messagebox
import os
import subprocess

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def open_markdown(file_name):
    path = os.path.join(PROJECT_DIR, file_name)
    if os.path.exists(path):
        try:
            subprocess.Popen(["code", path], shell=True)
        except Exception as e:
            messagebox.showerror("Ошибка открытия .md", f"Не удалось открыть файл: {path}\n{e}")
    else:
        messagebox.showerror("Ошибка открытия .md", f"Файл не найден: {path}")

def run_bat():
    path = os.path.join(PROJECT_DIR, "launch_pub3.bat")
    if os.path.exists(path):
        subprocess.Popen(path, shell=True)
    else:
        messagebox.showerror("Ошибка запуска .bat", f".BAT-файл не найден: {path}")

def open_html():
    messagebox.showinfo("Интерактивная версия", "Интерактивная версия ПУП доступна в платном модуле, стоимость 15$")

root = tk.Tk()
root.title("Pub3: GUI Shell")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Pub3: GUI Shell", font=("Helvetica", 14, "bold")).pack(pady=10)

tk.Button(frame, text="Открыть Shell Launcher (.md)", width=40,
          command=lambda: open_markdown("Pub3_shell_launcher.md")).pack(pady=5)

tk.Button(frame, text="Открыть TODO (.md)", width=40,
          command=lambda: open_markdown("TODO_Pub3.md")).pack(pady=5)

tk.Button(frame, text="Запустить .BAT", width=40,
          command=run_bat).pack(pady=5)

tk.Button(frame, text="Открыть экспорт HTML", width=40,
          command=open_html).pack(pady=5)

tk.Button(frame, text="Выход", width=40,
          command=root.quit).pack(pady=10)

root.mainloop()
