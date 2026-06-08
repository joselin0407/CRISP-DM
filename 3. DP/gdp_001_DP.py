# gdp_001_DP.py - Script de preparación de datos de prueba
import pandas as pd
from sklearn.preprocessing import StandardScaler

print("Iniciando la fase de Data Preparation para el proyecto GDP_001...")

# Carga de datos de ejemplo
df = pd.read_csv("raw_data/calibration_factors.csv")

# Imputación de valores nulos
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())

# Escalamiento estándar de variables de presión
scaler = StandardScaler()
df['pressure_scaled'] = scaler.fit_transform(df[['pressure']])

print("Preparación de datos completada exitosamente con Pandas y Scikit-Learn.")
