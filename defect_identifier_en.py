import cv2
import hashlib
import numpy as np
from tkinter import Tk, Button, Label, filedialog, messagebox

# Function to select a file path
def load_image_path(prompt):
    file_path = filedialog.askopenfilename(
        title=prompt,
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if not file_path:
        print(f"{prompt}: No file selected.")
        return None
    print(f"{prompt}: File successfully selected:", file_path)
    return file_path

# Function to compute the MD5 hash of a file
def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Function to compare two images
def compare_images(image1, image2):
    # Resize images to the same dimensions for comparison
    image1_resized = cv2.resize(image1, (300, 300))
    image2_resized = cv2.resize(image2, (300, 300))

    # Calculate the absolute difference between the images
    diff = cv2.absdiff(image1_resized, image2_resized)

    # Convert the difference to grayscale for analysis
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, threshold_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    # Count the number of non-zero (white) pixels, which indicate differences
    non_zero_count = cv2.countNonZero(threshold_diff)
    total_pixels = threshold_diff.size

    # Determine the similarity percentage
    similarity = (1 - non_zero_count / total_pixels) * 100
    print(f"Similarity between images: {similarity:.2f}%")

    return similarity

# Main function to start the application
def main():
    root = Tk()
    root.title("Defect Detection Tool")
    root.geometry("400x300")
    root.configure(bg="black")  # Black background theme

    # Function to run the comparison
    def on_compare():
        # Load the reference image
        reference_path = load_image_path("Select the reference image")
        if not reference_path:
            return

        # Load the new image
        new_path = load_image_path("Select the new detail image")
        if not new_path:
            return

        # Check if paths are the same
        if reference_path == new_path:
            messagebox.showerror("Error", "The files are the same. Choose another file to compare.")
            return

        # Check MD5 hash
        reference_hash = calculate_md5(reference_path)
        new_hash = calculate_md5(new_path)
        if reference_hash == new_hash:
            messagebox.showerror("Error", "The files are identical. Choose another image to compare.")
            return

        # Read images using OpenCV
        reference_image = cv2.imread(reference_path)
        new_image = cv2.imread(new_path)

        # Compare images
        similarity = compare_images(reference_image, new_image)

        if similarity > 80:
            messagebox.showinfo("Result", "No defects found on the detail.")
        else:
            messagebox.showwarning("Result", "The detail has defects or significant differences.")

    # Title label
    title_label = Label(root, text="Defect Detection", font=("Arial", 16, "bold"), bg="black", fg="white")
    title_label.pack(pady=10)

    # Button to trigger comparison
    compare_button = Button(
        root,
        text="Select Images",
        font=("Arial", 12),
        bg="#006400",  # Green background
        fg="white",    # White text
        activebackground="#228B22",  # Dark green when pressed
        height=2,
        width=20,
        command=on_compare
    )
    compare_button.pack(pady=20)

    # Footer label
    footer_label = Label(
        root,
        text="© 2025 Defect Identifier Tool",
        font=("Arial", 10),
        bg="black",
        fg="white"
    )
    footer_label.pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
