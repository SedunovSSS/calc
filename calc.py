from tkinter import ttk
from tkinter import *
from math import sqrt, pi, e, sin, cos, radians, log10, log2, log
from ttkthemes import ThemedTk
import re
import random
import webbrowser

root = ThemedTk(theme='arc')
root.title('Calculator')
root.resizable(False, False)
root.iconbitmap('calculator.ico')
btn_w = 10
mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label="Creator", command=lambda: webbrowser.open_new_tab('https://github.com/SedunovSSS'))
mainmenu.add_command(label="Copy to clipboard", command=lambda: ctc())
mainmenu.add_command(label="Exit", command=lambda: root.destroy())


def ctc():
    root.clipboard_clear()
    root.clipboard_append(calc.get())


def add_num(text):
    if calc.get() == '0':
        calc.delete(0, END)
    calc.insert(END, text)


def add_op(text):
    calc.insert(END, text)


def num(text):
    return ttk.Button(text=text, width=btn_w, command=lambda: add_num(text))


def op(text):
    return ttk.Button(text=text, width=btn_w, command=lambda: add_op(text))


def r():
    return ttk.Button(text='=', width=btn_w, command=lambda: ravno())


def ravno():
    value = calc.get()
    calc.delete(0, END)
    try:
        if float(eval(value)) == int(eval(value)):
            i_val = int(eval(value))
        else:
            i_val = eval(value)
        calc.insert(END, i_val)
    except:
        calc.insert(0, '0')


def c():
    return ttk.Button(text='AC', width=btn_w, command=lambda: clear())


def clear():
    calc.delete(0, END)
    calc.insert(0, '0')


def d():
    return ttk.Button(text='←', width=btn_w, command=lambda: delete())


def delete():
    value = calc.get()
    calc.delete(0, END)
    value = value[:-1]
    calc.insert(END, value)
    if value == '':
        calc.insert(END, '0')


def p():
    return ttk.Button(text='π', width=btn_w, command=lambda: pi_f())


def pi_f():
    if calc.get() == '0':
        calc.delete(0, END)
    calc.insert(END, str(pi))


def e_f():
    return ttk.Button(text='e', width=btn_w, command=lambda: num_e())


def num_e():
    if calc.get() == '0':
        calc.delete(0, END)
    calc.insert(END, str(e))


def s():
    return ttk.Button(text='√', width=btn_w, command=lambda: sqrt_f())


def sqrt_f():
    value = calc.get()
    try:
        last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
        if float(sqrt(abs(float(last)))) == int(sqrt(abs(float(last)))):
            i_last = int(sqrt(abs(float(last))))
        else:
            i_last = sqrt(abs(float(last)))
        if len(value) == len(last):
            calc.delete(len(value)-len(last), END)
            calc.insert(END, str(i_last))
        else:
            calc.delete(len(value) - len(last) + 1, END)
            calc.insert(END, str(i_last))
    except:
        calc.delete(0, END)
        calc.insert(END, '0')


def x2():
    return ttk.Button(text='x²', width=btn_w, command=lambda: get_x2())


def get_x2():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if float(last) == int(float(last)):
        if len(value) == len(last):
            calc.delete(len(value) - len(last), END)
            calc.insert(END, str(int(last)**2))
        else:
            calc.delete(len(value) - len(last), END)
            calc.insert(END, str(int(last) ** 2))
    else:
        if len(value) == len(last):
            calc.delete(len(value) - len(last), END)
            calc.insert(END, str(float(last) ** 2))
        else:
            calc.delete(len(value) - len(last), END)
            calc.insert(END, str(float(last) ** 2))


def pm():
    return ttk.Button(text='±', width=btn_w, command=lambda: plus_minus())


def plus_minus():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if value[-len(last)-1:][0] == "-":
        calc.delete(len(value) - len(last) - 1, END)
        if float(last) == int(float(last)):
            calc.insert(END, str(abs(int(float(last)))))
        else:
            calc.insert(END, str(abs(float(last))))
    else:
        calc.delete(len(value) - len(last), END)
        if float(last) == int(float(last)):
            calc.insert(END, str(-int(float(last))))
        else:
            calc.insert(END, str(-float(last)))


def f():
    return ttk.Button(text='n!', width=btn_w, command=lambda: fact())


def fact():
    value = calc.get()
    last = float(re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1])
    result = 1
    for i in range(1, int(last) + 1):
        result *= i
    calc.delete(len(value) - len(str(last)), END)
    calc.insert(END, str(result))


def sin_btn():
    return ttk.Button(text='sin', width=btn_w, command=lambda: get_sin())


def get_sin():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    elif value[-len(last) - 1:][0] in ["*", "/"]:
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    if sin(radians(float(last))) == int(sin(radians(float(last)))):
        calc.insert(END, str(int(sin(radians(float(last))))))
    else:
        calc.insert(END, str(round(sin(radians(float(last))), 15)))


