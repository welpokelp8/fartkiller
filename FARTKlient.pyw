import tkinter as tk
import subprocess

def launch_fartkiller():
  subprocess.Popen(['python', 'C:/Users/welpokelp8/Downloads/fartkiller.py'])
def launch_fartroaster():
  subprocess.Popen(['python', 'C:/Users/welpokelp8/Downloads/fartroaster.py'])



root = tk.Tk()
root.title("FARTKlient")

button1 = tk.Button(root, text="Denial Of Service Thread", command=launch_fartkiller)
button2 = tk.Button(root, text="File Overflow Thread", command=launch_fartkiller)
button1.pack()
button2.pack()

root.mainloop()
