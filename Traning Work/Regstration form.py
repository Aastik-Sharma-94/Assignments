label_0 = Label(root, text="REGISTRATION FORM",width=25,background="aqua",font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="SR. No.",width=20,font=("bold", 10))
label_1.place(x=66,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="NAME",width=20,font=("bold", 10))
label_2.place(x=66,y=160)

entry_2 = Entry(root)
entry_2.place(x=240,y=160)

label_2 = Label(root, text="Roll no",width=20,font=("bold", 10))
label_2.place(x=66,y=190)

entry_2 = Entry(root)
entry_2.place(x=240,y=190)

label_3 = Label(root, text="Address",width=20,font=("bold", 10))
label_3.place(x=66,y=220)

entry_2 = Entry(root)
entry_2.place(x=240,y=220)

label_5=Label(root,text="Branch",width=20,font=("bold",10))
label_5.place(x=66,y=250)
list_of_branches=[ 'CSE' ,'ECE' , 'Electrical' ,'Mechanical' ,'Civil']
c=StringVar()
droplist=OptionMenu(root,c, *list_of_branches)
droplist.config(width=15)
c.set('Select your branch')
droplist.place(x=240,y=250)

label_6 =Label(root,text="Gender", width=20,font=("bold",10))
label_6.place(x=66,y=290)


var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=240,y=290)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=299,y=290)

Button(root, text='Submit',width=20,bg='blue',fg='white').place(x=150,y=380)
root.configure(background = "white")
root.mainloop()
print("Registration Form  successfully created...")