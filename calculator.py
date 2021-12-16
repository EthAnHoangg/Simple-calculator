from tkinter import *
import tkinter.font as font
from math import *

root = Tk()
#set title for the app
root.title('Calculator')
root.geometry('500x600')

#Set the name and intro
frame1 = Frame(root)
frame1.pack(fill = X, expand= True)
myFont = font.Font(size=30)
intro = Label(
    frame1, 
    text='WELCOME TO CALCULATOR FX AN DEEP TRY PLUS\n\n\
    ENTER YOUR CALCULATION',
    font=font.Font(size = 16),  
    fg='blue',
    borderwidth=3)
intro.pack(side='top')

#create entry box to enter the calculation
entry = Entry(frame1, width = 23, font = font.Font(size = 30), bg= '#aaf2eb')
entry.pack()

#method of calculating
content = ''
def add_text_input(text):
    global content
    if text == 'π':
        content += 'pi'
    elif text == '^':
        content += '**'
    else:
        content += text
    entry.insert(END, text)
def equation():
    global content
    try:
        result = eval(content)
        content = str(result)
        entry.delete(0, END)
        entry.insert(END, str(round(result,9)))
    except:
        entry.delete(0, END)
        entry.insert(END, 'SyntaxError')
def clear():
    global content
    entry.delete(len(content)-1, END)
    content = content[:-1]
def reset():
    global content
    content = ''
    entry.delete(0, END)

#creatr numpad
frame2 = Frame()
frame2.pack(side = 'top', expand= True)
button1 = Button(frame2, text='1', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('1')).grid(row=2,column=0)
button2 = Button(frame2, text='2', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('2')).grid(row=2,column=1)
button3 = Button(frame2, text='3', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('3')).grid(row=2,column=2)
button4 = Button(frame2, text='4', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('4')).grid(row=1,column=0)
button5 = Button(frame2, text='5', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('5')).grid(row=1,column=1)
button6 = Button(frame2, text='6', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('6')).grid(row=1,column=2)
button7 = Button(frame2, text='7', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('7')).grid(row=0,column=0)
button8 = Button(frame2, text='8', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('8')).grid(row=0,column=1)
button9 = Button(frame2, text='9', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('9')).grid(row=0,column=2)
button0 = Button(frame2, text='0', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('0')).grid(row=3,column=0)
buttondot = Button(frame2, text='.', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('.')).grid(row=3,column=1)
buttoneq = Button(frame2, text='=', font= myFont, height = 2, width = 4,\
    command = lambda:equation()).grid(row=3,column=2)
buttonplus = Button(frame2, text='+', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('+')).grid(row=0,column=3)
buttonminus = Button(frame2, text='-', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('-')).grid(row=1,column=3)
buttonmul = Button(frame2, text='*', font= myFont, height = 2, width = 4,\
    command = lambda:add_text_input('*')).grid(row=2,column=3)
buttondiv = Button(frame2, text='/', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('/')).grid(row = 3,column = 3)
buttonAC = Button(frame2, text = 'AC', fg='#f03c30', font = myFont, height = 2, width=4,\
    command = lambda:reset()).grid(row = 0, column = 4)
buttonC = Button(frame2, text='C', fg='#f03c30', font = myFont, height = 2, width = 4,\
    command = lambda:clear()).grid(row = 1,column = 4)
button_open = Button(frame2, text='(', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('(')).grid(row = 2 , column=4)
button_close = Button(frame2, text=')', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input(')')).grid(row = 3 , column=4)
button_cos =  Button(frame2, text = 'cos', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('cos(')).grid(row = 4, column = 0)
button_sin = Button(frame2, text = 'sin', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('sin(')).grid(row = 4, column = 1)
button_tan = Button(frame2, text = 'tan', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('tan(')).grid(row = 4, column = 2)
button_pi = Button(frame2, text = 'π', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('π')).grid(row = 4, column = 3)
button_power = Button(frame2, text = '^', font = myFont, height = 2, width = 4,\
    command = lambda:add_text_input('^')).grid(row = 4, column = 4)



root.mainloop()
