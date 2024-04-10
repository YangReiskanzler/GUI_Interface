import customtkinter

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x1000")
root.title("Beerpong")

label = customtkinter.CTkLabel(root, text="Beerpong", font=("Arial", 24))
label.pack(padx=20, pady=20)

root.counter = 0


def clicked():
    root.counter += 1
    score_label.configure(text=f"Score: {root.counter}")


def display_name():
    name = myentry.get()
    if name:
        myentry.pack_forget()
        submit_button.pack_forget()
        instruction_label.pack_forget()
        message_label.configure(text=f"{name}")
        score_label.pack(padx=20, pady=20)
        score_button.pack(padx=20, pady=20)
        draw_pyramid()


instruction_label = customtkinter.CTkLabel(root, text="Input your name:")
instruction_label.pack(pady=10)

myentry = customtkinter.CTkEntry(root, font=("Arial", 16))
myentry.pack()

submit_button = customtkinter.CTkButton(root, text="Submit", command=display_name)
submit_button.pack(pady=10)

message_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 16))
message_label.pack()

score_label = customtkinter.CTkLabel(root, text=f"Score: {root.counter}", font=("Helvetica", 16))

score_button = customtkinter.CTkButton(root, text="Click me", command=clicked)


def draw_pyramid():
    canvas = customtkinter.CTkCanvas(root,width=700, height=500)
    canvas.configure(bg="black")
    canvas.pack()

    x0 = 250
    y0 = 250
    radius = 15
    gap = 5
    rows = 4  # Anzahl der Reihen

    for i in range(rows):
        for j in range(i + 1):
            canvas.create_oval(
                x0 + j * (2 * radius + gap) + (rows - i - 1) * (radius + gap),  # x-Koordinate
                y0 - i * (2 * radius + gap),  # y-Koordinate
                x0 + j * (2 * radius + gap) + 2 * radius + (rows - i - 1) * (radius + gap),  # x-Koordinate + Durchmesser
                y0 - i * (2 * radius + gap) + 2 * radius,  # y-Koordinate + Durchmesser
                fill="red", outline="black"
            )



root.mainloop()
