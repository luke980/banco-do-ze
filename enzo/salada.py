import tkinter as tk
from tkinter import messagebox, Label


#função de verificar saldo
def verificar_saldo(saldo, label_saldo):
    label_saldo.config(text=f"saldo: R${saldo:.2f}")

def sacar_dinheiro(saldo, entry_valor, label_saldo):
    try:
        valor = float(entry_valor.get())
        if valor <= 0:
            messagebox.showerror("Erro","O vslor deve ser maior que zero!")
        elif valor > saldo:
            messagebox.showerror("Error", "saldo insulficiente!")
        else:
            saldo - valor
            messagebox.showinfo("Sucesso", f"Saque de R${valor:.:2f} realizaso!")
            verificar_saldo(saldo, label_saldo)
        entry_valor.delete(0, tk.END)
        return saldo


def criar_interface():
    # saldo inicial
    saldo = 1.00

    #criação da janela principal
    janela = tk.Tk()
    janela.title("caixa do santo zé")
    janela.geometry("700x600")
    janela.configure(bg="#64ffbd")


    #titulo do app
    tk.Label(janela, text="caixa do santo zé", font=("arial", 20, "bold"), bg="#64ffbd", fg="black").pack(pady=20)

#
    label_saldo = tk.Label(janela, text=f'saldo: R${saldo:.2f}', font=("Arial", 14), bg="#64ffbd", fg="black").pack(pady=10)

    tk.Label(janela, text="Valor:R$", font=("Arial"), bg='#64ffbd', fg="black").pack(pady=10)
    entry_valor = tk.Entry(janela, font=("arial",12), width=20).pack(pady=5)

    def btn_sacar():
        nonlocal saldo
        saldo = sacar_dinheiro(saldo, entry_valor, label_saldo)

    def btn_depositar():
        nonlocal saldo
        saldo = btn_depositar(saldo, entry_valor, label_saldo)

    def sair():
        if messagebox.askyesno("sair", "deseja sair?"):
            janela.destroy()

    btn_sacar = tk.Button(janela, text="sacar dinheiro", font=("Arial", 12), bg="#0ee500", fg="black", command=btn_sacar).pack(pady=10, padx=20, fill=tk.X)

    btn_sair = tk.Button(janela, text="sair", font=("Arial", 12), bg="#00ffc9", fg="black", command='btn_sair').pack(pady=10, padx=20, fill=tk.X)

    btn_depositar = tk.Button(janela, text="depositardinheiro", font=("Arial", 12), bg="#ff0000", fg="black", command=btn_depositar).pack(pady=10, padx=20, fill=tk.X)


    janela.mainloop()




criar_interface()