class Conta:
    def __init__(self, saldo=0, limite=500, limite_saques=3):
        self.saldo = saldo
        self.extrato_atual = []
        self.numero_saques = 0
        self.limite = limite
        self.limite_saques = limite_saques
        self.agencia = '0001'

    def menu(self):
        while True:
            menulogado = f'''
=======================MENU=============================
Ag.{self.agencia}                               Saldo: R${self.saldo:.2f}

Olá, 
Para prosseguir, por favor digite uma opção:

Para sacar digite:                          [1]
Para depositar digite:                      [2]
Para visualizar o extrato digite:           [3] 
Para sair digite:                           [0]  
========================================================
Escolha uma opção:'''
            opcao = input(f'{menulogado} ')
            if opcao == '1':
                self.sacar()
            elif opcao == '2':
                self.depositar()
            elif opcao == '3':
                self.exibir_extrato()
            elif opcao == '0':
                self.sair()

    def sacar(self):
        from datetime import datetime
        t = 0
        while t < 3:  # While para que faça com que o usuário tenha no máximo 3 tentativas em caso de erro.
            data = datetime.now().strftime('%d/%m/%Y')
            hora_atual = datetime.now().strftime('%H:%M:%S')
            if self.numero_saques < self.limite_saques:
                saque = float(input('Quanto você deseja sacar? '))
                if saque > 0:
                    if saque <= self.limite:
                        if float(saque) <= self.saldo:
                            self.saldo -= saque
                            self.numero_saques += 1
                            self.extrato_atual.append(f'{hora_atual}: Saque de R${saque:.2f} realizado.')
                            extrato_saque = input(f'''
===============================COMPROVANTE================================            
            {data} - Autoatendimento - {hora_atual}
    
Cliente: nome    
    
Saque de R${saque:.2f} realizado com sucesso!
Seu novo saldo é: R${self.saldo:.2f}
    
Para voltar ao menu principal aperte:  [ENTER] ou digite qualquer coisa.
Para finalizar operação digite:         [0]
==========================================================================
Digite aqui: ''')
                            if extrato_saque != '0' or quit('''
==========================================      
Operação finalizada. Até mais!              
=========================================='''): return
                        else:
                            print('Saldo insuficiente.')
                            t += 1
                    else:
                        print(f'Você só pode sacar no máximo R${self.limite}.')
                        t += 1
                else:
                    print('Digite um valor válido para saque')
                    t += 1
            else:
                print('Você atingiu o valor máximo de saques por dia. Tente novamente amanhã.')
                return
        else:
            print('Limite máximo de tentativas excedido. Por favor tente novamente mais tarde.')

    def depositar(self):
        from datetime import datetime
        while True:
            data = datetime.now().strftime('%d/%m/%Y')
            hora_atual = datetime.now().strftime('%H:%M:%S')
            deposito = float(input('Quanto você deseja depositar? '))
            if float(deposito) > 0:
                self.saldo += deposito
                self.extrato_atual.append(f'{hora_atual}: Depósito de R${deposito:.2f} realizado.')
                extrato_deposito = input(f'''
===============================COMPROVANTE================================
            {data} - Autoatendimento - {hora_atual}
    
Cliente: nome
    
Depósito de R${deposito:.2f} realizado com sucesso!
Seu novo saldo é: R${self.saldo:.2f}
    
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

    def exibir_extrato(self):
        from datetime import datetime
        data = datetime.now().strftime('%d/%m/%Y')
        hora_atual = datetime.now().strftime('%H:%M:%S')
        print(f'''
===============================EXTRATO===================================
            {data} - Autoatendimento - {hora_atual}
    
Cliente: nome                    
''')
        self.extrato_atual or print('Não há operações a serem mostradas.')
        print('\n'.join(self.extrato_atual))
        print(f'''Saldo disponível: R${self.saldo:.2f}''')
        extrato = input(f'''
Para voltar ao menu principal aperte:   [ENTER] ou digite qualquer coisa.
Para finalizar operação digite:          [0]
==========================================================================
Digite aqui: ''')
        if extrato != '0' or quit('''
==========================================
Operação finalizada. Até mais!
=========================================='''): return
        
    def sair(self):
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


conta = Conta()
conta.menu()
