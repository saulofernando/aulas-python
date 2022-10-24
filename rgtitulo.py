documento = int(input('''digite seu tipo de documento:
    1 - para rg
    2 - para titulo de eleitor
    '''))                 
if documento == 1:
    rg = int(input("digite seu rg: "))
    if rg == 11122233344:
        print("joão do carmo: ")
        print("pode votar: ")
    else:
        print("nõo encontrado: ")

if documento == 2:
    titulo = int(input("digite seu titulo: "))
    if titulo == 12345678:
        print("joão do carmo: ")
        print("pode votar: ")
    else:
        print("nõo encontrado: ")
