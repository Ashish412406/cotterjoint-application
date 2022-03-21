from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk



def myfunc():
    
    pass

def exit():
    root.destroy()

def how_to_use():
    tmsg.showinfo("How to use this application","step 1 - First read about cotter joint from V.B bhandari.\nstep 2 - Type the values to the respective field provided.\nstep 3 - Click on Run button.\nstep 4 - See the output in righthandside white frame.\nstep 5 - No more steps. Enjoy !!! ")
    pass

def cotterjoint_section():
    listbox.insert(END,f"You are in Cotter Joint Section")

def knnucklejoint_section():
    listbox.insert(END,f"Knuckle Joint section will be added soon")

def cotterinfo():
    tmsg.showinfo("What is Cotter Joint", "A cotter joint is used to connect two co-axial rods, which are subjected to either axial tensile force or axial compressive force. It is also used to connect a rod on one side with some machine part like a crosshead or base plate on the other side. It is not used for connecting shafts that rotate and transmit torque. Typical applications of cotter joint are as follows: (i) Joint between the piston rod and the crosshead of a steam engine (ii) Joint between the slide spindle and the fork of the valve mechanism (iii) Joint between the piston rod and the tail or pump rod")

    pass

def knuckleinfo():
    tmsg.showinfo("What is Knucle Joint", "Knuckle joint is used to connect two rods whose axes either coincide or intersect and lie in one plane. The knuckle joint is used to transmit axial tensile force. The construction of this joint permits limited angular movement between rods, about the axis of the pin. ")
    

def getvals():
    # listbox.insert(END,  yeild.get())
    

    #print(f"{yeild.get()} {fos_s.get()} {fos_c.get()} {load_value.get()}")

    import math
    #material=input("enter material ")
    yeild_stress=int(yeild.get())
    fos_socket_and_spigot=float(fos_s.get())
    fos_cotter=float(fos_c.get())
    load=int(load_value.get())

    # Design stress valve for socket and spigot 
    socket_sdt=yeild_stress/fos_socket_and_spigot
    #print("Design tensile stress valve of socket and spigot is ",socket_sdt)
    socket_sds=0.6*socket_sdt
    #print("Design shear stress valve of socket and spigot is ",socket_sds)
    socket_sdcr=1.2*socket_sdt
    #print("Design crushing stress valve of socket and spigot is ",socket_sdcr)

    # Design stress valve for cotter
    cotter_sdt=yeild_stress/fos_cotter
    #print("Design tensile stress valve of cotter is ",cotter_sdt)
    cotter_sds=0.6*cotter_sdt
    #print("Design shear stress valve of cotter is ",cotter_sds)
    cotter_sdcr=1.2*cotter_sdt
    #print("Design crushing stress valve of cotter is ",cotter_sdcr)

    #Step_1 : Tensile failure of socket rod 
    d=(load/socket_sdt*1.273239545)**0.5
    #print("The valve of d is ",d,"mm")

    #step_2: Failure of spigot in tension across the weakest section 
    d2=(load/socket_sdt*1.867768828)**0.5
    #print("The valve of d2 is ",d2,"mm")
    t=d2/4
    #print("The valve of t is ",t,"mm")

    #Step_3 : Crushing failure of spigot ennd
    crushing_indunced = load/(d2*t)
    #print("crushing stress induce at spigot end is ",crushing_indunced)
    if (crushing_indunced<socket_sdcr):
        pass
        #print("crushing stress induced is less than design crushing stress hence the design crushing stress is safe")
    #reevalating safe dimensiones of d2 and t
    else:
        d2=((4*load)/socket_sdcr)**0.5
        t=d2/4
        #print(f"now after evaluating d2 becomes {d2}mm and t becomes {t}mm")

    # Step_4 : failure of socket in tension across the slot



    # import complex math module
    import cmath
  
    a = 0.7853981*socket_sdt
    # print(a)
    b = -t
    # print(b)
    c = (d2*t)-(socket_sdt*0.7853981634*(d2**2))-(load)
    # print(c) 

    # Python program to find roots of quadratic equation
    import math 
  
  

    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
    d1= (-b + sqrt_val)/(2 * a)
      
    #print("The value of d1 is ",d1,"mm") 

    #step_5 Failure of cotter in shear
    b=load/(2*t*cotter_sds)
    #print("The value of b is ",b,"mm")

    # step_6 failure of socket coller in crushing
    d4=(load+(d2*t*socket_sdcr))/(t*socket_sdcr)
    #print("The value of d4 is ",d4,"mm")
      
    # Step_7 : Failure of socket end in shearing
    c=(load)/((2*socket_sds*d4)-(2*socket_sds*d2))
    #print("The value of c is ",c,"mm")
  

    # Step_8 : Failure of rod end in shear
    a=(load)/(2*d2*socket_sds)
    #print("The value of a is ",a,"mm")

    #   Step_9 : Failure of spigot coller in crushing 
    d3=((load/(0.7853981634*socket_sdcr))+(d2**2))**0.5
    #print("The value of d3 is ",d3,"mm")

    #Step_10 : Failure of spigot coller in shearing 
    t1=load/(3.141592654*d2*socket_sds)
    #print("The value of t1 is ",t1,"mm")

    # Step_11 : Failure of cotter in bending 
    BMmax=(((d4-d2)/6)+(d2/4))*(load/2)
    #print(BMmax)

    z=t*b*b/6
    #print(z)

    bending_stress_induced=(load*(d4+0.5*d2))/(2*t*b*b)
    #print(bending_stress_induced)

    if(bending_stress_induced>cotter_sdt):
       # print("bending stress induced is greater than cotter design stress hance design is unsafe")
        b=((6*BMmax)/(t*cotter_sdt))**0.5
       # print("The safe valve of b is ",b,"mm")
    else:
        pass
        #print("bending stress induced is lesser than cotter design stress hance design is safe")

    listbox.insert(END,f"The valve of d is {round(d,2)} mm")
    listbox.insert(END, f"The value of d1 is {round(d1,2)} mm")
    listbox.insert(END, f"The valve of d2 is {round(d2,2)} mm")
    listbox.insert(END, f"The value of d3 is {round(d3,2)} mm")
    listbox.insert(END, f"The value of d4 is {round(d4,2)} mm")
    listbox.insert(END, f"The valve of t is {round(t,2)} mm")
    listbox.insert(END, f"The value of t1 is {round(t1,2)} mm")
    listbox.insert(END, f"The value of a is {round(a,2)} mm")
    listbox.insert(END, f"The safe valve of b is {round(b,2)} mm")
    listbox.insert(END, f"The value of c is {round(c,2)} mm")
    



