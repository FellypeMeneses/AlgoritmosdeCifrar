import customtkinter as ctk
import tkinter as tk

# --- ESPAÇO PARA SUA IMPLEMENTAÇÃO FUTURA ---
# Aqui você criará as funções seguindo os conceitos da Aula 02:
# Substituição e Transposição [cite: 44, 110, 113]

def aplicar_cesar(texto):
    # Futura lógica: C = (p + k) mod 26 [cite: 286]
    return f"Lógica de César para: {texto}"

def aplicar_monoalfabetica(texto):
    # Futura lógica: Substituição arbitrária/permutação [cite: 391, 401]
    return f"Lógica Monoalfabética para: {texto}"

def aplicar_playfair(texto):
    # Futura lógica: Matriz 5x5 e dígrafos [cite: 450, 455]
    return f"Lógica de Playfair para: {texto}"

def aplicar_hill(texto):
    # Futura lógica: Álgebra linear e matrizes [cite: 576, 582]
    return f"Lógica de Hill para: {texto}"

# --- INTERFACE GRÁFICA (TELA) ---

class TelaCriptografia(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Sistema de Cifras Clássicas - UFRPE")
        self.geometry("500x500")
        self.grid_columnconfigure(0, weight=1)

        # 1. Título
        self.label_titulo = ctk.CTkLabel(
            self, text="Criptografia Simétrica", 
            font=("Roboto", 22, "bold")
        )
        self.label_titulo.pack(pady=20)

        # 2. Entrada de Texto (Plaintext - X) [cite: 70, 719]
        self.label_input = ctk.CTkLabel(self, text="Digite o Texto Original:")
        self.label_input.pack(pady=(10, 0))
        
        self.entry_texto = ctk.CTkEntry(
            self, width=400, placeholder_text="Texto para encriptar..."
        )
        self.entry_texto.pack(pady=10)

        # 3. Seleção do Algoritmo [cite: 45, 107]
        self.label_combo = ctk.CTkLabel(self, text="Selecione a Técnica:")
        self.label_combo.pack(pady=(10, 0))
        
        self.combo_algoritmos = ctk.CTkComboBox(
            self, width=400,
            values=["Cifra de César", "Cifra Monoalfabética", "Cifra de Playfair", "Cifra de Hill"]
        )
        self.combo_algoritmos.pack(pady=10)

        # 4. Botão de Execução (Cifragem - E) [cite: 21, 78]
        self.btn_cifrar = ctk.CTkButton(
            self, text="Cifrar Mensagem", 
            command=self.executar_comando,
            fg_color="#1f538d"
        )
        self.btn_cifrar.pack(pady=30)

        # 5. Saída do Resultado (Ciphertext - Y) [cite: 18, 77, 720]
        self.label_saida = ctk.CTkLabel(self, text="Resultado (Texto Cifrado):", font=("Arial", 12, "bold"))
        self.label_saida.pack(pady=(10, 0))
        
        self.entry_resultado = ctk.CTkEntry(
            self, width=400, fg_color="#2b2b2b", text_color="white"
        )
        self.entry_resultado.pack(pady=10)

    def executar_comando(self):
        """
        Função que direciona qual algoritmo será usado. 
        É aqui que você conectará sua lógica futuramente.
        """
        texto_original = self.entry_texto.get()
        escolha = self.combo_algoritmos.get()
        
        if escolha == "Cifra de César":
            resultado = aplicar_cesar(texto_original)
        elif escolha == "Cifra Monoalfabética":
            resultado = aplicar_monoalfabetica(texto_original)
        elif escolha == "Cifra de Playfair":
            resultado = aplicar_playfair(texto_original)
        elif escolha == "Cifra de Hill":
            resultado = aplicar_hill(texto_original)
        else:
            resultado = "Selecione um algoritmo."

        # Exibe o resultado na tela
        self.entry_resultado.delete(0, tk.END)
        self.entry_resultado.insert(0, resultado)

if __name__ == "__main__":
    app = TelaCriptografia()
    app.mainloop()