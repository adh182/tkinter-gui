from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import os

class Window(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
		
	def init_window(self):
		'''Initialize windows'''

		self.master.title('Login System')
		self.fontstyle = Font(family='Times New Roman', size=12)
		self.login_icon()
		self.username_password()
		self.register_login_button()
		self.menus()

	def login_icon(self):
		'''Load login icon'''

		load = Image.open('icon_login3.png')
		render = ImageTk.PhotoImage(load)

		img = Label(image=render)
		img.image = render
		img.place(x=155, y=3)

	def menus(self):
		'''Add menus'''

		menu = Menu(self.master)
		self.master.config(menu=menu)

		file = Menu(menu)
		file.add_command(label='Exit', command=self.exit)
		menu.add_cascade(label='File', menu=file)

		view = Menu(menu)
		view.add_command(label='Show Credit', command=self.show_credit)
		view.add_command(label='Hide Credit', command=self.hide_credit)
		menu.add_cascade(label='View', menu=view)

		helps = Menu(menu)
		helps.add_command(label='About')
		menu.add_cascade(label='Help', menu=helps)

	def exit(self):
		'''Exit command'''
		exit()

	def show_credit(self):
		'''Show credit command'''

		self.credit = Label(text='This program created by Adh', font=self.fontstyle, fg='dark grey')
		self.credit.place(x=10, y=275)

	def hide_credit(self):
		'''Hide credit command'''

		self.credit.place_forget()

	def username_password(self):
		"""Create Label and Entry and ask user to enter Username and Password"""

		#Create text for username and password
		
		lbl_username = Label(text='Username', font=self.fontstyle)
		lbl_username.place(x=50, y=110)

		lbl_password = Label(text='Password', font=self.fontstyle)
		lbl_password.place(x=50, y=150) 

		#Create entry for entering the form
		input_username = StringVar()
		self.ent_username = Entry(text=input_username, font=self.fontstyle, width=25, bg='light blue')
		self.ent_username.place(x=130, y=110)

		input_password = StringVar()
		self.ent_password = Entry(text=input_password, font=self.fontstyle, width=25, bg='light blue')
		self.ent_password.place(x=130, y=150)

	def register_login_button(self):
		"""Create Sign Up and Login Button"""
		global style
		style = ttk.Style()
		style.configure('TButton', font=('Times New Roman', 12),background='blue', width=10)
	
		#sign up button
		reg_label = Label(text='Do not have an account? Try ', font=self.fontstyle).place(x=70, y=240)
		self.btn_register = ttk.Button(text='Register', style='TButton', command=self.register)
		self.btn_register.place(x=230, y=240)

		#login button
		self.btn_login = ttk.Button(text='Login', style='TButton', command=self.login_user_verify)
		self.btn_login.place(x=230, y=200)

	def register(self):
		"""Make toplevel window; registration window"""

		global register
		register = Toplevel()
		register.title('Register')
		register.geometry('350x200')
		register.resizable(0,0)
		icon_photo = PhotoImage(file='icon_login3.png')
		register.iconphoto(False, icon_photo)
		
		lbl_top = Label(master=register, text='Register your account here ', font=self.fontstyle, fg='dark grey').pack()
		lbl_username = Label(master=register, text='Username ', font=self.fontstyle)
		lbl_username.place(x=20, y=40)
		lbl_password = Label(master=register, text='Password', font=self.fontstyle)
		lbl_password.place(x=20, y=80)

		global username
		global password
		username = StringVar()
		password = StringVar()

		global ent_username
		global ent_password
		ent_username = Entry(master=register, text=username, font=self.fontstyle, width=25, bg='light blue')
		ent_username.place(x=100, y=40)
		ent_password = Entry(master=register, text=password, font=self.fontstyle, width=25, bg='light blue')
		ent_password.place(x=100, y=80)

		btn_register = ttk.Button(master=register, text='Register', style='TButton', command=self.register_user)
		btn_register.place(x=140, y=150)

		btn_close = ttk.Button(master=register, text='Close', style='TButton', command=self.close_register)
		btn_close.place(x=250, y=150)

	def register_user(self):
		"""Handle user's username and password"""

		username_info = username.get()
		password_info = password.get()
		list_of_files = os.listdir()
		try:
			if username_info not in list_of_files:
				if username_info != '' and password_info != '':
					file = open(username_info, 'w')
					file.write(username_info+'\n')
					file.write(password_info+'\n')
					file.close()

					ent_username.delete(0, END)
					ent_password.delete(0, END)

					succes_lbl = Label(master=register, text='Your registration succes!', font=self.fontstyle, fg='red')
					succes_lbl.place(x=120, y=115)
					succes_lbl.after(2000, lambda: succes_lbl.place_forget())
					succes_lbl.after(3000, lambda: self.close_register())


				else:
					no_user_pass = Label(master=register, text='Please enter username and password!', font=self.fontstyle, fg='red')
					no_user_pass.place(x=100, y=115)
					no_user_pass.after(2000, lambda: no_user_pass.place_forget())

			else:
				user_used = Label(master=register, text='Username is already used', font=self.fontstyle, fg='red')
				user_used.place(x=120, y=115)
				user_used.after(2000, lambda: user_used.place_forget())

		except (FileNotFoundError):
			no_user_pass = Label(master=register, text='Please enter username and password!', font=self.fontstyle, fg='red')
			no_user_pass.place(x=100, y=115)
			no_user_pass.after(2000, lambda: no_user_pass.place_forget())

		'''
		To fix later, register succes eventhough there is no password or username entered
		--> fixed
		''' 

	def close_register(self):
		"""Close registration window"""
		register.destroy()

	def login_user_verify(self):
		"""Verify user's credentials"""

		username_info = self.ent_username.get()
		password_info = self.ent_password.get()

		list_of_files = os.listdir()
		if username_info in list_of_files:
			file = open(username_info, 'r')
			verify = file.read()

			if password_info in verify:
				if password_info != '':
					self.ent_username.delete(0, END)
					self.ent_password.delete(0, END)
					self.login_succes()

			else:
				self.ent_password.delete(0, END)
				self.wrong_password()
		else:
			self.user_not_found()

	def user_not_found(self):
		"""User not found"""
	
		not_found_lbl = Label(text='User not found. Your account not registered',
						font=('Times New Roman', 10), fg='red')
		not_found_lbl.place(x=130, y=175)
		not_found_lbl.after(1000, lambda: not_found_lbl.place_forget())

	def login_succes(self):
		"""Login success"""
		''''to do later : open new windows'''
		
		login_succes_lbl = Label(text='Login succes', font=('Times New Roman', 10), fg='green')
		login_succes_lbl.place(x=130, y=175)
		login_succes_lbl.after(1000, lambda: exit())

	def wrong_password(self):
		"""Wrong password"""

		wrong_password_lbl = Label(text='You entered wrong password', font=('Times New Roman', 10),
							 fg='red')
		wrong_password_lbl.place(x=130, y=175)
		wrong_password_lbl.after(1000, lambda: wrong_password_lbl.place_forget())


root = Tk()
app = Window(root)
root.geometry('400x300')
root.resizable(0,0)
icon_photo = PhotoImage(file='icon_login3.png')
root.iconphoto(False, icon_photo)
root.mainloop()