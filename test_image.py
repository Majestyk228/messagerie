# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:13:06 2024

@author: Titan
"""
import tkinter as Tk
 
def imgaffiche():
    img = Tk.PhotoImage(file = imgfile)  ## Création d'un objet PhotoImage qui reconnait les extensions .gif et .ppm    
    gifsdict[imgfile] = img              ## si on commente cette ligne, l'image ne s'affichera pas
    button.configure(image=img)          ## Ajout de l'image sur le bouton
    ## On pourrait aussi directement faire
    ## gifsdict[imgfile] = Tk.PhotoImage(file = imgfile)              
    ## button.configure(image = gifsdict[imgfile])
    
root = Tk.Tk()
button = Tk.Button(text = "affiche image", command = imgaffiche)
 
imgfile = "C:/Users/Titan/Desktop/messagerie/messagerie/ressources/image_target.png" ## strchemin:str, chemin d'accès à l'image
 
gifsdict={}  ## Utilisation d'un dictionnaire pour conserver une référence sur la PhotoImage créée
 
button.pack()
root.mainloop()