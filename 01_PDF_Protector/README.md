# PDF Password Protector

A simple, user-friendly GUI-based tool to add password protection to one or multiple PDF files. Built using Python, PyPDF2, and Tkinter, this application is designed to ensure your PDF documents are securely encrypted with minimal effort.

---

## 🔒 Features

- ✅ Select single or multiple PDF files
- 🔐 Set a password to lock the PDFs
- 💾 Encrypted files are saved separately to preserve originals
- 🖥️ Simple and clean GUI interface (no terminal needed)


## 🚀 How to Run
### ⚡ Easiest Way — Just Run the App (Windows only)

1. **Download the `.exe` file** from the [Download](https://github.com/Nazmussakib247/ScriptForge-By-Sakib/blob/main/01_PDF_Protector/PDF_Protector.exe).
2. Double-click the file to launch the app — no installation or Python required.

✅ No coding needed. Just click and use.

---

### 🔧 From Source Code

1. **Install Python (if not already):**  
   Download and install Python 3.x from [python.org](https://www.python.org/)

2. **Install required packages:**

````
   pip install PyPDF2
````

3. **Run the script:**

   ```
   python pdf_protector.py
   ```

---

### 📦 Create Standalone `.exe` (Optional)

> Only for Windows users who want a standalone executable version.

1. **Install PyInstaller:**

   ```
   pip install pyinstaller
   ```

2. **Generate `.exe`:**

   ```
   pyinstaller --onefile --windowed --icon=icon.ico pdf_protector.py
   ```

3. The `.exe` file will be located in the `dist/` folder.

---

## 📂 Folder Structure

```
01_PDF_Protector/
│
├── pdf_protector.py      # Main script
├── icon.ico              # App icon (optional)
├── README.md             # Project description
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
├── dist/                 # Output folder for .exe (ignored in Git)
├── build/                # Build temp files (ignored in Git)
```

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 🙌 Author

[**Nazmus Sakib**](https://github.com/Nazmussakib247)
*Crafted with care using Python 🐍*

---

## 🤝 Contributions

Feel free to open issues or submit pull requests for improvements and new features!
