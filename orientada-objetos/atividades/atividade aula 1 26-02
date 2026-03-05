def salario(sal):
    novo = 0
    aum = 0

    if sal <= 280:
        per = 0.2
    elif sal<=700:
        per = 0.15
    elif sal <=1500:
        per = 0.1
    else:
        per = 0.05

    novo = (per+1)*sal
    aum = per*sal

    print(f'o salário antes do reajuste;: R${sal}')
    print(f'o percentual de aumento aplicado; {per*100}%')
    print(f'o valor do aumento; R${aum}')
    print(f'o novo salário, após o aumento. R${novo}')

def fatorial(num):
    fat = 1
    while num > 1:
        fat = fat * num
        num = num -1
    return fat

def cubo(m):
    for n in range(1, m+1):
        primeira = n*n - n + 1
        impares = []
        for i in range(primeira, primeira + 2*n, 2):
            impares.append(i)
        print(f"n={n}, n³={n**3}, ímpares consecutivos: {impares}, soma: {sum(impares)}")

cubo(5)
