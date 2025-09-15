import dash_mantine_components as dmc
from components.badges import badge_nadac, badge_sdud, badge_analytics
from config import HEADER_TITLE
from ui.header import header
from ui.controls import map_controls, line_chart_controls
from ui.chart import chart
from ui.footer import footer
from ui.help import help_section

layout = dmc.Container(
    [
        header(HEADER_TITLE, [badge_nadac(), badge_sdud()]),
        help_section(),
        map_controls(),
        chart(title="U.S. State Heat Map — Payment per Unit vs NADAC", id="map", chart_title_id="map-title"),
        line_chart_controls(),
        chart(title='', id="line-chart", chart_title_id="line-chart-title"),
        footer(HEADER_TITLE, [badge_nadac(), badge_sdud(), badge_analytics()]),
    ],
    maw="1000px"
)
    
