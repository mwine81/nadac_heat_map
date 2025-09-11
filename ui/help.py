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
                        "This heat map dashboard visualizes NADAC (National Average Drug Acquisition Cost) pricing data across US states. ",
                        "Explore drug pricing patterns geographically and track price trends over time for specific states and drugs."
                    ], size="sm"),
                    dmc.List([
                        dmc.ListItem("View state-by-state drug pricing with interactive heat map"),
                        dmc.ListItem("Compare payment per unit vs weighted NADAC over time"),
                        dmc.ListItem("Filter by drug, brand/generic, and utilization type"),
                        dmc.ListItem("Switch between percentile and absolute color scaling"),
                        dmc.ListItem("Hover for detailed state-specific pricing information")
                    ], size="sm"),
                    dmc.Alert([
                        dmc.Text("Colors represent relative pricing - use the colorbar to interpret values across states.", size="sm")
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
                        "The NADAC (National Average Drug Acquisition Cost) data comes from CMS and represents average prices paid by retail pharmacies. ",
                        "This heat map application processes the data using Polars for efficient filtering and aggregation."
                    ], size="sm"),
                    dmc.Divider(),
                    dmc.Title("Data Processing", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Payment per unit calculated from total payment and units dispensed"),
                        dmc.ListItem("Weighted NADAC computed using prescription volumes"),
                        dmc.ListItem("State-level aggregations for geographic visualization"),
                        dmc.ListItem("Time series data grouped by quarter and converted to monthly display"),
                        dmc.ListItem("Lazy evaluation with Polars for performance on large datasets")
                    ], size="sm"),
                    dmc.Alert([
                        dmc.Text("Data path configured in config.py - verify BASE_DATA points to valid Parquet file.", size="sm")
                    ], title="Data Configuration", color="orange", variant="light")
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
                                label="Select Filters",
                                description="Choose drug, brand/generic type, utilization type, and date"
                            ),
                            dmc.StepperStep(
                                label="Choose Metric", 
                                description="Select payment_per_unit or markup_per_unit for heat map coloring"
                            ),
                            dmc.StepperStep(
                                label="Analyze Heat Map",
                                description="View state-by-state pricing patterns with color intensity"
                            ),
                            dmc.StepperStep(
                                label="Explore Time Series",
                                description="Select a state to view price trends over time in the line chart"
                            )
                        ]
                    ),
                    dmc.Divider(),
                    dmc.Title("Interactive Features", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Hover over states for detailed pricing information"),
                        dmc.ListItem("Use colorbar to interpret relative pricing across states"),
                        dmc.ListItem("Switch between percentile and absolute color scaling"),
                        dmc.ListItem("Line chart shows payment vs NADAC trends over time"),
                        dmc.ListItem("Top/bottom state annotations show extreme values")
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
                        dmc.ListItem("Data processing powered by Polars for lazy evaluation and streaming"),
                        dmc.ListItem("Interactive choropleth maps and line charts with Plotly"),
                        dmc.ListItem("Marimo-based UI alternative available (app_beta.py)"),
                        dmc.ListItem("Responsive design with professional styling")
                    ], size="sm"),
                    dmc.Divider(),
                    dmc.Title("Performance Features", order=4, size="md"),
                    dmc.List([
                        dmc.ListItem("Lazy frame processing keeps large datasets in memory efficiently"),
                        dmc.ListItem("Streaming collection for memory-optimized aggregations"),
                        dmc.ListItem("Percentile-based color scaling reduces outlier impact"),
                        dmc.ListItem("USD currency formatting throughout visualizations"),
                        dmc.ListItem("State-level aggregations cached for quick filtering")
                    ], size="sm"),
                    dmc.Alert([
                        dmc.Text("Heat map uses Viridis colorscale for accessibility. Configure BASE_DATA in config.py before running.", size="sm")
                    ], title="Configuration", color="green", variant="light")
                ], gap="md")
            ]
        )
    ])



