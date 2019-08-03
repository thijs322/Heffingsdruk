import plotly
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json

def create_plot(N):
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON




def make_sankey(data):
    data['consumptie'] = data['BTW laag'] + data['BTW hoog']
    data['vervoer'] = data['Motorrijtuigen'] + data['Accijns op brandstof']
    data['wonen'] = data['Afvalstoffenheffing'] + data['Rioolheffing'] + data['OZB (Indirect)']
    data['inkomen'] = data['Premie volksverzekeringen'] + data['Vermogensbelasting'] + data['Belasting op bonussen en vakantiegeld'] + data['Inkomensbelasting - kortingen']
    data['totaal'] = data['inkomen'] + data['wonen'] + data['vervoer'] + data['consumptie']

    for key, value in data.items():
        data[key] = round(value)

    values = list(data.values())[::-1]
    labels = list(data.keys())[::-1]

    # Heeeeeey Thijs, daar zijn we dan. 'Even' de grah aanpassen. 
    # Pak maar een peukie en biertje. Hieronder staat een wiskundig probleem
    # waar jij je de komende 2,5u op blind gaat staren. 
    # Succes!
    arrows = [(0, 1), (0, 2), (0, 3), (0, 4),
            (1, 5), (1, 6), (1, 14), (1, 15),
            (2, 7), (2, 8), (2, 9),
            (3, 11), (3, 12),
            (4, 10), (4, 13)]

    sources = list()
    targets = list()
    for arrow in arrows:
        sources.append(arrow[0])
        targets.append(arrow[1])

    fig = [go.Sankey(
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "red", width = 1),
        label = labels,
        color = "red"
        ),
        link = dict(
        source = sources, # indices correspond to labels, eg A1, A2, A2, B1, ...
        target = targets,
        value = values
    ))]

    # fig.update_layout(
    #     title="Kankerveel belasting",
    #     font=dict(size = 20, color = 'white'),
    #     plot_bgcolor='black',
    #     paper_bgcolor='black'
    # )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # print(graphJSON)

    return graphJSON
