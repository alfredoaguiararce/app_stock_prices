"""
Hecho por Alfredo Aguiar Arce. 25-febrero-2021.
Un proyecto hecho para probar la plataforma/libreria streamlit.
"""

#Importamos las librerias necesarias.
import yfinance as yf
import streamlit as st
import datetime

#opciones de datos para graficar.
opciones = ['Open', 'Close','High','Low', 'Volume']


#Markdown ... Comentarios para explicar los datos.
st.write("""
# Aplicación para ver las acciones de Google.

Se muestran las acciones de Google. con ayuda de la libreria **yfinance** de Python, que no es mas que la informacion recopilada por **Yahoo! Finance**.
El proposito de esta aplicacion es mostrar los datos de un dataset de forma que se pueda interactuar con el, haciendo uso ademas del uso de la libraria **StreamLit**.

*   [Mas sobre StreamLit.](https://www.streamlit.io/)
*   [Mas sobre yfinance.](https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75)

### A continuacion, se muestra como esta estructurada la informacion del dataset.

Pero primero selecciona la fecha inicial y fecha final, esto representa el intervalo durante el cual se tomaron los datos que deseas graficar.

""")

#Definir el símbolo de cotización
simbolo_cotizacion = 'GOOGL'  #simbolo de Google.
#Obtener la data de esta cotizacion.
data_cotizacion = yf.Ticker(simbolo_cotizacion)
#Obtener el historial de datos de la cotiacion.
fecha_inicio = st.date_input("Selecciona la fecha inicial:  ", datetime.date(2010, 1, 1))
fecha_final = st.date_input("Selecciona la fecha final:  ", datetime.date(2020, 5, 31))
dataframe_cotizacion = data_cotizacion.history(period='1d',  start=fecha_inicio, end=fecha_final)


st.write("""Se muestran los primeros 5 elementos de los datos a graficar y como se encuntran estructurados.""")
#Imprimir los primeros 5 elementos del dataset.
st.table(dataframe_cotizacion.head())

st.write("""
### Entre las variables que se pueden ver en el data set estan:

*   **Open :** El precio de la accion al inicio del dia,mes,año.
*   **Close : ** El precio de la accion al final del dia,mes,año.
*   **High : ** El precio mas alto de la accion ese dia,mes,año.
*   **Low : ** El precio mas bajo de la accion ese dia,mes,año.
*   **Volume :** Cuántas acciones se negociaron ese dia,mes,año.

""")

#Iniciamos el menu de opciones para la grafica.
opcion = st.selectbox('Selecciona la variable que deseas graficar.',opciones)
#Titulo de la grafica
st.write(f""" ### Grafica de la variable '{opcion}' '""")
#Configuramos la grafica en base a la opcion elegida.
st.line_chart(dataframe_cotizacion.get(opcion))

st.write("""
#### Hecho por Alfredo Aguiar Arce , mis redes son :

*   [Github.](https://github.com/alfredoaguiararce)
*   [LinkedIn.](https://www.linkedin.com/in/alfredoaguiararce/)

""")


