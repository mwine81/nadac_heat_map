import dash_mantine_components as dmc

def section_container(items: list):
    return dmc.Paper(
        items,
        p="md", shadow="sm", withBorder=True, style={"margin": "20px"}
    )