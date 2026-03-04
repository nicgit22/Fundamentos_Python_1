#------Importar a biblioteca de UI --User Interface-----
import tkinter as tk #Interface gráfica
from tkinter import scrolledtext, ttk

#----Função-----
def gerar_tabuada(numeroBase, limiteMaximo):
    txt_resposta = f"Claro!, aqui está a tabuada do {numeroBase} até o {limiteMaximo}:\n\n"

    for i in range(1,limiteMaximo+1):
        resultado = numeroBase * i
   
        linha_formatada = f"{numeroBase} x {i} = {resultado} \n"

        txt_resposta += linha_formatada

    return txt_resposta

def processar_e_responder():
    mensagem_usuario = campo_entrada_usuario.get().strip()

    if mensagem_usuario:
        adicionar_texto_ao_chat(f"Você: {mensagem_usuario}\n")
        campo_entrada_usuario.delete(0, tk.END)

        try:
            partes_da_mensagem = mensagem_usuario.split()

            if len(partes_da_mensagem) != 2:
                raise ValueError("O formato da entrada é inválido.")
           
            numero_base = int(partes_da_mensagem[0])
            limite_maximo = int(partes_da_mensagem[1])

            resposta_do_bot = gerar_tabuada(numero_base, limite_maximo)
        except (ValueError, IndexError):
            resposta_do_bot = ("Desculpe, não entendi. Por favor, digite dois números separados por um espaço.\n\nExemplo: 5 10")
       
        adicionar_texto_ao_chat(f"ChatBot: {resposta_do_bot}\n\n", tag = "tag_bot")

def adicionar_texto_ao_chat(texto, tag=None):
    janela_chat.config(state = tk.NORMAL)
    janela_chat.insert(tk.END, texto, tag)
    janela_chat.config(state = tk.DISABLED)
    janela_chat.see(tk.END)

#--------- Seção de configuração da interface gráfica --------
janela_principal = tk.Tk()
janela_principal.title("Chat de tabuada")
janela_principal.geometry("450x550")
janela_principal.resizable(False,False)


frame_principal = ttk.Frame(janela_principal, padding="10")
frame_principal.pack(fill=tk.BOTH, expand=True)

janela_chat = scrolledtext.ScrolledText(
    frame_principal,
    wrap = tk.WORD,
    state = tk.DISABLED,
    font = ("Arial", 11)
)
janela_chat.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

janela_chat.tag_config("tag_bot", foreground="#005b96")

frame_entrada = ttk.Frame(frame_principal)
frame_entrada.pack(padx=5, pady=10, fill=tk.X)

campo_entrada_usuario = ttk.Entry(frame_entrada, font=("Arial", 12))
campo_entrada_usuario.pack(side=tk.LEFT, fill=tk.X, expand=True, ipadx=5)
campo_entrada_usuario.focus()

botao_enviar = ttk.Button(
    frame_entrada,
    text="Enviar",
    command=processar_e_responder
)
botao_enviar.pack(side=tk.RIGHT, padx=(5,0))

mensagem_inicial = (
    "Olá!, Sou seu assistente de tabuadas Prof° Clodoaldo.\n\n"
    "Digite o número da tabuada, um espaço, e até qual valor você deseja calcular. \n\n"
    "Exemplo: 7 12\n\n"
)

adicionar_texto_ao_chat(f"ChatBot: {mensagem_inicial}", tag="tag_bot")

janela_principal.bind('<Return>', lambda evento: processar_e_responder())

janela_principal.mainloop()