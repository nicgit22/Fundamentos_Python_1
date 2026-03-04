try:
    #Lê o número de pessoas 1 
    n = int(input("Digite o número de alturas das pessoas: "))
    
    #Lê altura mínima e máxima permitidas
    altura_min = int(input("Digite a altura mínima (cm): "))
    altura_max = int(input("Digite a altura máxima (cm): "))
    
    contador = 0  # Vai contar quantas pessoas podem andar
    
    #Lê a altura de cada pessoa
    for i in range(1, n + 1):
        altura = int(input(f"Digite a altura da pessoa número {i}: "))
        
        # Verifica se está dentro do limite permitido
        if altura_min <= altura <= altura_max:
            contador += 1
    
    # Mostra o resultado
    print(f"{contador} pessoas podem andar na montanha-russa.")

except ValueError:
    print("Erro: Entrada inválida. Por favor, insira números inteiros válidos.")