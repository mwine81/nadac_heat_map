import dash_mantine_components as dmc
from dash import dcc
from components.section_container import section_container
from config import PRIMARY_COLOR

def chart(title:str, id: str):
    return section_container(
        [
            dmc.Title(title, order=2, c=PRIMARY_COLOR), # type: ignore
            dcc.Graph(figure={}, id=id),
        ]
    )