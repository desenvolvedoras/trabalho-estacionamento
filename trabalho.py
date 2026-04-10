import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

janela = tk.Tk()
janela.title("Gerenciador de Vagas- Estacionamento Frangiomar")

conexao = sqlite3.connect("frangio.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS cadastro (
    nome TEXT,
    placa INTEGER PRIMARY KEY,
    modelo TEXT,
    cor TEXT,
    data DATE,
    horario TIME
)
""")
conexao.commit()



def entradaveiculo():
    nome = entrada_nome.get().strip()
    placa= entrada_placa.get().strip()
    modelo= entrada_modelo.get().strip()
    cor= entrada_cor.get().strip()
    horario= entrada_horario.get().strip()
    data= entrada_data.get().strip()
    
    if nome== "" or placa == "" or modelo == "" or cor == "" or horario == "" or data == "":
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return
    
    cursor.execute("""
    INSERT INTO titulos (nome, placa, modelo, cor, data, horario)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, placa, modelo, cor, data, horario))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")



#DEFINE ABAS
abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")

#ABA ENTRADA DE VEÍCULOS

aba_entradaveiculos = tk.Frame(abas)

abas.add(aba_entradaveiculos, text="Entrada de Veículos")

tk.Label(aba_entradaveiculos, text="Nome:").grid(row=1, column=0)
entrada_nome = tk.Entry(aba_entradaveiculos)
entrada_nome.grid(row=1, column=1)

tk.Label(aba_entradaveiculos, text="Placa do Carro:").grid(row=2, column=0)
entrada_placa = tk.Entry(aba_entradaveiculos)
entrada_placa.grid(row=2, column=1)

tk.Label(aba_entradaveiculos, text="Modelo do Carro:").grid(row=3, column=0)
entrada_modelo = tk.Entry(aba_entradaveiculos)
entrada_modelo.grid(row=3, column=1)

tk.Label(aba_entradaveiculos, text="Cor:").grid(row=4, column=0)
entrada_cor = tk.Entry(aba_entradaveiculos)
entrada_cor.grid(row=4, column=1)

tk.Label(aba_entradaveiculos, text="Horário de Entrada(00:00):").grid(row=5, column=0)
entrada_horario = tk.Entry(aba_entradaveiculos)
entrada_horario.grid(row=5, column=1)

tk.Label(aba_entradaveiculos, text="Data: (00/00/00):").grid(row=6, column=0)
entrada_data = tk.Entry(aba_entradaveiculos)
entrada_data.grid(row=6, column=1)

tk.Button(aba_entradaveiculos, text="Enviar", command=entradaveiculo).grid(row=7, column=0, columnspan=2)


# ABA SAÍDA DE VEÍCULOS

aba_saidaveiculo = tk.Frame(abas)
abas.add(aba_saidaveiculo, text="Saída de Veículos")

tk.Label(aba_saidaveiculo, text="Placa").grid(row=1, column=0)
saida_placa = tk.Entry(aba_saidaveiculo)
saida_placa.grid(row=1, column=1)

tk.Button(aba_saidaveiculo, text="Enviar", command=saidaveiculo).grid(row=1, column=2, columnspan=2)


def saidaveiculo():
placa = saida_placa.get().strip()
    




#ABA ATUALIZAR/EXCLUIR 
aba_update = tk.Frame(abas)
abas.add(aba_update, text="Atualizar/Excluir")

#ABA RElATÓRIO
aba_relatorio = tk.Frame(abas)
abas.add(aba_relatorio, text="Relatórios")




janela.mainloop()
