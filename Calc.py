from tkinter import *
from random import randint

expression = ""
display = ""

buttonColor = "#4b5474"

def secret():
	equation.set("DON'T DO THAT.")

def remember(num):
	global expression, display
	if len(expression) < 16:
		print(str(num))
		expression = str(expression) + str(num)

		if num == "*":
			display = display + "×"
		elif num == "/":
			display = display + "÷"
		else:
			display = str(display) + str(num)
		equation.set(display)
	else:
		print("Too long")
		clear_buffer()
		equation.set("TOO LONG")


def clear_buffer():
	global expression, display
	print("Clear")
	expression = " "
	display = " "
	equation.set(display)

def get_answer():
	global expression, display
	print(expression + " is...")

	try: 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = total 
		display = total
		print(total)
	except ZeroDivisionError: 
		expression = " "
		display = " "
		equation.set("--ERROR--")
		if randint(0, 3) == 2:
			secret()
		else:
			pass

	except: 
		equation.set("--ERROR--") 
		expression = " "
		display = " "

w = 184
h = 185

root = Tk() 
root.title("Calc") 
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
windo_x = (screen_w/2) - (w/2)
windo_y = (screen_h/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, windo_x, windo_y))
root.minsize(w, h)
root.maxsize(w, h)

display_frame = Frame(root, height = 50, bg="#1f263e")
display_frame.grid(row=0, columnspan=4, ipadx=2)

control_panel = Frame(root, height = 135, width=184, bg="#1f263e")
control_panel.grid(row=5, columnspan=4, ipadx=2)

equation = StringVar() 
expression_field = Label(display_frame, textvariable=equation, width=14, fg="#bccbff", bg="#282f47")
expression_field.grid(ipadx=2, row=0)
equation.set("")


# make buttons
clear_button = Button(display_frame, text="Clear", command = clear_buffer, height=2, width=4, highlightbackground=buttonColor)
clear_button.grid(row=0, column=4)

equals_button = Button(control_panel, text="=", command = get_answer, height=2, width=4, highlightbackground=buttonColor)
equals_button.grid(row=6, column=2)

seven_button = Button(control_panel, text="7", command =lambda: remember(7), height=2, width=4, highlightbackground=buttonColor)
seven_button.grid(row=5, column=0)

eight_button = Button(control_panel, text="8", command =lambda: remember(8), height=2, width=4, highlightbackground=buttonColor)
eight_button.grid(row=5, column=1)

nine_button = Button(control_panel, text="9", command =lambda: remember(9), height=2, width=4, highlightbackground=buttonColor)
nine_button.grid(row=5, column=2)

sub_button = Button(control_panel, text="-", command =lambda: remember("-"), height=2, width=4, highlightbackground=buttonColor)
sub_button.grid(row=4, column=3)

four_button = Button(control_panel, text="4", command =lambda: remember(4), height=2, width=4, highlightbackground=buttonColor)
four_button.grid(row=4, column=0)

five_button = Button(control_panel, text="5", command =lambda: remember(5), height=2, width=4, highlightbackground=buttonColor)
five_button.grid(row=4, column=1)

six_button = Button(control_panel, text="6", command =lambda: remember(6), height=2, width=4, highlightbackground=buttonColor)
six_button.grid(row=4, column=2)

add_button = Button(control_panel, text="+", command = lambda: remember("+"), height=2, width=4, highlightbackground=buttonColor)
add_button.grid(row=3, column=3)

one_button = Button(control_panel, text="1", command =lambda: remember(1), height=2, width=4, highlightbackground=buttonColor)
one_button.grid(row=3, column=0)

two_button = Button(control_panel, text="2", command =lambda: remember(2), height=2, width=4, highlightbackground=buttonColor)
two_button.grid(row=3, column=1)

three_button = Button(control_panel, text="3", command =lambda: remember(3), height=2, width=4, highlightbackground=buttonColor)
three_button.grid(row=3, column=2)

zero_button = Button(control_panel, text="0", command =lambda: remember(0), height=2, width=4, highlightbackground=buttonColor)
zero_button.grid(row=6, column=0)

dot_button = Button(control_panel, text='.', fg='black', command=lambda: remember('.'), height=2, width=4, highlightbackground=buttonColor)
dot_button.grid(row=6, column=1)

mult_button = Button(control_panel, text='×', fg='black', bg='red', command=lambda: remember("*"), height=2, width=4, highlightbackground=buttonColor)
mult_button.grid(row=5, column=3)

div_button = Button(control_panel, text='÷', fg='black', bg='red', command=lambda: remember("/"), height=2, width=4, highlightbackground=buttonColor)
div_button.grid(row=6, column=3)


# Start!
root.mainloop() 