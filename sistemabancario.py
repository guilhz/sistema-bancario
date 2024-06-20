from datetime import datetime
saldo = 0
extrato_atual = []
numero_saques = 0
limite = 500
limite_saques = 3

usuario = str(input('Caro usuário, por favor digite seu nome: ')).title()

while True:
    data = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M:%S')
    menu = f'''
=======================MENU=============================
                                Saldo: R${saldo:.2f}
Olá, {usuario}
Para prosseguir, por favor digite uma opção:
        
Para sacar digite:                          [1]
Para depositar digite:                      [2]
Para visualizar o extrato digite:           [3] 
Para sair digite:                           [0]  
========================================================
Escolha uma opção:'''
    opcao = input(f'{menu} ')
# ---------- OPÇÃO 1 do Menu - Aqui o usuário ao digitar 1 poderá realizar um saque de sua conta bancária. ---------- #
    if opcao == '1':
        t = 0
        while t < 3:  # While para que faça com que o usuário tenha no máximo 3 tentativas em caso de erro.
            if numero_saques < limite_saques:
                saque = float(input('Quanto você deseja sacar? '))
                if saque > 0:
                    if saque <= limite:
                        if float(saque) <= saldo:
                            saldo -= saque
                            numero_saques += 1
                            extrato_atual.append(f'{hora_atual}: Saque de R${saque:.2f} realizado.')
                            extrato_saque = input(f'''
===============================COMPROVANTE================================            
                {data} - Autoatendimento - {hora_atual}
 
Cliente: {usuario}    
                                   
Saque de R${saque:.2f} realizado com sucesso!
Seu novo saldo é: R${saldo:.2f}
                                                    
Para voltar ao menu principal aperte:  [ENTER] ou digite qualquer coisa.
Para finalizar operação digite:         [0]
==========================================================================
Digite aqui: ''')
                            if extrato_saque != '0' or quit('''
==========================================      
    Operação finalizada. Até mais!              
=========================================='''): break
                        else:
                            print('Saldo insuficiente.')
                            t += 1
                    else:
                        print(f'Você só pode sacar no máximo R${limite}.')
                        t += 1
                else:
                    print('Digite um valor válido para saque')
                    t += 1
            else:
                print('Você atingiu o valor máximo de saques por dia. Tente novamente amanhã.')
                break
        else:
            print('Limite máximo de tentativas excedido. Por favor tente novamente mais tarde.')
            continue
# ---------------- OPÇÃO 2 DO MENU - AO DIGITAR 2 PODERÁ REALIZAR UM DEPÓSITO EM SUA CONTA BANCÁRIA. ---------------- #
    elif opcao == '2':
        while True:
            deposito = float(input('Quanto você deseja depositar? '))
            if float(deposito) > 0:
                saldo += deposito
                extrato_atual.append(f'{hora_atual}: Depósito de R${saldo:.2f} realizado.')
                extrato_deposito = input(f'''
===============================COMPROVANTE================================
                {data} - Autoatendimento - {hora_atual}
 
Cliente: {usuario}
                                                
Depósito de R${deposito:.2f} realizado com sucesso!
Seu novo saldo é: R${saldo:.2f}
                                                    
Para voltar ao menu principal aperte:  [ENTER] ou digite qualquer coisa.
Para finalizar operação digite:         [0]       
==========================================================================
Digite aqui: ''')
                if extrato_deposito != '0' or quit('''
==========================================        
    Operação finalizada. Até mais!              
=========================================='''): break
            else:
                print('Digite um valor válido para depósito.')
# ------------- OPÇÃO 3 DO MENU - AO DIGITAR 3 IRÁ MOSTRAR O EXTRATO DAS OPERAÇÕES DE SAQUE E DEPÓSITO. ------------- #
    elif opcao == '3':
        print(f'''
===============================EXTRATO===================================
                {data} - Autoatendimento - {hora_atual}
 
Cliente: {usuario}                     
''')
        extrato_atual or print('Não há operações a serem mostradas.')
        print('\n'.join(extrato_atual))
        print(f'''Saldo disponível: R${saldo:.2f}''')
        extrato = input(f'''
Para voltar ao menu principal aperte:   [ENTER] ou digite qualquer coisa.
Para finalizar operação digite:          [0]
==========================================================================
Digite aqui: ''')
        if extrato != '0' or quit('''
==========================================
    Operação finalizada. Até mais!
=========================================='''): ''
# ---------------- OPÇÃO 0 DO MENU - USUÁRIO AO DIGITAR 0 DEVERÁ CONFIRMAR OPERAÇÃO DE SAÍDA. ---------------- #
    elif opcao == '0':
        while True:
            saida = input('''     
=========================================================================================
    Deseja realmente finalizar a operação? Digite [S] para Confirmar e [N] para Voltar
=========================================================================================
Digite aqui: ''')
            if saida.upper() == 'S': quit(''' 
==========================================
    Operação finalizada. Até mais!
==========================================''')
            elif saida.upper() == 'N': break
            if saida != ['S', 'N']:
                print('Digite uma opção válida.')
    else:
        print('Por favor, digite uma opção válida.')
