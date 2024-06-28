from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()
root.title("Обработка формы")
root.geometry('600x600')

label = ttk.Label(root, text='Форма регистрации пользователя', font='Arial')
label.grid(row=0, column=0, padx=130, pady=40)

frame_gray = Frame(root, bg='gray', bd=2)
frame_white = Frame(frame_gray, bg="white", bd=10)
frame_gray.grid()
frame_white.grid()

name_label = ttk.Label(frame_white, text="Ваше имя:")
name = ttk.Entry(frame_white, textvariable="", width=45)
name_label.grid(row=1, column=0)
name.grid(row=1, column=1, columnspan=3)

pass_label = ttk.Label(frame_white, text="Пароль:")
pass_ = ttk.Entry(frame_white, textvariable="", width=45, show="*")
pass_label.grid(row=2, column=0)
pass_.grid(row=2, column=1, columnspan=3)

old_label = ttk.Label(frame_white, text="Возраст:")
old = ttk.Entry(frame_white, textvariable="", width=45)
old_label.grid(row=3, column=0)
old.grid(row=3, column=1, columnspan=3)

var_sex = IntVar()
sex_label = ttk.Label(frame_white, text="Пол:")
sex_male = ttk.Radiobutton(frame_white, text="Мужской", variable=var_sex, value=1)
sex_female = ttk.Radiobutton(frame_white, text="Женский", variable=var_sex, value=2)
sex_label.grid(row=4, column=0)
sex_male.grid(row=4, column=1)
sex_female.grid(row=4, column=3)

var_mus = IntVar()
var_vid = IntVar()
var_draw = IntVar()

hob_label = ttk.Label(frame_white, text="Ваши увлечения:")
hob_mus = ttk.Checkbutton(frame_white, text="Музыка", variable=var_mus, onvalue=1, offvalue=0)
hob_vid = ttk.Checkbutton(frame_white, text="Видео", variable=var_vid, onvalue=1, offvalue=0)
hob_draw = ttk.Checkbutton(frame_white, text="Рисование", variable=var_draw, onvalue=1, offvalue=0)

hob_label.grid(row=5, column=0)
hob_mus.grid(row=5, column=1)
hob_vid.grid(row=5, column=2)
hob_draw.grid(row=5, column=3)

country_label = ttk.Label(frame_white, text="Ваша страна:")
country= ('Россия','Беларусь','Казахстан','Украина','Другая страна')
var_country = StringVar()
country_combobox = ttk.Combobox(frame_white, textvariable=var_country, width=42)
country_combobox['values'] = country
country_combobox['state'] = 'readonly'
country_label.grid(row=6, column=0)
country_combobox.grid(row=6, column=1, columnspan=3)

city_label = ttk.Label(frame_white, text="Ваш город:")
city = ('Ростов-на-Дону','Москва','Минск','Киев','Другой город')
var_city = StringVar()
city_combobox = ttk.Combobox(frame_white, textvariable=var_city, width=42)
city_combobox['values'] = city
city_combobox['state'] = 'readonly'
city_label.grid(row=7, column=0)
city_combobox.grid(row=7, column=1, columnspan=3)

# class EntryWithPlaceholder(tkinter.Entry):
#     def __init__(self, master=None, placeholder=None):
#         self.entry_var = tkinter.StringVar()
#         super().__init__(master, textvariable=self.entry_var)
#
#         if placeholder is not None:
#             self.placeholder = placeholder
#             self.placeholder_color = 'grey'
#             self.default_fg_color = self['fg']
#             self.placeholder_on = False
#             self.put_placeholder()
#
#             self.entry_var.trace("w", self.entry_change)
#
#             # При всех перечисленных событиях, если placeholder отображается, ставить курсор на 0 позицию
#             self.bind("<FocusIn>", self.reset_cursor)
#             self.bind("<KeyRelease>", self.reset_cursor)
#             self.bind("<ButtonRelease>", self.reset_cursor)
#
#     def entry_change(self, *args):
#         if not self.get():
#             self.put_placeholder()
#         elif self.placeholder_on:
#             self.remove_placeholder()
#             self.entry_change()  # На случай, если после удаления placeholder остается пустое поле
#
#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color
#         self.icursor(0)
#         self.placeholder_on = True
#
#     def remove_placeholder(self):
#         # Если был вставлен какой-то символ в начало, удаляем не весь текст, а только placeholder:
#         text = self.get()[:-len(self.placeholder)]
#         self.delete('0', 'end')
#         self['fg'] = self.default_fg_color
#         self.insert(0, text)
#         self.placeholder_on = False
#
#     def reset_cursor(self, *args):
#         if self.placeholder_on:
#             self.icursor(0)


about_label = ttk.Label(frame_white, text="Кратко о себе")
about = ttk.Entry(frame_white, textvariable="", width=45)
# about = EntryWithPlaceholder(frame_white, "краткая информация о ваших увлечениях")
about_label.grid(row=8, column=0)
about.grid(row=8, column=1, columnspan=3)

ex_label = ttk.Label(frame_white, text="Решите пример, запишите результат в поле ниже", justify=LEFT)
ex = ttk.Entry(frame_white, textvariable="", width=45)
ex_label.grid(row=9, column=0)
ex.grid(row=10, column=1, columnspan=3)

def clear():
    name.delete(0, END)
    pass_.delete(0, END)
    old.delete(0, END)
    var_sex.set(0)
    var_mus.set(0)
    var_vid.set(0)
    var_draw.set(0)
    var_country.set("")
    var_city.set("")

button_cancel = ttk.Button(frame_white,
                           text="Отменить ввод",
                           command=clear)

def show_message():
    print(name.get(), pass_.get(), old.get(), var_sex.get(), var_mus.get(), var_vid.get(), var_draw.get(), var_country.get(), var_city.get())

button_enter = ttk.Button(frame_white,
                    text="Данные подтверждаю",
                          command=show_message)




button_cancel.grid(row=11, column=1, columnspan=1)
button_enter.grid(row=11, column=2, columnspan=2)

root.mainloop()

# label.place(x=150, y=25)
# frame_gray.place()
# name_label.place(x=110, y=100)
# name.place(x=250, y=100)
# pass_label.place(x=110, y=150)
# pass_.place(x=250, y=150)
# button_cancel.place(x=250, y=450)
# button_enter.place(x=350, y=450)