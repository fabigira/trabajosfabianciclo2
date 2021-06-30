def auxilios(info:dict) -> str:

    numero_auxilios = info['numero_auxilios'] * 50000
    ayuda_govierno = 100000

    if info['edades_hijos'][0] < 18:
        ayuda_govierno = numero_auxilios + 100000
        return True

    return f"El valor del subsidio de {info['nombre']} es {ayuda_govierno}"

edades_hijos = [5,1,20,21]    
filter (auxilios, edades_hijos)
list(filter(auxilios, edades_hijos))
        


print(auxilios({"nombre": "david", 
    "numero_auxilios": 10, "edades_hijos": [5,1,20,21]}))



