valor = float(input())

n_achou = True
resposta = ''

if(valor < 0 or valor > 100):
    resposta += 'Fora de intervalo'
    n_achou = False
    
if(valor <= 25.00 and n_achou):
    resposta += 'Intervalo [0,25]'
    n_achou = False

if(valor <= 50.0 and n_achou):
    resposta += 'Intervalo (25,50]'
    n_achou = False
    
if(valor <=75.0 and n_achou):
    resposta += 'Intervalo (50,75]'
    n_achou = False

if(valor <=100.0 and n_achou):
    resposta += 'Intervalo (75,100]'
    n_achou = False

print(resposta)

1038
valores = input().split()
codigo, qte = valores

qte = int(qte)

tab_preco = {"1":4.0, "2":4.5,"3":5.0,"4":2.0,"5":1.5}

resultado = qte * tab_preco[codigo]

print('Total: R$ %.2f' %resultado)

