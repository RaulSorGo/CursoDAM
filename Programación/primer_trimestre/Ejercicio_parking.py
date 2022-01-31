   # 1. Calcular las semanas
    # 2. Calcular los días restantes
    # 3. Coste por semanas
    # 4. Coste por días
    # 5. Cálculo del total

from Constantes_parking import DIAS_SEMANA, PRECIO_DIA, PRECIO_SEMANA

def calcular_coste(dias):
    semanas = dias // DIAS_SEMANA
    dias_restantes = dias % DIAS_SEMANA
    coste_semanal = semanas*PRECIO_SEMANA
    coste_dias = dias_restantes*PRECIO_DIA
    total = coste_semanal+coste_dias

    return total

print(calcular_coste(1))

  

