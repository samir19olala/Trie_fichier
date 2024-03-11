import tkinter as tk
import customtkinter as ctk
import script
from tkinter import filedialog
from tkinter import messagebox


# fonction 
def Valider():
    extensions = None
    if extension_entry.get():
        extensions = extension_entry.get().split(",")
    try:
        # Récupérer l'année sélectionnée dans la Combobox
        Selctionner_annee = [int(anne.get()),int(anne2.get())]
        # appel de la fonction pour archiver les fichiers dans le repertoire
        dossier_archive = "Archive"+str(Selctionner_annee)
        sortie = entry_sorti.get()+"\\"+ dossier_archive

        if entry_nomFichier.get():
            sortie = entry_sorti.get()+"\\"+ entry_nomFichier.get()

        script.archiver_fichiers(entry_entre.get(),sortie, Selctionner_annee , extensions)
        messagebox.showinfo("confirmation", "operation effectuée avec succes")
    except Exception:
        messagebox.showerror("Echec" ,"Veuillez verifier vos parametres entrés")
        
def parcourir_dossier():
    entry_entre.delete(0,tk.END)
    entry_entre.insert(0,filedialog.askdirectory())

def parcourir_dossier2():
    entry_sorti.delete(0,tk.END)
    entry_sorti.insert(0,filedialog.askdirectory())
    
def reset():
    extension_entry.delete(0,tk.END)
    entry_entre.delete(0,tk.END)
    entry_sorti.delete(0,tk.END)
    entry_nomFichier.delete(0,tk.END)

# valeurs a choisir lors des tries 
# rajout des annees 
valeurs = ['2024','2023','2022','2021','2020','2019','2018','2017','2016','2015','2014'
           ]
# extensions = ["exe","png","jpg","webp","docx","xlsx","jpeg","py","cpp"]

root = ctk.CTk()
root.title("TRIE FICHIER")
# root.iconbitmap("./iconx.ico")
# changer le theme de la fenetre

ctk.set_appearance_mode("dark")

root.geometry("600x600")


frame = ctk.CTkFrame(root, width=480, height=350, fg_color="transparent")
# frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
frame.pack(ipady = 20 , pady = 20)

# Rajout du titre 
titre = ctk.CTkLabel(frame, text="TRIE FICHIER ", fg_color="transparent", font=('arial black', 16,'bold'))
titre.place(relx = 0.5 , rely = 0.06 , anchor = tk.N)

entry_entre=ctk.CTkEntry(frame, placeholder_text="chemin\\vers\\mon dossier a trier\\")
entry_entre.place(relx=0.1, rely=0.2, relwidth=0.85)
# une liste deroulante
#---------------------------------

bouton = ctk.CTkButton(frame , text="parcourir...",command= parcourir_dossier )
bouton.place(relx=0.95, rely=0.28, anchor = tk.NE)


lbl_nomFichier = ctk.CTkLabel(frame, text="dossier sauvegarde", fg_color="transparent", font=('arial', 13) )
lbl_nomFichier.place(relx=0.1, rely=0.4)

entry_nomFichier = ctk.CTkEntry(frame,placeholder_text="-- nom du dossier de sortie -(optionnel)")
entry_nomFichier.place(relx=0.4, rely=0.4, relwidth=0.55)


lbl_extension= ctk.CTkLabel(frame, text="extensions: ", fg_color="transparent", font=('arial', 13) )
lbl_extension.place(relx=0.1, rely=0.5)

extension_entry = ctk.CTkEntry(frame,placeholder_text="ce champ est optionnel  [exe, png ,mp4...] ")
extension_entry.place(relx=0.4, rely=0.5, relwidth=0.55)


entry_sorti=ctk.CTkEntry(frame, placeholder_text="chemin\\vers\\mon dossier de sortie\\")
entry_sorti.place(relx=0.1, rely=0.6, relwidth=0.85)

bouton2 = ctk.CTkButton(frame , text="parcourir...",command= parcourir_dossier2)
bouton2.place(relx=0.95, rely=0.68, anchor = tk.NE)


intervale= ctk.CTkLabel(frame, text="INTERVALE D'ANNEE (2024-2024 par defaut)", fg_color="transparent", font=('arial', 14) )
intervale.place(relx=0.5, rely=0.82 , anchor = tk.CENTER)

lbl_annee1= ctk.CTkLabel(frame, text="DE", fg_color="transparent", font=('arial', 14) )
lbl_annee1.place(relx=0.1, rely=0.9, relwidth=0.1)

anne = ctk.CTkComboBox(frame, values=valeurs)
anne.place(relx=0.22, rely=0.9, relwidth=0.3)

lbl_annee2= ctk.CTkLabel(frame, text="A", fg_color="transparent", font=('arial', 14) )
lbl_annee2.place(relx=0.6, rely=0.9, relwidth=0.1 ,anchor = tk.N)

anne2 = ctk.CTkComboBox(frame, values=valeurs)
anne2.place(relx=0.95, rely=0.9, relwidth=0.3 ,anchor = tk.NE)
# rajout d'une frame pour stabiliser les bouton


footer = ctk.CTkFrame(root,width=480, height=50)
# footer.place(relx=0.5 , rely= 0.8 , anchor=tk.N) 
footer.pack(ipady = 30 , pady = 5)
btn_annuler = ctk.CTkButton(footer, text="Annuler",fg_color="#ff0033" , hover_color="#660033",command=reset)
btn_annuler.place(relx=0.314, rely=0.8, anchor=tk.SE)

btn_valider = ctk.CTkButton(footer, text="Valider", command=Valider)
btn_valider.place(relx=0.98, rely=0.8, anchor=tk.SE)

signature= ctk.CTkLabel(root, text="vesrion 1.1 by samir olala", fg_color="transparent", font=('arial', 12) )
signature.place(relx=0.95, rely=1,anchor=tk.SE)

root.mainloop()