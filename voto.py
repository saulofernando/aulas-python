
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
candidato = int(input('''CANDIDATO: 1 - PAULO FREIRE
CANDIDATO: 2 - JEAN PIAGET'''))          
voto = int(input(''''digite seu voto: 10 - Paulo Freire
20 - Jean Piaget'''))
if voto == 10:
    print("Paulo Freire")
    print("candidato a presidente")

if voto == 20:
    print("Jean Piaget")
    print("candidato a presidente")

    
    