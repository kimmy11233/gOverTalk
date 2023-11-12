from keyboardListener import trigger_passive_listen
import psutil

import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


        self.winfo_toplevel().title("G Over Talk")

if __name__ == '__main__':
    processes = psutil.process_iter()
    root = tk.Tk()
    root.geometry("400x100") 
    Example(root).pack(fill="both", expand=True)

    
    p_names = []
    for p in processes:
        p_names.append(p.name())
    if 'ConanSandbox.exe' in p_names:
        trigger_passive_listen()
        root.mainloop()
    else:
        print('Conan not detected!')
    
    

    

    



