import plotly.express as px
import plotly.graph_objects as go
from typing import Any
import polars as pl
import pandas as pd

def _friendly_label(metric: str) -> str:
    """Turn snake_case metric into a human-friendly title."""
    return metric.replace('_', ' ').title()


def create_heat_map(data: pl.LazyFrame, metric: str, color_friendly: bool = False) -> go.Figure:
    """
    Create a professional-looking US choropleth.

    - data: polars DataFrame or LazyFrame already collected (function will call .to_pandas()).
    - metric: column name to color by (e.g. 'payment_per_unit' or 'markup_per_unit').
    - title: optional figure title. If omitted, a sensible default is used.
    """
    metric = metric.replace(' ', '_').lower()
    df = data.collect(engine='streaming').to_pandas()
    label = _friendly_label(metric)

    # Define hover data formatting for additional columns
    hover_columns = ['units', 'rx_ct', 'total_amt', 'weighted_nadac_total', 
                    'payment_per_unit', 'markup_per_unit', 'markup_percentile', 
                    'payment_per_unit_percentile']
    
    # Create hover_data dict with appropriate formatting
    hover_data = {}
    for col in hover_columns:
        if col in df.columns:
            if col in ['units', 'rx_ct']:
                hover_data[col] = ':,'  # Integer formatting with commas
            elif col in ['total_amt', 'weighted_nadac_total']:
                hover_data[col] = ':$,.0f'  # Currency with no decimals
            elif col in ['payment_per_unit', 'markup_per_unit']:
                hover_data[col] = ':$,.2f'  # Currency with 2 decimals
            elif col in ['markup_percentile', 'payment_per_unit_percentile']:
                hover_data[col] = ':.1%'  # Percentage formatting
    


    fig = px.choropleth(
        df,
        locations='state',
        locationmode='USA-states',
        color=metric,
        scope='usa',
        color_continuous_scale=px.colors.sequential.Cividis if color_friendly else px.colors.sequential.Viridis,
        labels={metric: label},
        hover_data=hover_data,
    )

    # Create comprehensive hover template with all the data
    # Determine format for the main metric based on type
    if 'percentile' in metric:
        main_metric_format = "{z:.1%}"
        colorbar_format = '.1%'
        colorbar_title = f"{label}"
    else:
        main_metric_format = "{z:$,.2f}"
        colorbar_format = '$,.2f'
        colorbar_title = f"{label} (USD)"
    
    hover_template = f"<b>%{{location}}</b><br>"
    hover_template += f"<b>{label}: %{main_metric_format}</b><br><br>"
    
    # Add each hover column if it exists in the data
    if 'units' in df.columns:
        hover_template += "Units: %{customdata[0]:,}<br>"
    if 'rx_ct' in df.columns:
        hover_template += "Prescriptions: %{customdata[1]:,}<br>"
    if 'total_amt' in df.columns:
        hover_template += "Total Amount: %{customdata[2]:$,.0f}<br>"
    if 'weighted_nadac_total' in df.columns:
        hover_template += "Weighted NADAC Total: %{customdata[3]:$,.0f}<br>"
    if 'payment_per_unit' in df.columns:
        hover_template += "Payment/Unit: %{customdata[4]:$,.2f}<br>"
    if 'markup_per_unit' in df.columns:
        hover_template += "Markup/Unit: %{customdata[5]:$,.2f}<br>"
    if 'markup_percentile' in df.columns:
        hover_template += "Markup Percentile: %{customdata[6]:.1%}<br>"
    if 'payment_per_unit_percentile' in df.columns:
        hover_template += "Payment Percentile: %{customdata[7]:.1%}<br>"
    
    hover_template += "<extra></extra>"
    
    # Prepare custom data array for hover template
    customdata_cols = []
    for col in ['units', 'rx_ct', 'total_amt', 'weighted_nadac_total', 
                'payment_per_unit', 'markup_per_unit', 'markup_percentile', 
                'payment_per_unit_percentile']:
        if col in df.columns:
            customdata_cols.append(df[col])

    # Polished trace styling and hover info
    fig.update_traces(
        marker_line_width=0.5,
        marker_line_color='white',
        hovertemplate=hover_template,
        customdata=list(zip(*customdata_cols)) if customdata_cols else None,
    )    # Update colorbar using coloraxis method (more reliable)
    if 'percentile' in metric:
        fig.update_coloraxes(
            colorbar_title_text=colorbar_title,
            colorbar_thickness=12,
            colorbar_len=0.6,
            colorbar_ticks="outside",
            colorbar_tickformat=".1%"
        )
    else:
        fig.update_coloraxes(
            colorbar_title_text=colorbar_title,
            colorbar_thickness=12,
            colorbar_len=0.6,
            colorbar_ticks="outside",
            colorbar_tickformat="$,.2f"
        )

    # Layout improvements
    fig.update_layout(
        # title_text="US by state",
        # title_x=0.5,
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


def create_line_chart(data, selected_year_quarter: str | None = None) -> go.Figure:
    """Create a polished time series comparing payment_per_unit and weighted_nadac_per_unit.

    - data: a pandas DataFrame (from Polars .collect()) with columns `date`,
      `payment_per_unit`, and `weighted_nadac_per_unit`.
    - selected_year_quarter: optional year_quarter string to highlight specific period
    """
    data = data.collect(engine='streaming').to_pandas()
    y_cols = ['payment_per_unit', 'weighted_nadac_per_unit']
    labels = {c: _friendly_label(c) for c in y_cols}

    # Additional hover data columns if available
    hover_columns = ['units', 'rx_ct', 'total_amt', 'weighted_nadac_total', 'markup_per_unit']
    hover_data = {}
    for col in hover_columns:
        if col in data.columns:
            if col in ['units', 'rx_ct']:
                hover_data[col] = ':,'  # Integer formatting with commas
            elif col in ['total_amt', 'weighted_nadac_total']:
                hover_data[col] = ':$,.0f'  # Currency with no decimals
            else:
                hover_data[col] = ':$,.2f'  # Currency with 2 decimals

    fig = px.line(
        data,
        x='date',
        y=y_cols,
        markers=True,
        labels={**labels, 'date': 'Date'},
        color_discrete_sequence=px.colors.qualitative.Set2,  # Professional color palette
        hover_data=hover_data,
    )

    # Ensure legend uses friendly labels (px may keep original column names as trace names)
    for trace in fig.data:
        orig = getattr(trace, 'name', None)
        if orig in labels:
            friendly = labels[orig]
            t: Any = trace
            t.update(name=friendly, legendgroup=friendly)

    # Create comprehensive hover template similar to heat map
    hover_template = "<b>%{x|%b %Y}</b><br>"
    hover_template += "<b>%{fullData.name}: %{y:$,.2f}</b><br><br>"
    
    # Add additional data if available
    if 'units' in data.columns:
        hover_template += "Units: %{customdata[0]:,}<br>"
    if 'rx_ct' in data.columns:
        hover_template += "Prescriptions: %{customdata[1]:,}<br>"
    if 'total_amt' in data.columns:
        hover_template += "Total Amount: %{customdata[2]:$,.0f}<br>"
    if 'weighted_nadac_total' in data.columns:
        hover_template += "Weighted NADAC Total: %{customdata[3]:$,.0f}<br>"
    if 'markup_per_unit' in data.columns:
        hover_template += "Markup/Unit: %{customdata[4]:$,.2f}<br>"
    
    hover_template += "<extra></extra>"

    # Prepare custom data array for hover template
    customdata_cols = []
    for col in hover_columns:
        if col in data.columns:
            customdata_cols.append(data[col])

    # General layout with professional styling
    fig.update_layout(
        template='plotly_white',
        margin=dict(l=50, r=20, t=70, b=50),
        hovermode='x unified',
        legend=dict(
            orientation='h', 
            yanchor='bottom', 
            y=1.02, 
            xanchor='center', 
            x=0.5,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='LightGray',
            borderwidth=1
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    # Enhanced trace styling and hover formatting
    fig.update_traces(
        marker=dict(size=8, line=dict(width=1, color='white')), 
        line=dict(width=3),
        hovertemplate=hover_template,
        customdata=list(zip(*customdata_cols)) if customdata_cols else None,
    )

    # Professional axis formatting matching heat map style
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        gridwidth=1,
        tickformat='%b %Y', 
        ticks='outside',
        tickfont_size=12,
        title_font_size=14,
        linecolor='LightGray',
        mirror=True
    )
    
    fig.update_yaxes(
        showgrid=True, 
        gridcolor='rgba(128,128,128,0.2)',
        gridwidth=1,
        zeroline=True,
        zerolinecolor='rgba(128,128,128,0.4)',
        zerolinewidth=1,
        tickformat='$,.2f', 
        ticks='outside',
        tickfont_size=12,
        title_font_size=14,
        title_text='Price per Unit (USD)',
        linecolor='LightGray',
        mirror=True
    )

    # Add range slider for exploration (consistent with professional dashboards)
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True,
                thickness=0.05,
                bgcolor='rgba(128,128,128,0.1)',
                bordercolor='LightGray',
                borderwidth=1
            ), 
            type='date'
        )
    )

    # Add annotations for selected period or latest values
    if len(data) > 0:
        # Convert selected year_quarter to date for annotation
        if selected_year_quarter:
            try:
                # Parse year_quarter format like "2023 Q1" -> find matching date
                year, quarter = selected_year_quarter.split(' Q')
                year = int(year)
                quarter = int(quarter)
                
                # Create target date for the quarter (using first month of quarter)
                quarter_month_map = {1: 1, 2: 4, 3: 7, 4: 10}
                target_month = quarter_month_map.get(quarter, 1)
                target_date = pd.Timestamp(year=year, month=target_month, day=1)
                
                # Find the closest date in the data to the target
                data['date_diff'] = abs(data['date'] - target_date)
                selected_data = data.loc[data['date_diff'].idxmin()]
                annotation_date = selected_data['date']
                
                # Clean up temporary column
                data = data.drop('date_diff', axis=1)
                
            except (ValueError, KeyError):
                # Fallback to latest date if parsing fails
                annotation_date = data['date'].max()
                selected_data = data[data['date'] == annotation_date].iloc[0]
        else:
            # Use latest date if no year_quarter selected
            annotation_date = data['date'].max()
            selected_data = data[data['date'] == annotation_date].iloc[0]
        
        # Define colors for annotations
        annotation_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        
        for i, col in enumerate(y_cols):
            if col in data.columns:
                annotation_value = selected_data[col] if hasattr(selected_data, col) else selected_data.get(col)
                if annotation_value is not None and not pd.isna(annotation_value):
                    color = annotation_colors[i % len(annotation_colors)]
                    
                    # Add annotation text with period info
                    if selected_year_quarter:
                        annotation_text = f"{selected_year_quarter}<br>${annotation_value:,.2f}"
                    else:
                        annotation_text = f"Latest<br>${annotation_value:,.2f}"
                    
                    fig.add_annotation(
                        x=annotation_date,
                        y=annotation_value,
                        text=annotation_text,
                        showarrow=True,
                        arrowhead=2,
                        arrowsize=1,
                        arrowwidth=2,
                        arrowcolor=color,
                        bgcolor='rgba(255,255,255,0.9)',
                        bordercolor=color,
                        borderwidth=2,
                        font=dict(size=10, color=color),
                        ax=20,
                        ay=-30
                    )

    return fig