import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import requests
from PIL import Image, ImageTk
import io

# Function to handle sending a Line Sticker
def send_line_sticker(package_id, sticker_id):
    # Your code to send a Line Sticker using the package_id and sticker_id
    # This is a placeholder
    print(f"Sending Line Sticker with package_id: {package_id} and sticker_id: {sticker_id}")

# Function to handle sending a Local Image File
def send_local_image(file_path):
    # Your code to send a local image file
    # This is a placeholder
    print(f"Sending Local Image from file_path: {file_path}")

# Function to handle sending a Web Image File
def send_web_image(url):
    try:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        # Your code to process and send the web image
        # This is a placeholder
        print(f"Sending Web Image from URL: {url}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image from URL. Error: {e}")

# Function to handle the button press
def on_submit():
    choice = option_var.get()
    
    if choice == "Line Sticker":
        package_id = simpledialog.askstring("Input", "Enter Sticker Package ID:")
        sticker_id = simpledialog.askstring("Input", "Enter Sticker ID:")
        if package_id and sticker_id:
            send_line_sticker(package_id, sticker_id)
        else:
            messagebox.showwarning("Input Error", "Please provide both Package ID and Sticker ID.")
    
    elif choice == "Local Image File":
        file_path = filedialog.askopenfilename(title="Select Local Image File")
        if file_path:
            send_local_image(file_path)
        else:
            messagebox.showwarning("Input Error", "No file selected.")
    
    elif choice == "Web Image File":
        url = simpledialog.askstring("Input", "Enter Image URL:")
        if url:
            send_web_image(url)
        else:
            messagebox.showwarning("Input Error", "Please provide an Image URL.")
    else:
        messagebox.showwarning("Input Error", "Please select an option.")

# Create the main window
root = tk.Tk()
root.title("Image Sender")

# Create a variable for option selection
option_var = tk.StringVar(value="")

# Create the dropdown menu
dropdown = tk.OptionMenu(root, option_var, "Line Sticker", "Local Image File", "Web Image File")
dropdown.pack(pady=10)

# Create the Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)
# Run the application
root.mainloop()