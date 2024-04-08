#bissexto.py 

ano = int(input("digite um ano:"))

if ano % 4 == 0 or ano % 400 == 0:
    print(f"{ano} eh um ano bissexto")
else:
    print(f"{ano} nao eh um ano bissexto")