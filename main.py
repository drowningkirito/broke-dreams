import ttkbootstrap as ttk
import tkinter as tk
import requests as re
import json
import currencyapicom
url = "https://api.currencyapi.com/v3/latest"
headers = {
'apikey': 'YOUR API'
}
        
response=re.get(url,headers=headers)
currency=json.loads(response.text)
currency_name=[]
for i in currency["data"]:
    currency_name.append(i)
class Mycurrency():
    def converting(self):
        client = currencyapicom.Client('Your API')
        c1=c1_menu.get()
        c2=c2_menu.get()
        print(c1,c2)
        result = client.latest(c1,currencies=[c2])
        convertedVal=float(entry1.get())*result["data"][c2]["value"]
        display.config(text=str(convertedVal))
   
    def __init__(self,window):
        self.window=window
        self.window.geometry("600x300+400+200")
        self.window.title("Currency Converter")
        photoimage=tk.PhotoImage(file="pay.png")
        self.window.iconphoto(False,photoimage)
        self.window.columnconfigure((0,1,2),weight=1)
        self.window.rowconfigure((0,1,2,3),weight=1)
        ttk.Label(self.window,text="select currency-1",bootstyle="inverse-primary",font=[("Arial",30)]).grid(row=0,column=0,sticky="s")
        ttk.Label(self.window,text="------>",bootstyle="inverse-dark").grid(row=0,column=1,sticky="s")
        ttk.Label(self.window,text="select currency-2",bootstyle="inverse-primary",font=[("Arial",30)]).grid(row=0,column=2,sticky="s")
        global c1_menu
        c1_menu=ttk.Combobox(self.window,
                          bootstyle="info",
                          state="readonly",
                         values=tuple(currency_name))
        c1_menu.grid(row=1,column=0,sticky="n")
        c1_menu.current(0)
        global c2_menu
        c2_menu=ttk.Combobox(self.window,
                          bootstyle="info",
                          state="readonly",
                         values=tuple(currency_name))
        c2_menu.grid(row=1,column=2,sticky="n")
        c2_menu.current(0)
        global entry1
        entry1 =ttk.Entry(self.window)
        entry1.grid(row=2,column=0,sticky="n")
        global display
        display=ttk.Label(self.window,bootstyle="inverse-dark")
        display.grid(row=2,column=2,sticky="n")
        ttk.Button(self.window,text="Convert",command=self.converting).grid(row=3,column=1)

        self.window.mainloop()
    
if __name__=="__main__":
    win=ttk.Window(themename="morph")
    app=Mycurrency(win)
        
