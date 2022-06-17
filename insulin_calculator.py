from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')


def button_clicked():
    scale = float(ratio_entry.get())
    food = float(meal_entry.get())
    units = food / scale
    if int(blood_sugar_entry.get()) < 70:
        take_less_carbs = float(meal_entry.get())
        units_of_insulin = take_less_carbs / scale - 35
        total_units_label.config(text=f"Please take {units_of_insulin} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 200) and (int(blood_sugar_entry.get()) < 225):
        total_units = units + 1
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 225) and (int(blood_sugar_entry.get()) < 250):
        total_units = units + 2
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 250) and (int(blood_sugar_entry.get()) < 275):
        total_units = units + 3
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 275) and (int(blood_sugar_entry.get()) < 300):
        total_units = units + 4
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 300) and (int(blood_sugar_entry.get()) < 325):
        total_units = units + 5
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 325) and (int(blood_sugar_entry.get()) < 350):
        total_units = units + 6
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 350) and (int(blood_sugar_entry.get()) < 375):
        total_units = units + 7
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 375) and (int(blood_sugar_entry.get()) < 400):
        total_units = units + 8
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 400) and (int(blood_sugar_entry.get()) < 425):
        total_units = units + 9
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 425) and (int(blood_sugar_entry.get()) < 450):
        total_units = units + 10
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 450) and (int(blood_sugar_entry.get()) < 475):
        total_units = units + 11
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 475) and (int(blood_sugar_entry.get()) < 500):
        total_units = units + 12
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 500) and (int(blood_sugar_entry.get()) < 525):
        total_units = units + 13
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 525) and (int(blood_sugar_entry.get()) < 550):
        total_units = units + 14
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 550) and (int(blood_sugar_entry.get()) < 575):
        total_units = units + 15
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif (int(blood_sugar_entry.get()) >= 575) and (int(blood_sugar_entry.get()) < 600):
        total_units = units + 16
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    elif int(blood_sugar_entry.get()) >= 600:
        total_units = units + 17
        total_units_label.config(text=f"Please take {total_units} units. Have a great day!")
    else:
        total_units_label.config(text=f"Please take {units}. Have a great day!")


def populate_list():
    insulin_calculator_list.delete(0, END)
    for row in db.fetch():
        insulin_calculator_list.insert(END, row)


def add_item():
    if ratio_text.get() == '' or meal_text.get() == '' or date_text.get() == '' or blood_sugar_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(ratio_text.get(), meal_text.get(), date_text.get(), blood_sugar_text.get())
    insulin_calculator_list.delete(0, END)
    insulin_calculator_list.insert(END, (ratio_text.get(), meal_text.get(), date_text.get(), blood_sugar_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = insulin_calculator_list.curselection()[0]
        selected_item = insulin_calculator_list.get(index)

        ratio_entry.delete(0, END)
        ratio_entry.insert(END, selected_item[1])
        meal_entry.delete(0, END)
        meal_entry.insert(END, selected_item[2])
        date_entry.delete(0, END)
        date_entry.insert(END, selected_item[3])
        blood_sugar_entry.delete(0, END)
        blood_sugar_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], ratio_text.get(), meal_text.get(), date_text.get(), blood_sugar_text.get())
    populate_list()


def clear_text():
    ratio_entry.delete(0, END)
    meal_entry.delete(0, END)
    date_entry.delete(0, END)
    blood_sugar_entry.delete(0, END)


# Create window object
app = Tk()

# Daily spending list: Place of Purchase
ratio_text = StringVar()
ratio_label = Label(app, text="Enter carb/ units of Insulin Ratio:", font=("bold", 10), pady=20)
ratio_label.grid(row=0, column=0, sticky=W)
ratio_entry = Entry(app, textvariable=ratio_text)
ratio_entry.grid(row=0, column=1)

# Daily spending list: Amount of Purchase
meal_text = StringVar()
meal_label = Label(app, text="Total Carbs of meal/snack:", font=("bold", 10))
meal_label.grid(row=0, column=2, sticky=W)
meal_entry = Entry(app, textvariable=meal_text)
meal_entry.grid(row=0, column=3)

# Daily spending list: Time/Date
date_text = StringVar()
date_label = Label(app, text="Time/Date:", font=("bold", 10))
date_label.grid(row=0, column=4, sticky=W)
date_entry = Entry(app, textvariable=date_text)
date_entry.grid(row=0, column=5)

# Daily spending list: Checking account Total
blood_sugar_text = StringVar()
blood_sugar_label = Label(app, text="Enter Glucose level:", font=("bold", 10), pady=20)
blood_sugar_label.grid(row=1, column=0, sticky=W)
blood_sugar_entry = Entry(app, textvariable=blood_sugar_text)
blood_sugar_entry.grid(row=1, column=1)

# Total units of insulin to take
total_units_label = Label(text="Total # of Units", font=("Arial", 12))
total_units_label.config(text="Total # of Units")
total_units_label.grid(row=1, column=3)


# spending list (Listbox)
insulin_calculator_list = Listbox(app, height=30, width=50, border=0)
insulin_calculator_list.grid(row=5, column=0, columnspan=3, rowspan=6, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=3)
# set scroll to listbox
insulin_calculator_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=insulin_calculator_list.yview)
# Bind select
insulin_calculator_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Readings', width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

# Buttons
remove_btn = Button(app, text='Remove Readings', width=14, command=remove_item)
remove_btn.grid(row=3, column=1)

# Buttons
update_btn = Button(app, text='Update Readings', width=14, command=update_item)
update_btn.grid(row=3, column=2)

# Buttons
clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=3, column=3)

# Calculate button
calculate_btn = Button(app, text='Calculate', width=12, command=button_clicked)
calculate_btn.grid(row=3, column=5)

app.title("Diabetes Tracker")
app.geometry('1000x800')

# Populate data
populate_list()


# Start program
app.mainloop()
