import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

janela = tk.Tk()
janela.title("Gerenciador de Vagas- Estacionamento Frangiomar")


def cadastrar():
    placa= entrada_placa.get().strip()
    modelo= entrada_modelo.get().strip()
    cor= entrada_cor.get().strip()
    if placa == "" or modelo == "" or cor == "":
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    


#DEFINE ABAS
abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")

#ABA CADASTRO

aba_cadastro = tk.Frame(abas)
abas.add(aba_cadastro, text="Cadastro")

tk.Label(aba_cadastro, text="Placa do Carro:").grid(row=1, column=0)
entrada_placa = tk.Entry(aba_cadastro)
entrada_placa.grid(row=1, column=1)

tk.Label(aba_cadastro, text="Modelo do Carro:").grid(row=2, column=0)
entrada_modelo = tk.Entry(aba_cadastro)
entrada_modelo.grid(row=2, column=1)

tk.Label(aba_cadastro, text="Cor:").grid(row=3, column=0)
entrada_cor = tk.Entry(aba_cadastro)
entrada_cor.grid(row=3, column=1)

tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar).grid(row=6, column=0, columnspan=2)

# ABA REGISTRO

aba_registro = tk.Frame(abas)
abas.add(aba_registro, text="Registro")



janela.mainloop()
