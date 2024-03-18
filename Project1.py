import tkinter as tk
from tkinter import filedialog
import csv

#Here is the class definition for my Check-In App. 
#tk.TK is noting that CheckInApp will inherit from tk.TK. 
class CheckInApp(tk.Tk):

    #Here is my constructor. This will set up the main window("TK"), sets the... 
    #... title, geometry and initializes vavriables needed for the app.
    def __init__(self):
        super().__init__()
        self.title("Event Check-in App")
        self.geometry("400x200")

        # Variables
        self.allowed_names = []

        # Setup Page UI
        
        #.setup_frame is a frame, containg a label, and prompts for the user to enter
        self.setup_frame = tk.Frame(self)
        self.setup_frame.pack(fill=tk.BOTH, expand=True)

        self.setup_label = tk.Label(self.setup_frame, text="Upload the list of allowed names")
        self.setup_label.pack(pady=10)

        self.setup_button = tk.Button(self.setup_frame, text="Upload File", command=self.upload_file)
        self.setup_button.pack(pady=5)

        self.run_button = tk.Button(self.setup_frame, text="Run", command=self.show_check_in_page, state=tk.DISABLED)
        self.run_button.pack(pady=5)

        # Check-in Page UI
        self.check_in_frame = tk.Frame(self)

        self.name_label = tk.Label(self.check_in_frame, text="Enter Your Name:")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.check_in_frame)
        self.name_entry.pack(pady=5)

        self.check_button = tk.Button(self.check_in_frame, text="Check", command=self.check_name)
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(self.check_in_frame, text="")
        self.result_label.pack(pady=10)

        self.close_button = tk.Button(self.check_in_frame, text="Close", command=self.show_setup_page)
        self.close_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
        if file_path:
            self.allowed_names = self.read_names_from_file(file_path)
            if self.allowed_names:
                self.run_button.config(state=tk.NORMAL)

    def read_names_from_file(self, file_path):
        allowed_names = []
        try:
            with open(file_path, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    allowed_names.extend(row)
        except Exception as e:
            print("Error reading file:", e)
        return allowed_names

    def show_check_in_page(self):
        self.setup_frame.pack_forget()
        self.check_in_frame.pack(fill=tk.BOTH, expand=True)

    def show_setup_page(self):
        self.check_in_frame.pack_forget()
        self.setup_frame.pack(fill=tk.BOTH, expand=True)

    def check_name(self):
        name = self.name_entry.get().strip()
        if name in self.allowed_names:
            self.result_label.config(text="✅ Name found", fg="green")
        else:
            self.result_label.config(text="❌ Name not found", fg="red")

if __name__ == "__main__":
    app = CheckInApp()
    app.mainloop()
