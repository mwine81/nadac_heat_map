import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

def _social_media_icon(label: str, icon_name: str, color: str, url: str):
    return dmc.Tooltip(
            label=label,
            children=[
                dmc.Anchor(
                    dmc.ActionIcon(
                        DashIconify(icon=icon_name, width=18),
                        variant="subtle",
                        color=color, #type: ignore
                        size="md",
                        style={"transition": "all 0.2s ease"}
                    ),
                    href=url,
                    target="_blank",
                    style={"textDecoration": "none"}
                )
            ]
        )

def twitter():
    return _social_media_icon(
        label="Follow @46brooklyndata on Twitter",
        icon_name="mdi:twitter",
        color="blue",
        url="https://twitter.com/46brooklyndata"
    )

def linkedin():
    return _social_media_icon(
        label="Connect on LinkedIn",
        icon_name="mdi:linkedin",
        color="blue",
        url="https://www.linkedin.com/company/46brooklyn-research/"
    )

def instagram():
    return _social_media_icon(
        label="Follow on Instagram",
        icon_name="mdi:instagram",
        color="pink",
        url="https://www.instagram.com/46brooklynresearch/"
    )
     
def facebook():
    return _social_media_icon(
        label="Like on Facebook",
        icon_name="mdi:facebook",
        color="blue",
        url="https://www.facebook.com/46brooklyn/"
    )

def donate():
    return _social_media_icon(
        label="Support their research",
        icon_name="tabler:heart-filled",
        color="red",
        url="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YEF4YPTGZN9EJ&source=url"
    )


def social_media_icons():
    return dmc.Group([
        twitter(),
        linkedin(),
        instagram(),
        facebook(),
        donate()
    ], gap="xs")    