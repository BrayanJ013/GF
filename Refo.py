def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def laberB(lab, res, f, c, vidas):
    if f == 0 and c == 0:
        if valido(lab, res, f, c):
            
            res[f][c] = 1
            
            imprime(res)
            return True
        else:
            return False
    else:
        if valido(lab, res, f, c):
            if lab [f][c] < 0:
                vidas += lab[f][c]
            res[f][c] = 1
            print("Vidas: ",vidas)
            imprime(res)
            if vidas > 0 and laberB(lab, res, f+1, c, vidas):
                return True
            elif vidas > 0 and laberB(lab, res, f, c+1, vidas):
                return True
            elif vidas > 0 and laberB(lab, res, f-1, c, vidas):
                return True
            elif vidas > 0 and laberB(lab, res, f, c-1, vidas):
                return True
            else:
                vidas -= lab[f][c]
                res[f][c] = 0
                return False
        else:
            return False

lab = [
    [1,1,1,1,0,1,1,1,1],
    [-2,0,0,-1,0,1,0,1,0],
    [1,1,0,1,1,1,0,1,0],
    [0,1,0,-1,0,0,0,-1,0],
    [1,1,1,1,1,1,1,1,0],
    [-1,0,0,0,0,0,0,1,1],
    [1,1,1,1,-1,1,1,1,0],
    [1,0,0,1,0,1,0,1,0],
    [1,1,-1,1,1,1,0,1,1]
]
res = [[0 for _ in range(9)] for _ in range(9)]
print("LABERINTO ORIGINAL")
imprime(lab)
print("RECORRIDO DEL RATON")
if laberB(lab, res, 8, 0, 3):
    print("Salimos!")
    print("CAMINO PARA SALIR:")
    imprime(res)
else:
    print("Quedamos atrapados")
    print("NO EXISTE UN CAMINO VIABLE:")
    imprime(res)