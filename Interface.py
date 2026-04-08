import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# --- LÓGICA DE CRIPTOGRAFIA ---

def cifrar_cesar(texto, chave):
    try: n = int(chave)
    except: n = 3
    res = ""
    for char in texto:
        if char.isalpha():
            base = 97 if char.islower() else 65
            res += chr((ord(char) - base + n) % 26 + base)
        else: res += char
    return res

def decifrar_cesar(texto, chave):
    try: n = int(chave)
    except: n = 3
    return cifrar_cesar(texto, -n)

def cifrar_monoalfabetica(texto, chave):
    if len(chave) != 26: return "ERRO: A chave deve ter 26 letras!"
    alfabeto = string.ascii_lowercase
    tabela = str.maketrans(alfabeto + alfabeto.upper(), chave.lower() + chave.upper())
    return texto.translate(tabela)

def decifrar_monoalfabetica(texto, chave):
    if len(chave) != 26: return "ERRO: A chave deve ter 26 letras!"
    alfabeto = string.ascii_lowercase
    tabela = str.maketrans(chave.lower() + chave.upper(), alfabeto + alfabeto.upper())
    return texto.translate(tabela)

# --- PLAYFAIR ---
def playfair_matriz(chave_txt="MONARCHY"):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    chave_limpa = ""
    for c in (chave_txt.upper() + alfabeto):
        if c == 'J': c = 'I'
        if c not in chave_limpa and c in alfabeto:
            chave_limpa += c
    return [list(chave_limpa[i:i+5]) for i in range(0, 25, 5)]

def buscar_pf(matriz, letra):
    if letra == 'J': letra = 'I'
    for r in range(5):
        for c in range(5):
            if matriz[r][c] == letra: return r, c
    return 0, 0

def processar_playfair(texto, modo, chave_txt):
    matriz = playfair_matriz(chave_txt)
    texto = texto.upper().replace("J", "I").replace(" ", "")
    if modo == "cifrar" and len(texto) % 2 != 0: texto += "X"
    
    res = ""
    passo = 1 if modo == "cifrar" else -1
    for i in range(0, len(texto), 2):
        r1, c1 = buscar_pf(matriz, texto[i])
        r2, c2 = buscar_pf(matriz, texto[i+1])
        if r1 == r2:
            res += matriz[r1][(c1 + passo) % 5] + matriz[r2][(c2 + passo) % 5]
        elif c1 == c2:
            res += matriz[(r1 + passo) % 5][c1] + matriz[(r2 + passo) % 5][c2]
        else:
            res += matriz[r1][c2] + matriz[r2][c1]
    return res

# --- HILL ---
K = [[5, 8], [17, 3]]
K_INV = [[3, 18], [17, 5]]

def processar_hill(texto, matriz_k):
    texto = "".join(filter(str.isalpha, texto.lower()))
    if len(texto) % 2 != 0: texto += 'x'
    res = ""
    for i in range(0, len(texto), 2):
        p = [ord(texto[i]) - 97, ord(texto[i+1]) - 97]
        c = [(p[0]*matriz_k[0][0] + p[1]*matriz_k[1][0]) % 26,
             (p[0]*matriz_k[0][1] + p[1]*matriz_k[1][1]) % 26]
        res += chr(c[0] + 97) + chr(c[1] + 97)
    return res.upper()

# --- INTERFACE ---

