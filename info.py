import tkinter as tk


def get_info1():
    win = tk.Toplevel()
    win.grab_set()
    win.geometry("400x150+550+150")
    win.title("Условие задачи")
    win.resizable(False, False)
    info = tk.Label(win, text="Пусть даны стержень  длиной L и n видов деталей.\n"
                              "Деталь вида j имеет длину a(j) > 0 и стоимость\n"
                              "c(j) > 0, j = 1,...,n. Стержень необходимо раскроить\n"
                              "на детали таким образом, чтобы их общая стоимость\n"
                              "была максимальна.", height=6, width=53, font=15)
    info.pack()
    win.mainloop()


def get_info3():
    win = tk.Toplevel()
    win.grab_set()
    win.geometry("500x200+550+150")
    win.title("Условие задачи")
    win.resizable(False, False)
    info = tk.Label(win, text="Пусть даны стержень  длиной L, шириной спила S\n"
                              "и n видов деталей. "
                              "Деталь вида j имеет длину \n a(j) > 0 и стоимость "
                              "c(j) > 0, j = 1,...,n.\n Стержень необходимо раскроить"
                              " на детали таким образом,\n чтобы их общая стоимость"
                              "была максимальна, учитывая, что \nв оптимальном раскрое i деталь содержится не больше m раз.", height=7,
                    width=53, font=13)
    info.pack()
    win.mainloop()


def get_info2():
    win = tk.Toplevel()
    win.grab_set()
    win.geometry("500x200+550+150")
    win.title("Условие задачи")
    win.resizable(False, False)
    info = tk.Label(win, text="Пусть даны стержень  длиной L, шириной спила S\n"
                              "и n видов деталей. "
                              "Деталь вида j имеет длину \n a(j) > 0 и стоимость "
                              "c(j) > 0, j = 1,...,n.\n Стержень необходимо раскроить"
                              " на детали таким образом,\n чтобы их общая стоимость "
                              "была максимальна, учитывая, \nчто при каждом спиле от L отнимается l.", height=7,
                    width=53, font=13)
    info.pack()
    win.mainloop()
