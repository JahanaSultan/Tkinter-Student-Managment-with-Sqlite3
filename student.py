from tkinter import *
from PIL import ImageTk, Image 
import db as sql
from tkinter import messagebox
from functools import partial


def student_info(name,surname,fullname,student_id,window):
    z=280
    def change_mark(student_id,date,index):
        def change(student_id,date):
            mark=h.get()
            if mark and mark.strip!='':
             sql.update_mark(mark,student_id,date)
            else:
                messagebox.showinfo(title="Error", message="Fill Blank")
            Button(window4,text=mark,font=("Arial",18), bg='#F0F0F0',width=5,command=partial(change_mark,student_id,date,index)).place(x=500,y=z+index*70)
            Label(window4,text=date,font=("Arial",18), bg='#F0F0F0').place(x=800,y=y)
            g.place_forget()
            h.place_forget()
            

        h=Entry(window4,font=("Arial",28), bg='#F0F0F0',width=4)
        h.place(x=500,y=z+index*70)
        g=Button(window4,text="Update",font=("Arial",16), bg='#00AEEF',width=20,command=partial(change,student_id,date))
        g.place(x=800,y=z+index*70)


    window.destroy()
    window4=Tk()
    window4.title("Teacher Profile")
    window4.config(bg="#F0F0F0")
    window4.minsize(width=1100, height=600)
    image1 = Image.open("./user.jpg").resize((150, 150))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=10, y=60)

    Label(window4,text="Hello"+" "+name+" "+surname, font=("Arial",25,"bold"), bg='#F0F0F0', fg="#00AEEF",pady=25).pack()

    Label(window4,text="Name:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=100)
    Label(window4,text=name,font=("Arial",18), bg='#F0F0F0').place(x=320,y=100)
    Label(window4,text="Surname:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=150)
    Label(window4,text=surname,font=("Arial",18), bg='#F0F0F0').place(x=320,y=150)
    Label(window4,text=fullname,font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=480, y=240)
    r=Button(window4,text='←',font=("Arial",18,"bold"),width=3,bg='red',fg="#fff",command=partial(group_info,name,surname,sql.group_name(student_id)[0][0],window4))
    r.place(x=1050,y=0)

    y=280
    f=0
    for i,j,k in sql.s_marks(student_id):
        f+=1
        y+=70
        Label(window4,text=i,font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=50,y=y)
        h=Button(window4,text=j,font=("Arial",18), bg='#F0F0F0', width=5,command=partial(change_mark,student_id,k,f))
        h.place(x=500,y=y)
        Label(window4,text=k,font=("Arial",18), bg='#F0F0F0').place(x=800,y=y)
    




def group_info(name,surname,group_name,window):
    window.destroy()
    window3=Tk()
    window3.title("Teacher Profile")
    window3.config(bg="#F0F0F0")
    window3.minsize(width=1100, height=600)
    image1 = Image.open("./user.jpg").resize((150, 150))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=10, y=60)

    Label(window3,text="Hello"+" "+name+" "+surname, font=("Arial",25,"bold"), bg='#F0F0F0', fg="#00AEEF",pady=25).pack()

    Label(window3,text="Name:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=100)
    Label(window3,text=name,font=("Arial",18), bg='#F0F0F0').place(x=320,y=100)
    Label(window3,text="Surname:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=150)
    Label(window3,text=surname,font=("Arial",18), bg='#F0F0F0').place(x=320,y=150)
    Label(window3,text=group_name,font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=480, y=240)
    r=Button(window3,text='←',font=("Arial",18,"bold"),width=3,bg='red',fg="#fff",command=partial(teacher_interface,name,surname,sql.teacher_id(group_name)[0][0],window3))
    r.place(x=1050,y=0)
    
    y=280
    def mark(index,s_id):
        Button(window3,text='+',font=("Arial",18,"bold"),state=DISABLED).place(x=400,y=360+index*80)
        
        def add(s_id):
            en=t.get()
            if en and en.strip!='':
                if sql.add_mark(s_id,en):
                    messagebox.showinfo(title="Success", message="Succesfully Added")
                    Label(window3, text=en,font=("Arial",24),width=10).place(x=600,y=360+index*80)
                    b.place_forget()

                else:
                    messagebox.showinfo(title="Error", message="Please check info")
            else:
                messagebox.showinfo(title="Error", message="Fill The Blank")


        t=Entry(window3,font=("Arial",24),width=10)
        t.place(x=600,y=360+index*80)
        b=Button(window3,text='Add Mark',font=("Arial",16),command=partial(add,s_id))
        b.place(x=850,y=360+index*80)

    
    for fullname in sql.list_student(group_name):
        y+=80
        v=Button(window3, text=fullname[0],font=("Arial",20), bg='#F0F0F0',command=partial(student_info,name,surname,fullname[0],fullname[1],window3))
        v.place(x=50,y=y)
        l=Button(window3,text='+',font=("Arial",18,"bold"),command=partial(mark,sql.list_student(group_name).index(fullname),fullname[1]))
        l.place(x=400,y=y)
    

        

def teacher_interface(name,surname,id,window):
    window.destroy()
    window2=Tk()
    window2.title("Teacher Profile")
    window2.config(bg="#F0F0F0")
    window2.minsize(width=1100, height=600)
    image1 = Image.open("./user.jpg").resize((150, 150))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=10, y=60)

    Label(window2,text="Hello"+" "+name+" "+surname, font=("Arial",25,"bold"), bg='#F0F0F0', fg="#00AEEF",pady=25).pack()

    Label(window2,text="Name:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=100)
    Label(window2,text=name,font=("Arial",18), bg='#F0F0F0').place(x=320,y=100)
    Label(window2,text="Surname:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=150)
    Label(window2,text=surname,font=("Arial",18), bg='#F0F0F0').place(x=320,y=150)
    Label(window2,text="Groups: ",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=480, y=240)
    x=50
    for group in sql.groups(id):
        x+=120
        Button(window2,text=group[0],font=("Arial", 20), bg="#00AEEF", fg="white", command=partial(group_info,name,surname,group[0],window2)).place(x=x,y=300)
    
    window2.mainloop()
    
    
def student_interface(name,surname,student_id, phone, email,window):
    window.destroy()
    window1=Tk()
    window1.title("Student Profile")
    window1.config(bg="#F0F0F0")
    window1.minsize(width=1100, height=600)
    image1 = Image.open("./user.jpg").resize((150, 150))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=10, y=60)

    


    Label(window1,text="Hello"+" "+name+" "+surname, font=("Arial",25,"bold"), bg='#F0F0F0', fg="#00AEEF",pady=25).pack()

    Label(window1,text="Name:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=100)
    Label(window1,text=name,font=("Arial",18), bg='#F0F0F0').place(x=320,y=100)
    Label(window1,text="Surname:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=200,y=150)
    Label(window1,text=surname,font=("Arial",18), bg='#F0F0F0').place(x=320,y=150)
    Label(window1,text="Phone:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=480,y=100)
    Label(window1,text=phone,font=("Arial",18), bg='#F0F0F0').place(x=580,y=100)
    Label(window1,text="Email:",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=480,y=150)
    Label(window1,text=email,font=("Arial",18), bg='#F0F0F0').place(x=580,y=150)
    Label(window1, text="Avarage: ", font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=830,y=120)
    Label(window1, text=sql.avarage(student_id), font=("Arial",18,"bold"), bg='#F0F0F0').place(x=940,y=120)

    Label(window1,text="MARKS: ",font=("Arial",18,"bold"), bg='#F0F0F0',fg="#00AEEF").place(x=480, y=260)
    Label(window1,text="Lesson",font=("Arial",18,"bold"), bg='#F0F0F0',fg="red").place(x=50, y=320)
    Label(window1,text="Mark",font=("Arial",18,"bold"), bg='#F0F0F0',fg="red").place(x=500, y=320)
    Label(window1,text="Date",font=("Arial",18,"bold"), bg='#F0F0F0',fg="red").place(x=900, y=320)

    y=360
    for i,j,k in sql.s_marks(student_id):
        y+=40
        Label(window1,text=i,font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=50,y=y)
        Label(window1,text=j,font=("Arial",18), bg='#F0F0F0').place(x=500,y=y)
        Label(window1,text=k,font=("Arial",18), bg='#F0F0F0').place(x=800,y=y)
        
    window1.mainloop()


def group_register(window):
    def g_register():
        group_id=gid.get()
        group_name=gname.get()
        teacher_name=tn.get()
        teacher_surname=ts.get()
        
        if group_id.strip()!='' and group_name.strip()!='' and teacher_name.strip()!='' and teacher_surname.strip()!='':
            if sql.group_register(group_id, group_name,teacher_name,teacher_surname):
                gid.delete(0,END)
                gname.delete(0,END)
                tn.delete(0,END)
                ts.delete(0,END)
                messagebox.showinfo(title="Success", message="Succesfully Added")
            else:
                messagebox.showinfo(title="Error", message="Please Check Informations")
        else:
            messagebox.showinfo(title="Error", message="Please Fill Blanks")




    
    window.destroy()
    window8=Tk()
    window8.title("Admin Profile")
    window8.config(bg="#F0F0F0")
    window8.minsize(width=1100, height=600)

    r=Button(window8,text='←',font=("Arial",18,"bold"),width=3,bg='red',fg="#fff",command=lambda:admin_interface(window8))
    r.place(x=1050,y=0)

    Label(window8,text="Group Registration",font=("Arial",20,"bold"), bg='#F0F0F0',fg="#00AEEF").pack()
    Label(window8,text="Group Id: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=60)
    Label(window8,text="Group Name: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=110)
    gid=Entry(window8,font=("Arial",18), bg='#F0F0F0')
    gid.place(x=220, y=60)
    gname=Entry(window8,font=("Arial",18), bg='#F0F0F0')
    gname.place(x=220, y=110)
    Label(window8,text="Teacher Name: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=60)
    Label(window8,text="Teacher Surname: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=110)
    tn=Entry(window8,font=("Arial",18), bg='#F0F0F0')
    tn.place(x=690, y=60)
    ts=Entry(window8,font=("Arial",18), bg='#F0F0F0')
    ts.place(x=690, y=110)
    btn=Button(window8,text="Group Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=2,command=g_register)
    btn.place(x=450,y=240)
    window8.mainloop()



def teacher_register(window):
    def t_register():
        name1=name.get()
        surname1=surname.get()
        teid=tid.get()
        email1=email.get()
        lesson1=lesson.get()
        password1=pasw.get()
        
        if name1 and name1.strip()!='' and surname1 and surname1.strip!='' and teid and teid.strip()!='' and email1 and email1.strip()!='' and lesson1 and lesson1.strip()!='' and password1 and password1.strip()!='':
            if sql.teacher_register(name1,surname1,teid,email1,lesson1,password1):
                name.delete(0,END)
                surname.delete(0,END)
                tid.delete(0,END)
                email.delete(0,END)
                lesson.delete(0,END)
                pasw.delete(0,END)
                messagebox.showinfo(title="Success", message="Succesfully Added")
            else:
                messagebox.showinfo(title="Error", message="Please Check Informations")
        else:
            messagebox.showinfo(title="Error", message="Please Fill Blanks")


    window.destroy()
    window7=Tk()
    window7.title("Admin Profile")
    window7.config(bg="#F0F0F0")
    window7.minsize(width=1100, height=600)

    r=Button(window7,text='←',font=("Arial",18,"bold"),width=3,bg='red',fg="#fff",command=lambda:admin_interface(window7))
    r.place(x=1050,y=0)

    Label(window7,text="Teacher Registration",font=("Arial",20,"bold"), bg='#F0F0F0',fg="#00AEEF").pack()
    Label(window7,text="Name:",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=60)
    Label(window7,text="Surname: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=110)
    Label(window7,text="Teacher ID: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=160)
    name=Entry(window7,font=("Arial",18), bg='#F0F0F0')
    name.place(x=220, y=60)
    surname=Entry(window7,font=("Arial",18), bg='#F0F0F0')
    surname.place(x=220, y=110)
    tid=Entry(window7,font=("Arial",18), bg='#F0F0F0')
    tid.place(x=220, y=160)
    Label(window7,text="Email: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=60)
    Label(window7,text="Lesson: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=110)
    Label(window7,text="Password: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=160)
    email=Entry(window7,font=("Arial",18), bg='#F0F0F0')
    email.place(x=650, y=60)
    lesson=Entry(window7,font=("Arial",18), bg='#F0F0F0')
    lesson.place(x=650, y=110)
    pasw=Entry(window7,font=("Arial",18), bg='#F0F0F0')
    pasw.place(x=650, y=160)
    btn=Button(window7,text="Teacher Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=2,command=t_register)
    btn.place(x=450,y=290)

    window7.mainloop()
    


def student_register(window):

    def s_register():
        name1=name.get()
        surname1=surname.get()
        s_number=snumber.get()
        p_number=pnumber.get()
        email1=email.get()
        group1=group.get()
        password=pasw.get()
        

        if name1 and surname1 and s_number and p_number and email1 and group1 and password and name1.strip()!='' and surname1.strip()!='' and s_number.strip()!='' and p_number.strip()!='' and email1.strip()!='' and group1.strip()!='' and password.strip()!='':

            if sql.student_register(name1,surname1,s_number,p_number,email1,group1,password):
                name.delete(0,END)
                surname.delete(0,END)
                snumber.delete(0,END)
                pnumber.delete(0,END)
                email.delete(0,END)
                group.delete(0,END)
                pasw.delete(0,END)
                pasw1.delete(0,END)
                messagebox.showinfo(title="Success", message="Succesfully Added")
            else:
                messagebox.showinfo(title="Error", message="Please Check Informations")
        else:
            messagebox.showinfo(title="Error", message="Please Fill Blanks")

    window.destroy()
    window6=Tk()
    window6.title("Admin Profile")
    window6.config(bg="#F0F0F0")
    window6.minsize(width=1100, height=600)

    r=Button(window6,text='←',font=("Arial",18,"bold"),width=3,bg='red',fg="#fff",command=lambda:admin_interface(window6))
    r.place(x=1050,y=0)

    Label(window6,text="Student Registration",font=("Arial",20,"bold"), bg='#F0F0F0',fg="#00AEEF").pack()
    Label(window6,text="Name:",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=60)
    Label(window6,text="Surname: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=110)
    Label(window6,text="Student Number: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=160)
    Label(window6,text="Phone Number: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=210)
    name=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    name.place(x=220, y=60)
    surname=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    surname.place(x=220, y=110)
    snumber=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    snumber.place(x=220, y=160)
    pnumber=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    pnumber.place(x=220, y=210)
    Label(window6,text="Email: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=60)
    Label(window6,text="Group: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=110)
    Label(window6,text="Password: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=160)
    Label(window6,text="Password: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=500, y=210)
    email=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    email.place(x=650, y=60)
    group=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    group.place(x=650, y=110)
    pasw=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    pasw.place(x=650, y=160)
    pasw1=Entry(window6,font=("Arial",18), bg='#F0F0F0')
    pasw1.place(x=650, y=210)

    btn=Button(window6,text="Student Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=2,command=s_register)
    btn.place(x=450,y=290)
    
    window6.mainloop()


def lesson_register(window):
    def l_register():
        lid=id.get()
        lname=name.get()

        if lid.strip()!='' and lname.strip()!='':
            if sql.lesson_register(lid,lname):
                id.delete(0,END)
                name.delete(0,END)
                messagebox.showinfo(title="Success", message="Succesfully Added")
            else:
                messagebox.showinfo(title="Error", message="Please Check Informations")
        else:
            messagebox.showinfo(title="Error", message="Please Fill Blanks")


    window.destroy()
    window8=Tk()
    window8.title("Admin Profile")
    window8.config(bg="#F0F0F0")
    window8.minsize(width=1100, height=600)

    r=Button(window8,text='←',font=("Arial",18,"bold"),width=3,bg='red',fg="#fff",command=lambda:admin_interface(window8))
    r.place(x=1050,y=0)

    Label(window8,text="Lesson Registration",font=("Arial",20,"bold"), bg='#F0F0F0',fg="#00AEEF").pack()
    Label(window8,text="Lesson Id: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=60)
    Label(window8,text="Lesson Name: ",font=("Arial",18), bg='#F0F0F0',fg="#00AEEF").place(x=20, y=110)
    id=Entry(window8,font=("Arial",18), bg='#F0F0F0')
    id.place(x=220, y=60)
    name=Entry(window8,font=("Arial",18), bg='#F0F0F0')
    name.place(x=220, y=110)
    btn=Button(window8,text="Lesson Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=2,command=l_register)
    btn.place(x=450,y=220)
    window8.mainloop()




def admin_interface(window):
    window.destroy()
    window5=Tk()
    window5.title("Admin Profile")
    window5.config(bg="#F0F0F0")
    window5.minsize(width=1100, height=600)
    image1 = Image.open("./admin.png").resize((500, 250))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=300, y=90)

    Label(window5,text="Hello Admin", font=("Arial",25,"bold"), bg='#F0F0F0', fg="#00AEEF",pady=25).pack()
    b1=Button(window5,text="Student Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=lambda:student_register(window5))
    b1.place(x=480,y=350)
    b2=Button(window5,text="Teacher Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=lambda:teacher_register(window5))
    b2.place(x=480,y=400)
    b3=Button(window5,text="Group Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=lambda:group_register(window5))
    b3.place(x=480,y=450)
    b4=Button(window5,text="Lesson Register",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=lambda:lesson_register(window5))
    b4.place(x=480,y=500)


    window5.mainloop()



    


def login():

    def s_login():
        username=un.get()
        password=pswd.get()

        if sql.s_login(username,password):
            student_interface(sql.s_login(username,password)[0][0],sql.s_login(username,password)[0][1],sql.s_login(username,password)[0][2],sql.s_login(username,password)[0][3],sql.s_login(username,password)[0][4],window)
        else:
            messagebox.showinfo(title="Login", message="Username or password incorrect")
    

    def t_login():
        username=un.get()
        password=pswd.get()

        if sql.t_login(username,password):
            teacher_interface(sql.t_login(username,password)[0][0],sql.t_login(username,password)[0][1],sql.t_login(username,password)[0][2],window)
        else:
            messagebox.showinfo(title="Login", message="Username or password incorrect")

    def admin():
        username=un.get()
        password=pswd.get()

        if sql.admin_login(username,password):
            admin_interface(window)
        else:
            messagebox.showinfo(title="Login", message="Username or password incorrect")


    

    window=Tk()
    window.title("Student Managment Login")
    window.config(bg="#F0F0F0")
    window.minsize(width=1100, height=600)
    image1 = Image.open("./icon.png").resize((450, 300))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0, y=150)

    Label(text="Welcome Student Managment System",font=("New Times Roman", 25,"bold"),pady=25,bg="#F0F0F0").pack()
    Label(text="Please Login", font=("Arial",25,"bold"),bg="#F0F0F0").pack()
    Label(text="username",font=("New Times Roman", 20),bg="#F0F0F0",fg="#00AEEF").place(x=400,y=220)
    Label(text="password",font=("New Times Roman", 20),bg="#F0F0F0",fg="#00AEEF").place(x=400,y=270)
    
    un=Entry(width=20,font=("Arial",20))
    un.place(x=550,y=220)
    pswd=Entry(width=20,font=("Arial",20))
    pswd.place(x=550,y=270)

    st_login=Button(text="Student Login",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=s_login)
    st_login.place(x=400,y=350)
    t_login=Button(text="Teacher Login",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=t_login)
    t_login.place(x=592,y=350)
    admin=Button(text="Admin",font=("Arial",16),bg="#00AEEF",fg="white",width=15,height=1,command=admin)
    admin.place(x=784,y=350)




    window.mainloop()

login()


    
    
    
   