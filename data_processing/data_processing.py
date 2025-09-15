import polars as pl
from polars import col as c
import polars.selectors as cs
from data_processing.expressions import payment_per_unit, weighted_nadac_per_unit, markup_per_unit, markup_percentile, make_date, payment_per_unit_percentile, year_quarter
from config import BASE_DATA
from assets.states import STATE_ABBREV


def year_quarters() -> pl.LazyFrame:
    """Return sorted unique year/quarter combinations."""
    return (
        load_base_data()
        .select(c.year,c.quarter)
        .unique()
        .with_columns(year_quarter())
        .sort(['year','quarter'])
    )

def load_base_data() -> pl.LazyFrame:
    df = pl.scan_parquet(BASE_DATA)
    return df

def year_quarter_list() -> list[str]:
    """Return sorted unique year/quarter combinations as strings."""
    return (
        year_quarters()
        .select('year_quarter')
        .collect(engine='streaming')['year_quarter']
        .to_list()
    )

def state_list() -> list[str]:
    """Return sorted unique state values."""
    return (
        load_base_data()
        .select(c.state)
        .unique()
        .with_columns(c.state.replace(STATE_ABBREV))
        .sort('state')
        .collect(engine='streaming')['state']
        .to_list()
    )

def drug_list(how: str = 'all') -> list[str]:
    """Return sorted unique drug descriptions.
    how: 'all' | 'brand' | 'generic' (case-insensitive, accepts plurals)
    """
    how = (how or 'all').strip().lower()
    df = load_base_data()

    if how in ('brand', 'brands'):
        lf = df.filter(c.is_brand)
    elif how in ('generic', 'generics'):
        lf = df.filter(~c.is_brand)
    else:
        lf = df

    return (
        lf
        .select(c.description)
        .unique()
        .sort('description')
        .collect(engine='streaming')['description']
        .to_list()
    )


def filter_map_data(year_quarter: str,drug: str | None, brand_generic: str | None, utilization_type: str | None) -> pl.LazyFrame:
    year = int(year_quarter.split(' ')[0])
    quarter = int(year_quarter.split(' ')[1][1])
    
    data = (
        load_base_data()
        .filter(c.year == year)
        .filter(c.quarter == quarter)
    )

    if drug is not None:
        data = data.filter(c.description == drug)

    if brand_generic is not None:
        data = data.filter(c.is_brand if brand_generic == 'Brand' else ~c.is_brand)
    
    if utilization_type is not None:
        data = data.filter(c.is_ffsu if utilization_type == 'Fee-for-Service' else ~c.is_ffsu)

    data = (
        data
        .group_by(c.state)
        .agg(cs.matches('(?i)rx|total|units').sum().round(4))
        .with_columns(
            payment_per_unit(),
            markup_per_unit(),
            markup_percentile(),
            payment_per_unit_percentile()
        )
    )

    return data

def filter_line_data(state: str,drug: str | None, brand_generic: str | None, utilization_type: str | None):
    data = load_base_data().filter(c.weighted_nadac_total.is_not_null())

    if state is not None:
        data = data.filter(c.state == state)

    if drug is not None:
        data = data.filter(c.description == drug)

    if brand_generic is not None:
        data = data.filter(c.is_brand if brand_generic == 'Brand' else ~c.is_brand)
    
    if utilization_type is not None:
        data = data.filter(c.is_ffsu if utilization_type == 'ffsu' else ~c.is_ffsu)

    data = (
        data
        .group_by(make_date())
        .agg(cs.matches('(?i)rx|total|units').sum().round(4))
        .with_columns(
            payment_per_unit(),
            weighted_nadac_per_unit(),
            markup_per_unit()
        )
        .sort('date')
    )

    return data