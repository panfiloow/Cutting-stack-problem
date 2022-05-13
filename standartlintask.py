import tkinter as tk
from array import *
from tkinter import messagebox
from tkinter import ttk

count = 0
len_details = array('i', [])
prise_details = array('i', [])


def validate(new_value):
    try:
        value = int(new_value)
    except ValueError:
        value = True
    return (new_value == "" or new_value.isnumeric()) and value < 2147483647


def solve_standard_linear_task():
    def reset():
        global len_details
        global prise_details
        global count
        len_details = array('i', [])
        prise_details = array('i', [])
        count = 0
        label_6.config(text=f"Количество деталей: {count}")
        stick_length_entry.config(state="normal")
        stick_length_entry.delete(0, 'end')
        detail_length_entry.delete(0, 'end')
        detail_prise_entry.delete(0, 'end')
        for i in tree.get_children():
            tree.delete(i)

    def solve_problem():
        def show_answer():
            answer_win = tk.Toplevel()
            answer_win.grab_set()
            answer_win.geometry("400x350+550+150")
            answer_win.title("Ответ")
            answer_win.resizable(False, False)
            answer_win.lift()
            answer_label = tk.Label(answer_win, text="Решение найдено !", font=20)
            answer_label.place(x=125, y=10)
            max_label = tk.Label(answer_win, text=f"Максимальная стоимость: {dp[stick_len]}", font=20)
            max_label.place(x=10, y=35)
            # Tree Answer
            frame = tk.Frame(answer_win)
            frame.place(x=10, y=60)
            tree_scroll1 = ttk.Scrollbar(tree_frame)
            tree_scroll1.pack(side="right", fill="y")
            ans_tree = ttk.Treeview(frame, columns=("#1", "#2", "#3"), show="headings", height=10,
                                    yscrollcommand=tree_scroll1.set)
            tree_scroll1.config(command=ans_tree.yview)
            ans_tree.pack()
            ans_tree.heading("#1", text="Длина детали")
            ans_tree.heading("#2", text="Цена детали")
            ans_tree.heading("#3", text="Необходимое кол-во")
            ans_tree.column("#1", width=125, anchor="center")
            ans_tree.column("#2", width=125, anchor="center")
            ans_tree.column("#3", width=125, anchor="center")
            for i in range(count):
                ans_tree.insert('', "end", values=(len_details[i], prise_details[i], x[i]))

        global count
        global len_details
        global prise_details
        if count < 2:
            messagebox.showerror("Недостаточно данных", "Введите хотя бы 2 детали !")
            return
        else:
            stick_len = int(stick_length_entry.get())
            dp = [0 for i in range(stick_len + 1)]
            dw = [-1 for i in range(stick_len + 1)]
            for i in range(stick_len + 1):
                for j in range(count):
                    if len_details[j] <= i and dp[i] < dp[i - len_details[j]] + prise_details[j]:
                        dp[i] = dp[i - len_details[j]] + prise_details[j]
                        dw[i] = j

            x = [0 for i in range(count)]
            y = stick_len
            while dw[y] != -1:
                k = dw[y]
                x[k] = x[k] + 1
                y = y - len_details[k]
            show_answer()

    def add_detail():
        if stick_length_entry.get() == '':
            messagebox.showerror("Ошибка", "Прежде чем заполнять детали введите длину стержня L.")
            return

        if detail_length_entry.get() != '' and detail_prise_entry.get() != '':
            current_len = int(detail_length_entry.get())
            current_prise = int(detail_prise_entry.get())
            stick_len = int(stick_length_entry.get())
            if current_len > stick_len:
                messagebox.showerror("Ошибка длины детали", "Длина введенной детали превышает длину стержня L")
                return
            if current_len == 0:
                messagebox.showerror("Ошибка длины детали", "Длина детали не может быть равна 0")
                return
            not_in_len_flag = current_len not in len_details
            if not_in_len_flag:
                len_details.append(current_len)
                prise_details.append(current_prise)
                tree.insert('', 'end', values=(current_len, current_prise))
                stick_length_entry.config(state="readonly")
                global count
                count += 1
                label_6.config(text=f"Количество деталей: {count}")
            else:
                messagebox.showerror("Ошибка повтора длины", "Вы уже ввели деталь с данной длиной")
                return
        else:
            messagebox.showerror("Ошибка заполнения данных", "Пожалуйста введите длину и стоимость детали.")
            return

    win2 = tk.Toplevel()
    win2.grab_set()
    win2.geometry("500x500+550+150")
    win2.title("Стандартный линейный раскрой")
    win2.resizable(False, False)
    icon = tk.PhotoImage(file="image/icon.png")
    win2.iconphoto(False, icon)
    # Заполнение данных
    label_1 = tk.Label(win2, text="Заполните данные.", font=20)
    label_1.pack(ipady=10)
    label_2 = tk.Label(win2, text="Введите длину стержня: ", font=16)
    label_2.place(x=10, y=50)
    validate_cmd = (win2.register(validate), '%P')
    stick_length_entry = tk.Entry(win2, width=30, validate='key', validatecommand=validate_cmd)
    stick_length_entry.place(x=205, y=52)
    label_3 = tk.Label(win2, text="Деталь:", font=16)
    label_3.place(x=10, y=100)
    label_4 = tk.Label(win2, text="Длина", font=14)
    label_4.place(x=120, y=80)
    label_5 = tk.Label(win2, text="Стоимость", font=14)
    label_5.place(x=220, y=80)
    detail_length_entry = tk.Entry(win2, width=17, validate='key', validatecommand=validate_cmd)
    detail_length_entry.place(x=93, y=102)
    detail_prise_entry = tk.Entry(win2, width=17, validate='key', validatecommand=validate_cmd)
    detail_prise_entry.place(x=210, y=102)
    add_detail_button = tk.Button(win2, text="Добавить деталь", command=add_detail)
    add_detail_button.place(x=325, y=97)
    # Дерево
    tree_frame = tk.Frame(win2)
    tree_frame.place(x=10, y=130)
    tree_scroll = ttk.Scrollbar(tree_frame)
    tree_scroll.pack(side="right", fill="y")
    tree = ttk.Treeview(tree_frame, columns=("#1", "#2"), show="headings", height=10, yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=tree.yview)
    tree.pack()
    tree.heading("#1", text="Длина детали")
    tree.heading("#2", text="Цена детали")
    tree.column("#1", width=207, anchor="center")
    tree.column("#2", width=207, anchor="center")
    # Кнопка решения
    global count
    label_6 = tk.Label(win2, text=f"Количество деталей: {count}", font=16)
    label_6.place(x=10, y=380)
    reset_button = tk.Button(win2, text="Сбросить", width=12, font=15, command=reset)
    reset_button.place(x=310, y=370)
    solve_button = tk.Button(win2, text="Решить", width=15, font=15, command=solve_problem)
    solve_button.place(x=180, y=425)