class AppCripto:
    def __init__(self, root):
        self.root = root
        root.title("Cripto Lab v2.0")
        root.geometry("750x700")
        root.configure(bg="#0f172a")

        # Título
        tk.Label(root, text="SISTEMA DE CRIPTOGRAFIA", font=("Inter", 20, "bold"), 
                 bg="#0f172a", fg="#38bdf8").pack(pady=20)

        main_frame = tk.Frame(root, bg="#0f172a")
        main_frame.pack(padx=20, fill=tk.BOTH, expand=True)

        # Entrada
        tk.Label(main_frame, text="Texto de Entrada:", bg="#0f172a", fg="#94a3b8").pack(anchor="w")
        self.entrada = tk.Text(main_frame, height=5, bg="#1e293b", fg="white", 
                               font=("Consolas", 11), borderwidth=0, padx=10, pady=10, insertbackground="white")
        self.entrada.pack(fill=tk.X, pady=5)

        # Configurações
        config_frame = tk.Frame(main_frame, bg="#1e293b", padx=15, pady=15)
        config_frame.pack(fill=tk.X, pady=15)

        tk.Label(config_frame, text="Algoritmo:", bg="#1e293b", fg="white").grid(row=0, column=0, sticky="w")
        self.combo = ttk.Combobox(config_frame, state="readonly", width=25,
                                  values=["Cifra de César", "Monoalfabética", "Playfair", "Hill"])
        self.combo.grid(row=0, column=1, padx=10, sticky="w")
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.ajustar_dica_chave)

        tk.Label(config_frame, text="Chave:", bg="#1e293b", fg="white").grid(row=1, column=0, sticky="w", pady=10)
        self.entry_chave = tk.Entry(config_frame, width=30, bg="#0f172a", fg="#38bdf8", 
                                    insertbackground="white", borderwidth=0)
        self.entry_chave.grid(row=1, column=1, padx=10, sticky="w")
        self.entry_chave.insert(0, "3")

        btn_gerar = tk.Button(config_frame, text="🎲 GERAR ALEATÓRIO", command=self.gerar_chave,
                              bg="#334155", fg="white", relief="flat", padx=10, cursor="hand2")
        btn_gerar.grid(row=1, column=2, padx=5)

        # Botões de Ação
        btn_frame = tk.Frame(main_frame, bg="#0f172a")
        btn_frame.pack(pady=10)

        self.btn_cifrar = tk.Button(btn_frame, text="🔒 CIFRAR", command=lambda: self.processar("cifrar"),
                                   bg="#059669", fg="white", font=("bold"), width=15, relief="flat", cursor="hand2")
        self.btn_cifrar.pack(side=tk.LEFT, padx=10)

        self.btn_decifrar = tk.Button(btn_frame, text="🔓 DECIFRAR", command=lambda: self.processar("decifrar"),
                                     bg="#2563eb", fg="white", font=("bold"), width=15, relief="flat", cursor="hand2")
        self.btn_decifrar.pack(side=tk.LEFT, padx=10)

        # Saída
        tk.Label(main_frame, text="Resultado:", bg="#0f172a", fg="#94a3b8").pack(anchor="w")
        self.saida = tk.Text(main_frame, height=5, bg="#020617", fg="#10b981", 
                             font=("Consolas", 12, "bold"), borderwidth=0, padx=10, pady=10)
        self.saida.pack(fill=tk.X, pady=5)

    def ajustar_dica_chave(self, event=None):
        escolha = self.combo.get()
        self.entry_chave.delete(0, tk.END)
        if escolha == "Cifra de César": self.entry_chave.insert(0, "3")
        elif escolha == "Monoalfabética": self.entry_chave.insert(0, "zyxwvutsrqponmlkjihgfedcba")
        elif escolha == "Playfair": self.entry_chave.insert(0, "KEYWORD")
        else: self.entry_chave.insert(0, "Matriz Fixa 2x2")

    def gerar_chave(self):
        escolha = self.combo.get()
        self.entry_chave.delete(0, tk.END)
        if escolha == "Cifra de César":
            self.entry_chave.insert(0, str(random.randint(1, 25)))
        elif escolha == "Monoalfabética":
            alfabeto = list(string.ascii_lowercase)
            random.shuffle(alfabeto)
            self.entry_chave.insert(0, "".join(alfabeto))
        elif escolha == "Playfair":
            letras = list(string.ascii_uppercase.replace("J", ""))
            random.shuffle(letras)
            self.entry_chave.insert(0, "".join(letras[:8]))
        else:
            self.entry_chave.insert(0, "Chave Automática")

    def processar(self, modo):
        txt_entrada = self.entrada.get("1.0", tk.END).strip()
        chave = self.entry_chave.get().strip()
        escolha = self.combo.get()

        if not txt_entrada:
            messagebox.showwarning("Aviso", "Digite um texto para processar.")
            return

        try:
            # Cálculo do resultado
            if escolha == "Cifra de César":
                res = cifrar_cesar(txt_entrada, chave) if modo == "cifrar" else decifrar_cesar(txt_entrada, chave)
            elif escolha == "Monoalfabética":
                res = cifrar_monoalfabetica(txt_entrada, chave) if modo == "cifrar" else decifrar_monoalfabetica(txt_entrada, chave)
            elif escolha == "Playfair":
                res = processar_playfair(txt_entrada, modo, chave)
            elif escolha == "Hill":
                res = processar_hill(txt_entrada, K) if modo == "cifrar" else processar_hill(txt_entrada, K_INV)
            
            if modo == "decifrar":
                # Lógica de Troca (Swap):
                # O que era resultado vira entrada, e o que era entrada vira resultado informativo.
                self.entrada.delete("1.0", tk.END)
                self.entrada.insert(tk.END, res)
                
                self.saida.delete("1.0", tk.END)
                self.saida.insert(tk.END, txt_entrada)
            else:
                # Cifragem normal
                self.saida.delete("1.0", tk.END)
                self.saida.insert(tk.END, res)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppCripto(root)
    root.mainloop()