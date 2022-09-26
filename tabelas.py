from tkinter import *
from tkinter import ttk
import json,requests

class Tabela():
    def __init__(self,titulo, coluna1, coluna2, dados, coluna3, coluna4= None):

        self.tabela= Tk()
        self.tabela.title(titulo)
        self.tabela.geometry("700x600")
        self.coluna1= coluna1
        self.coluna2= coluna2
        self.coluna3= coluna3
        self.coluna4= coluna4
        self.dados= dados

        self.add_frame= Frame(self.tabela)
        self.add_frame.pack(pady=1)

        self.arv_scroll = Scrollbar(self.add_frame)
        self.arv_scroll.pack(side=RIGHT, fill=Y)

        self.arvore1= ttk.Treeview(self.add_frame,yscrollcommand=self.arv_scroll.set, selectmode="browse")
        self.arvore1.pack()
        self.arv_scroll.config(command=self.arvore1.yview)

        if self.coluna4 != None:
            self.arvore1["columns"]=(self.coluna1, self.coluna2, self.coluna3, self.coluna4)
        else:
            self.arvore1["columns"]=(self.coluna1, self.coluna2, self.coluna3)

        self.arvore1.column("#0", width= 0, stretch= NO)
        self.arvore1.column(self.coluna1, anchor=W, width= 80)
        self.arvore1.column(self.coluna2, anchor=W, width= 80)
        self.arvore1.column(self.coluna3, anchor=CENTER, width= 400)


        self.arvore1.heading("#0", text="", anchor=W)
        self.arvore1.heading(self.coluna1, text="userId", anchor=W)
        self.arvore1.heading(self.coluna2, text= "id", anchor=W)
        self.arvore1.heading(self.coluna3, text= self.coluna3, anchor=CENTER)
        if self.coluna4 != None:
            self.arvore1.column(self.coluna4, anchor=W, width= 80)
            self.arvore1.heading(self.coluna4, text= self.coluna4, anchor=W)

        self.dec= ttk.Style()

        self.dec.theme_use("clam")

        self.dec.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
    
        self.dec.map('Treeview',background=[('selected', "purple")])

        
        self.add_data()
        self.caixas_for_metodos()
        self.tabela.mainloop()


    def add_data(self):
    
        count=0
        if self.coluna4 != None:
            for item in self.dados:
                self.arvore1.insert(parent="", index= "end", iid= count, text="", values=(str(item["userId"]), str(item["id"]), item[self.coluna3], str(item[self.coluna4])))
                count+=1
            
        else:
            for item in self.dados:
                self.arvore1.insert(parent="", index= "end", iid= count, text="", values=(str(item["userId"]), str(item["id"]), item[self.coluna3]))
                count+=1

    def caixas_for_metodos(self):

        self.arvore1.pack(pady=1)

        self.add_frame2= Frame(self.tabela)
        self.add_frame2.pack(pady=20)

        self.user= Label(self.add_frame2, text="userId")
        self.user.grid(row=0, column=0)
        self.ID= Label(self.add_frame2, text="id")
        self.ID.grid(row=0, column=1)
        self.title= Label(self.add_frame2, text= self.coluna3)
        self.title.grid(row=0, column=2)
        if self.coluna4 != None:
            self.label4= Label(self.add_frame2, text= self.coluna4)
            self.label4.grid(row=0, column=3)
        else:
            pass



        self.user_caixa= Entry(self.add_frame2)
        self.user_caixa.grid(row=1, column=0)

        self.id_caixa= Entry(self.add_frame2)
        self.id_caixa.grid(row=1, column=1)

        self.title_caixa= Entry(self.add_frame2)
        self.title_caixa.grid(row=1, column=2)
        if self.coluna4 != None:
            self.coluna4_caixa= Entry(self.add_frame2)
            self.coluna4_caixa.grid(row=1, column=3)


        self.temp_label= Label(self.tabela, text="")
        self.temp_label.pack(pady=20)
        self.button_frame = LabelFrame(self.tabela, text="Comandos")
        self.button_frame.pack(fill="x", expand="yes", padx=20)
        self.select_record_button = Button(self.button_frame, text="Selecionar item", command= self.select_record)
        self.select_record_button.grid(row=0, column=0, padx=10, pady=10)
        self.search_button= Button(self.button_frame, text="Buscar id", command= self.buscar_data)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)
    
    def buscar_data(self):
        self.procurar= self.id_caixa.get()
        
        for item in self.dados:

            if int(self.procurar) == item["id"]:

                self.user_caixa.delete(0, END)
                self.id_caixa.delete(0, END)
                self.title_caixa.delete(0, END)
                if self.coluna4 != None:
                    self.coluna4_caixa.delete(0, END)
                else:
                    pass
                self.user_caixa.insert(0, item["userId"])
                self.id_caixa.insert(0, item["id"])
                self.title_caixa.insert(0, item[self.coluna3])
                if self.coluna4 != None:
                    self.coluna4_caixa.insert(0, item[self.coluna4])           
                

    def select_record(self):
        self.user_caixa.delete(0, END)
        self.id_caixa.delete(0, END)
        self.title_caixa.delete(0, END)
        if self.coluna4 != None:
            self.coluna4_caixa.delete(0, END)
        else:
            pass
    
    
        selected = self.arvore1.focus()
        values = self.arvore1.item(selected, 'values')
        self.user_caixa.insert(0, values[0])
        self.id_caixa.insert(0, values[1])
        self.title_caixa.insert(0, values[2])
        if self.coluna4 != None:
            self.coluna4_caixa.insert(0, values[3])