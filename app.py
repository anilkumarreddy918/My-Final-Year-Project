import tkinter as tk
from tkinter import messagebox, ttk
import db

def submit():
    name = name_var.get().strip()
    subject = subject_var.get().strip()
    marks = marks_var.get().strip()

    if not name.isalpha():
        messagebox.showerror("Error", "Name must contain only letters.")
        return
    if not subject.isalpha():
        messagebox.showerror("Error", "Subject must contain only letters.")
        return
    if not marks.isdigit() or not (0 <= int(marks) <= 100):
        messagebox.showerror("Error", "Marks must be 0–100.")
        return

    db.insert_result(name, subject, int(marks))
    messagebox.showinfo("Success", "Record added.")
    clear_entries()

def clear_entries():
    name_var.set("")
    subject_var.set("")
    marks_var.set("")

def show_results():
    results = db.fetch_results()
    result_window = tk.Toplevel(root)
    result_window.title("Past Results")

    tree = ttk.Treeview(result_window, columns=("ID", "Name", "Subject", "Marks", "Achievement"), show="headings")
    for col in ("ID", "Name", "Subject", "Marks", "Achievement"):
        tree.heading(col, text=col, command=lambda _col=col: sort_column(tree, _col, False))
        tree.column(col, width=120)
    for row in results:
        tree.insert("", tk.END, values=row)
    tree.pack(fill="both", expand=True)

    btn_frame = tk.Frame(result_window)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Delete Selected", command=lambda: delete_selected(tree)).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Edit Selected", command=lambda: edit_selected(tree)).pack(side="left", padx=5)

def sort_column(tree, col, reverse):
    data_list = [(tree.set(item, col), item) for item in tree.get_children('')]
    data_list.sort(reverse=reverse)
    for index, (val, item) in enumerate(data_list):
        tree.move(item, '', index)
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))

def delete_selected(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No record selected.")
        return
    record_id = tree.item(selected[0])['values'][0]
    db.delete_result(record_id)
    tree.delete(selected[0])
    messagebox.showinfo("Deleted", "Record deleted successfully.")

def edit_selected(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No record selected.")
        return
    record = tree.item(selected[0])['values']

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Record")

    tk.Label(edit_window, text="Name").grid(row=0, column=0)
    name_edit = tk.Entry(edit_window)
    name_edit.insert(0, record[1])
    name_edit.grid(row=0, column=1)

    tk.Label(edit_window, text="Subject").grid(row=1, column=0)
    subject_edit = tk.Entry(edit_window)
    subject_edit.insert(0, record[2])
    subject_edit.grid(row=1, column=1)

    tk.Label(edit_window, text="Marks").grid(row=2, column=0)
    marks_edit = tk.Entry(edit_window)
    marks_edit.insert(0, record[3])
    marks_edit.grid(row=2, column=1)

    def save_changes():
        new_name = name_edit.get().strip()
        new_subject = subject_edit.get().strip()
        new_marks = marks_edit.get().strip()

        if not new_name.isalpha():
            messagebox.showerror("Error", "Name must contain only letters.")
            return
        if not new_subject.isalpha():
            messagebox.showerror("Error", "Subject must contain only letters.")
            return
        if not new_marks.isdigit() or not (0 <= int(new_marks) <= 100):
            messagebox.showerror("Error", "Marks must be 0–100.")
            return

        db.update_result(record[0], new_name, new_subject, int(new_marks))
        messagebox.showinfo("Updated", "Record updated successfully.")
        edit_window.destroy()

    tk.Button(edit_window, text="Save", command=save_changes).grid(row=3, column=0, columnspan=2)

root = tk.Tk()
root.title("Student Result Management")

name_var = tk.StringVar()
subject_var = tk.StringVar()
marks_var = tk.StringVar()

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=subject_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Marks").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=marks_var).grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Submit", command=submit).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Show Results", command=show_results).grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
