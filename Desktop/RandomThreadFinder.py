import tkinter as tk


root = tk.Tk()
root.title("Subreddit thread finder")
root.geometry("400x200")

stfchose = tk.StringVar()

def on_submit():
    stf_var = stfchose.get()
    print(stf_var)



label = tk.Label(root, text = "Enter a subreddit's name you would like to find a random thread for.")
label.grid(row=0, column=0)

user_entry = tk.Entry(root,textvariable=stfchose, font=('calibre', 10, 'normal'))
user_entry.grid(row=1,column=0)

confirmbtn=tk.Button(root, text = 'Find', command = on_submit)
confirmbtn.grid(row=2, column=0)
root.mainloop()