from tkinter import * 


root = Tk()

main_entry=Entry(root,width=53,borderwidth=0,bg="#212121",fg="white")
main_entry.grid(row=0,column=0,columnspan=4,ipady=28)
root.title("CALCULATOR")
root.configure(bg='#212121')


def button_clicked(number):
    # main_entry.delete(0,END)
    get = main_entry.get()
    main_entry.delete(0,END)
    main_entry.insert(0,str(get) + str(number))
    
    


def plus():

    global second_number

    global first_number

    global operation 


    operation ="plus"

    first_number = float(main_entry.get())      
    main_entry.delete(0,END)

   



def minus():

     global second_number

     global first_number
 
     global operation 

     operation = "minus"

     first_number = float(main_entry.get())
     main_entry.delete(0,END)


def divide():
     global second_number

     global first_number
 
     global operation 

     operation = "divide"

     first_number = float(main_entry.get())
     main_entry.delete(0,END)


def impact():
     global second_number

     global first_number
 
     global operation 

     operation = "impact"

     first_number = float(main_entry.get())
     main_entry.delete(0,END)

def translate():

    global first_number
    global operation


    operation = "translate"
    first_number = float(main_entry.get())
    main_entry.delete(0,END)


   




def delet():

    current = main_entry.get()
    main_entry.delete(0, END)
    main_entry.insert(0, current[:-1])


def delet_all():

    main_entry.delete(0,END)



def percentage():

    global first_number
    global operation

    operation="percenet"
    first_number = float(main_entry.get())
    main_entry.delete(0,END)

    



def squal():
    
    global second_number

    global first_number

    global operation



    try:


    

        if operation == "plus":
            second_number = float(main_entry.get())
            main_entry.delete(0,END)

            main_entry.insert(0,first_number + second_number)


            

        elif operation == "minus":
            second_number = float(main_entry.get())
            main_entry.delete(0,END)

            main_entry.insert(0,first_number - second_number)


        elif operation == "divide":
            second_number = float(main_entry.get())
            main_entry.delete(0,END)

            main_entry.insert(0,first_number // second_number)

        elif operation == "impact":

            second_number = float(main_entry.get())
            main_entry.delete(0,END)

            main_entry.insert(0,first_number * second_number)

        elif operation == "translate":
            main_entry.insert(0,0 - first_number)


        else:
            second_number = float(main_entry.get())
            main_entry.delete(0,END)
            main_entry.insert(0,first_number*second_number // 100)
   
     
    except ValueError:
        print("PLEASE ENTER A VALİD NUMBER")



    
 
    



spc1 = Button(root, text="%", width=10, height=3,command=lambda : percentage(), bg='#323232', fg='#FFFFFF')
spc2 = Button(root, text="C", width=10, height=3,command=lambda : delet_all(), bg='#323232', fg='#FFFFFF')
spc3 = Button(root, text="DELETE", width=10, height=3,command=lambda : delet(), bg='#323232', fg='#FFFFFF')
spc4 = Button(root, text=chr(247), width=10, height=3,command=lambda : divide(), bg='#323232', fg='#FFFFFF')

num7 = Button(root, text=7,width=10,height=3,command=lambda : button_clicked(7), bg='#323232', fg='#FFFFFF')
num8 = Button(root, text=8,width=10,height=3,command=lambda : button_clicked(8), bg='#323232', fg='#FFFFFF')
num9 = Button(root, text=9,width=10,height=3,command=lambda : button_clicked(9), bg='#323232', fg='#FFFFFF')
spc5 = Button(root, text="x",width=10,height=3,command=lambda : impact(), bg='#323232', fg='#FFFFFF')

num4 = Button(root, text=4,width=10,height=3,command=lambda : button_clicked(4), bg='#323232', fg='#FFFFFF')
num5 = Button(root, text=5,width=10,height=3,command=lambda : button_clicked(5), bg='#323232', fg='#FFFFFF')
num6 = Button(root, text=6,width=10,height=3,command=lambda : button_clicked(6), bg='#323232', fg='#FFFFFF')
spc6 = Button(root, text="-",width=10,height=3,command=lambda : minus(), bg='#323232', fg='#FFFFFF')

num1 = Button(root, text=1,width=10,height=3,command=lambda : button_clicked(1), bg='#323232', fg='#FFFFFF')
num2 = Button(root, text=2,width=10,height=3,command=lambda : button_clicked(2), bg='#323232', fg='#FFFFFF')
num3 = Button(root, text=3,width=10,height=3,command=lambda : button_clicked(3), bg='#323232', fg='#FFFFFF')
spc7 = Button(root, text="+",width=10,height=3,command=lambda : plus(), bg='#323232', fg='#FFFFFF')

spc8 = Button(root, text="+/-",width=10,height=3,command=lambda : translate(), bg='#323232', fg='#FFFFFF')
num0 = Button(root, text=0,width=10,height=3,command=lambda : button_clicked(0), bg='#323232', fg='#FFFFFF')
spc9 = Button(root, text=".",width=10,height=3,command=lambda : button_clicked("."), bg='#323232', fg='#FFFFFF')
spc10 = Button(root, text="=",width=10,height=3,command=lambda : squal(), bg='#323232', fg='#FFFFFF')




spc1.grid(row=1, column=0,padx=1)
spc2.grid(row=1, column=1,padx=1)
spc3.grid(row=1, column=2,padx=1)
spc4.grid(row=1, column=3,padx=1)

num7.grid(row=2, column=0,padx=1)
num8.grid(row=2, column=1,padx=1)
num9.grid(row=2, column=2,padx=1)
spc5.grid(row=2, column=3,padx=1)

num4.grid(row=3, column=0,padx=1)
num5.grid(row=3, column=1,padx=1)
num6.grid(row=3, column=2,padx=1)
spc6.grid(row=3, column=3,padx=1)

num1.grid(row=4, column=0,padx=1)
num2.grid(row=4, column=1,padx=1)
num3.grid(row=4, column=2,padx=1)
spc7.grid(row=4, column=3,padx=1)

spc8.grid(row=5, column=0,padx=1)
num0.grid(row=5, column=1,padx=1)
spc9.grid(row=5, column=2,padx=1)
spc10.grid(row=5, column=3,padx=1)








root.mainloop()