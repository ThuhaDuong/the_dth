
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # ✅ Add this line


# Wardrobe with image file paths
wardrobe = {
    "tops": [
        ("White T-shirt", "white-t-shirt-women-png.webp"),
        ("Black Blouse", "png-clipart-shirts-black-scoop-neck-blouse.png"),
        ("Blue Hoodie", "hoodie-adidas-jacket-clothing-png-favpng-5GXm1nyrGvpvJ14e2YRByPuWX.jpg")
    ],
    "bottoms": [
        ("Jeans", "ca7b80d078d888ac8974df6ed5a6f670.jpg"),
        ("Black Skirt", "black-resourcesforbitches-black-and-white-mini-skirt.jpg"),
        ("Cargo Pants", "cargopant.jpeg")
    ],
    "shoes": [
        ("Sneakers", "sneaker.webp"),
        ("Boots", "boots.jpeg"),
        ("Heels", "elegant-black-patent-leather-high-heels-with-red-insoles_191095-86032.jpg")
    ]
}


class DigitalCloset(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Closet - Clueless Style")
        self.geometry("600x700")

        # Keep track of indexes
        self.indexes = {"tops": 0, "bottoms": 0, "shoes": 0}

        # --- Top Section ---
        tk.Label(self, text="Top").pack()
        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)
        tk.Button(frame_top, text="◀", command=lambda: self.prev_item("tops")).pack(side="left")
        self.top_label = tk.Label(frame_top)
        self.top_label.pack(side="left", padx=10)
        tk.Button(frame_top, text="▶", command=lambda: self.next_item("tops")).pack(side="left")

        # --- Bottom Section ---
        tk.Label(self, text="Bottom").pack()
        frame_bottom = tk.Frame(self)
        frame_bottom.pack(pady=5)
        tk.Button(frame_bottom, text="◀", command=lambda: self.prev_item("bottoms")).pack(side="left")
        self.bottom_label = tk.Label(frame_bottom)
        self.bottom_label.pack(side="left", padx=10)
        tk.Button(frame_bottom, text="▶", command=lambda: self.next_item("bottoms")).pack(side="left")

        # --- Shoes Section ---
        tk.Label(self, text="Shoes").pack()
        frame_shoes = tk.Frame(self)
        frame_shoes.pack(pady=5)
        tk.Button(frame_shoes, text="◀", command=lambda: self.prev_item("shoes")).pack(side="left")
        self.shoes_label = tk.Label(frame_shoes)
        self.shoes_label.pack(side="left", padx=10)
        tk.Button(frame_shoes, text="▶", command=lambda: self.next_item("shoes")).pack(side="left")

        # Outfit Display Text
        self.outfit_text = tk.Label(self, text="", font=("Arial", 14))
        self.outfit_text.pack(pady=20)

        # Initial load
        self.update_display()

    def load_image(self, path, target_label, size=(200, 200)):
        """Load and show an image in a given label."""
        img = Image.open(path).resize(size)
        tk_img = ImageTk.PhotoImage(img)
        target_label.config(image=tk_img)
        target_label.image = tk_img  # keep reference

    def update_display(self):
        """Refresh all category displays."""
        # Top
        top_name, top_path = wardrobe["tops"][self.indexes["tops"]]
        self.load_image(top_path, self.top_label)

        # Bottom
        bottom_name, bottom_path = wardrobe["bottoms"][self.indexes["bottoms"]]
        self.load_image(bottom_path, self.bottom_label)

        # Shoes
        shoes_name, shoes_path = wardrobe["shoes"][self.indexes["shoes"]]
        self.load_image(shoes_path, self.shoes_label)

        # Outfit text
        self.outfit_text.config(
            text=f"👕 {top_name} + 👖 {bottom_name} + 👟 {shoes_name}"
        )

    def next_item(self, category):
        self.indexes[category] = (self.indexes[category] + 1) % len(wardrobe[category])
        self.update_display()

    def prev_item(self, category):
        self.indexes[category] = (self.indexes[category] - 1) % len(wardrobe[category])
        self.update_display()


if __name__ == "__main__":
    app = DigitalCloset()
    app.mainloop()
