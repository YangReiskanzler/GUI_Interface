import customtkinter as ctk


class MyGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("500x1000")
        self.root.title("Beerpong")

        self.label = ctk.CTkLabel(self.root, text="Beerpong", font=("Arial", 24))
        self.label.pack(padx=20, pady=20)

        self.root.counter = 0
        self.click_counter = 0
        self.num_circles = 8
        self.canvas_width = 700
        self.canvas_height = 500
        self.canvas = ctk.CTkCanvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.configure(bg="black")

        self.instruction_label = ctk.CTkLabel(self.root, text="Input your name:")
        self.instruction_label.pack(pady=10)

        self.myentry = ctk.CTkEntry(self.root, font=("Arial", 16))
        self.myentry.pack()

        self.submit_button = ctk.CTkButton(self.root, text="Submit", command=self.display_name)
        self.submit_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(self.root, text="", font=("Helvetica", 16))
        self.message_label.pack()

        self.score_label = ctk.CTkLabel(self.root, text=f"Score: {self.root.counter}", font=("Helvetica", 16))

    def circle_clicked(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]
        self.canvas.itemconfigure(item, fill="gray")
        self.root.counter += 1
        self.score_label.configure(text=f"Score: {self.root.counter}")
        self.click_counter += 1
        if self.click_counter == 4:
            self.num_circles = 6
            self.redraw_pyramid()
        elif self.click_counter == 7:
            self.num_circles = 3
            self.redraw_pyramid()
        elif self.click_counter == 9:
            self.num_circles = 1
            self.redraw_pyramid()
        elif self.click_counter == 10:
            self.canvas.delete("all")
            self.canvas.create_text(self.canvas_width // 2, self.canvas_height // 2,
                                    text="Congratulations! You won!", font=("Arial", 24), fill="white")

    def redraw_pyramid(self):
        self.canvas.delete("all")
        if self.click_counter == 4:
            self.num_circles = 6
        elif self.click_counter == 7:
            self.num_circles = 3
        elif self.click_counter == 9:
            self.num_circles = 1
        self.draw_pyramid()

    def display_name(self):
        name = self.myentry.get()
        if name:
            self.myentry.pack_forget()
            self.submit_button.pack_forget()
            self.instruction_label.pack_forget()
            self.message_label.configure(text=f"{name}")
            self.score_label.pack(padx=20, pady=20)
            self.draw_pyramid()
            self.canvas.pack()

    def draw_pyramid(self):
        x0 = self.canvas_width // 3
        y0 = self.canvas_height // 2
        radius = 15
        gap = 5
        rows = (self.num_circles + 1) // 2
        for i in range(rows):
            for j in range(i + 1):
                circle = self.canvas.create_oval(
                    x0 + j * (2 * radius + gap) + (rows - i - 1) * (radius + gap),  # x-Koordinate
                    y0 - i * (2 * radius + gap),  # y-Koordinate
                    x0 + j * (2 * radius + gap) + 2 * radius + (rows - i - 1) * (radius + gap),
                    # x-Koordinate + Durchmesser
                    y0 - i * (2 * radius + gap) + 2 * radius,  # y-Koordinate + Durchmesser
                    fill="red", outline="black"
                )
                self.canvas.tag_bind(circle, '<Button-1>',
                                     lambda e: self.circle_clicked(e))  # Mausklick-Ereignis binden

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = MyGUI()
    gui.run()
