# Jogo da Velha - Versão com Práticas duvidosas
# Autor: Programador que gosta de complicar as coisas

a1 = []
a2 = "X"
a3 = False
a4 = None
a5 = 0
a6 = []
a7 = []
a8 = []
a9 = []
a10 = None
a11 = None
a12 = None


def b1():
    global a1, a2, a3, a4, a5
    global a6, a7, a8
    global a9, a10, a11, a12
    
    a1 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    a2 = "X"
    a3 = False
    a4 = None
    a5 = 0
    a6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a7 = []
    a8 = []
    a9 = []
    a10 = None
    a11 = None
    a12 = None


def b2():
    global a1
    print("\n" + "=" * 20)
    print("       JOGO DA VELHA")
    print("=" * 20)
    print("       1   2   3")
    print("      -----------")
    for c1 in range(3):
        print(f"    {c1+1} | {a1[c1][0]} | {a1[c1][1]} | {a1[c1][2]} |")
        if c1 < 2:
            print("      -----------")
    print("      -----------")
    print()


def b3(c2, c3):
    global a1
    if a1[c2][c3] == " ":
        return True
    else:
        return False


def b4():
    global a1, a6, a7
    a6 = []
    a7 = []
    
    for c1 in range(3):
        for c4 in range(3):
            c5 = c1 * 3 + c4 + 1
            if a1[c1][c4] == " ":
                a6.append(c5)
            else:
                a7.append(c5)


def b6(c5):
    c2 = (c5 - 1) // 3
    c3 = (c5 - 1) % 3
    return c2, c3


def b7():
    global a2, a3, a4, a5
    global a8, a6
    
    print(f"Vez do jogador: {a2}")
    print(f"Posições disponíveis: {a6}")
    
    try:
        c5 = int(input("Escolha uma posição (1-9): "))
        
        if c5 < 1 or c5 > 9:
            print("Posição inválida! Escolha entre 1 e 9.")
            return False
        
        if c5 not in a6:
            print("Posição já ocupada! Escolha outra.")
            return False
        
        c2, c3 = b6(c5)
        
        a1[c2][c3] = a2
        a5 += 1
        a8.append((a2, c5))
        
        b4()
        
        return True
        
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return False


def b8(c2):
    global a1
    if a1[c2][0] == a1[c2][1] == a1[c2][2] and a1[c2][0] != " ":
        return True
    return False


def b9(c3):
    global a1
    if a1[0][c3] == a1[1][c3] == a1[2][c3] and a1[0][c3] != " ":
        return True
    return False


def b10():
    global a1
    if a1[0][0] == a1[1][1] == a1[2][2] and a1[0][0] != " ":
        return True
    return False


def b11():
    global a1
    if a1[0][2] == a1[1][1] == a1[2][0] and a1[0][2] != " ":
        return True
    return False


def b12():
    global a1, a4, a10, a11, a12
    
    for c1 in range(3):
        if b8(c1):
            a4 = a1[c1][0]
            a10 = c1
            return True
    
    for c4 in range(3):
        if b9(c4):
            a4 = a1[0][c4]
            a11 = c4
            return True
    
    if b10():
        a4 = a1[0][0]
        a12 = "principal"
        return True
    
    if b11():
        a4 = a1[0][2]
        a12 = "secundaria"
        return True
    
    return False


def b13():
    global a5
    if a5 == 9 and a4 is None:
        return True
    return False


def b14():
    global a2
    if a2 == "X":
        a2 = "O"
    else:
        a2 = "X"


def b15():
    global a4, a3
    
    print("\n" + "=" * 30)
    if a4 is not None:
        print(f"    JOGADOR {a4} VENCEU!")
    else:
        print("    DEU VELHA! EMPATE!")
    print("=" * 30)
    
    print("\nHistórico de jogadas:")
    for c6 in a8:
        print(f"  Jogador {c6[0]} na posição {c6[1]}")


def b16():
    global a3, a4, a5, a8
    global a10, a11, a12
    
    a3 = False
    a4 = None
    a5 = 0
    a8 = []
    a10 = None
    a11 = None
    a12 = None
    
    b1()


def b17():
    c7 = input("\nDeseja jogar novamente? (s/n): ").lower()
    return c7 == "s" or c7 == "sim"


def b18():
    global a1, a9
    a9 = []
    for c1 in range(3):
        for c4 in range(3):
            a9.append(a1[c1][c4])


def b19():
    global a3, a4
    
    if b12():
        a3 = True
        return True
    
    if b13():
        a3 = True
        a4 = None
        return True
    
    return False


def b20():
    global a2
    
    b2()
    b4()
    
    if not b7():
        return False
    
    b18()
    
    if b19():
        b2()
        b15()
        return True
    
    b14()
    return False


def main():
    global a3
    
    print("Bem-vindo ao JOGO DA VELHA!")
    print("As posições são numeradas de 1 a 9:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    b1()
    
    while not a3:
        b20()
    
    if b17():
        b16()
        main()
    else:
        print("\nObrigado por jogar! Até a próxima!")


if __name__ == "__main__":
    main()