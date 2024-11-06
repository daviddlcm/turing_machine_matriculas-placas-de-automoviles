from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from turing_machine import process_string
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
            print(data)
            print("procesado")
            # if process_string(text):
            #     messagebox.showinfo("Resultado", "La matricula es valida")
            # else:
            #     messagebox.showinfo("Resultado", "La matricula no es valida")
        elif extension in [".txt"]:
            text = extract_text_txt(file)
            if process_string(text):
                messagebox.showinfo("Resultado", "La matricula es valida")
            else:
                messagebox.showinfo("Resultado", "La matricula no es valida")
        else:
            messagebox.showerror("Error", "El archivo seleccionado no es valido")
        



root = Tk()

root.title("Validador de Matriculas de Automoviles")
root.minsize(400,400)

container = Frame(root)
container.pack(expand=True,fill="both")

#cargar imagen
label_load_image = Label(container, text="Selecciona un archivo para validar:",font = ("Arial", 16))
label_load_image.pack(pady=10)

button_load_image = Button(container, text="Cargar archivo",font = ("Arial", 16), command = load_image)
button_load_image.pack(pady=10)

root.mainloop()