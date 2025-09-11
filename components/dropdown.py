import dash_mantine_components as dmc

def dropdown(label: str, options: list[str]):
    return dmc.Select(
        label=label,
        data=options,
    )