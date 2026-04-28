import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ----------------------------
# BANCO DE DADOS
# ----------------------------
conexao = sqlite3.connect("catraca_onibus.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS passageiros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pagamento TEXT,
    valor REAL,
    horario TEXT
)
""")

conexao.commit()

# ----------------------------
# FUNÇÕES
# ----------------------------
def registrar_passageiro():
    pagamento = combo_pagamento.get()

    if pagamento == "":
        messagebox.showerror("Erro", "Selecione o tipo de pagamento")
        return

    valor = 0

    if pagamento == "Dinheiro":
        valor = 5.00
    elif pagamento == "Cartão":
        valor = 5.00
    elif pagamento == "Gratuito":
        valor = 0

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cursor.execute("""
    INSERT INTO passageiros (pagamento, valor, horario)
    VALUES (?, ?, ?)
    """, (pagamento, valor, horario))

    conexao.commit()

    messagebox.showinfo("Sucesso", "Catraca liberada!")

    combo_pagamento.set("")

    atualizar_tabela()
    atualizar_total()


def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    cursor.execute("SELECT id, pagamento, valor, horario FROM passageiros")
    dados = cursor.fetchall()

    for row in dados:
        tabela.insert("", tk.END, values=row)


def atualizar_total():
    cursor.execute("SELECT SUM(valor) FROM passageiros")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    lbl_total.config(text=f"Total arrecadado: R$ {total:.2f}")


def excluir_passageiro():
    item_selecionado = tabela.selection()

    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione um registro para excluir")
        return

    valores = tabela.item(item_selecionado, "values")
    id_passageiro = valores[0]

    confirmar = messagebox.askyesno("Confirmar", "Deseja excluir este registro?")

    if confirmar:
        cursor.execute("DELETE FROM passageiros WHERE id = ?", (id_passageiro,))
        conexao.commit()

        atualizar_tabela()
        atualizar_total()

        messagebox.showinfo("Sucesso", "Registro excluído!")

# INTERFACE
janela = tk.Tk()
janela.title("Sistema de Catraca de Ônibus")
janela.geometry("700x500")
janela.configure(bg="#dfe6e9")

# Pagamento
tk.Label(janela, text="Tipo de Pagamento:", bg="#dfe6e9").pack()

combo_pagamento = ttk.Combobox(
    janela,
    values=["Dinheiro", "Cartão", "Gratuito"]
)
combo_pagamento.pack(pady=5)

# Frame para botões
frame_botoes = tk.Frame(janela, bg="#dfe6e9")
frame_botoes.pack(pady=10)

# Botão registrar
btn_registrar = tk.Button(
    frame_botoes,
    text="Liberar Catraca",
    command=registrar_passageiro,
    bg="green",
    fg="white",
    width=20
)
btn_registrar.grid(row=0, column=0, padx=5)

# Botão excluir
btn_excluir = tk.Button(
    frame_botoes,
    text="Excluir Selecionado",
    command=excluir_passageiro,
    bg="red",
    fg="white",
    width=20
)
btn_excluir.grid(row=0, column=1, padx=5)

# Tabela
colunas = ("ID", "Pagamento", "Valor", "Horário")

tabela = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)

tabela.column("ID", width=50)
tabela.column("Pagamento", width=120)
tabela.column("Valor", width=80)
tabela.column("Horário", width=200)

tabela.pack(pady=20)

# Total arrecadado
lbl_total = tk.Label(
    janela,
    text="Total arrecadado: R$ 0.00",
    font=("Arial", 12, "bold"),
    bg="#4ff508"
)
lbl_total.pack()

# Inicialização
atualizar_tabela()
atualizar_total()

janela.mainloop()

conexao.close()