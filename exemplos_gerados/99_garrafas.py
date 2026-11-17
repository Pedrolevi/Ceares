garrafas = 99
while garrafas > 0 :
    if garrafas > 1 :
        print(garrafas, "garrafas de cerveja no muro,", garrafas, "garrafas de cerveja.")
        garrafas -= 1
        if garrafas > 1 :
            print("Pega uma e passa ao redor,", garrafas, "garrafas de cerveja no muro.")
        else:
            print("Pega uma e passa ao redor, 1 garrafa de cerveja no muro.")
    else:
        print("1 garrafa de cerveja no muro, 1 garrafa de cerveja.")
        garrafas -= 1
        print("Pega uma e passa ao redor, nenhuma garrafa de cerveja no muro.")
    print("")
print("Nenhuma garrafa de cerveja no muro, nenhuma garrafa de cerveja.")
print("Vá na bodega, compre mais uma ruma e acunhe tudo de novo!")
