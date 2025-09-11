import dash_mantine_components as dmc
from components.badges import badge_nadac, badge_sdud, badge_analytics
from config import HEADER_TITLE
from ui.header import header
from ui.controls import controls
from ui.chart import chart
from ui.footer import footer
from ui.help import help_section

layout = dmc.Container(
    [
        header(HEADER_TITLE, [badge_nadac(), badge_sdud()]),
        help_section(),
        controls(),
        chart(title="U.S. State Heat Map — Payment per Unit vs NADAC", id="map"),
        chart(title="NADAC vs SDUD — Unit Price and Payment per Unit (Time Series)", id="line-chart"),
        footer(HEADER_TITLE, [badge_nadac(), badge_sdud(), badge_analytics()]),
    ],
    maw="1000px"
)
    
