import customtkinter as ctk
import tkinter as tk
import random
import string

# --- LÓGICA DOS ALGORITMOS (Aula 02) ---

def cifrar_cesar(texto, chave="3"):
    """C = (p + k) mod 26 [cite: 286]"""
    try:
        k = int(chave)
    except:
        k = 3 # Deslocamento padrão de Júlio César 
    
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
    """Substituição arbitrária usando permutação do alfabeto [cite: 391, 402]"""
    alfabeto = list(string.ascii_lowercase)
    cifrado = list(alfabeto)
    random.seed(42) # Seed fixa para demonstração da chave
    random.shuffle(cifrado)
    tabela = str.maketrans("".join(alfabeto), "".join(cifrado))
    return texto.lower().translate(tabela).upper()

def cifrar_playfair(texto):
    """Substituição por digramas usando matriz 5x5 [cite: 450, 455]"""
    # Matriz baseada na palavra MONARCHY 
    matriz = [
        ['M','O','N','A','R'],
        ['C','H','Y','D','B'],
        ['E','F','G','I','K'],
        ['L','P','Q','S','T'],
        ['U','V','W','X','Z']
    ]
    
    def buscar(letra):
        if letra == 'j': letra = 'i'
        for r in range(5):
            for c in range(5):
                if matriz[r][c] == letra.upper():
                    return r, c
        return 0, 0

    texto = texto.lower().replace(" ", "").replace("j", "i")
    # Trata letras repetidas e preenchimento (filler) [cite: 472, 507]
    processado = ""
    i = 0
    while i < len(texto):
        a = texto[i]
        b = texto[i+1] if (i+1) < len(texto) else 'x'
        if a == b:
            processado += a + 'x'
            i += 1
        else:
            processado += a + b
            i += 2
            
    res = ""
    for i in range(0, len(processado), 2):
        r1, c1 = buscar(processado[i])
        r2, c2 = buscar(processado[i+1])
        
        if r1 == r2: # Mesma linha [cite: 473]
            res += matriz[r1][(c1+1)%5] + matriz[r2][(c2+1)%5]
        elif c1 == c2: # Mesma coluna [cite: 483]
            res += matriz[(r1+1)%5][c1] + matriz[(r2+1)%5][c2]
        else: # Regra do retângulo [cite: 485]
            res += matriz[r1][c2] + matriz[r2][c1]
    return res

def cifrar_hill(texto):
    """C = PK mod 26 usando matriz 2x2 invertível [cite: 717, 721]"""
    K = [[5, 8], [17, 3]] # Matriz invertível módulo 26 [cite: 634, 648]
    texto = texto.lower().replace(" ", "")
    if len(texto) % 2 != 0: texto += 'x'
    
    res = ""
    for i in range(0, len(texto), 2):
        p1 = ord(texto[i]) - ord('a')
        p2 = ord(texto[i+1]) - ord('a')
        c1 = (p1 * K[0][0] + p2 * K[1][0]) % 26
        c2 = (p1 * K[0][1] + p2 * K[1][1]) % 26
        res += chr(c1 + ord('a')) + chr(c2 + ord('a'))
    return res.upper()

# --- INTERFACE ---

class AppCripto(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Criptografia Clássica - Aula 02")
        self.geometry("500x450")
        
        # UI Elements
        ctk.CTkLabel(self, text="Texto de Entrada:", font=("Arial", 14)).pack(pady=(20,5))
        self.entrada = ctk.CTkEntry(self, width=400, placeholder_text="Digite aqui...")
        self.entrada.pack(pady=10)
        
        ctk.CTkLabel(self, text="Escolha o Algoritmo:", font=("Arial", 14)).pack(pady=5)
        self.algo_box = ctk.CTkComboBox(self, values=["Cifra de César", "Cifra Monoalfabética", "Cifra de Playfair", "Cifra de Hill"], width=400)
        self.algo_box.pack(pady=10)
        
        self.btn = ctk.CTkButton(self, text="CIFRAR", command=self.processar, fg_color="blue")
        self.btn.pack(pady=20)
        
        ctk.CTkLabel(self, text="Chave Sifrada (Resultado):", font=("Arial", 14, "bold")).pack(pady=5)
        self.saida = ctk.CTkEntry(self, width=400, fg_color="#2b2b2b", text_color="white")
        self.saida.pack(pady=10)

    def processar(self):
        txt = self.entrada.get()
        escolha = self.algo_box.get()
        
        if escolha == "Cifra de César":
            res = cifrar_cesar(txt)
        elif escolha == "Cifra Monoalfabética":
            res = cifrar_monoalfabetica(txt)
        elif escolha == "Cifra de Playfair":
            res = cifrar_playfair(txt)
        elif escolha == "Cifra de Hill":
            res = cifrar_hill(txt)
        else:
            res = ""

        self.saida.delete(0, tk.END)
        self.saida.insert(0, res)

if __name__ == "__main__":
    app = AppCripto()
    app.mainloop()