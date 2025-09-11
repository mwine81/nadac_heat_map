import dash_mantine_components as dmc
from config import THEME
from dash import Dash, Input, Output, State
from ui.layout import layout
from data_processing.data_processing import filter_map_data, filter_line_data
from figures import create_heat_map, create_line_chart

app = Dash()


app.layout = dmc.MantineProvider(theme=THEME, children=layout)

@app.callback(
    Output('map', 'figure'),
    Input('bg-select', 'value'),
    Input('date-select', 'value'),
    Input('utilization-select', 'value'),
    Input('metric-select', 'value'),
    Input('drug-select', 'value'),
)
def update_map(bg_value, date_value, utilization_value, metric_value, drug_value):
    # Update the chart based on the selected filters
    filtered_data = filter_map_data(
        year_quarter=date_value,
        drug=drug_value,
        utilization_type=utilization_value,
        brand_generic=bg_value
    )
    fig = create_heat_map(filtered_data, metric_value)
    return fig


@app.callback(
    Output('line-chart', 'figure'),
    Input('bg-select', 'value'),
    Input('state-select', 'value'),
    Input('utilization-select', 'value'),
    Input('drug-select', 'value'),
)
def update_line_chart(bg_value, state_value, utilization_value, drug_value):
    filtered_data = filter_line_data(
        state=state_value,
        drug=drug_value,
        brand_generic=bg_value,
        utilization_type=utilization_value
    )
    fig = create_line_chart(filtered_data)
    return fig

# Help modal callbacks
@app.callback(
    Output("help-overview-modal", "opened"),
    Input("help-overview-btn", "n_clicks"),
    State("help-overview-modal", "opened"),
    prevent_initial_call=True
)
def toggle_overview_modal(n_clicks, opened):
    return not opened

@app.callback(
    Output("help-data-modal", "opened"),
    Input("help-data-btn", "n_clicks"),
    State("help-data-modal", "opened"),
    prevent_initial_call=True
)
def toggle_data_modal(n_clicks, opened):
    return not opened

@app.callback(
    Output("help-usage-modal", "opened"),
    Input("help-usage-btn", "n_clicks"),
    State("help-usage-modal", "opened"),
    prevent_initial_call=True
)
def toggle_usage_modal(n_clicks, opened):
    return not opened

@app.callback(
    Output("help-technical-modal", "opened"),
    Input("help-technical-btn", "n_clicks"),
    State("help-technical-modal", "opened"),
    prevent_initial_call=True
)
def toggle_technical_modal(n_clicks, opened):
    return not opened

if __name__ == "__main__":
    app.run(debug=True)