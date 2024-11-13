import customtkinter as ctk

root = ctk.CTk()
root.geometry("300x200")
    
# Создаем кнопку с индивидуальными скруглениями углов
button = ctk.CTkButton(
            root,
            corner_radius=5,
            width=150,
            height=50,
            command=lambda: print("Button Clicked"))
button.pack(pady=20)
    
root.mainloop()
