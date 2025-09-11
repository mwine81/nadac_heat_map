import dash_mantine_components as dmc
from components.badges import badge_nadac, badge_sdud, badge_analytics
from config import HEADER_TITLE
from ui.header import header
from ui.controls import controls
from ui.chart import chart
from ui.footer import footer


layout = dmc.Container(
    [
    header(HEADER_TITLE, [badge_nadac(), badge_sdud()]),
    # help_section(),
    controls(),
    chart(title = 'US - States' ,id = 'map'),
    chart(title= "NADAC to Pay Per Unit", id='line-chart'),
    footer(HEADER_TITLE, [badge_nadac(), badge_sdud(), badge_analytics()]),
    ],
    maw='1000px'

)
    
