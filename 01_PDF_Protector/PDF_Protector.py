import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

def protect_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not files:
        return

    password = password_entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    save_dir = filedialog.askdirectory(title="Select Folder to Save Protected PDFs")
    if not save_dir:
        return

    for file_path in files:
        try:
            reader = PdfReader(file_path)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)

            file_name = os.path.basename(file_path)
            new_path = os.path.join(save_dir, f"protected_{file_name}")

            with open(new_path, "wb") as f:
                writer.write(f)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to protect {file_path}\n\n{e}")
            continue

    messagebox.showinfo("Success", "All PDFs were successfully password protected!")

# GUI setup
root = tk.Tk()
root.title("PDF Password Protector")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="🔐 Enter password to protect selected PDFs:", font=("Arial", 12))
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
password_entry.pack()

protect_button = tk.Button(root, text="📂 Select PDFs & Protect", command=protect_pdfs, font=("Arial", 12), bg="#4CAF50", fg="white")
protect_button.pack(pady=20)

root.mainloop()