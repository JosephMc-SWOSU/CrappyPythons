import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Create the main application window
root = tk.Tk()
root.title("IRS Tax Filing Free Version")  # Set the window title
root.geometry("1000x1000")  # Set the window size to 1000x1000 pixels

# Create a container frame to hold all the pages
container = ttk.Frame(root)
container.grid(row=0, column=0, sticky="nsew")

# Create frames for each page
page0 = ttk.Frame(container)
page1 = ttk.Frame(container)
page2 = ttk.Frame(container)
page3 = ttk.Frame(container)
page4 = ttk.Frame(container)
page5 = ttk.Frame(container)

# Page List
pages = [page0, page1, page2, page3, page4, page5]

current_page = 0

# Function to move to the next page
def next_page():
    global current_page
    current_page = (current_page + 1) % len(pages)
    pages[current_page].tkraise()

# Make all frames expand to fill the window
for frame in pages:
    frame.grid(row=0, column=0, sticky="nsew")

# Function to generate letter dropdowns based on the selected number of letters
def generate_letter_dropdowns(frame, num_letters_var, letter_vars, letter_frame):
    for widget in letter_frame.winfo_children():
        widget.destroy()  # Clear existing widgets
    num_letters = int(num_letters_var.get())
    letter_vars.clear()
    letter_vars.extend([tk.StringVar() for _ in range(num_letters)])
    for i in range(num_letters):
        ttk.Label(letter_frame, text=f"Letter {i + 1}:").grid(column=0, row=i, padx=10, pady=5)
        ttk.OptionMenu(letter_frame, letter_vars[i], None, *[chr(j) for j in range(65, 91)]).grid(column=1, row=i, padx=10, pady=5)

# Create variables to store user input
num_first_letters_var = tk.StringVar()
num_last_letters_var = tk.StringVar()
street_name_var = tk.StringVar()
town_name_var = tk.StringVar()
house_number_var = tk.StringVar(value="1")
zip_code_var = tk.StringVar(value="00000")

# Page 0: Image and option boxes
# Load the image
image_path = "C:/Users/joseph/Documents/Github/Pythons/CrappyPythons/realirs.png"
image = Image.open(image_path)
resized_image = image.resize((975, 520), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Configure grid weights to center the image
page0.grid_columnconfigure(0, weight=1)
page0.grid_columnconfigure(1, weight=1)
page0.grid_rowconfigure(0, weight=1)
page0.grid_rowconfigure(1, weight=1)

# Create a label to display the image
image_label = ttk.Label(page0, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.grid(row=0, column=0, padx=10, pady=10)

# Create a label to display the message
message_label = ttk.Label(page0, font=("Helvetica", 14), text="Welcome to the IRS Tax Filing Free Version. Please click 'Next' to proceed.")
message_label.grid(row=1, column=0, padx=10, pady=10)

# Create a button to move to the next page
next_button = ttk.Button(page0, text="Next", command=next_page)
next_button.grid(row=2, column=0, padx=10, pady=10)

# Page 1: Number of letters in the first and last name
page1.grid_columnconfigure(0, weight=1)
page1.grid_columnconfigure(1, weight=1)
page1.grid_rowconfigure(0, weight=1)
page1.grid_rowconfigure(1, weight=1)
page1.grid_rowconfigure(2, weight=1)

ttk.Label(page1, text="Number of letters in your first name:", font=("Helvetica", 14)).grid(column=0, row=0, padx=10, pady=10, sticky="e")
ttk.OptionMenu(page1, num_first_letters_var, None, *[str(i) for i in range(1, 21)]).grid(column=1, row=0, padx=10, pady=10, sticky="w")
ttk.Label(page1, text="Number of letters in your last name:", font=("Helvetica", 14)).grid(column=0, row=1, padx=10, pady=10, sticky="e")
ttk.OptionMenu(page1, num_last_letters_var, None, *[str(i) for i in range(1, 21)]).grid(column=1, row=1, padx=10, pady=10, sticky="w")

# Create a button to move to the next page
next_button = ttk.Button(page1, text="Next", command=lambda: [generate_letter_dropdowns(page2, num_first_letters_var, first_name_vars, first_name_frame), generate_letter_dropdowns(page2, num_last_letters_var, last_name_vars, last_name_frame), next_page()])
next_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Page 2: First and last name letter selection
page2.grid_columnconfigure(0, weight=1)
page2.grid_columnconfigure(1, weight=1)
page2.grid_rowconfigure(0, weight=1)
page2.grid_rowconfigure(1, weight=1)
page2.grid_rowconfigure(2, weight=1)
page2.grid_rowconfigure(3, weight=1)
page2.grid_rowconfigure(4, weight=1)

ttk.Label(page2, text="Select the letters in your first name:", font=("Helvetica", 14)).grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky="n")
first_name_frame = ttk.Frame(page2)
first_name_frame.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky="n")
first_name_vars = []

