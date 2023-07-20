from tkinter import *
from functools import partial
root = Tk()

def detect():
    import login
def exit():
	root.destroy()
	import first
def nextPage2():
    root.destroy()
    import run
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return


canvas1 = Canvas( root, width = 400,height = 400,bg="skyblue")
canvas1.create_text( 700, 50, text = "Sign Up", font=('Helvetica','50','bold'))
canvas1.pack(fill = "both", expand = True)
button1 = Button( root, text = "Login", bg='yellow',  fg = 'blue', height = 3, width = 10,command=detect)
button2 = Button( root, text = "Sign Up",bg='yellow',  fg = 'blue', height = 3, width = 10,command=nextPage2)
button3 = Button( root, text = "Exit",bg = 'Red', height = 2, width = 10,command=exit)
#username label and text entry box
usernameLabel = Label(root, text="Name")
username = StringVar()
usernameEntry = Entry(root, textvariable=username)

useremailLabel = Label(root, text="Email")
useremailEntry = Entry(root, textvariable=username)

userageLabel = Label(root, text="Age")
userageEntry = Entry(root, textvariable=username)

usercontactLabel = Label(root, text="Contact No :")
usercontactEntry = Entry(root, textvariable=username)

#password label and password entry box
passwordLabel = Label(root,text="Password")
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*')

genderlabel = Label(root,text="Gender")


radiomale=Radiobutton(root, text="Male",padx = 5, value=1)
radiofemale=Radiobutton(root, text="Female",padx = 20,  value=2)

validateLogin = partial(validateLogin, username, password)



# Display Buttons
button1_canvas = canvas1.create_window( 520, 500,
									anchor = "nw",
									window = button1)
button2_canvas = canvas1.create_window( 650, 500,
									anchor = "nw",
									window = button2)
button3_canvas = canvas1.create_window( 600, 600, anchor = "nw",
									window = button3)
labelcanvas = canvas1.create_window( 500, 200, anchor = "nw",
									window = usernameLabel)
usernameEntrylabel=canvas1.create_window( 600, 200, anchor = "nw",
									window = usernameEntry)
passwordLabel1=canvas1.create_window( 500, 250, anchor = "nw",
									window = passwordLabel)
passwordEntry1=canvas1.create_window( 600, 250, anchor = "nw",
									window = passwordEntry)
useremailLabel1=canvas1.create_window( 500, 150, anchor = "nw",
									window = useremailLabel)
useremailEntry1=canvas1.create_window( 600, 150, anchor = "nw",
									window = useremailEntry)

userageLabel1=canvas1.create_window( 500, 300, anchor = "nw",
									window = userageLabel)
userageEntry1=canvas1.create_window( 600, 300, anchor = "nw",
									window = userageEntry)
genderlabel1=canvas1.create_window( 500, 350, anchor = "nw",
									window = genderlabel)

radiomale1=canvas1.create_window( 600, 350, anchor = "nw",
									window = radiomale)
radiofemale1=canvas1.create_window( 650, 350, anchor = "nw",
									window = radiofemale)

usercontactLabel1=canvas1.create_window( 500, 400, anchor = "nw",
									window = usercontactLabel)
usercontactEntry1=canvas1.create_window( 600, 400, anchor = "nw",
									window = usercontactEntry)


root.geometry("1366x768")
