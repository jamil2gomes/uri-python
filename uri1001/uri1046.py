valores = input().split()
valores = list(map(int,valores))

ini, fim = valores

if ini == fim:
    print("O JOGO DUROU 24 HORA(S)")
elif ini > fim:
    duracao = (24 - ini) + fim
    print("O JOGO DUROU {:d} HORA(S)".format(duracao))
elif ini < fim:
    duracao = fim - ini
    print("O JOGO DUROU {:d} HORA(S)".format(duracao))
