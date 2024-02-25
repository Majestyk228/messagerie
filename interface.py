# IMPORTS
from tkinter import *
from PIL import Image, ImageTk

# MAIN WINDOW
root=Tk()
root.geometry("700x500")
root.title("Trojanworld")
root.resizable(False,False) # NON RESIZABLE WINDOW









# FUNCTIONS
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def printt():
    print("Command sent.")

def cancel():
    print("Text erased.")
    
def on_select(event):
    # Récupérer l'index de l'élément sélectionné
    index = listbox.curselection()
    if index:  # Vérifier si un élément est sélectionné
        # Récupérer le texte de l'élément sélectionné
        selected_text = listbox.get(index)
        # Passer le texte de la cellule sélectionnée à une autre fonction
        process_selected_text(selected_text)
        print("Index: ",index[0])

def process_selected_text(text):
    # Faire quelque chose avec le texte de la cellule sélectionnée
    print("Texte sélectionné à traiter:", text)
    
    
    
    
    
    
    
    
    
    
# Créer un Frame pour contenir l'image et le label
frame = Frame(root,bg=_from_rgb((255,198,37)))
frame.pack(side="top")  # Aligner le frame à gauche

# VARIABLES
list_targets=['015b3or2iqfbnq', 'usia020u2cmbip', 'u5uvsb4epvbr4c', 'xjclld13j091ly', '9il7a640y2o1vb'] 
cmd=StringVar()

# GUI ELEMENTS
## LOGO APP
image = Image.open("C:/Users/Titan/Desktop/TKinter_Project/trojanworld_logo_clean.png")
image = image.resize((32, 36), Image.NEAREST)
photo = ImageTk.PhotoImage(image)


# Créer un Label pour afficher l'image
image_label = Label(frame, image=photo)
image_label.grid(row=0, column=0, sticky="w")

lb_title=Label(frame,text="Trojanworld",bg=_from_rgb((255,198,37)),width="700",height="1",font=("Roboto",20,"bold"),anchor="w", justify="left")
lb_title.grid(row=0, column=1, sticky="w")

# SIDE SCROLL LIST OF TARGETS
listbox = Listbox(root) 
listbox.pack(side = LEFT, fill = BOTH)
scrollbar = Scrollbar(root) 
scrollbar.pack(side = LEFT, fill = BOTH) 
  
# Insert elements into the listbox 
for target in list_targets:
    listbox.insert(END, target) 
    
listbox.configure(yscrollcommand = scrollbar.set,background=_from_rgb((229,229,229)), foreground="black", font=('Roboto',16),width=15)    
scrollbar.config(command = listbox.yview)

listbox.bind('<<ListboxSelect>>', on_select) 

# TEXTFLIELDS
cmd_entry=Text(root,width=50,height=5,fg=_from_rgb((255,255,255)),bg=_from_rgb((0,0,0)))
cmd_entry.place(x=215,y=400)

cmd_return=Text(root,width=58,height=21,fg=_from_rgb((0,0,0)),bg=_from_rgb((255,255,255)))
cmd_return.place(x=215,y=53)

bt_send=Button(root,text="Send",width=5,bg=_from_rgb((255,198,37)),fg="black",font=("Roboto",11,"bold"),command=printt)
bt_send.place(x=628,y=400)

bt_cancel=Button(root,text="Cancel",width=5,bg=_from_rgb((255,255,255)),fg="black",font=("Roboto",11,"bold"),command=cancel)
bt_cancel.place(x=628,y=450)

root.mainloop()

