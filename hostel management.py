from datetime import datetime
from tkinter.ttk import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3



base = Tk()
base.title("HOSTEL MANAGEMENT SOFTWARE")
base.geometry("1535x790")
base.config(bg="midnightblue")
back=PhotoImage(file="background1.png")
Label(base, image=back,bg="midnightblue").place(x=-1, y=0)
global stname
stname=""

def admin_login():

    frame = Frame(base, bg='#A7ECFF', height=475, width=800)
    frame.place(x=330, y=215)
    global bg
    bg = PhotoImage(file="admin_logo.png")
    lb = Label(frame, image=bg, bg="#A7ECFF").place(x=300, y=0)
    username = Label(frame, text="Username :", font=("cambria 25 bold"), bg="#A7ECFF", fg="black").place(x=120, y=200)
    user_entry = Entry(frame, width=17, font=("cambria 20"))
    user_entry.place(x=320, y=200)
    user_entry.focus()
    password = Label(frame, text="Password :", font=("cambria 25 bold"), bg="#A7ECFF", fg="black").place(x=120, y=300)
    pass_entry = Entry(frame, width=17, font="cambria 20")
    pass_entry.place(x=320, y=300)

    def login():
        id = str(user_entry.get())
        key = str(pass_entry.get())
        if id == "admin" and key == "1234":
            messagebox.showinfo("SUCCESS","Admin login Succesful....")
            afteradmin_login()
        else:
            user_entry.focus()
            user_entry.delete(0, END)
            pass_entry.delete(0, END)
            messagebox.showerror("ERROR","Wrong username or password")

    login_btn = Button(frame, text="Login", command=login, font=("cambria 15 bold"), bg="yellow", fg="black", width=13,border=10)
    login_btn.place(x=330, y=380)