root = Tk()
root.geometry("1100x700")
root.title("Design of Cotter Joint by Ashish")
root.iconbitmap("logo.ico")



mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Cotter Joint", command=cotterjoint_section)
m1.add_command(label="Knuckle Joint", command=knnucklejoint_section)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="What is Cotter joint", command=cotterinfo)
m3.add_command(label="What is Knuckle joint", command=knuckleinfo)
m3.add_separator()
m3.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Info", menu=m3)

m4 = Menu(mainmenu, tearoff=0)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="How to use",command=how_to_use)

m5 = Menu(mainmenu, tearoff=0)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Exit",command=exit)

# Read the Image
image = Image.open("cotter.png")
 
# Resize the image using resize() method
resize_image = image.resize((550, 500))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.grid(column=0,pady=20,padx=10)

#Entry Widget
yeild = Label(root, text="Yeild Stress (Nmm)")
fos_s = Label(root, text="FOS (soket and spigot) ")
fos_c = Label(root, text="FOS (Cotter)")
load_value = Label(root, text="load value (Nmm)")


yeild.grid(row=1,sticky="e")
fos_s.grid(row=2,sticky="e")
fos_c.grid(row=3,sticky="e")
load_value.grid(row=4,sticky="e")


# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

yeild = StringVar()
fos_s = StringVar()
fos_c = StringVar()
load_value = StringVar()


yeild = Entry(root, textvariable = yeild)
fos_s = Entry(root, textvariable = fos_s)
fos_c = Entry(root, textvariable = fos_c)
load_value = Entry(root, textvariable = load_value)


yeild.grid(row=1, column=2)
fos_s.grid(row=2, column=2)
fos_c.grid(row=3, column=2)
load_value.grid(row=4, column=2)


Button(text="Run ",font="lucida 14 bold", fg="yellow",padx=20,bg="grey", command=getvals).grid(column=2,pady=10)


# Output screen
listbox=Listbox(root,height=30,width=50)
listbox.grid(row=0, column=4, rowspan=6, columnspan=5,padx=25)
 


root.mainloop()