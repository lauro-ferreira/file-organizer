import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organizar_pasta(pasta):
    """
    Organiza todos os arquivos da pasta em subpastas por extensão.
    """
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)
            extensao = extensao[1:].upper()  # Remove ponto e põe em maiúsculas

            if extensao == '':
                extensao = 'SEM_EXTENSAO'

            pasta_destino = os.path.join(pasta, extensao)
            if not os.path.exists(pasta_destino):
                os.mkdir(pasta_destino)

            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))


def escolher_pasta():
    """
    Abre um diálogo para o usuário escolher a pasta a organizar.
    """
    pasta = filedialog.askdirectory()
    if pasta:
        organizar_pasta(pasta)
        messagebox.showinfo("Concluído", f"Arquivos organizados em: {pasta}")


# Cria a janela principal
janela = tk.Tk()
janela.title("Organizador de Arquivos por Extensão")
janela.geometry("300x150")

label = tk.Label(janela, text="Clique no botão para escolher a pasta a organizar:")
label.pack(padx=10, pady=10)

botao_escolher = tk.Button(janela, text="Escolher Pasta", command=escolher_pasta)
botao_escolher.pack(padx=10, pady=10)

janela.mainloop()
