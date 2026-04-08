import tkinter as tk
from tkinter import ttk, messagebox

teste = 0
janela = tk.Tk()
janela.title("Gerenciador de Vagas- Estacionamento Frangiomar")

#ABA CADASTRO
abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")
#CAMPO DE ENTRADA
aba_cadastro = tk.Frame(abas)
abas.add(aba_cadastro, text="Cadastro")




#ABA REGISTRO
aba_registros = tk.Frame(abas)
abas.add(aba_registros, text="Registros")

tk.Label(aba_registros, text="Placa:").grid(row=0, column=0)
entrada_placa = tk.Entry(aba_registros)
entrada_placa.grid(row=0, column=1)

#BOTÃO DE ENVIAR
tk.Button(aba_registros, text="Enviar",command='teste').grid(row=0, column=2, columnspan=1)


janela.mainloop()
