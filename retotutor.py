def compraempanadas(precios:dict, tipopersona:str, numerounidades:int) -> str:
    precios = {"estudiante": 700, "profesor": 850, "otro": 1000}
    tipopersona = ("estudiante", "profesor", "otro")
    numerounidades = int(5)

    if precios == 700:
        tipopersona("estudiantes") = precios[0] + numerounidades
    return f"debe pagar en total {tipopersona('estudiante')}"

print(compraempanadas())