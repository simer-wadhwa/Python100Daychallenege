from tkinter import *


def button_clicked():
    mile = float(miles.get())
    kilometers = round(mile * 0.621371)
    label4.config(text=kilometers)


window = Tk()
window.title("Miles to km convertor")
#window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Labels
label = Label()
label.config(text="is equal to ")
label.grid(column=1, row=2)

label2 = Label()
label2.config(text="Miles ")
label2.grid(column=3, row=1)

label3 = Label()
label3.config(text="km")
label3.grid(column=3, row=2)

label4 = Label()
label4.config(text="0")
label4.grid(column=2, row=2)

miles = Entry(width=10)
miles.grid(column=2, row=1)
#mile = float(miles.get())
#km = Entry(width=10)
#print(km.get())
#km.grid(column=2, row=2)

# The error you're encountering is likely due to the attempt to read the value of the miles Entry widget (mile = float(miles.get())) immediately after creating it. At that point, the user has not inputted any value into the Entry widget, so miles.get() returns an empty string (""). Attempting to convert an empty string to a float causes a ValueError.

# To fix this issue, you should retrieve the value from the Entry widget within the button_clicked function when the button is pressed. Here's an updated version of your code that addresses this problem:

#Button
button = Button(text="calculate", command=button_clicked)
button.grid(column=2, row=3)



window.mainloop()

