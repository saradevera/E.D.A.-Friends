import pandas as pd
import numpy as np
import variables as v
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go


def filtro_a_df(df, columna, personaje, orden):
    nuevodf = df[df[columna]==personaje].value_counts()
    nuevodf=pd.DataFrame(nuevodf).sort_values(by=orden)
    nuevodf.reset_index(inplace=True)
    return nuevodf

def grafico_goscatter(df, columna, personaje, color, columna_texto):
    trace = go.Scatter(
                x = df[columna],
                y = df[0],
                name = personaje,
                mode= 'lines',
                marker = dict(color = color),
                texttemplate="simple_white",
                text = df[columna_texto])
    return trace

