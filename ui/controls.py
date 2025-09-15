import dash_mantine_components as dmc
from components.section_container import section_container
from config import PRIMARY_COLOR, METRIC_DROPDOWN_LABELS
# from scratch import state_list, drug_list
from data_processing.data_processing import year_quarter_list, state_list, drug_list

def map_controls() -> dmc.Container:
    return section_container(
        [
            dmc.Title("Map Filter Options", order=2, c=PRIMARY_COLOR), #type: ignore
            dmc.Center(
                dmc.Grid(
                    [
                        dmc.GridCol(
                            span=4,
                            children=[
                                dmc.Select(
                                    label="Brand/Generic",
                                    data=['Brand', 'Generic'],
                                    clearable=True,
                                    searchable=True,
                                    radius="md",
                                    placeholder="Select Brand/Generic...",
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
                                    data=['Fee-for-Service','Managed Care'],
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
                                    data=METRIC_DROPDOWN_LABELS,
                                    value=METRIC_DROPDOWN_LABELS[0],
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
                                    label="Drug",
                                    data=drug_list(),
                                    searchable=True,
                                    radius="md",
                                    placeholder="Select Drug...",
                                    clearable=True,
                                    id="drug-select"
                                )
                            ]
                        ),
                        dmc.GridCol(
                            span=4,
                            children=[
                                dmc.Switch(
                                    label='Color-vision-friendly mode',
                                    id='color-blind-switch',
                                    size='sm',
                                )
                            ]
                        ),
                    ],
                    justify="center",
                    align="center",
                ),
                style={"width": "100%"},
            ),
        ]
    )

def line_chart_controls() -> dmc.Container:
    return section_container(
        [
            dmc.Title("Line Chart Filter Options", order=2, c=PRIMARY_COLOR), #type: ignore
            dmc.Grid([
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
                )
            ])
    ]
)