from datetime import datetime, time ,timedelta

from Data import Recursos,Persistencia_de_Citas
#Esto de typing es pa q sea mas bonito el codigo en plan mas legible
from typing import List,Optional.Tuple
#

from Restricciones import PERSONAL_AUTORIZADO,DURACION_MIN,CO_REQUISITOS


#Definir los limites de los dias laborales
#Y definir los horarios Diarios
Rango_Semana = range(0,5) 
Horarios_Laborables=[
    (time(hour=9,minute=00),time(hour=12,minute=30)),
    (time(hour=13,minute=00),time(hour=16,minute=30)),
]



class Gestor:
    def __init__(self,recursos: List[Recursos],eventos:List[Eventos]) :
        pass    
    