import tkinter as tk
import EventManager
from threading import Thread
from tkinter.filedialog import askopenfilename
import file_save_test as file_test

def popup(msg, geometry):
    popup = tk.Tk()
    popup.geometry(geometry)

    popup.title('!')
    label = tk.Label(popup, text=msg, font=('default', 15))
    label.pack(side='top')
    popup.mainloop()

files = [('Text Document', '*txt')]

window = tk.Tk()
window.title('Proxy Scraper')
window.resizable(False, False)
window.geometry('350x450')


geckodriver_path_set_entry = tk.Entry(window, font=('default', 20))
geckodriver_path_set_entry.place(x=30, y=260)
geckodriver_path_set_button = tk.Button(window, text='Set Geckodriver Path', font=('default', 19), command=lambda: geckodriver_path_set_entry.insert('0', askopenfilename()))
geckodriver_path_set_button.place(x=30, y=200)

is_headless = tk.BooleanVar()

headless_option = tk.Checkbutton(window, text='Headless', variable=is_headless, onvalue=True, offvalue=False, font=('default', 15))
headless_option.place(x=30, y=20)

dir_button = tk.Button(window, text='Set Output File Directory', font=('default', 17), command=lambda: dir_path_textbox.insert('0', askopenfilename()))
dir_button.place(x=30, y=60)
dir_path_textbox = tk.Entry(window, font=('default', 20))
dir_path_textbox.place(x=30, y=130)

submit_button = tk.Button(window, text='Get Proxies', font=('default', 30), command=lambda: Thread(target=EventManager.onSubmission, args=(is_headless.get(), dir_path_textbox.get(), popup, geckodriver_path_set_entry.get())).start())
submit_button.place(x=30, y=330)

window.mainloop()