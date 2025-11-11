import streamlit as st
import pandas as pd
import plotly.express as px

# Datos simulados
data = {
    "categoria": ["A", "A", "B", "B"],
    "producto": ["Producto1", "Producto2", "Producto3", "Producto4"],
    "ventas": [100, 150, 200, 250]
}
df = pd.DataFrame(data)

# Título
st.title("Cuadro de mando interactivo")

# Filtro
opcion = st.selectbox("Selecciona categoría", df["categoria"].unique())

# Filtrar datos
df_filtrado = df[df["categoria"] == opcion]

# Gráfico
fig = px.bar(df_filtrado, x="producto", y="ventas", title="Ventas por producto")
st.plotly_chart(fig)