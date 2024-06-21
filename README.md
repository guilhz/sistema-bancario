# 💲 Sistema Bancário

## O projeto
O projeto se trata de um sistema bancário básico onde o usuário deve poder realizar depósitos, saques e visualizar seu extrato.
- Depósito: O usuário pode realizar depósitos de qualquer valor.
- Saque: O usuário pode realizar saques de no máximo R$500,00 e poderá realizar no máximo 3 operações de saques por dia.
- Extrato: O usuário pode visualizar seu extrato contendo todas as operações feitas de depósito e saque.

```pyx
=======================MENU=============================
                                Saldo: R${saldo:.2f}
Olá, {usuario}
Para prosseguir, por favor digite uma opção:
        
Para sacar digite:                          [1]
Para depositar digite:                      [2]
Para visualizar o extrato digite:           [3] 
Para sair digite:                           [0]  
========================================================
```

Principais variáveis que foram utilizadas no projeto:
```pyx
saldo = 0
extrato_atual = []
numero_saques = 0
limite = 500
limite_saques = 3
```

Biblioteca utilizada no projeto para o registro dos comprovantes e extratos:
```pyx
from datetime import datetime
```
```pyx
data = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M:%S')
```

## Usuário
Como ponto inicial, antes do usuário ir para o menu é necessário que ele insira um nome. Esse nome será utilizado para o menu, comprovantes e extratos que serão gerados ao decorrer do sistema.
```pyx
usuario = str(input('Caro usuário, por favor digite seu nome: ')).title()  # Pergunta para o usuário o seu nome
```
O .title() fará com que o nome comece em letra maiúscula como deve ser.
A parte do nome de usuário não é obrigatória, podendo o usuário apenas apertar ENTER ou digitar qualquer coisa e prosseguir. Apenas uma formalidade para ficar mais realista o sistema.

## Menu
O menu foi feito para ser "próprio" para cada tipo de usuário, tendo o menu como se fosse uma conta bancária mesmo do usuário, com o nome e as opções para que o mesmo possa realizar as operações básicas de um sistema bancário.
Para criar o menu foi necessário criar uma variável chamada menu e foi utilizado f-string para chamar as variáveis de saldo para informar o saldo atual do usuário, e a variável usuário para citar o nome do mesmo. Para o menu ficar ativo foi utilizado a estrutura de repetição while:
```pyx
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
```
Em casos do usuário digitar algo além de 0,1,2 ou 3 - foi colocado uma condicional if not in, para caso o usuário digitar qualquer outra coisa sem ser 0,1,2 ou 3 apresente uma mensagem de erro.

Dentro do while foi colocado as variáveis data e hora_atual, utilizando a biblioteca datetime, para que a cada operação de saque ou depósito registre o momento em que o usuário realizou tais operações e registre no extrato. Além de também ser registrado nos comprovantes de saque e depósito em que o usuário realiza.

## Opção de Saque
O saque foi feito com base em características "reais", tendo uma função para caso o usuário faça 3 tentativas de operações incorretas(erro), o usuário é levado de volta para o menu. Além disso o usuário só poderá sacar no máximo R$500,00 e fazendo isso apenas 3x por "dia".

```pyx
t = 0
        while t < 3:  # While para que faça com que o usuário tenha no máximo 3 tentativas em caso de erro.
```

```pyx
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
```

Ao realizar um saque com sucesso, é gerado um comprovante da operação e é registrado na variável extrato_atual para exibir na opção extrato pelo menu:
```pyx
extrato_atual.append(f'{hora_atual}: Saque de R${saque:.2f} realizado.')
```

Ao gerar o comprovante é perguntado ao usuário se ele deseja encerrar a operação ou voltar ao menu para realizar outras operações:
```pyx
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
```


## Opção de Depósito
A opção de depósito não há limitações, podendo o cliente realizar depósitos de qualquer valor.
```pyx
elif opcao == '2':
        while True:
            deposito = float(input('Quanto você deseja depositar? '))
            if float(deposito) > 0:
                saldo += deposito
                extrato_atual.append(f'{hora_atual}: Depósito de R${saldo:.2f} realizado.')
```
Com depósito realizado,é gerado um comprovante:
```pyx
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
```


## Opção de Extrato
Quando o usuário realizar operações poderá visualizar o seu extrato selecionando a opção 3 do menu:
```pyx
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
```
Caso o usuário não tenha operações a serem mostradas, é gerado um extrato porém citando a informação que não há operações a serem mostradas:
```pyx
extrato_atual or print('Não há operações a serem mostradas.')
```



## Autor

#### Guilherme Leite

- Visualize o meu: <a href="https://www.linkedin.com/in/guilherme-leite10/" title="Linked-in" target="_blank">Linked-in</a>
