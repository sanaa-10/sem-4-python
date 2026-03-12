import tkinter as tk

def submit_form():
    name = name_var.get()
    age = age_var.get()
    dob = dob_var.get()
    gender = gender_var.get()
    qualification = qualification_var.get()
    address = address_text.get("1.0", tk.END).strip()
    phone = phone_var.get()

    if name == "" or age == "" or dob == "" or gender == "" or qualification == "" or address == "" or phone == "":
        status_label.config(text="Error: All fields are required!", fg="red")
    else:
        info = (
            f"Registered Student:\n"
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"DOB: {dob}\n"
            f"Gender: {gender}\n"
            f"Qualification: {qualification}\n"
            f"Address: {address}\n"
            f"Phone: {phone}"
        )
        status_label.config(text=info, fg="green")

        # Clear input fields
        name_var.set("")
        age_var.set("")
        dob_var.set("")
        gender_var.set("")
        qualification_var.set("")
        address_text.delete("1.0", tk.END)
        phone_var.set("")

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x650")

name_var = tk.StringVar()
age_var = tk.StringVar()
dob_var = tk.StringVar()
gender_var = tk.StringVar()
qualification_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(root, text="Student Registration Form", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var, width=40).pack()

tk.Label(root, text="Age").pack()
tk.Entry(root, textvariable=age_var, width=40).pack()

tk.Label(root, text="Date of Birth (DD-MM-YYYY)").pack()
tk.Entry(root, textvariable=dob_var, width=40).pack()

tk.Label(root, text="Gender").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

tk.Label(root, text="Qualification").pack()
tk.Entry(root, textvariable=qualification_var, width=40).pack()

tk.Label(root, text="Address").pack()
address_text = tk.Text(root, height=4, width=30)
address_text.pack()

tk.Label(root, text="Phone Number").pack()
tk.Entry(root, textvariable=phone_var, width=40).pack()

tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white", width=20).pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
status_label.pack(pady=10)

root.mainloop()