def cos_btn():
    return ttk.Button(text='cos', width=btn_w, command=lambda: get_cos())


def get_cos():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    elif value[-len(last) - 1:][0] in ["*", "/"]:
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    if cos(radians(float(last))) == int(cos(radians(float(last)))):
        calc.insert(END, str(int(cos(radians(float(last))))))
    else:
        calc.insert(END, str(round(cos(radians(float(last))), 15)))


def tan_btn():
    return ttk.Button(text='tg', width=btn_w, command=lambda: get_tan())


def tg(angle):
    return round(sin(angle), 15) / round(cos(angle), 15)


def get_tan():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    elif value[-len(last) - 1:][0] in ["*", "/"]:
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    try:
        if tg(radians(float(last))) == int(tg(radians(float(last)))):
            calc.insert(END, str(int(tg(radians(float(last))))))
        else:
            calc.insert(END, str(round(tg(radians(float(last))), 15)))
    except:
        calc.delete(0, END)
        calc.insert(END, '0')


def ctg_btn():
    return ttk.Button(text='ctg', width=btn_w, command=lambda: get_ctg())


def ctg(angle):
    return round(cos(angle), 15) / round(sin(angle), 15)


def get_ctg():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    elif value[-len(last) - 1:][0] in ["*", "/"]:
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    try:
        if ctg(radians(float(last))) == int(ctg(radians(float(last)))):
            calc.insert(END, str(int(ctg(radians(float(last))))))
        else:
            calc.insert(END, str(round(ctg(radians(float(last))), 15)))
    except:
        calc.delete(0, END)
        calc.insert(END, '0')


def rd():
    return ttk.Button(text='rand', width=btn_w, command=lambda: rand())


def rand():
    if calc.get() == '0':
        calc.delete(0, END)
    calc.insert(END, str(random.random()))


def l10():
    return ttk.Button(text='log10', width=btn_w, command=lambda: get_l10())


def get_l10():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    try:
        if log10(float(last)) == int(log10(float(last))):
            calc.insert(END, str(int(log10(float(last)))))
        else:
            calc.insert(END, str(log10(float(last))))
    except:
        calc.delete(0, END)
        calc.insert(END, '0')


def l2():
    return ttk.Button(text='log2', width=btn_w, command=lambda: get_l2())


def get_l2():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    try:
        if log2(float(last)) == int(log2(float(last))):
            calc.insert(END, str(int(log2(float(last)))))
        else:
            calc.insert(END, str(log2(float(last))))
    except:
        calc.delete(0, END)
        calc.insert(END, '0')


def l():
    return ttk.Button(text='ln', width=btn_w, command=lambda: get_l())


def get_l():
    value = calc.get()
    last = re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1]
    if len(value) == len(last):
        calc.delete(len(value) - len(last), END)
    else:
        calc.delete(len(value) - len(last) + 1, END)
    try:
        if log(float(last)) == int(log(float(last))):
            calc.insert(END, str(int(log(float(last)))))
        else:
            calc.insert(END, str(log(float(last))))
    except:
        calc.delete(0, END)
        calc.insert(END, '0')


calc = ttk.Entry(width=40, justify='right')
calc.grid(row=0, column=0, columnspan=3)
calc.insert(0, '0')
num('7').grid(row=1, column=0)
num('8').grid(row=1, column=1)
num('9').grid(row=1, column=2)
num('4').grid(row=2, column=0)
num('5').grid(row=2, column=1)
num('6').grid(row=2, column=2)
num('1').grid(row=3, column=0)
num('2').grid(row=3, column=1)
num('3').grid(row=3, column=2)
num('0').grid(row=4, column=0)
op('+').grid(row=5, column=0)
op('-').grid(row=5, column=1)
op('*').grid(row=5, column=2)
op('/').grid(row=5, column=3)
r().grid(row=9, column=3)
c().grid(row=1, column=3)
op('.').grid(row=2, column=3)
d().grid(row=0, column=3)
op('(').grid(row=3, column=3)
op(')').grid(row=4, column=3)
op('**').grid(row=6, column=1)
p().grid(row=4, column=1)
op('//').grid(row=6, column=3)
e_f().grid(row=4, column=2)
op('%').grid(row=6, column=0)
s().grid(row=6, column=2)
sin_btn().grid(row=7, column=0)
cos_btn().grid(row=7, column=1)
tan_btn().grid(row=7, column=2)
ctg_btn().grid(row=7, column=3)
l2().grid(row=8, column=0)
l10().grid(row=8, column=1)
l().grid(row=8, column=2)
rd().grid(row=8, column=3)
x2().grid(row=9, column=2)
pm().grid(row=9, column=1)
f().grid(row=9, column=0)

root.mainloop()
