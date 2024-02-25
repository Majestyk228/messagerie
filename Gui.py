from tkinter import *
from PIL import Image, ImageTk
import threading

import socket
import signal #identifie les signaux pour kill le programme
import sys #utilisé pour sortir du programme
import time
import threading
from ClientThread import ClientListener

class Gui:
        
    def __init__(self,list_targets):
        self.root = Tk()
        self.root.geometry("700x500")
        self.root.title("Trojanworld")
        self.root.resizable(False, False)
        self.message=""
        self.index=0
        
        # Frame pour le titre et le logo
        self.frame = Frame(self.root, bg=self._from_rgb((255,198,37)))
        self.frame.pack(side="top")
        
        # Liste des cibles
        self.list_targets = list_targets
        
        # Logo de l'application
        image = Image.open("C:/Users/Titan/Desktop/TKinter_Project/trojanworld_logo_clean.png")
        image = image.resize((32, 36), Image.NEAREST)
        self.photo = ImageTk.PhotoImage(image)
        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.grid(row=0, column=0, sticky="w")
        
        # Titre
        self.lb_title = Label(self.frame, text="Trojanworld", bg=self._from_rgb((255,198,37)), width="700", height="1", font=("Roboto",20,"bold"), anchor="w", justify="left")
        self.lb_title.grid(row=0, column=1, sticky="w")
        
        # Liste des cibles
        self.listbox = Listbox(self.root)
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=LEFT, fill=BOTH)
        
        for target in self.list_targets:
            self.listbox.insert(END, target[0])
        
        self.listbox.configure(yscrollcommand=self.scrollbar.set, background=self._from_rgb((229,229,229)), foreground="black", font=('Roboto',16), width=15)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        
        # Champ de texte pour la commande
        self.cmd_entry = Text(self.root, width=50, height=5, fg=self._from_rgb((255,255,255)), bg=self._from_rgb((0,0,0)))
        self.cmd_entry.place(x=215, y=400)
        
        # Champ de texte pour le retour de commande
        self.cmd_return = Text(self.root, width=58, height=21, fg=self._from_rgb((0,0,0)), bg=self._from_rgb((255,255,255)))
        self.cmd_return.place(x=215, y=53)
        
        # Bouton "Send"
        self.bt_send = Button(self.root, text="Send", width=5, bg=self._from_rgb((255,198,37)), fg="black", font=("Roboto",11,"bold"), command=self.sendCommand)
        self.bt_send.place(x=628, y=400)
        
        # Bouton "Cancel"
        self.bt_cancel = Button(self.root, text="Cancel", width=5, bg=self._from_rgb((255,255,255)), fg="black", font=("Roboto",11,"bold"), command=self.cancel)
        self.bt_cancel.place(x=628, y=450)
        
        self.root.mainloop()
    
    def _from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code"""
        return "#%02x%02x%02x" % rgb

    def printt(self):
        print("Command sent.")

    def cancel(self):
        print("Text erased.")
    
    def on_select(self, event):
        index = self.listbox.curselection()
        if index:
            selected_text = self.listbox.get(index)
            self.process_selected_text(selected_text)
            print("Index: ", index[0])
            self.index = index[0]

    def process_selected_text(self, text):
        print("Texte sélectionné à traiter:", text)
        
    def setTargetList(targets):
        self.list_targets=targets
        self.listbox.delete(0, END)
        # Insérer les nouveaux éléments de list_targets dans la Listbox
        for target in targets:
            self.listbox.insert(END, target)


    def execute_command_every_second():
        # Exécute la commande une fois
        self.setTargetList(self.list_targets)
        # Planifie l'exécution de la commande toutes les secondes
        threading.Timer(1, setTargetList).start()
        
    
    
    def sendCommand(self, event=None):
        # TAKES CONTENT OF cmd_entry AND PASSES IT TO SERVER
        text = self.cmd_entry.get("1.0", END)
        print("commande récupérée : ",text)
        return(text)