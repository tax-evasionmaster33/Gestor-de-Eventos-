#Restricciones
from typing import Dict, List


Personal_Autorizado:Dict[str, List[str]] = {
    "España": ["Zahili", "Yuli"],
    "EEUU": ["Yanara"],
    "Canadá": ["Betsy"],
    "Brasil": ["Dania"],
    "Turkia": ["Dania"],
}

CO_Requisitos:Dict[str, List[str]] = {
    "España": ["Planilla", "Laptop", "Escaner"],
    "EEUU": ["Planilla", "Laptop"],
    "Canadá": ["Planilla", "Laptop", "Escaner"],
    "Brasil": ["Planilla", "Laptop", "Escaner"],
    "Turquía": ["Planilla", "Laptop", "Escaner"]
}

Duracion_Min:Dict[str, Dict[str, int]] = {
    "España": {
        "lmd": 50,
        "visado": 30,
        "legalización": 30,
        "transcripción de matrimonio": 40,
        "asesoría": 20,
        "cita de pasaporte": 20
    },
    "EEUU": {
        "visa turismo": 50,
        "visa trabajo": 50,
        "asesoría": 20
    },
    "Canadá": {
        "visa turismo": 80,
        "asesoría": 30
    },
    "Brasil": {
        "visa turismo": 80,
        "asesoría": 30
    },
    "Turkia": {
        "visa turismo": 45,
        "asesoría": 20
    }
}






