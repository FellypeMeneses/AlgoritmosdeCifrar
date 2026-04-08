import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QTextEdit, QLineEdit, QComboBox, 
                             QPushButton, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class TelaCriptografia(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # --- Configurações da Janela ---
        self.setWindowTitle("Sistema de Cifras Clássicas - UFRPE")
        self.setGeometry(100, 100, 550, 700)
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: #E0E0E0;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #3B8ED0;
            }
            QTextEdit, QLineEdit {
                background-color: #1E1E1E;
                border: 1px solid #333333;
                border-radius: 5px;
                padding: 8px;
                font-size: 13px;
            }
            QComboBox {
                background-color: #1E1E1E;
                border: 1px solid #333333;
                border-radius: 5px;
                padding: 5px;
                min-height: 30px;
            }
            QPushButton#btn_cifrar {
                background-color: #1F538D;
                border-radius: 5px;
                font-weight: bold;
                height: 40px;
            }
            QPushButton#btn_cifrar:hover {
                background-color: #2969B0;
            }
            QPushButton#btn_decifrar {
                background-color: transparent;
                border: 2px solid #1F538D;
                border-radius: 5px;
                font-weight: bold;
                height: 40px;
            }
            QPushButton#btn_decifrar:hover {
                background-color: #1F1F1F;
            }
        """)

        # --- Layout Principal ---
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(15)

        # 1. Título
        titulo = QLabel("Criptografia Simétrica")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 22px; margin-bottom: 10px;")
        layout_principal.addWidget(titulo)

        # 2. Entrada de Texto
        layout_principal.addWidget(QLabel("Texto Original:"))
        self.input_texto = QTextEdit()
        self.input_texto.setPlaceholderText("Digite a mensagem aqui...")
        layout_principal.addWidget(self.input_texto)

        # 3. Configurações (Algoritmo e Chave)
        layout_config = QHBoxLayout()
        
        # Coluna Algoritmo
        col_algo = QVBoxLayout()
        col_algo.addWidget(QLabel("Algoritmo:"))
        self.combo_algoritmos = QComboBox()
        self.combo_algoritmos.addItems([
            "Cifra de César", 
            "Cifra Monoalfabética", 
            "Cifra de Playfair", 
            "Cifra de Hill"
        ])
        col_algo.addWidget(self.combo_algoritmos)
        layout_config.addLayout(col_algo)

        # Coluna Chave
        col_chave = QVBoxLayout()
        col_chave.addWidget(QLabel("Chave (Key):"))
        self.input_chave = QLineEdit()
        self.input_chave.setPlaceholderText("Ex: 3 ou CHAVE")
        col_chave.addWidget(self.input_chave)
        layout_config.addLayout(col_chave)

        layout_principal.addLayout(layout_config)

        # 4. Botões
        layout_botoes = QHBoxLayout()
        
        self.btn_cifrar = QPushButton("CIFRAR")
        self.btn_cifrar.setObjectName("btn_cifrar")
        self.btn_cifrar.clicked.connect(lambda: self.processar("cifrar"))
        
        self.btn_decifrar = QPushButton("DECIFRAR")
        self.btn_decifrar.setObjectName("btn_decifrar")
        self.btn_decifrar.clicked.connect(lambda: self.processar("decifrar"))

        layout_botoes.addWidget(self.btn_cifrar)
        layout_botoes.addWidget(self.btn_decifrar)
        layout_principal.addLayout(layout_botoes)

        # 5. Saída
        layout_principal.addWidget(QLabel("Resultado:"))
        self.output_resultado = QTextEdit()
        self.output_resultado.setReadOnly(True)
        self.output_resultado.setStyleSheet("color: #00FF41; border: 1px solid #1F538D;")
        layout_principal.addWidget(self.output_resultado)

        # 6. Rodapé
        footer = QLabel("UFRPE - Segurança de Sistemas")
        footer.setStyleSheet("color: #666666; font-size: 10px;")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_principal.addWidget(footer)

        self.setLayout(layout_principal)

    def processar(self, modo):
        texto = self.input_texto.toPlainText()
        chave = self.input_chave.text()
        algoritmo = self.combo_algoritmos.currentText()

        if not texto:
            self.output_resultado.setPlainText("Erro: Digite um texto para processar.")
            return

        # Template para futuras lógicas
        resultado = f"--- MODO: {modo.upper()} ---\nAlgoritmo: {algoritmo}\nChave: {chave}\n\n[Resultado será exibido aqui]"
        self.output_resultado.setPlainText(resultado)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TelaCriptografia()
    janela.show()
    sys.exit(app.exec())