from tkinter import ttk
from tkinter import *
from math import sqrt, pi, e
from ttkthemes import ThemedTk
import re

root = ThemedTk(theme='arc')
root.title('Calculator')
root.resizable(False, False)
root.iconbitmap('calculator.ico')
btn_w = 10


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
    return ttk.Button(text='E', width=btn_w, command=lambda: num_e())


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
        if float(sqrt(float(last))) == int(sqrt(float(last))):
            i_last = int(sqrt(float(last)))
        else:
            i_last = sqrt(float(last))
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
    calc.delete(len(value) - len(last), END)
    calc.insert(END, str(float(last)**2))


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
    return ttk.Button(text='!', width=btn_w, command=lambda: fact())


def fact():
    value = calc.get()
    last = float(re.findall(r"[-+]?(?:\d*\.*\d+)", value)[-1])
    result = 1
    for i in range(1, int(last) + 1):
        result *= i
    calc.delete(len(value) - len(str(last)), END)
    calc.insert(END, str(result))


calc = ttk.Entry(width=40, justify='right')
calc.grid(row=0, column=0, columnspan=3)
calc.insert(0, '0')
num('1').grid(row=1, column=0)
num('2').grid(row=1, column=1)
num('3').grid(row=1, column=2)
num('4').grid(row=2, column=0)
num('5').grid(row=2, column=1)
num('6').grid(row=2, column=2)
num('7').grid(row=3, column=0)
num('8').grid(row=3, column=1)
num('9').grid(row=3, column=2)
num('0').grid(row=4, column=0)
op('+').grid(row=5, column=0)
op('-').grid(row=5, column=1)
op('*').grid(row=5, column=2)
op('/').grid(row=5, column=3)
r().grid(row=7, column=3)
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
x2().grid(row=7, column=2)
pm().grid(row=7, column=1)
f().grid(row=7, column=0)

root.mainloop()
