import customtkinter as ctk
import tkinter as tk
import random
import string

# --- LÓGICA DOS ALGORITMOS ---

def cifrar_cesar(texto, chave="3"):
    """C = (p + k) mod 26"""
    try:
        k = int(chave)
    except:
        k = 3  # padrão
    
    res = ""
    for char in texto.lower():
        if char.isalpha():
            p = ord(char) - ord('a')
            c = (p + k) % 26
            res += chr(c + ord('a'))
        else:
            res += char
    return res.upper()

def cifrar_monoalfabetica(texto):
    """Substituição com permutação do alfabeto"""
    alfabeto = list(string.ascii_lowercase)
    cifrado = list(alfabeto)
    random.seed(42)  # fixa para sempre gerar a mesma chave
    random.shuffle(cifrado)
    
    tabela = str.maketrans("".join(alfabeto), "".join(cifrado))
    return texto.lower().translate(tabela).upper()


# --- INTERFACE ---

class AppCripto(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Criptografia Clássica")
        self.geometry("500x400")
        
        ctk.CTkLabel(self, text="Texto de Entrada:", font=("Arial", 14)).pack(pady=(20,5))
        self.entrada = ctk.CTkEntry(self, width=400)
        self.entrada.pack(pady=10)
        
        ctk.CTkLabel(self, text="Escolha o Algoritmo:", font=("Arial", 14)).pack(pady=5)
        self.algo_box = ctk.CTkComboBox(
            self, 
            values=["Cifra de César", "Cifra Monoalfabética"], 
            width=400
        )
        self.algo_box.pack(pady=10)
        
        self.btn = ctk.CTkButton(self, text="CIFRAR", command=self.processar)
        self.btn.pack(pady=20)
        
        ctk.CTkLabel(self, text="Resultado:", font=("Arial", 14, "bold")).pack(pady=5)
        self.saida = ctk.CTkEntry(self, width=400)
        self.saida.pack(pady=10)

    def processar(self):
        txt = self.entrada.get()
        escolha = self.algo_box.get()
        
        if escolha == "Cifra de César":
            res = cifrar_cesar(txt)
        elif escolha == "Cifra Monoalfabética":
            res = cifrar_monoalfabetica(txt)
        else:
            res = ""

        self.saida.delete(0, tk.END)
        self.saida.insert(0, res)


if __name__ == "__main__":
    app = AppCripto()
    app.mainloop()