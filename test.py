import customtkinter as ctk

class GradientButton(ctk.CTkCanvas):
    def __init__(self, parent, text, color1, color2, command=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.text = text
        self.color1 = color1
        self.color2 = color2
        self.command = command

        # Рисуем градиент и текст
        self.bind("<Configure>", self.draw_gradient)
        self.bind("<Button-1>", self.on_click)

    def draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        
        for i in range(height):
            ratio = i / height
            r = int(self.color1[0] * (1 - ratio) + self.color2[0] * ratio)
            g = int(self.color1[1] * (1 - ratio) + self.color2[1] * ratio)
            b = int(self.color1[2] * (1 - ratio) + self.color2[2] * ratio)
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.create_line(0, i, width, i, fill=color, tags=("gradient",))

        # Отображаем текст в центре кнопки
        self.create_text(width // 2, height // 2, text=self.text, fill="white", font=("Arial", 12), tags=("text",))

    def on_click(self, event=None):
        if self.command:
            self.command()

# Пример использования GradientButton
def button_clicked():
    print("Button clicked!")

app = ctk.CTk()
app.geometry("400x400")

color1 = (0, 128, 255)  # Начальный цвет
color2 = (0, 255, 128)  # Конечный цвет

gradient_button = GradientButton(app, text="Gradient Button", color1=color1, color2=color2, width=200, height=50, command=button_clicked)
gradient_button.pack(pady=20)

app.mainloop()
