from tkinter import * 
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter.font import Font

class Window(Frame):
	"""Main window"""

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title('Temperature Converter')
		self.pack(expand=1)
		self.main_menus()
		self.upper_part()
		self.lower_part()
		self.convert_button()

	def main_menus(self):
		'''Creates and packs menus in the main window'''

		menu = Menu(self.master)
		self.master.config(menu=menu)

		file = Menu(menu)
		file.add_command(label='Show Credit', command=self.show_credit)
		file.add_command(label='Hide Credit', command=self.hide_credit)
		file.add_command(label='Exit', command=self.exit_window)

		edit = Menu(menu)
		edit.add_command(label='Delete', command=self.delete)
		edit.add_command(label='Undo', command=self.undo)
		edit.add_command(label='Redo', command=self.redo)

		helps = Menu(menu)
		helps.add_command(label='Show Help', command=self.help)

		menu.add_cascade(label='File', menu=file)
		menu.add_cascade(label='Edit', menu=edit)
		menu.add_cascade(label='Help', menu=helps)

	def upper_part(self):
		'''Upper part of the window'''

		font_style1 = Font(family='Lucinda Grande', size=40)
		font_style2 = Font(family='Lucinda Frande', size=50)
		input_text = StringVar()

		#Create entry box for temperature
		self.ent_temp = Entry(text=input_text, font=(font_style1), justify='center', bg='dark orange', fg='grey')
		self.ent_temp.place(x=10, y=10, width=200, height=80)

		self.ent_temp.bind('<<Button-1>>', self.undo)
		self.ent_temp.bind('<<BUtton-2>>', self.redo)

		#Create combobox to choose temperature
		self.cmb_temp = Combobox(font=font_style2, state='readonly')
		self.cmb_temp.place(x=230, y=10, width=150, height=80)
		self.cmb_temp['value'] = (f'\N{DEGREE SIGN} C', '\N{DEGREE SIGN} F', '\N{DEGREE SIGN} K')
		self.cmb_temp.current(0)

	def lower_part(self):
		'''Lower part of the window'''

		font_style1 = Font(family='Lucinda Grande', size=40)
		font_style2 = Font(family='Lucinda Grande', size=50)

		#Create result box
		self.lbl_result = Label(text='     0    ', font=font_style1,  bg='dark orange', fg='grey')
		self.lbl_result.place(x=10, y=110, width=200, height=80)

		#Create combobox to show result
		self.cmb_result = Combobox(font=font_style2, state='readonly')
		self.cmb_result.place(x=230, y=110, width=150, height=80)
		self.cmb_result['value'] = (f'\N{DEGREE SIGN} C', '\N{DEGREE SIGN} F', '\N{DEGREE SIGN} K')
		self.cmb_result.current(1)

		self.lbl_result.bind('<<Button-1>>', self.undo)
		self.lbl_result.bind('<<Button-2>>', self.redo)


	def convert_button(self):
		'''Convert button'''

		font_style3 = Font(family='Lucinda Grande', size=12)
		btn_convert = Button(text='CONVERT', font=font_style3, bg='dark red', fg='black', command=self.convert_temperature)
		btn_convert.place(x=260, y=210, width=90, height=60)

	def exit_window(self):
		exit()

	def show_credit(self):
		self.show_credit = Label(text="This was created by Adh.. ^-^", font=(12), bg='black', fg='white')
		self.show_credit.place(x=10, y=270)

	def hide_credit(self):
		self.show_credit.place_forget()

	def delete(self):
		self.ent_temp.configure(text='     ')
		self.lbl_result.configure(text='0')

	def undo(self, event=None):
		self.event_generate("<<Undo>>")

	def redo(self, event=None):
		self.event_generate("<<Redo>>")

	def help(self):
		self.helps = messagebox.showwarning("Help", 'For further informatioan contact \nAdh on 0895804643781')

	def convert_temperature(self):
		'''Command for temperature converter button'''
		try:

			degree = float(self.ent_temp.get())

			if self.cmb_temp.current() == 0:
				if self.cmb_result.current() == 1:
					result = (degree * 9/5) + 32
					temp_result = f'{round(result, 2)}'
					self.lbl_result.configure(text=temp_result)

				elif self.cmb_result.current() == 2:
					result = (degree + 273.15)
					temp_result = f'{round(result, 2)}'
					self.lbl_result.configure(text=temp_result)

				else:
					return None

			elif self.cmb_temp.current() == 1:
				if self.cmb_result.current() == 0:
					result = (degree - 32) * 5/9
					temp_result = f'{round(result, 2)}'
					self.lbl_result.configure(text=temp_result)

				elif self.cmb_result.current() == 2:
					result = ((degree - 32) * 5/9) + 273.15
					temp_result = f'{round(result, 2)}'
					self.lbl_result.configure(text=temp_result)

				else:
					return None

			elif self.cmb_temp.current() == 2:
				if self.cmb_result.current() == 0:
					result = (degree - 273.15)
					temp_result = f'{round(result, 2)}'
					self.lbl_result.configure(text=temp_result)

				elif self.cmb_result.current() == 1:
					result = ((degree - 273.15) * 9/5) + 32
					temp_result = f'{round(result, 2)}'
					self.lbl_result.configure(text=temp_result)

				else:
					return None

			else:
				return None

		except ValueError:
			return None


root = Tk()
app = Window(root)
root.geometry('400x300')
root.configure(bg='black')
root.resizable(0,0)
root.mainloop()
