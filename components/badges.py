import dash_mantine_components as dmc
from dash_iconify import DashIconify

def badge_nadac():
    return dmc.Badge(
        [DashIconify(icon="tabler:database", width=12), "NADAC"],
        variant="dot",
        color="blue",
        size="xs"
    )

def badge_analytics():
    return dmc.Badge(
        [DashIconify(icon="tabler:chart-line", width=12), "Analytics"],
        variant="dot",
        color="green",
        size="xs"
                        )

def badge_sdud():
    return dmc.Badge(
        [DashIconify(icon="tabler:cloud", width=12), "SDUD"],
        variant="dot",
        color="teal",
        size="xs"
    )