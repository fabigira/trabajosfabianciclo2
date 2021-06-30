def desperdicio_de_gaseosa(amigo1:dict, amigo2:dict, amigo3:dict, capacidad_boton:float)->str:
    if amigo1["capacidad_actual"]+capacidad_boton >= amigo1["capacidad_vaso"]:
        return amigo1["nombre"]
    elif amigo2["capacidad_actual"]+capacidad_boton >= amigo2["capacidad_vaso"]:
        return amigo2["nombre"]
    elif amigo3["capacidad_actual"]+capacidad_boton >= amigo3["capacidad_vaso"]:
        return amigo3["nombre"]
    else:
        return None 


amigo1 = {"nombre": "joshua", "capacidad_vaso": 90, "capacidad_actual": 30}
amigo2 = {"nombre": "manuela", "capacidad_vaso": 75, "capacidad_actual": 20}
amigo3 = {"nombre": "edwin", "capacidad_vaso": 30, "capacidad_actual": 25}
capacidad_boton = 40
print(desperdicio_de_gaseosa(amigo1, amigo2, amigo3, capacidad_boton))


