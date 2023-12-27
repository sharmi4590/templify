from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw

root = Tk()
root.title('Templify.com - Add Text To Images')
root.geometry("600x650")

# Function to open the file dialog and get the image
def open_image():
    global my_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    my_image = Image.open(file_path)
    my_label.config(image="")  # Clear existing image
    my_label.config(image=my_image)

# Function to add text to the image and save it
def add_it():
    if "my_image" in globals():
        # Get text to add to image
        text_to_add = my_entry.get()

        # Edit the Image
        edit_image = ImageDraw.Draw(my_image)
        edit_image.text((150, 300), text_to_add, fill="green")
        my_image.show()

        # Save The Image
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            my_image.save(file_path)

        # Clear the entry box
        my_entry.delete(0, END)
        my_entry.insert(0, "Saving File...")

        # Wait a couple of seconds and then show the new image
        my_label.after(2000, lambda: my_label.config(image=""))
    else:
        my_entry.insert(0, "Please select an image first!")

# Create A Label
my_label = Label(root)
my_label.pack(pady=20)

# Button to open the file dialog and get the image
open_button = Button(root, text="Open Image", command=open_image, font=("Helvetica", 24))
open_button.pack(pady=10)

# Entry Box
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=10)

# Button to add text to the image and save it
my_button = Button(root, text="Add Text To Image", command=add_it, font=("Helvetica", 24))
my_button.pack(pady=10)

root.mainloop()
