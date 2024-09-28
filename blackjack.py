import tkinter as tk
from tkinter import ttk

# Function to handle the submission of the survey
def submit_survey():
    first_name = ''.join([var.get() for var in first_name_vars])
    last_name = ''.join([var.get() for var in last_name_vars])
    street_name = street_name_var.get()
    town_name = town_name_var.get()
    house_number = house_number_var.get()
    zip_code = zip_code_var.get()
    print(f"First Name: {first_name}, Last Name: {last_name}, Street: {street_name}, Town: {town_name}, House Number: {house_number}, Zip Code: {zip_code}")
    # You can add more logic here to save the data or process it further

# Function to show a specific frame
def show_frame(frame):
    frame.tkraise()

# Function to generate letter dropdowns based on the selected number of letters
def generate_letter_dropdowns(frame, num_letters_var, letter_vars, letter_frame):
    for widget in letter_frame.winfo_children():
        widget.destroy()
    
    num_letters = int(num_letters_var.get())
    letter_vars.clear()
    letter_vars.extend([tk.StringVar() for _ in range(num_letters)])
    
    for i in range(num_letters):
        ttk.Label(letter_frame, text=f"Letter {i + 1}:").grid(column=0, row=i, padx=10, pady=5)
        ttk.OptionMenu(letter_frame, letter_vars[i], None, *[chr(j) for j in range(65, 91)]).grid(column=1, row=i, padx=10, pady=5)
    

# Create the main application window
root = tk.Tk()
root.title("IRS Tax Survey")

# Create variables to store user input
num_first_letters_var = tk.StringVar()
num_last_letters_var = tk.StringVar()
street_name_var = tk.StringVar()
town_name_var = tk.StringVar()
house_number_var = tk.StringVar(value="1")
zip_code_var = tk.StringVar(value="00000")

# Create a container frame to hold all the pages
container = ttk.Frame(root)
container.grid(row=0, column=0, sticky="nsew")

# Create frames for each page
page1 = ttk.Frame(container)
page2 = ttk.Frame(container)
page3 = ttk.Frame(container)
page4 = ttk.Frame(container)
page5 = ttk.Frame(container)

for frame in (page1, page2, page3, page4, page5):
    frame.grid(row=0, column=0, sticky="nsew")

# Page 1: Number of letters in the first and last name
ttk.Label(page1, text="Number of letters in your first name:").grid(column=0, row=0, padx=10, pady=5)
ttk.OptionMenu(page1, num_first_letters_var, None, *[str(i) for i in range(1, 21)]).grid(column=1, row=0, padx=10, pady=5)

ttk.Label(page1, text="Number of letters in your last name:").grid(column=0, row=1, padx=10, pady=5)
ttk.OptionMenu(page1, num_last_letters_var, None, *[str(i) for i in range(1, 21)]).grid(column=1, row=1, padx=10, pady=5)

ttk.Button(page1, text="Next", command=lambda: [generate_letter_dropdowns(page2, num_first_letters_var, first_name_vars, first_name_frame), generate_letter_dropdowns(page2, num_last_letters_var, last_name_vars, last_name_frame), show_frame(page2)]).grid(column=1, row=2, pady=10)

# Page 2: First and last name letter selection
first_name_frame = ttk.Frame(page2)
first_name_frame.grid(column=0, row=0, columnspan=2, padx=10, pady=5)
first_name_vars = []

last_name_frame = ttk.Frame(page2)
last_name_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=5)
last_name_vars = []

ttk.Button(page2, text="Back", command=lambda: show_frame(page1)).grid(column=0, row=2, pady=10)
ttk.Button(page2, text="Next", command=lambda: show_frame(page5)).grid(column=1, row=2, pady=10)

# Page 5: Address input
ttk.Label(page5, text="Town Name:").grid(column=0, row=0, padx=10, pady=5)
ttk.Entry(page5, textvariable=street_name_var).grid(column=1, row=0, padx=10, pady=5)

ttk.Label(page5, text="Street Name:").grid(column=0, row=1, padx=10, pady=5)
ttk.Entry(page5, textvariable=town_name_var).grid(column=1, row=1, padx=10, pady=5)

ttk.Label(page5, text="House Number:").grid(column=0, row=2, padx=10, pady=5)
tk.Spinbox(page5, from_=1, to=1000, textvariable=house_number_var, state='readonly').grid(column=1, row=2, padx=10, pady=5)

ttk.Label(page5, text="Zip Code:").grid(column=0, row=3, padx=10, pady=5)
tk.Spinbox(page5, from_=0, to=99999, textvariable=zip_code_var, state='readonly').grid(column=1, row=3, padx=10, pady=5)

ttk.Button(page5, text="Submit", command=submit_survey).grid(column=1, row=4, pady=10)
ttk.Button(page5, text="Back", command=lambda: show_frame(page4)).grid(column=0, row=4, pady=10)

# Show the first page initially
show_frame(page1)

# Start the main event loop
root.mainloop()