def stud_login():
    frame = Frame(base, bg='#A7ECFF', height=480, width=800)
    frame.place(x=330, y=215)
    global bg
    bg = PhotoImage(file="student_logo.png")
    lb = Label(frame, image=bg, bg="#A7ECFF").place(x=330, y=20)
    username = Label(frame, text="Username :", font=("cambria 25 bold"), bg="#A7ECFF", fg="black").place(x=120, y=200)
    user_entry = Entry(frame, width=17, font=("cambria 20"))
    user_entry.place(x=320, y=200)
    user_entry.focus()
    password = Label(frame, text="Password :", font=("cambria 25 bold"), bg="#A7ECFF", fg="black").place(x=120, y=300)
    pass_entry = Entry(frame, width=17, font="cambria 20")
    pass_entry.place(x=320, y=300)


    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS users (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT UNIQUE,
           password TEXT)''')
    conn.commit()
    conn.close()

    def register_stud():

        username = user_entry.get()
        password = pass_entry.get()
        if not username or not password:
            messagebox.showerror("Error", "User not registred")
            return
        else:
            # Connect to the SQLite database
            conn = sqlite3.connect("user_database.db")
            cursor = conn.cursor()

            # Check if the username already exists
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                messagebox.showerror("Error", "Username already exists. Choose a different one.")
            else:
                # Insert the new user into the database
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                messagebox.showinfo("Success", "student registered successfully!")
                conn.close()

    def login():

        username = user_entry.get()
        password = pass_entry.get()
        global stname
        stname = username

        # Connect to the SQLite database
        conn = sqlite3.connect("user_database.db")
        cursor = conn.cursor()

        # Check if the username and password match
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        authenticated_user = cursor.fetchone()

        if authenticated_user:
            messagebox.showinfo("Success", "Login successful!")
            afterstudlogin()

        else:
            user_entry.delete(0, END)
            pass_entry.delete(0, END)
            if username == "" and password == "":
                messagebox.showerror("Error", "Please Enter Username & Password")
            else:
                messagebox.showerror("Error", "Student not registered")

        conn.close()

    reg_btn = Button(frame, text="Register student", command=register_stud, font=("cambria 15 bold"), bg="turquoise", fg="black",width=13, border=8)
    reg_btn.place(x=600, y=380)
    login_btn = Button(frame, text="Login", command=login, font=("cambria 15 bold"), bg="yellow", fg="black", width=13,border=10)
    login_btn.place(x=330, y=380)




def start():

    global abc
    abc = PhotoImage(file="std1.png")
    Button(base,image=abc,command=stud_login,border=10,bg="gold").place(x=410,y=280)
    global lmn
    lmn = PhotoImage(file="adm.png")
    Button(base, image=lmn,command=admin_login,border=10,bg="gold").place(x=820, y=280)

def afterstudlogin():


    can = Frame(base, bg='grey', height=800, width=1550)
    can.place(x=0, y=130)
    global backg
    backg = PhotoImage(file="background.png")
    Label(can, image=backg).place(x=-5, y=0)
    global personal_img
    personal_img = PhotoImage(file="personal_info.png")
    Label(can, image=personal_img).place(x=125, y=80)
    global notice_img
    notice_img = PhotoImage(file="notice.png")
    Label(can, image=notice_img).place(x=425, y=80)
    global rule_img
    rule_img = PhotoImage(file="rules.png")
    Label(can, image=rule_img).place(x=730, y=80)
    global feedback_img
    feedback_img = PhotoImage(file="feedback.png")
    Label(can, image=feedback_img).place(x=1025, y=80)
    global logout_img
    logout_img = PhotoImage(file="logout.png")
    Label(can, image=logout_img).place(x=1325, y=80)


    def show_rules():
        can = Frame(base, bg='#A7ECFF', height=475, width=1300)
        can.place(x=125, y=310)
        Label(can, text=" ->  PLEASE FOLLOW HOSTEL TIME",font=("cambria 15 bold"),bg="#A7ECFF").place(x=500,y=50)
        Label(can, text=" ->  OUTSIDERS ARE NOT ALLOWED WITHOUT PERMISSION",font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=100)
        Label(can, text=" ->  ALCOHOL & SMOKING IS STRICTLY PROHABBITED",font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=150)
        Label(can, text=" ->  PLEASE KEEP HOSTEL AREA CLEAN",font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=200)
        Label(can, text=" ->  USE ELECTRICITY & WATER AS PER NEED ONLY",font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=250)
        Label(can, text=" ->  DON'T USE BAD WORDS IN HOSTEL AREA",font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=300)
        Label(can, text=" ->  SWITCH OFF ELECTRIC APPLIANCES WHILE GOING OUTSIDE", font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=350)
        Label(can, text=" ->  DON'T MAKE NOISE AFTER 10 PM", font=("cambria 15 bold"), bg="#A7ECFF").place(x=500,y=400)
        global rules2_img
        rules2_img = PhotoImage(file="rules2.png")
        Label(can, image=rules2_img,bg="#A7ECFF").place(x=10, y=60)


    def pdetails():
        frame = Frame(base, bg='#A7ECFF', height=475, width=1300)
        frame.place(x=125, y=310)
        Label(frame, text="First Name:", font=("cambria 15 bold"), bg='#A7ECFF', fg="black").place(x=100, y=50)
        fn = Entry(frame, width=15, font=("cambria 15"), bg='#A7ECFF', border=0, fg="red")
        fn.place(x=100, y=80)
        Label(frame, text="Last Name", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=310, y=50)
        ln = Entry(frame, width=15, font=("cambria 15"), bg='#A7ECFF', border=0, fg="red")
        ln.place(x=310, y=80)
        Label(frame, text="Father Name", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=100, y=120)
        ftn = Entry(frame, width=15, font=("cambria 15"), bg='#A7ECFF', border=0, fg="red")
        ftn.place(x=100, y=150)
        Label(frame, text="Mother Name", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=310, y=120)
        mn = Entry(frame, width=15, font=("cambria 15"), bg='#A7ECFF', border=0, fg="red")
        mn.place(x=310, y=150)
        Label(frame, text="DOB", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=100, y=200)
        dob = Entry(frame, width=15, font=("cambria 15 "), bg='#A7ECFF', border=0, fg="red")
        dob.place(x=100, y=230)
        Label(frame, text="Collage Name", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=310, y=200)
        clg = Entry(frame, width=15, font=("cambria 15 "), bg='#A7ECFF', border=0, fg="red")
        clg.place(x=310, y=230)
        Label(frame, text="Mobile_No", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=100, y=280)
        mbn = Entry(frame, width=15, font=("cambria 15 "), bg='#A7ECFF', border=0, fg="red")
        mbn.place(x=100, y=310)
        Label(frame, text="Address", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=310, y=280)
        addrs = Entry(frame, width=15, font=("cambria 15 "), bg='#A7ECFF', border=0, fg="red")
        addrs.place(x=310, y=310)
        Label(frame, text="Gender", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=100, y=350)
        gender = Entry(frame, width=15, font=("cambria 15 "), bg='#A7ECFF', border=0, fg="red")
        gender.place(x=100, y=390)
        Label(frame, text="Room No", font=("cambria 15 bold"), bg="#A7ECFF", fg="black").place(x=310, y=350)
        rmbn = Entry(frame, width=15, font=("cambria 15 "), bg='#A7ECFF', border=0, fg="red")
        rmbn.place(x=310, y=390)

        global pb
        pb = PhotoImage(file="pinfo.png")
        Label(frame, image=pb, bg="#A7ECFF").place(x=750, y=80)

        conn =sqlite3.connect("admin.db")
        cursor=conn.cursor()
        cursor.execute("select Last_Name from students where First_Name=? ",(stname.capitalize(),))
        ln.insert(0,cursor.fetchone())

        cursor.execute("select First_Name from students where First_Name=? ", (stname.capitalize(),))
        fn.insert(0, cursor.fetchone())

        cursor.execute("select Father_Name from students where First_Name=? ", (stname.capitalize(),))
        ftn.insert(0, cursor.fetchone())

        cursor.execute("select Mother_Name from students where First_Name=? ", (stname.capitalize(),))
        mn.insert(0, cursor.fetchone())

        cursor.execute("select DOB from students where First_Name=? ", (stname.capitalize(),))
        dob.insert(0, cursor.fetchone())

        cursor.execute("select Address from students where First_Name=? ", (stname.capitalize(),))
        addrs.insert(0, cursor.fetchone())

        cursor.execute("select Mobile_No from students where First_Name=? ", (stname.capitalize(),))
        mbn.insert(0, cursor.fetchone())

        cursor.execute("select Collage from students where First_Name=? ", (stname.capitalize(),))
        clg.insert(0, cursor.fetchone()[0])

        cursor.execute("select Room_No from students where First_Name=? ", (stname.capitalize(),))
        rmbn.insert(0, cursor.fetchone())

        cursor.execute("select Gender from students where First_Name=? ", (stname.capitalize(),))
        gender.insert(0, cursor.fetchone())

        conn.close()






    def show_notice():
        can = Frame(base, bg='#A7ECFF', height=475, width=1300)
        can.place(x=125, y=310)
        Label(can, text="NOTICE", font=("cambria 25 bold"), bg="#A7ECFF").place(x=550, y=50)
        global noticebg
        noticebg = PhotoImage(file="impnotice.png")
        Label(can, image=noticebg, bg="#A7ECFF").place(x=80, y=100)

        conn =sqlite3.connect("admin.db")
        cursor=conn.cursor()
        cursor.execute("SELECT notice FROM noticeboard WHERE date='{}'".format(datetime.now().date()))
        notice=cursor.fetchall()

        y=150
        for i in notice:
            Label(can, text=i[0], font=("cambria 25 bold"),fg="red", bg="#A7ECFF").place(x=450, y=y)
            y=y+60
        conn.close()


    def send_feedback():
        can = Frame(base, bg='#A7ECFF', height=475, width=1300)
        can.place(x=125, y=310)
        Label(can, text="Suggestions / Feedback", font=("cambria 25 bold"), bg="#A7ECFF").place(x=470, y=50)
        feedback_entry = Entry(can, width=20, font=("cambria 20 bold"))
        feedback_entry.place(x=500, y=200)

        def add_feedback():
            conn = sqlite3.connect("admin.db")
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                              suggestions TEXT , date TEXT)''')
            conn.commit()
            feedback = feedback_entry.get()
            cursor.execute("INSERT INTO feedback (suggestions,date) VALUES ( ?, ?)", (feedback, datetime.now().date()))
            messagebox.showinfo("success", "Suggestion / Feedback sent Succesfully")
            conn.commit()
            conn.close()

        Submit_btn = Button(can, text="Submit", command=add_feedback, font=("cambria 15 bold"), bg="yellow", fg="black",width=10, border=10)
        Submit_btn.place(x=600, y=300)



    Button(can, text="PERSONAL INFO",command=pdetails, font=("cambria 15 bold"), bg="gold", width=12, border=5).place(x=100, y=20)
    Button(can, text="NOTICE BOARD",command=show_notice, font=("cambria 15 bold"), bg="gold", width=12, border=5).place(x=400, y=20)
    Button(can, text="RULES",command=show_rules, font=("cambria 15 bold"), bg="gold", width=12, border=5).place(x=700, y=20)
    Button(can, text="FEEDBACK",command=send_feedback, font=("cambria 15 bold"), bg="gold", width=12, border=5).place(x=1000, y=20)
    Button(can, text="EXIT",command=quit, font=("cambria 15 bold"), bg="gold", width=12, border=5).place(x=1300, y=20)



