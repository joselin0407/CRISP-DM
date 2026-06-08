# gdp_001_DEPL.py - Exportación de modelos para producción
import pickle

print("Iniciando la fase de Despliegue para el proyecto GDP_001...")

# Simulación de guardado del modelo en disco para simular producción
modelo_entrenado = "XGBoostRegressorModel"
with open("gdp_001_model_final.pkl", "wb") as f:
    pickle.dump(modelo_entrenado, f)

print("Modelo exportado en formato .pkl de forma exitosa en el directorio.")
