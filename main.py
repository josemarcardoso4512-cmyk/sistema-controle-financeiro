    #controle financeiro
while True:
    print ("\n---Bem vindo ao sistema de controle financeiro")
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cidade = input("Digite sua cidade: ")     
        salario = float(input("Digite seu salario: "))
        despesas = float(input("Digite suas despesas: "))
        saldo = salario - despesas 
        print("\n---Resumo financeiro---")
        print("Nome: ", nome)
        print("Idade: ", idade)
        print("Cidade: ", cidade)
        print("Salario: R$", salario)
        print("Despesas: R$", despesas) 
        if saldo > 0:
            status = "saldo positivo"
            print("Saldo positivo: R$", saldo)
        else:
            print("Saldo negativo: R$", saldo) 
            status = "saldo negativo"
        with open("banco_de_dados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nome} | Idade: {idade} | Cidade: {cidade} | Salário: {salario} | Despesas: {despesas} | Saldo: {saldo} ({status})\n")
    
        print("\n✔ Dados salvos com sucesso no arquivo 'banco_de_dados.txt'!")
        continuar = input("\nd deseja cadastrar outra pessoa(s/n)")
        if continuar == "n":
            print ("fechando sistemas" )
            break
    except ValueError:
        print("erro na digitacao")
        print ("tente novamente")
        continue  
