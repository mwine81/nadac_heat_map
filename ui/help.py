from components.section_container import section_container
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
from config import PRIMARY_COLOR

def help_section():
    return section_container([
        dmc.Title("Help & Information", order=2, mb="md", c=PRIMARY_COLOR),# type: ignore
        dmc.Group([
            dmc.Button(
                "Dashboard Overview",
                id="help-overview-btn",
                variant="light",
                leftSection=DashIconify(icon="material-symbols:info-outline", width=16),
                size="sm"
            ),
            dmc.Button(
                "Data Sources",
                id="help-data-btn", 
                variant="light",
                leftSection=DashIconify(icon="material-symbols:database-outline", width=16),
                size="sm"
            ),
            dmc.Button(
                "How to Use",
                id="help-usage-btn",
                variant="light", 
                leftSection=DashIconify(icon="material-symbols:help-outline", width=16),
                size="sm"
            ),
            dmc.Button(
                "Technical Details",
                id="help-technical-btn",
                variant="light",
                leftSection=DashIconify(icon="material-symbols:settings-outline", width=16), 
                size="sm"
            )
        ], gap="sm"),
        
        # Modal for Dashboard Overview
        dmc.Modal(
            title=dmc.Title("Dashboard Overview", order=3),
            id="help-overview-modal",
            children=[
                dmc.Stack([
                    dmc.Text([
                        "This dashboard provides comprehensive analysis of NADAC (National Average Drug Acquisition Cost) pricing data. ",
                        "It allows you to explore drug pricing trends across different categories, products, and package sizes."
                    ], size="sm"),
                    dmc.List([
                        dmc.ListItem("View price trends over time for specific drug products"),
                        dmc.ListItem("Compare prices across different package sizes"),
                        dmc.ListItem("Filter by drug class and specific products"),
                        dmc.ListItem("Interactive charts with detailed legends")
                    ], size="sm"),
                    dmc.Alert([
                        dmc.Text("The data reflects average acquisition costs and may not represent actual retail prices.", size="sm")
                    ], title="Important Note", color="blue", variant="light")
                ], gap="md")
            ]
        ),
        
        # Modal for Data Sources
        dmc.Modal(
            title=dmc.Title("Data Sources & Methodology", order=3),
            id="help-data-modal", 
            children=[
                dmc.Stack([
                    dmc.Text([
                        "The National Average Drug Acquisition Cost (NADAC) data is sourced from CMS (Centers for Medicare & Medicaid Services). ",
                        "This data represents the national average of invoice prices paid by retail community pharmacies."
                    ], size="sm"),
                    dmc.Divider(),
                    dmc.Title("Data Processing", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Prices are grouped by product and effective date"),
                        dmc.ListItem("Unit prices are averaged across all reporting pharmacies"),
                        dmc.ListItem("Data is filtered by drug classification and package size"),
                        dmc.ListItem("Historical trends show price evolution over time")
                    ], size="sm"),
                    dmc.Alert([
                        dmc.Text("Data is updated regularly but may have reporting delays of 1-2 months.", size="sm")
                    ], title="Data Freshness", color="orange", variant="light")
                ], gap="md")
            ]
        ),
        
        # Modal for How to Use
        dmc.Modal(
            title=dmc.Title("How to Use the Dashboard", order=3),
            id="help-usage-modal",
            children=[
                dmc.Stack([
                    dmc.Title("Step-by-Step Guide", order=4, size="md"),
                    dmc.Stepper(
                        active=0,
                        children=[
                            dmc.StepperStep(
                                label="Select Drug Class",
                                description="Choose a drug classification from the dropdown"
                            ),
                            dmc.StepperStep(
                                label="Filter Products", 
                                description="Select specific products within that class (optional)"
                            ),
                            dmc.StepperStep(
                                label="Choose Package Size",
                                description="Filter by package size if needed (optional)"
                            ),
                            dmc.StepperStep(
                                label="Analyze Chart",
                                description="View price trends and use the legend for reference"
                            )
                        ]
                    ),
                    dmc.Divider(),
                    dmc.Title("Chart Features", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Hover over data points for detailed information"),
                        dmc.ListItem("Use the legend to identify different products"),
                        dmc.ListItem("Zoom and pan functionality for detailed analysis"),
                        dmc.ListItem("Time series shows price evolution over months/years")
                    ], size="sm")
                ], gap="md")
            ]
        ),
        
        # Modal for Technical Details
        dmc.Modal(
            title=dmc.Title("Technical Information", order=3),
            id="help-technical-modal",
            children=[
                dmc.Stack([
                    dmc.Title("Technology Stack", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Built with Python Dash and Dash Mantine Components"),
                        dmc.ListItem("Data processing powered by Polars for high performance"),
                        dmc.ListItem("Interactive charts created with Plotly"),
                        dmc.ListItem("Responsive design for desktop and mobile devices")
                    ], size="sm"),
                    dmc.Divider(),
                    dmc.Title("Performance Notes", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Data is lazily loaded and processed for efficiency"),
                        dmc.ListItem("Charts update dynamically based on filter selections"),
                        dmc.ListItem("Optimized for large datasets with streaming operations"),
                        dmc.ListItem("Caching mechanisms reduce load times")
                    ], size="sm"),
                    dmc.Alert([
                        dmc.Text("For technical support or feature requests, please contact the development team.", size="sm")
                    ], title="Support", color="green", variant="light")
                ], gap="md")
            ]
        )
    ])



