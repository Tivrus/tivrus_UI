with open("ui.py", "w") as file:
    file.write("import customtkinter as ctk\n\n")
    file.write("class UI:\n")
    file.write("    def __init__(self, root):\n")
    file.write("        self.frame = ctk.CTkFrame(root)\n")
    file.write("        self.frame.pack()\n")