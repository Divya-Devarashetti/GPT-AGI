#Importing Libraries
import tkinter as tk
from tkinter import Button, Entry
from tkinter import *
import openai
import os
import subprocess


root = tk.Tk()
root.title("vennichat.ai")
root.geometry("312x260")
root.resizable(False, False)
message = tk.StringVar
#Here frame-sizes, background colour defined
chat_start = Frame(root,bd=1,bg='grey',width=40,height=8)
chat_start.place(x=6,y=6,height=200,width=300)

#Here text-border,background color, sizes
txt=tk.Text(chat_start,bd=1,bg='alice blue',width=30,height=4)
txt.pack(fill='both',expand=True)

#entry-where user will type message.xscrollcommand-it helps to print in chat place
msg= Entry(root,width=30, xscrollcommand=True, textvariable=message)
msg.place(x=6, y=210,height=40,width=230)
msg.focus()

#Bot and user text prints in black colour and bot message also given
txt.config(fg='black')
txt.tag_config('usr',foreground='black')
txt.insert(END," ")

openai.api_key = "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"
chrome_driver = "C:/Users/HP PRO BOOK/Downloads/chromedriver.exe"

#defining function for user's text
def sending_mesz(event=None):
    usr_input = msg.get()
    msg.delete(0, tk.END)
    txt.insert(END, f'you:{usr_input}'+'\n','usr')

    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "system", "content": "I will be giving you a prompt on what is to be performed, Give me selenium python script for it but don't explain how the code works. The code should come as a single output, i.e don't output the code in various parts. Set chromedriver path as '"+chrome_driver+"'. Do not create code that might raise NoSuchElementException.wrap code in a try-except block to catch the NoSuchElementException exception and handle it gracefully, for example, by retrying the operation after waiting for some time or logging the error. Make sure you wait for the js to execute before continuing.Please generate code to locate a button element with the class name '_2KpZ6l _2doB4z' on a webpage using a WebDriver object.Please dont show attribute errors."},
                {"role": "user", "content" : usr_input}]
    )
    output=completion['choices'][0]['message']['content']
    output=output.replace("```python","```")
    output=(output.split("```"))[1].split("```")[0]
    if output.startswith("python"):
        output=output.lstrip("python")
    generated_code=output.replace("driver.quit()","while len(driver.window_handles) > 0: pass\ndriver.quit()")
    with open("MLfile.py", "w") as f:
        f.write(generated_code)
    os.system("python \"MLfile.py\"")

    process = subprocess.Popen(['python', 'MLfile.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, errors = process.communicate()

    if process.returncode != 0:
        print('Execution failed with the following error:', errors.decode('utf-8'))
    else:
        print('Code executed successfully.')

b = Button(root, text="send", bg="brown", activebackground='grey',
              fg="black", font=('Arial'),command=sending_mesz,width=6,height=1) 
b.place(x=230, y=210)


root.mainloop()
