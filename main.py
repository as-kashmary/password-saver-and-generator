from tkinter import *
from tkinter import messagebox
import pass_gen
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
k=pass_gen.pass_ge1n();
def show():
    password_entry.insert(0,k)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web=website_entry.get();
    pas=password_entry.get();
    mail=email_entry.get();
    if len(pas)==0 or len(web)==0 or len(mail)==0 :
        messagebox.showinfo(message="Please enter valid info")
    else:
        is_ok =messagebox.askokcancel(message=f"Website:{web}\n Password:{pas}\n Email/Username:{mail}\n Is it ok to save?")
        if is_ok:
            with open("data.txt" ,"a") as file:
                file.write(f"{web} | {mail} |{pas}\n");
                website_entry.delete(0,END);
                password_entry.delete(0,END);
                email_entry.delete(0,END);


# ---------------------------- UI SETUP ------------------------------- #
window=Tk();
window.title("My password manager")
window.config(padx=20,pady=20)
pic=PhotoImage(file="logo.png")
canvas=Canvas(height=200,width=200)

canvas.create_image(100,100,image=pic)
canvas.grid(row=0,column=1)



website=Label(text="Website :")
website.grid(row=1,column=0)
email=Label(text="Email/Username :")
email.grid(row=2,column=0)
password=Label(text="Password :")
password.grid(row=3,column=0)

website_entry=Entry(width=60)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry=Entry(width=60)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry=Entry(width=50)
password_entry.grid(row=3,column=1)

gen=Button(text="Generate",command=show)
gen.grid(row=3,column=2)

add=Button(text="Add",width=36,command=save)
add.grid(row=4,column=1,)

window.mainloop()