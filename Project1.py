import tkinter as tk  #Import the TKinter framework.
from tkinter import filedialog  #Import filedialog for file handling.
import csv  #Import csv framework.

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
        #This is window A.

        #.setup_frame is a frame, containg a label and prompts for the user to upload their file.
        self.setup_frame = tk.Frame(self)  #Set up frame.
        self.setup_frame.pack(fill=tk.BOTH, expand=True)  #Set up functionality of page.

        self.setup_label = tk.Label(self.setup_frame, text="Upload the list of allowed names")	#Prompt user for the list/file.
        self.setup_label.pack(pady=10)  #Set up the functionality of the label... i.e, how it responds when windown is expanded ect...

        self.setup_button = tk.Button(self.setup_frame, text="Upload File", command=self.upload_file)	#Create the button for UPLOAD file.
        self.setup_button.pack(pady=5)  #Creates the visual aspect of the button... spacing ect... 

        self.run_button = tk.Button(self.setup_frame, text="Run", command=self.show_check_in_page, state=tk.DISABLED)  #Create the RUN buttom
        self.run_button.pack(pady=5)  #Creates the visual aspect of the button... spacing ect...

        # Check-in Page UI
	# This is window B.
        self.check_in_frame = tk.Frame(self)  #Set up the frame.

        self.name_label = tk.Label(self.check_in_frame, text="Enter Your Name:")  #Set up the display to "Enter your name".
        self.name_label.pack(pady=10)  #Create the visual aspect of the button... spacing ect...

        self.name_entry = tk.Entry(self.check_in_frame)  #Capture the name for processing.
        self.name_entry.pack(pady=5)  #Create the visual aspect of the object on the screen.

        self.check_button = tk.Button(self.check_in_frame, text="Check", command=self.check_name)  #Create the Check object.
        self.check_button.pack(pady=5)  #Create the visual aspect of the check sign... maybe?? lol

        self.result_label = tk.Label(self.check_in_frame, text="")  #This is where the check or X will be displayed.
        self.result_label.pack(pady=10)  #Create the visual aspect of the area. 

        self.close_button = tk.Button(self.check_in_frame, text="Close", command=self.show_setup_page)  #Create the CLOSE button towards the bottom.
        self.close_button.pack(side=tk.BOTTOM, padx=10, pady=10)  #Create the visual aspect of the button.

    #Here is the function that will upload a file:)
    def upload_file(self):
        
        #This is pretty cool... This line opens a file dialog window. The filetypes define the types of files the program will accept.
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
		
	#Check to see if file_path has been set successfully.
        if file_path:
            self.allowed_names = self.read_names_from_file(file_path)  #Load the names in from the file into the allowed_names array.

	    #Check if allowed_names is not null/empty/
            if self.allowed_names:
                self.run_button.config(state=tk.NORMAL)  #Set the state of the run buttom to NORMAL.

    #Function that reads the names from a file.
    def read_names_from_file(self, file_path):
        allowed_names = []  #Create a copy of allowed_names.

        #Try to open the file and loop through the names.
        try:
            #Open the file with the give path.
            with open(file_path, newline="") as file: 
                reader = csv.reader(file)  #Open a reader obj and pass it the file path.
	
		#Loop through the rows in the file
                for row in reader:
                    allowed_names.extend(row)  #Add the content of the col to the allowed_names array.

	#Create an exception case if I can't open the file.
        except Exception as exceptionA:
            print("Error reading file:", exceptionA)  #Display the exception that was caught.
        return allowed_names  #Return the array of names.

    #Function to display the check in page.
    def show_check_in_page(self):
        self.setup_frame.pack_forget()  #Clear the screen... getting ready to switch screens.
        self.check_in_frame.pack(fill=tk.BOTH, expand=True)  #Create the new window.

    #Function to display the set-up/landing page.
    def show_setup_page(self):
        self.check_in_frame.pack_forget()  #Clear the page... get ready to switch the screens.
        self.setup_frame.pack(fill=tk.BOTH, expand=True)  #Set up the new screen.

    #Function that checks the name of the user.
    def check_name(self):
        name = self.name_entry.get().strip()  #Strip the name of leading whitespace 

	#Check to see if the name entered is in the list of names
        if name in self.allowed_names:
            self.result_label.config(text="✅ Name found", fg="green")  #If so, display the correct sign: a green check mark.

	#Default case if the name is not in the list.
        else:
            self.result_label.config(text="❌ Name not found", fg="red")  #If not, display the correct sign: a red X.

#Here is my main method for the class/file
if __name__ == "__main__":

    #NOTE: When you create an instance of a class like this, you automatically call it's constructor...
    #... That will create these pages and already have the landing page (window A) ready for the user for when .mainloop() is called.
    app = CheckInApp()  #Create a CheckInApp instance named app
    app.mainloop()  #Enter TKinter's event loop!
