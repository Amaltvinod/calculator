from tkinter import *

root=Tk()
root.title("calculator")
root.geometry("600x600")
input=Entry(root,width=40)
input.grid(row=0, column=0, columnspan=3, pady=20)
def get_num(number):
    global previous
    previous=input.get()
    input.delete(0,END)
    input.insert(0,str(previous)+str(number))


def addition():
    pass
button1=Button(root,text="0", command= lambda: get_num(0), padx=32, pady=20)
button2=Button(root,text="1", command= lambda: get_num(1), padx=32, pady=20)
button3=Button(root,text="2", command= lambda: get_num(2), padx=32, pady=20)
button4=Button(root,text="3", command= lambda: get_num(3), padx=32, pady=20)
button5=Button(root,text="4", command= lambda: get_num(4), padx=32, pady=20)
button6=Button(root,text="5", command= lambda: get_num(5), padx=32, pady=20)
button7=Button(root,text="6", command= lambda: get_num(6), padx=32, pady=20)
button8=Button(root,text="7", command= lambda: get_num(7), padx=32, pady=20)
button9=Button(root,text="8", command= lambda: get_num(8), padx=32, pady=20)
button10=Button(root,text="9", command= lambda: get_num(9),padx=32, pady=20)
button11=Button(root,text="+",padx=32, pady=20)
button12=Button(root,text="-", padx=32, pady=20)
button13=Button(root,text="*", padx=32, pady=20)
button14=Button(root,text="/", padx=32, pady=20)
button15=Button(root,text="=", padx=32, pady=20)



button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button10.grid(row=4,column=1)
button11.grid(row=4,column=0)
button12.grid(row=4,column=2)
button13.grid(row=5,column=0)
button14.grid(row=5,column=1)
button15.grid(row=5,column=2)


root.mainloop()
