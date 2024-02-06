import tkinter as tk
window = tk.Tk()

button = tk.Button(text='...', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
aan = True

def schakelaar():
    global aan

    if aan:
        window.configure(bg='black')
        print('light is off')
        aan = False

    else:
        window.configure(bg='yellow')
        print('light is on')
        aan = True

button.config(text='Switch light on', command=schakelaar)
# schijf hier tussen je code

window.mainloop()