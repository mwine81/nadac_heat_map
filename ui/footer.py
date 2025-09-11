import dash_mantine_components as dmc
from components.section_container import section_container
from dash_iconify import DashIconify
from dash import html
from components.badges import badge_nadac, badge_analytics
from components.social_media import social_media_icons
from datetime import date

def footer(title: str, badges: list):
    return section_container(
        [
            dmc.Stack([
                # Main footer content
                dmc.Grid([
                    # Left section - About and attribution
                    dmc.GridCol([
                        dmc.Stack([
                            dmc.Group([
                                DashIconify(icon="tabler:info-circle", width=16, color="#1a365d"),
                                dmc.Text("Dashboard Information", fw="bold", size="sm", style={"color": "#1a365d"})
                            ], gap="xs"),
                            dmc.Text(
                                "Built with modern data visualization techniques for comprehensive drug spending insights.",
                                size="xs",
                                c="gray",
                                lh=1.4
                            ),
                            dmc.Group([
                                dmc.Anchor(
                                    "NADAC Data Source",
                                    href="https://www.medicaid.gov/medicaid/nadac",
                                    target="_blank",
                                    size="xs",
                                    style={"color": "#1a365d"}
                                ),
                                dmc.Text("•", size="xs", c="gray"),
                                dmc.Anchor(
                                    "SDUD Data Source",
                                    href="https://data.medicaid.gov/datasets?theme%5B0%5D=State%20Drug%20Utilization",
                                    target="_blank",
                                    size="xs",
                                    style={"color": "#1a365d"}
                                ),
                                dmc.Text("•", size="xs", c="gray"),
                                dmc.Anchor(
                                    "46brooklyn Research",
                                    href="https://www.46brooklyn.com/",
                                    target="_blank",
                                    size="xs",
                                    style={"color": "#1a365d"}
                                )
                            ], gap="xs")
                        ], gap="sm")
                    ], span=8),
                    
                    # Right section - 46brooklyn social media
                    dmc.GridCol([
                        dmc.Stack([
                            dmc.Group([
                                DashIconify(icon="tabler:share", width=16, color="#ed8936"),
                                dmc.Text("Follow 46brooklyn Research", fw="bold", size="sm", style={"color": "#ed8936"})
                            ], gap="xs"),
                            dmc.Text(
                                "Stay updated with the latest drug pricing research and insights:",
                                size="xs",
                                c="gray",
                                lh=1.4
                            ),
                            social_media_icons()
                        ], gap="sm")
                    ], span=4)
                ], gutter="lg"),
                
                # Bottom section - Copyright and additional info
                dmc.Divider(color="gray"),
                dmc.Group([
                    dmc.Group([
                        dmc.Text(f"© {date.today().year} {title}", size="xs", c="gray"),
                    ], gap="xs"),
                    dmc.Group([
                        *badges
                    ], gap="xs")
                ], justify="space-between", wrap="wrap")
            ], gap="md")
        ],
    )