def afteradmin_login():

    frame = Frame(base, bg='lime', height=70, width=1550)
    frame.place(x=1, y=130)
    Frame(frame,width=4,height=80,bg="black").place(x=150,y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=400, y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=650, y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=900, y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=1100, y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=1390, y=0)
    Frame(frame, width=1550, height=4, bg="black").place(x=0, y=66)
    Frame(frame, width=1550, height=4, bg="black").place(x=0, y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=0, y=0)
    Frame(frame, width=4, height=80, bg="black").place(x=1530, y=0)


    def home():
        can = Frame(base, bg='Turquoise', height=675, width=1540)
        can.place(x=0, y=200)
        global bg
        bg = PhotoImage(file="admin_logobig.png")
        Label(can, image=bg, bg="Turquoise").place(x=10, y=60)
        Label(can, text="Welcome.....", font=("algerian 50 "), bg="Turquoise", fg="black").place(x=420, y=350)
        Label(can, text="Room Details :", font=("cambria 18 bold "), bg="Turquoise", fg="red").place(x=850, y=100)
        conn = sqlite3.connect("admin.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rooms")
        rows = cursor.fetchall()
        tree = ttk.Treeview(can, height=15)
        tree.place(x=850, y=150)
        tree['show'] = 'headings'
        tree['columns'] = ('Room_No', 'Gender', 'Total_Beds', 'Allocated_Beds')

        for column in tree['columns']:
            tree.heading(column, text=column)

        tree.column("Room_No", width=90)
        tree.column("Gender", width=120)
        tree.column("Total_Beds", width=140)
        tree.column("Allocated_Beds", width=140)

        for row in rows:
            tree.insert('', 'end', values=row)
        conn.close()
        Frame(can, height=325, width=1, bg="black").place(x=930, y=152)
        Frame(can, height=325, width=1, bg="black").place(x=1060, y=152)
        Frame(can, height=325, width=1, bg="black").place(x=1200, y=152)
        Frame(can, height=1, width=490, bg="black").place(x=850, y=172)

    home()


    def add_stud():
        frame = Frame(base, bg='Turquoise', height=675, width=1540)
        frame.place(x=0, y=200)
        global bg1
        bg1 = PhotoImage(file="register.png")
        Label(frame, image=bg1, bg="Turquoise").place(x=700, y=80)
        Label(frame, text="First Name", font=("cambria 15 bold"), bg='Turquoise', fg="black").place(x=100, y=50)
        fn = Entry(frame, width=15, font=("cambria 15"))
        fn.place(x=100, y=80)
        fn.focus()
        Label(frame, text="Last Name", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=310, y=50)
        ln = Entry(frame, width=15, font=("cambria 15"))
        ln.place(x=310, y=80)
        Label(frame, text="Father Name", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=100,y=120)
        ftn = Entry(frame, width=15, font=("cambria 15"))
        ftn.place(x=100, y=150)
        Label(frame, text="Mother Name", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=310,y=120)
        mn = Entry(frame, width=15, font=("cambria 15"))
        mn.place(x=310, y=150)
        Label(frame, text="DOB", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=100, y=200)
        dob = Entry(frame, width=15, font=("cambria 15 bold"))
        dob.place(x=100, y=230)
        Label(frame, text="Collage Name", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=310, y=200)
        clg = Entry(frame, width=15, font=("cambria 15 bold"))
        clg.place(x=310, y=230)
        Label(frame, text="Mobile Number", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=100, y=280)
        mbn = Entry(frame, width=15, font=("cambria 15 bold"))
        mbn.place(x=100, y=310)
        Label(frame, text="Address", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=310, y=280)
        addrs = Entry(frame, width=15, font=("cambria 15 bold"))
        addrs.place(x=310, y=310)
        Label(frame, text="Gender", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=100, y=350)
        gender = ttk.Combobox(frame, values=["MALE", "FEMALE"], width=10, font=("cambria", 16, 'bold'))
        gender.place(x=100, y=380)

        Label(frame, text="Room No", font=("cambria 15 bold"), bg="Turquoise", fg="black").place(x=310, y=350)



        def show_rooms():
            conn = sqlite3.connect("admin.db")
            cursor = conn.cursor()

            cursor.execute("SELECT Room_No FROM rooms WHERE Gender=? AND Allocated_Beds < 4",(gender.get(),))
            data = cursor.fetchall()
            val=[]
            for i in data:
                val.append(i[0])
            global room
            room = ttk.Combobox(frame, values=val, width=10, font=("cambria", 16, 'bold'))
            room.place(x=310, y=380)

            conn.close()

        Button(frame, text="Fetch rooms", command=show_rooms, font=("cambria 14 bold"), bg="red", fg="black", border=10,width=10).place(x=350, y=450)


        def add_std():
            conn = sqlite3.connect("admin.db")
            cursor=conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                                          Last_Name TEXT , First_Name TEXT,Father_Name TEXT,
                                          Mother_Name TEXT,Gender TEXT,DOB TEXT,Address TEXT,Mobile_No TEXT,
                                          Collage TEXT,Room_No TEXT)''')
            conn.commit()

            cursor.execute("INSERT INTO students (Last_Name ,First_Name,Father_Name,Mother_Name,Gender,DOB,Address,Mobile_No,Collage ,Room_No ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (ln.get(),fn.get(),ftn.get(),mn.get(),gender.get(),dob.get(),addrs.get(),mbn.get(),clg.get(),room.get()))
            conn.commit()

            cursor.execute("SELECT Allocated_Beds FROM rooms WHERE Room_No='{}'".format(room.get()))
            z=cursor.fetchone()
            print(z)
            x=z[0]+1
            cursor.execute("UPDATE rooms SET Allocated_Beds=? WHERE Room_No=?",(x,room.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","STUDENT ADDED")

        Button(frame, text="SUBMIT",command=add_std, font=("cambria 14 bold"), bg="yellow", fg="black", border=10, width=10).place(
            x=150, y=450)


    def add_room():

        frame = Frame(base, bg='Turquoise', height=675, width=1530)
        frame.place(x=0, y=200)
        Label(frame, text="Add New Room", font=("cambria 30 bold"), fg="black",bg="Turquoise").place(x=590, y=50)
        Label(frame, text=" Room No.", font=("cambria 20 bold"), bg="Turquoise", fg="black").place(x=430, y=150)
        rm_no = Entry(frame, width=20, font=("cambria 15 bold"))
        rm_no.place(x=650, y=150)
        Label(frame, text=" Total Beds", font=("cambria 20 bold"), bg="Turquoise", fg="black").place(x=430, y=200)
        t_beds = Entry(frame, width=20, font=("cambria 15 bold"))
        t_beds.place(x=650, y=200)
        Label(frame,text="Gender", font=("cambria 20 bold"), bg="Turquoise", fg="black").place(x=432,y=250)
        gender = ttk.Combobox(frame, values=["MALE", "FEMALE"], width=10,font=("cambria", 16, 'bold'))
        gender.place(x=650, y=252)



        def add_newroom():

            conn = sqlite3.connect("admin.db")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (
                                                  Room_No TEXT , Gender TEXT,Total_Beds INTEGER,Allocated_Beds INTEGER)''')
            conn.commit()
            gen = gender.get()
            cursor.execute("INSERT INTO rooms (Room_No,Gender,Total_Beds,Allocated_Beds) VALUES ( ?, ?, ?, ?)",
                           (rm_no.get(), gender.get(),t_beds.get(),0))
            messagebox.showinfo("success", "Room added")
            conn.commit()
            conn.close()


        ad_rm_btn = Button(frame, text="Add Room",command=add_newroom, font=("cambria 17 bold"), bg="yellow", fg="black",border=10)
        ad_rm_btn.place(x=650, y=340)

    def visitor():
        frame = Frame(base, bg='turquoise', height=675, width=1540)
        frame.place(x=0, y=200)
        global bg
        bg = PhotoImage(file="visitor.png")
        Label(frame, image=bg, bg="turquoise").place(x=900, y=80)
        Label(frame, text="****** Visitor's Information ******", bg="turquoise", font=("cambria 23 bold"),fg="black").place(x=550, y=10)
        Label(frame, text="Visitor Name:", font=("cambria 20 bold"), bg="turquoise", fg="black").place(x=50, y=100)
        vname = Entry(frame, width=20, font=("cambria 20 bold"))
        vname.place(x=230, y=100)
        Label(frame, text="Contact:", font=("cambria 20 bold"), bg="turquoise", fg="black").place(x=115, y=200)
        vcontact = Entry(frame, width=20, font=("cambria 20 bold"))
        vcontact.place(x=230, y=200)
        Label(frame, text="Reason:", font=("cambria 20 bold"), bg="turquoise", fg="black").place(x=120, y=300)
        vreason = Entry(frame, width=20, font=("cambria 20 bold"))
        vreason.place(x=230, y=300)
        st_name = Label(frame, text="Student Name:", font=("cambria 20 bold"), bg="turquoise", fg="black").place(x=40, y=400)
        st_name = Entry(frame, width=20, font=("cambria 20 bold"))
        st_name.place(x=230, y=400)


        def add_visitor():

            conn = sqlite3.connect("admin.db")
            cursor = conn.cursor()
            cursor.execute('''
                      CREATE TABLE IF NOT EXISTS visitors (
                      Name TEXT ,
                      Contact TEXT,Reason TEXT ,Student_Name,Date TEXT)''')
            conn.commit()
            cursor.execute("INSERT INTO visitors (Name,Contact,Reason,Student_Name,Date) VALUES ( ?, ?, ?, ?, ?)", (vname.get(),vcontact.get(),vreason.get(),st_name.get(), datetime.now().strftime("%d%m%y %H:%M:%S")))
            messagebox.showinfo("Success","visitor info added")
            conn.commit()
            conn.close()


        Submit_btn = Button(frame, text="Submit",command=add_visitor, font=("cambria 20 bold"), bg="yellow", fg="black", width=8, border=8)
        Submit_btn.place(x=600, y=368)


    def view_info():
            frame1 = Frame(base, bg='Turquoise', height=675, width=1530)
            frame1.place(x=0, y=200)

            def view_feedback():
                frame3 = Frame(frame1, bg='turquoise', height=425, width=1340)
                frame3.place(x=10, y=110)
                frame = Frame(frame1, bg='Turquoise', height=345, width=780)
                frame.place(x=20, y=110)
                Frame(frame, bg='red', height=345, width=5).place(x=0,y=0)
                Frame(frame, bg='red', height=345, width=5).place(x=775, y=0)
                Frame(frame, bg='red', height=5, width=780).place(x=0, y=0)
                Frame(frame, bg='red', height=5, width=780).place(x=0, y=340)

                conn = sqlite3.connect("admin.db")
                cursor=conn.cursor()
                cursor.execute("SELECT suggestions FROM feedback WHERE date='{}'".format(datetime.now().date()))
                feedback=cursor.fetchall()
                conn.close()
                y=50
                for i in range(len(feedback)):
                    Label(frame, text=feedback[i][0], font=("cambria 20 bold"), bg="Turquoise", fg="black").place(x=200, y=y)
                    y+=50
            Submit_btn = Button(frame1, text="view_feedback", command=view_feedback, font=("cambria 15 bold"), bg="yellow",fg="black", width=13, border=10)
            Submit_btn.place(x=50, y=20)



            def view_stud_info():

                frame3 = Frame(frame1, bg='red', height=423, width=1330)
                frame3.place(x=10, y=110)
                conn = sqlite3.connect("admin.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students")
                rows = cursor.fetchall()

                tree = ttk.Treeview(frame3, height=19)
                tree.place(x=10, y=10)
                tree['show'] = 'headings'
                tree['columns'] = ('Sr_No', 'Last_Name', 'First_Name', 'Father_Name', 'Mother_Name', 'Gender','DOB','Address','Mobile_No','Collage','Room_No')
                s = ttk.Style()
                s.configure(".", font=("Cambria 12 "))
                s.configure("Treeview.Heading", font=("cambria 13 bold"))

                for column in tree['columns']:
                    tree.heading(column, text=column)

                tree.column("Sr_No", width=85)
                tree.column("Last_Name", width=130)
                tree.column("First_Name", width=130)
                tree.column("Father_Name", width=130)
                tree.column("Mother_Name", width=120)
                tree.column("Gender", width=100)
                tree.column("DOB", width=120)
                tree.column("Address", width=150)
                tree.column("Mobile_No", width=110)
                tree.column("Collage", width=140)
                tree.column("Room_No", width=95)

                c = 1
                for row in rows:
                    row = (c,) + (row)
                    c = c + 1
                    tree.insert('', 'end', values=row)
                conn.close()
                Frame(frame3,height=405,width=1,bg="black").place(x=90,y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=220, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=350, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=480, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=605, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=700, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=820, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=960, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=1080, y=10)
                Frame(frame3, height=405, width=1, bg="black").place(x=1220, y=10)
                Frame(frame3, height=1, width=1310, bg="black").place(x=10, y=35)


















            Submit_btn = Button(frame1, text="view student info", command=view_stud_info, font=("cambria 15 bold"),bg="yellow", fg="black", width=13, border=10)
            Submit_btn.place(x=450, y=20)


            def view_visitor():

                frame3 = Frame(frame1, bg='turquoise', height=425, width=1345)
                frame3.place(x=10, y=110)
                frame = Frame(frame1, bg='red', height=345, width=810)
                frame.place(x=20, y=110)
                conn = sqlite3.connect("admin.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM visitors")
                rows = cursor.fetchall()

                tree = ttk.Treeview(frame1, height=15)
                tree.place(x=30, y=120)
                tree['show'] = 'headings'
                tree['columns'] = ('Sr_No','Visitor_Name','Contact','Reason','Student_Name','Date & Time')
                s=ttk.Style()
                s.configure(".", font=("Cambria 12 "))
                s.configure("Treeview.Heading", font=("cambria 13 bold"))

                for column in tree['columns']:
                    tree.heading(column, text=column)

                tree.column("Sr_No", width=90)
                tree.column("Visitor_Name", width=120)
                tree.column("Contact", width=140)
                tree.column("Reason", width=140)
                tree.column("Student_Name", width=140)
                tree.column("Date & Time", width=155)

                c = 1
                for row in rows:
                    row = (c,) + (row)
                    c = c + 1
                    tree.insert('', 'end', values=row)
                conn.close()
                Frame(frame1, height=325, width=1, bg="black").place(x=120, y=120)
                Frame(frame1, height=325, width=1, bg="black").place(x=240, y=120)
                Frame(frame1, height=325, width=1, bg="black").place(x=380, y=120)
                Frame(frame1, height=325, width=1, bg="black").place(x=520, y=120)
                Frame(frame1, height=325, width=1, bg="black").place(x=660, y=120)
                Frame(frame1, height=1, width=780, bg="black").place(x=30, y=145)


            Submit_btn = Button(frame1, text="visitors info", command=view_visitor, font=("cambria 15 bold"),bg="yellow", fg="black", width=12, border=10)
            Submit_btn.place(x=250, y=20)




    def add_notice():
        frame = Frame(base, bg='Turquoise', height=675, width=1530)
        frame.place(x=0, y=200)
        Label(frame, text="Enter Notice:", font=("cambria 20 bold"), bg="Turquoise", fg="black").place(x=550, y=150)
        notice_entry = Entry(frame, width=20, font=("cambria 20 bold"))
        notice_entry.place(x=550, y=200)

        def add_notice():
            conn = sqlite3.connect("admin.db")
            cursor = conn.cursor()

            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS noticeboard (
                            notice TEXT , date TEXT)''')
            conn.commit()
            notice = notice_entry.get()
            cursor.execute("INSERT INTO noticeboard (notice,date) VALUES ( ?, ?)", (notice,datetime.now().date()))
            messagebox.showinfo("success", "Notice Added Succesfully")
            conn.commit()
            conn.close()

        Submit_btn = Button(frame, text="Submit",command=add_notice, font=("cambria 15 bold"), bg="yellow", fg="black", width=10, border=10)
        Submit_btn.place(x=650, y=300)

    home = Button(frame, text="Home", font=("cambria 17 bold"), bg="lime", command=home, width=9, border=0)
    home.place(x=10, y=10)
    add_std_btn = Button(frame, text="Add Student", font=("cambria 17 bold"), bg="lime", command=add_stud,width=13,border=0)
    add_std_btn.place(x=450, y=10)
    add_new_room = Button(frame, text="Add New Room", font=("cambria 17 bold"), bg="lime", command=add_room,width=13,border=0)
    add_new_room.place(x=185, y=10)
    in_ot_time = Button(frame, text="Add Notice",command=add_notice, font=("cambria 17 bold"), bg="lime",width=13,border=0)
    in_ot_time.place(x=670, y=10)
    visitor = Button(frame, text="Visitor",command=visitor, font=("cambria 17 bold"), bg="lime",width=10,border=0)
    visitor.place(x=950, y=10)
    view_info = Button(frame, text="View Information", font=("cambria 17 bold"), bg="lime", command=view_info,width=15,border=0)
    view_info.place(x=1150, y=10)
    exit = Button(frame, text="Exit", font=("cambria 17 bold"), bg="lime",command=quit,width=9,border=0)
    exit.place(x=1400, y=10)



start()
base.mainloop()