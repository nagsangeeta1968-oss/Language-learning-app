import tkinter as tk
import pandas as pd

window_main = tk.Tk(className='Languages')
window_main.geometry('400x200')
 
listbox_1 = tk.Listbox(window_main, selectmode=tk.EXTENDED)
df = pd.read_csv("Languages.csv")
l_name = df["Language Name"]
m = 1
for i in l_name :
    listbox_1.insert(m, i)
    m = m + 1
listbox_1.pack()

         
        
def submitFunction():
    selection = listbox_1.curselection()
    t_sel_name = listbox_1.get(selection)
    mtdet = [t_sel_name]
    sub_df = pd.read_csv('selectedlanguage.csv')
    n = len(sub_df[sub_df['Language Name']==t_sel_name])
    if(n == 0) :
        sub_df.loc[len(sub_df)] = mtdet
        sub_df.to_csv('selectedlanguage.csv', index = False)
    else :
        print("The record is already entered")
    
    return

    


 
submit = tk.Button(window_main, text='Submit', command=submitFunction)
submit.pack()
window_main.mainloop()
