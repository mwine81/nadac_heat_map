import dash_mantine_components as dmc
from components.section_container import section_container
from config import PRIMARY_COLOR
from scratch import year_quarter_list, state_list, drug_list

def controls():
    return section_container(
        [
            dmc.Title("Filter Options", order=2, c=PRIMARY_COLOR), #type: ignore
            dmc.Grid([
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="Brand/Generic",
                            data=['brand', 'generic'],
                            clearable=True,
                            searchable=True,
                            radius="md",
                            placeholder="Select brand/generic...",
                            id="bg-select",
                        ),
                    ]
                ),
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="Year/Quarter",
                            data=year_quarter_list(),
                            value=year_quarter_list()[-1],
                            searchable=True,
                            radius="md",
                            placeholder="Select year/quarter...",
                            clearable=False,
                            id="date-select"
                        ),
                    ]
                ),
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="Utilization Type",
                            data=['ffsu','mcou'],
                            searchable=True,
                            radius="md",
                            placeholder="Select utilization type...",
                            clearable=True,
                            id="utilization-select"
                        )
                    ]
                ),
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="Metric Type",
                            data=['payment_per_unit','markup_per_unit','markup_percentile','payment_per_unit_percentile'],
                            value='payment_per_unit',
                            searchable=True,
                            radius="md",
                            placeholder="Select a Metric...",
                            clearable=False,
                            id="metric-select"
                        )
                    ]
                ),
                 dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="State",
                            data=state_list(),
                            searchable=True,
                            radius="md",
                            placeholder="Select State...",
                            clearable=True,
                            id="state-select"
                        )
                    ]
                ),
                dmc.GridCol(
                    span=4,
                    children=[
                        dmc.Select(
                            label="Drug",
                            data=drug_list(),
                            searchable=True,
                            radius="md",
                            placeholder="Select Drug...",
                            clearable=True,
                            id="drug-select"
                        )
                    ]
                )

            ])
            #dmc.Text("This is the main content area."),
    ]
)