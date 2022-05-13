import tkinter as tk
import info
import standartlintask
import sawlintask
import amoutcuttask

# Инициализация окна
win = tk.Tk()
win.title("Линейный раскрой")
win.resizable(False, False)
win.geometry("500x250+500+100")
icon = tk.PhotoImage(file="image/icon.png")
question = tk.PhotoImage(file="image/question1.png")
win.iconphoto(False, icon)

label_1 = tk.Label(win, text="Выберете нужную задачу", font=25)
label_1.place(width=200, height=50, x=150, y=5)

# Стандартный раскрой
button_1 = tk.Button(win, text="1. Стандартный линейный раскрой", command=standartlintask.solve_standard_linear_task, anchor="w")
button_1.place(width=250, height=35, x=75, y=50)
info_button_1 = tk.Button(win, image=question, command=info.get_info1)
info_button_1.place(width=50, height=35, x=350, y=50)

# Раскрой с учетом распила
button_2 = tk.Button(win, text="2. Раскрой с учетом распила", command=sawlintask.solve_saw_lin_task, anchor="w")
button_2.place(width=250, height=35, x=75, y=100)
info_button_2 = tk.Button(win, image=question, command=info.get_info2)
info_button_2.place(width=50, height=35, x=350, y=100)

# Раскрой с ограничением на кромку и кол-во рулонов одного формата
button_2 = tk.Button(win, text="3. Раскрой с ограничением на кромку \n и кол-во деталей одного формата", command=amoutcuttask.solve_amount_lin_task, anchor="w")
button_2.place(width=250, height=35, x=75, y=150)
info_button_2 = tk.Button(win, image=question, command=info.get_info3)
info_button_2.place(width=50, height=35, x=350, y=150)

win.mainloop()
