def inventario(marca:str, precio_por_unidad:int, numero_de_unidades:int ) -> str:
    return f"La Tablet de marca {marca},  y el costo fue {precio_por_unidad * numero_de_unidades}"

def tablet():
    marca = (input("ingrese la marca"))
    precio_por_unidad = int(input("ingrese precio por unidad"))
    numero_de_unidades = int(input("ingrese el numero de unidades"))
    return inventario(marca, precio_por_unidad, numero_de_unidades)

print(tablet())

    





    




    










   







