from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Treeview
import os
from turing_machine import process_multiple_plates  
from extracts import extract_text_txt, extract_text_image  

def load_image():
    file = filedialog.askopenfilename(
        title="Selecciona una imagen", 
        filetypes=[
            ("All files", "*.png *.jpg *.jpeg, *.webp, *.txt")
        ]
    )
    if file:
        extension = os.path.splitext(file)[1].lower()
        if extension in [".jpg", ".png", ".jpeg", ".webp"]:
            data = extract_text_image(file)
            process_plates(data)
        elif extension in [".txt"]:
            text = extract_text_txt(file)
            process_plates(text)
        else:
            messagebox.showerror("Error", "El archivo seleccionado no es válido")

def process_plates(text):
    valid_plates = process_multiple_plates(text)

    for row in table.get_children():
        table.delete(row)
    
    for plate in valid_plates[1]:
        table.insert("", "end", values=(plate, valid_plates[0][valid_plates[1].index(plate)]))  


root = Tk()
root.title("Validador de Matrículas de Automóviles")
root.minsize(600, 400)

container = Frame(root)
container.pack(expand=True, fill="both")

label_load_image = Label(container, text="Selecciona un archivo para validar:", font=("Arial", 16))
label_load_image.pack(pady=10)

button_load_image = Button(container, text="Cargar archivo", font=("Arial", 16), command=load_image)
button_load_image.pack(pady=10)


table = Treeview(container, columns=("matricula", "matricula_encriptada"), show="headings")
table.heading("matricula", text="Matrícula Válida")
table.heading("matricula_encriptada", text="Matrícula Encriptada")


table.column("matricula", width=200)
table.column("matricula_encriptada", width=200)
table.pack(expand=True, fill="both", padx=20, pady=20)


root.mainloop()
