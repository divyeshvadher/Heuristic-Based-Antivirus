import tkinter as tk
from tkinter import filedialog, messagebox
from scanner import scan_file, scan_directory

class AntivirusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heuristic Antivirus Scanner")
        self.geometry("800x500")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Heuristic Antivirus Scanner", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.scan_file_btn = tk.Button(self, text="Scan File", command=self.scan_file)
        self.scan_file_btn.pack(pady=10)

        self.scan_dir_btn = tk.Button(self, text="Scan Directory", command=self.scan_directory)
        self.scan_dir_btn.pack(pady=10)

        self.result_text = tk.Text(self, height=10, width=60)
        self.result_text.pack(pady=20)

    def scan_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            suspicious = scan_file(file_path)
            status = "Suspicious" if suspicious else "Clean"
            self.result_text.insert(tk.END, f"{file_path} [{status}]\n")

    def scan_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            results = scan_directory(directory_path)
            for file_path, suspicious in results:
                status = "Suspicious" if suspicious else "Clean"
                self.result_text.insert(tk.END, f"{file_path} [{status}]\n")

if __name__ == "__main__":
    app = AntivirusApp()
    app.mainloop()
