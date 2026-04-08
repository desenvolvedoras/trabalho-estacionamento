import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("Gerenciador de Vagas- Estacionamento Frangiomar")

#ABA CADASTRO
abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")

aba_cadastro = tk.Frame(abas)
abas.add(aba_cadastro, text="Cadastro")


#ABA REGISTRO
aba_registros = tk.Frame(abas)
abas.add(aba_registros, text="Registros")

tk.Label(aba_registros, text="Placa:").grid(row=0, column=0)
entrada_placa = tk.Entry(aba_registros)
entrada_placa.grid(row=0, column=1)



janela.mainloop()