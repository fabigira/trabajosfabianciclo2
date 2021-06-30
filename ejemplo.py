def cuota_mensual(salario:int, informacion:dict) -> str:
    if informacion['estrato'] <= 3:
        valorcasa = 100000000 - 1000000
    else:
        valorcasa = 100000000
    
    if salario < 1150000:
        cuota = (valorcasa * 0.1) / 12
        return f"La cuota mensual de {informacion['nombre']} será de {cuota}"

    elif salario > 1150000 and salario < 1850000:
        cuota = (valorcasa * 0.2) / 12
        return f"La cuota mensual de {informacion['nombre']} será de {cuota}"  

     
    elif salario > 1850000 and salario < 3500000:
            cuota = (valorcasa * 0.3) / 12
            return f"La cuota mensual de {informacion['nombre']} será de {cuota}"

    elif  salario > 3500000:
            cuota = (valorcasa * 0.45) / 12
            return f"La cuota mensual de {informacion['nombre']} será de {cuota}"

  
print(cuota_mensual(900000, {'nombre': "David", 'estrato': 3} ))
print(cuota_mensual(900000, {'nombre': "Nelson", 'estrato': 6} )) 