ttk.Label(page2, text="Select the letters in your last name:", font=("Helvetica", 14)).grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky="n")
last_name_frame = ttk.Frame(page2)
last_name_frame.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky="n")
last_name_vars = []

# Create a button to move to the next page
next_button = ttk.Button(page2, text="Next", command=next_page)
next_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky="n")

# Page 3: State selection
# List of state names
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Function to update the state message
def update_state_message():
    state_name.set(random.choice(states))

# Function to handle the Yes button click
def yes_button_click():
    no_button.grid_remove()

# Create a StringVar to hold the state name
state_name = tk.StringVar(value=random.choice(states))

# Configure grid weights to center the widgets
page3.grid_columnconfigure(0, weight=1)
page3.grid_columnconfigure(1, weight=1)
page3.grid_columnconfigure(2, weight=1)
page3.grid_rowconfigure(0, weight=1)
page3.grid_rowconfigure(1, weight=1)
page3.grid_rowconfigure(2, weight=1)

# Create a label to display the state message
state_message_label = ttk.Label(page3, text="Your selected state is:", font=("Helvetica", 14))
state_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Create a label to display the state name
state_name_label = ttk.Label(page3, textvariable=state_name, font=("Helvetica", 14, "bold"), width=20, anchor="w")
state_name_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Create the Yes button
yes_button = ttk.Button(page3, text="Yes", command=yes_button_click)
yes_button.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Create the No button
no_button = ttk.Button(page3, text="No", command=update_state_message)
no_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Create a button to move to the next page
next_button = ttk.Button(page3, text="Next", command=next_page)
next_button.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Page 4: ZIP Code selection
# Configure grid weights to center the widgets
page4.grid_columnconfigure(0, weight=1)
page4.grid_columnconfigure(1, weight=1)
page4.grid_columnconfigure(2, weight=1)
page4.grid_rowconfigure(0, weight=1)
page4.grid_rowconfigure(1, weight=1)
page4.grid_rowconfigure(2, weight=1)
page4.grid_rowconfigure(3, weight=1)

# Function to update the ZIP Code based on the input numbers
def update_zip_code(*args):
    try:
        num1 = int(num1_var.get())
        num2 = int(num2_var.get())
        zip_code_var.set(str(num1 * num2))
    except ValueError:
        zip_code_var.set("Invalid input")

# Create StringVars to hold the input numbers
num1_var = tk.StringVar()
num2_var = tk.StringVar()

# Trace changes to the input variables to update the ZIP Code
num1_var.trace_add("write", update_zip_code)
num2_var.trace_add("write", update_zip_code)

# Create labels and entry boxes for the input numbers
ttk.Label(page4, text="Enter first number:", font=("Helvetica", 14)).grid(column=0, row=0, padx=10, pady=10, sticky="e")
ttk.Entry(page4, textvariable=num1_var, font=("Helvetica", 14)).grid(column=1, row=0, padx=10, pady=10, sticky="w")

ttk.Label(page4, text="Enter second number:", font=("Helvetica", 14)).grid(column=0, row=1, padx=10, pady=10, sticky="e")
ttk.Entry(page4, textvariable=num2_var, font=("Helvetica", 14)).grid(column=1, row=1, padx=10, pady=10, sticky="w")

# Create a label to display the ZIP Code
ttk.Label(page4, text="ZIP Code:", font=("Helvetica", 14)).grid(column=0, row=2, padx=10, pady=10, sticky="e")
ttk.Entry(page4, textvariable=zip_code_var, font=("Helvetica", 14), state="readonly").grid(column=1, row=2, padx=10, pady=10, sticky="w")

# Create a button to move to the next page
next_button = ttk.Button(page4, text="Next", command=next_page)
next_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Raise page0 to the top to make it the first page shown
page0.tkraise()

# Start the main event loop
root.mainloop()
