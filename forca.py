import tkinter as tk
from tkinter import messagebox
import random
from unidecode import unidecode

# Lista de palavras em português com suas respectivas dicas
palavras_com_dicas = {
    'abajur': 'Objeto de iluminação',
    'abacaxi': 'Fruta tropical',
    'abóbora': 'Legume',
    'agulha': 'Instrumento de costura',
    'alicate': 'Ferramenta de aperto',
    'alface': 'Folha de salada',
    'alfabeto': 'Sistema de letras',
    'amendoim': 'Fruto seco',
    'anel': 'Joia',
    'arco': 'Instrumento musical',
    'aspirador': 'Equipamento de limpeza',
    'avião': 'Meio de transporte',
    'bala': 'Doce',
    'banana': 'Fruta',
    'bicicleta': 'Meio de transporte',
    'blusa': 'Roupa',
    'bola': 'Objetos de jogo',
    'cachorro': 'Animal de estimação',
    'caderno': 'Material escolar',
    'café': 'Bebida',
    'caneta': 'Material de escrita',
    'carro': 'Veículo',
    'celular': 'Equipamento de comunicação',
    'chapéu': 'Acessório de cabeça',
    'chuva': 'Precipitação',
    'computador': 'Equipamento eletrônico',
    'cozinha': 'Ambiente doméstico',
    'copo': 'Utensílio doméstico',
    'coração': 'Órgão vital',
    'criança': 'Ser humano jovem',
    'dente': 'Parte do corpo',
    'dicionário': 'Fonte de palavras',
    'escola': 'Local de ensino',
    'estrada': 'Via de transporte',
    'faca': 'Utensílio de cozinha',
    'fato': 'Roupa',
    'festa': 'Celebração',
    'futebol': 'Esporte',
    'geladeira': 'Eletrodoméstico',
    'guitarra': 'Instrumento musical',
    'iguana': 'Animal réptil',
    'jacaré': 'Animal',
    'janela': 'Abertura na parede',
    'joia': 'Acessório',
    'livro': 'Material de leitura',
    'maçã': 'Fruta',
    'mesa': 'Móvel',
    'melancia': 'Fruta',
    'microfone': 'Equipamento de áudio',
    'música': 'Forma de arte',
    'navio': 'Meio de transporte',
    'notebook': 'Equipamento eletrônico',
    'oculos': 'Acessório de visão',
    'palete': 'Objetos de pintura',
    'panela': 'Utensílio de cozinha',
    'pá': 'Ferramenta',
    'pedra': 'Substância natural',
    'pente': 'Acessório de cabelo',
    'piano': 'Instrumento musical',
    'porta': 'Abertura em paredes',
    'prato': 'Utensílio doméstico',
    'raquete': 'Equipamento esportivo',
    'relógio': 'Acessório de tempo',
    'roda': 'Parte de veículo',
    'sapato': 'Calçado',
    'televisão': 'Equipamento eletrônico',
    'tigre': 'Animal',
    'torneira': 'Objeto de encanamento',
    'tucano': 'Animal',
    'vacina': 'Tratamento médico',
    'vela': 'Fonte de luz',
    'viagem': 'Deslocamento',
    'vulcão': 'Formação geológica',
    'zebra': 'Animal com listras'
}

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry('600x500')  # Define o tamanho inicial da janela
        self.root.minsize(400, 400)    # Define o tamanho mínimo da janela
        self.root.configure(bg='blue')  # Fundo azul para a janela principal
        self.iniciar_jogo()
    
    def iniciar_jogo(self):
        # Remover widgets existentes, se houver
        for widget in self.root.winfo_children():
            widget.destroy()

        self.frame_jogo = tk.Frame(self.root, bg='blue')
        self.frame_jogo.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.label_instrucoes = tk.Label(self.frame_jogo, text="Escolha a fonte da palavra:", bg='blue', fg='white')
        self.label_instrucoes.pack(pady=10)

        self.boton_palavra_aleatoria = tk.Button(self.frame_jogo, text="Palavra Aleatória", command=self.selecionar_palavra_aleatoria, bg='black', fg='white')
        self.boton_palavra_aleatoria.pack(pady=5)

        self.boton_palavra_usuario = tk.Button(self.frame_jogo, text="Adicionar Palavra do Jogador", command=self.adicionar_palavra_usuario, bg='black', fg='white')
        self.boton_palavra_usuario.pack(pady=5)

        self.label_dica = tk.Label(self.frame_jogo, text="", bg='blue', fg='white')
        self.label_dica.pack(pady=10)
        
        self.label_palavra_oculta = tk.Label(self.frame_jogo, text="", bg='blue', fg='white')
        self.label_palavra_oculta.pack(pady=10)
        
        self.label_forca = tk.Label(self.frame_jogo, text="", bg='blue', fg='white')
        self.label_forca.pack(pady=10)
        
        self.entry_palpite = tk.Entry(self.frame_jogo, width=10)
        self.entry_palpite.pack(pady=5)
        
        self.boton_palpite = tk.Button(self.frame_jogo, text="Chutar", command=self.processar_palpite, bg='black', fg='white')
        self.boton_palpite.pack(pady=5)
    
    def selecionar_palavra_aleatoria(self):
        self.palavra, self.dica = self.selecionar_palavra()
        self.palavra_oculta = ['_' for _ in self.palavra]
        self.letras_erradas = 0
        self.max_tentativas = 6
        self.atualizar_interface()

    def adicionar_palavra_usuario(self):
        self.frame_adicionar_palavra = tk.Toplevel(self.root)
        self.frame_adicionar_palavra.title("Adicionar Palavra")
        self.frame_adicionar_palavra.geometry('300x200')  # Define o tamanho da janela de adicionar palavra
        self.frame_adicionar_palavra.configure(bg='blue')  # Fundo azul para a janela de adicionar palavra
        
        tk.Label(self.frame_adicionar_palavra, text="Digite a palavra:", bg='blue', fg='white').pack(pady=5)
        self.entry_nova_palavra = tk.Entry(self.frame_adicionar_palavra)
        self.entry_nova_palavra.pack(pady=5)
        
        tk.Label(self.frame_adicionar_palavra, text="Digite a dica:", bg='blue', fg='white').pack(pady=5)
        self.entry_dica = tk.Entry(self.frame_adicionar_palavra)
        self.entry_dica.pack(pady=5)
        
        tk.Button(self.frame_adicionar_palavra, text="Adicionar", command=self.processar_palavra_usuario, bg='black', fg='white').pack(pady=10)
    
    def processar_palavra_usuario(self):
        nova_palavra = self.entry_nova_palavra.get().lower()
        dica = self.entry_dica.get()
        if nova_palavra and dica:
            palavras_com_dicas[nova_palavra] = dica
            self.palavra = nova_palavra
            self.dica = dica
            self.palavra_oculta = ['_' for _ in self.palavra]
            self.letras_erradas = 0
            self.max_tentativas = 6
            self.frame_adicionar_palavra.destroy()
            self.atualizar_interface()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def selecionar_palavra(self):
        palavra = random.choice(list(palavras_com_dicas.keys()))
        dica = palavras_com_dicas[palavra]
        return palavra, dica

    def desenhar_forca(self, tentativas):
        estagios = [
            '''
            -----
            |   |
                |
                |
                |
                |
            ========
            ''',
            '''
            -----
            |   |
            O   |
                |
                |
                |
            ========
            ''',
            '''
            -----
            |   |
            O   |
            |   |
                |
                |
            ========
            ''',
            '''
            -----
            |   |
            O   |
           /|   |
                |
                |
            ========
            ''',
            '''
            -----
            |   |
            O   |
           /|\\  |
                |
                |
            ========
            ''',
            '''
            -----
            |   |
            O   |
           /|\\  |
           /    |
                |
            ========
            ''',
            '''
            -----
            |   |
            O   |
           /|\\  |
           / \\  |
                |
            ========
            '''
        ]
        return estagios[tentativas]

    def processar_palpite(self):
        palpite = self.entry_palpite.get().lower()
        palpite_sem_acento = unidecode(palpite)
        palavra_sem_acento = unidecode(self.palavra)

        if palpite and len(palpite) == 1:
            if palpite_sem_acento in palavra_sem_acento:
                for i, letra in enumerate(self.palavra):
                    if unidecode(letra) == palpite_sem_acento:
                        self.palavra_oculta[i] = letra
                if '_' not in self.palavra_oculta:
                    self.exibir_mensagem(f"Parabéns! Você acertou a palavra: {self.palavra}", "Parabéns!")
                else:
                    self.atualizar_interface()
            else:
                self.letras_erradas += 1
                if self.letras_erradas >= self.max_tentativas:
                    self.exibir_mensagem(f"Você perdeu! A palavra era: {self.palavra}", "Game Over")
                else:
                    self.atualizar_interface()
        else:
            messagebox.showwarning("Aviso", "Digite uma única letra.")
        
        self.entry_palpite.delete(0, tk.END)

    def atualizar_interface(self):
        self.label_dica.config(text=f"Dica: {self.dica}")
        self.label_palavra_oculta.config(text=" ".join(self.palavra_oculta))
        self.label_forca.config(text=self.desenhar_forca(self.letras_erradas))
    
    def exibir_mensagem(self, mensagem, titulo):
        messagebox.showinfo(titulo, mensagem)
        self.iniciar_jogo()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()
