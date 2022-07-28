import json
from tkinter import *
from difflib import get_close_matches
window=Tk()
data = json.load(open("data.json"))

# def translate(w):
#     w = w.lower()
#     if w in data:
#         return data[w]
#     elif len(get_close_matches(w, data.keys())) > 0:
#         yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
#         if yn == "Y":
#             return data[get_close_matches(w, data.keys())[0]]
#         elif yn == "N":
#             return "The word doesn't exist. Please double check it."
#         else:
#             return "We didn't understand your entry."
#     else:
#         return "The word doesn't exist. Please double check it."

def insert():
    flag=1
    try: 
        flag=0
        l1.delete('0',END)
        l1.insert(END,(data[title1.get()]))
    except:
        flag=0
        l1.delete('0',END)
        l1.insert(END,title2)
        try:
            l1.insert(END,get_close_matches(title1.get(),data.keys())[0])
            l1.insert(END,(data[get_close_matches(title1.get(), data.keys())[0]]))    
        except:
            l1.insert(END,title3)      
    if flag==1:
        l1.insert(END,title3)    
    # Finally:
    #     l1.delete('0',END)
    #     l1.insert(END,title3.get())   
# word = input("Enter word: ")
# output = translate(word)
# if type(output) == list:
#     for item in output:
#         print(item)
# else:
#     print(output)
L1= Label(window, text='Word')
L1.grid(row=0,column=0)
title1=StringVar()
# title2=StringVar()
title2="Closest Match: "
# title3=StringVar()
title3="NOT FOUND"
e1=Entry(window,textvariable=title1)
e1.grid(row=2,column=0)
b1=Button(window,text='translate',command=insert)
b1.grid(row=3,column=0)
l1 = Listbox(window,height=7,width=35)
l1.grid(row=4,column=0,rowspan=7)
window.mainloop()