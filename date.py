#create class person
#create init method
# 2 attributes
#create an object form class
import datetime
import tkinter as tk




#create frame
window = tk.Tk()

#create frame geometry
window.geometry("400x400")



#set title of Frame
window.title("Age Calculator App")







#adding labels for app
year_label = tk.Label(text="Year")
year_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

day_label = tk.Label(text="Day")
day_label.grid(column=0, row=3)







#adding entry input
year_entry = tk.Entry()
year_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

day_entry = tk.Entry()
day_entry.grid(column=1, row=3)


def calculate_age():
	print(year_entry.get())
	print(month_entry.get())
	print(day_entry.get())
	qazi = Person('Qazi', datetime.date(int(year_entry.get()), int(month_entry.get()),int(day_entry.get())))
	print(qazi.age())
	text_answer = tk.Text(master=window, height=10, width=30)
	text_answer.grid(column=1, row=5)

	#answer_text = "{name} is {age} years old.".format(name=qazi.name, age=qazi.age())  
	#used if you have many repeated {name} and want to keep input paramters low

	answer_text = "{} is {} years old".format(qazi.name, qazi.age())

	text_answer.insert(tk.END, answer_text)

#adding button for event handler
calculate_button = tk.Button(text="Calculate Age", command=calculate_age)
calculate_button.grid(column=1, row=4)






class Person():

	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year
		return age









new = Person("Jesse", datetime.date(1977,9,2))

print(new.name)
print(new.birthdate)
print(new.age())


window.mainloop()