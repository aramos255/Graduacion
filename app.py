import streamlit as st
import joblib
import numpy as np

# Título de la aplicación
st.title("Predictor de Éxito Académico")

# Autor
st.subheader("Autor: Adriana Ramos Vilchis")

# Imagen debajo del autor
st.image("https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg")

# Introducción de cómo usar la aplicación
st.write("""
    Bienvenido al Predictor de Éxito Académico. Esta aplicación utiliza un modelo entrenado para predecir si una estudiante va a graduarse con éxito en la universidad. 
    Simplemente ajusta los deslizadores para introducir las notas de "Nota IA" y "GPA" en un rango de 0 a 1, y obtendrás la predicción si la estudiante se graduará o no.
""")

# Cargar el modelo entrenado
model = joblib.load("primermillon.joblib")

# Deslizadores para ingresar los valores de las variables "Nota IA" y "GPA"
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, step=0.1)

# Realizar la predicción
input_data = np.array([[nota_ia, gpa]])
prediction = model.predict(input_data)

# Mostrar el resultado con el emoticono y el color según la predicción
if prediction == 0:
    st.markdown('<h2 style="color:red;">❌ No se graduará</h2>', unsafe_allow_html=True)
else:
    st.markdown('<h2 style="color:green;">🎉 Felicitaciones, te vas a graduar</h2>', unsafe_allow_html=True)

# Pie de página
st.write("© 2025 UNAB")


