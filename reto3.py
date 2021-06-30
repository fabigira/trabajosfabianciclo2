def calculo_notas(listanotas:list, asistencias:int,) -> dict:

    listanotas = sum(listanotas) / 5

    if asistencias > 5 :
        return {'nota': listanotas}
   
    if asistencias <= 5:
        listanotas = 0
        return {'nota':listanotas}

asistencias = int()
print(calculo_notas([2,5,4,5,3],2))