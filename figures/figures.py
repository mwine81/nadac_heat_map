import plotly.express as px
import plotly.graph_objects as go
from typing import Any
import polars as pl

def _friendly_label(metric: str) -> str:
    """Turn snake_case metric into a human-friendly title."""
    return metric.replace('_', ' ').title()


def create_heat_map(data: pl.LazyFrame, metric: str) -> go.Figure:
    """
    Create a professional-looking US choropleth.

    - data: polars DataFrame or LazyFrame already collected (function will call .to_pandas()).
    - metric: column name to color by (e.g. 'payment_per_unit' or 'markup_per_unit').
    - title: optional figure title. If omitted, a sensible default is used.
    """
    metric = metric.replace(' ', '_').lower()
    df = data.collect(engine='streaming').to_pandas()
    label = _friendly_label(metric)

    fig = px.choropleth(
        df,
        locations='state',
        locationmode='USA-states',
        color=metric,
        scope='usa',
        color_continuous_scale=px.colors.sequential.Viridis,
        labels={metric: label},
    )

    # Polished trace styling and hover info
    fig.update_traces(
        marker_line_width=0.5,
        marker_line_color='white',
        hovertemplate=f"<b>%{{location}}</b><br>{label}: %{{z:$,.2f}}<extra></extra>",
        colorbar=dict(title={'text': f"{label} (USD)"}, thickness=12, len=0.6, tickformat='$,.2f', ticks='outside'),
    )   

    # Layout improvements
    fig.update_layout(
        title_text="US by state",
        title_x=0.5,
        template='plotly_white',
        margin=dict(l=10, r=10, t=50, b=10),
    )

    # Geo styling: subtle lake color and bounded view
    fig.update_geos(
        visible=False,
        showcountries=True,
        showsubunits=True,
        lakecolor='LightBlue',
    )


    return fig


def create_line_chart(data) -> go.Figure:
    """Create a polished time series comparing payment_per_unit and weighted_nadac_per_unit.

    - data: a pandas DataFrame (from Polars .collect()) with columns `date`,
      `payment_per_unit`, and `weighted_nadac_per_unit`.
    """
    data = data.collect(engine='streaming').to_pandas()
    y_cols = ['payment_per_unit', 'weighted_nadac_per_unit']
    labels = {c: _friendly_label(c) for c in y_cols}

    fig = px.line(
        data,
        x='date',
        y=y_cols,
        markers=True,
        labels={**labels, 'date': 'Date'},
        color_discrete_sequence=px.colors.qualitative.Dark2,
    )

    # Ensure legend uses friendly labels (px may keep original column names as trace names)
    for trace in fig.data:
        orig = getattr(trace, 'name', None)
        if orig in labels:
            friendly = labels[orig]
            t: Any = trace
            t.update(name=friendly, legendgroup=friendly)

    # General layout
    fig.update_layout(
        template='plotly_white',
        margin=dict(l=40, r=20, t=50, b=40),
        title_text='Payment per unit and Weighted NADAC over time',
        title_x=0.5,
        hovermode='x unified',
        legend=dict(orientation='h', yanchor='bottom', y=.97, xanchor='center', x=0.5),
    )

    # Trace styling and hover formatting
    fig.update_traces(marker=dict(size=6), line=dict(width=2), hovertemplate='%{x|%b %Y}<br>%{fullData.name}: %{y:$,.2f}<extra></extra>')

    # Axis formatting
    fig.update_xaxes(showgrid=False, tickformat='%b %Y', ticks='outside')
    fig.update_yaxes(showgrid=True, gridcolor='LightGray', zeroline=False, tickformat='$,.2f', ticks='outside')

    # Add a range slider for exploration
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True), type='date'))

    return fig