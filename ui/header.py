import dash_mantine_components as dmc
from config import PRIMARY_COLOR, TEXT_MUTED
from components.section_container import section_container
from components.badges import badge_nadac
from components.social_media import social_media_icons
from config import HEADER_TITLE

def header(title: str, badges: list):
    """App header with branding on the left and quick actions on the right."""
    brand = dmc.Group(
        align="center",
        gap="sm",
        children=[
            dmc.Box(dmc.Image(src="/assets/logo.png", h=36, alt="46brooklyn logo")),
            dmc.Stack(
                gap=0,
                children=[
                    dmc.Title(HEADER_TITLE, order=3, style={"color": PRIMARY_COLOR}),
                    dmc.Text("by 46brooklyn Research", size="sm", style={"color": TEXT_MUTED}),
                ],
            ),
        ],
    )

    actions = dmc.Group(
        align="center",
        gap="sm",
        children=[
            *badges,
            social_media_icons(),
        ],
    )

    return section_container([
        dmc.Group(
            justify="space-between",
            align="center",
            children=[brand, actions],
        )
    ])