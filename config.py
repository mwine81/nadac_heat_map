from pathlib import Path
from typing import Any

UPDATE_DATE = "October 2025"

PRIMARY_COLOR = '#1a365d'
SECONDARY_COLOR = '#2c5282'      
ACCENT_COLOR = '#ed8936'         
ACCENT_DARK = '#dd7324'          
BACKGROUND_PRIMARY = '#f8fafc'   
BACKGROUND_SECONDARY = '#ffffff'  
BACKGROUND_CARD = '#ffffff'      
TEXT_PRIMARY = '#1a202c'         
TEXT_SECONDARY = '#4a5568'       
TEXT_MUTED = '#718096'           
BORDER_COLOR = '#e2e8f0'

BASE_DATA = Path("data/heat_map.parquet")

HEADER_TITLE = "NADAC Heat Map Dashboard"
METRICS = ['payment_per_unit','markup_per_unit','markup_percentile','payment_per_unit_percentile']
METRIC_DROPDOWN_LABELS = [x.replace('_', ' ').title() for x in METRICS]

THEME: Any = {
    # Custom brand scale (light -> dark) anchored on our PRIMARY_COLOR (#1a365d)
    "colors": {
        "brand": [
            "#e9eff7",
            "#d7e3f0",
            "#c3d6ea",
            "#a9c4df",
            "#8bb0d3",
            "#6b96c3",
            "#4f80b5",
            "#3c6da7",
            "#2b5b93",
            "#1a365d",
        ]
    },
    "primaryColor": "brand",
    "fontFamily": "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
    "headings": {
        "fontFamily": "Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
        "sizes": {
            "h1": {"fontSize": "28px", "fontWeight": 700},
            "h2": {"fontSize": "22px", "fontWeight": 700},
            "h3": {"fontSize": "18px", "fontWeight": 700},
        },
    },
    "defaultRadius": "md",
}