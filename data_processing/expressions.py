import polars as pl
from polars import col as c
import polars.selectors as cs

def year_quarter() -> pl.Expr:
    """Return a year/quarter expression."""
    return pl.format("{} Q{}", c.year, c.quarter).alias('year_quarter')

def payment_per_unit() -> pl.Expr:
    """Return a payment per unit expression."""
    return (cs.matches('(?i)total_amt') / c.units).round(4).alias('payment_per_unit')

def weighted_nadac_per_unit() -> pl.Expr:
    """Return a weighted nadac per unit expression."""
    return (cs.matches('(?i)nadac.*total') / c.units).round(4).alias('weighted_nadac_per_unit')

def markup_per_unit() -> pl.Expr:
    """Return a markup per unit expression."""
    return payment_per_unit().sub(weighted_nadac_per_unit()).round(4).alias('markup_per_unit')

def markup_rank() -> pl.Expr:
    return markup_per_unit().rank(descending=False).alias('markup_rank')

def markup_percentile() -> pl.Expr:
    percentile = ((markup_rank()-1) / markup_rank().max())
    return pl.when(percentile < .01).then(0.01).otherwise(percentile).round(2).alias('markup_percentile')

def payment_per_unit_rank() -> pl.Expr:
    return payment_per_unit().rank(descending=False).alias('payment_per_unit_rank')

def convert_quarter_to_month() -> pl.Expr:
    return (c.quarter - 1) * 3 + 1

def make_date() -> pl.Expr:
    return pl.datetime(c.year, convert_quarter_to_month(), 1).alias('date')

def payment_per_unit_percentile() -> pl.Expr:
    percentile = ((payment_per_unit_rank()-1) / payment_per_unit_rank().max())
    return pl.when(percentile < .01).then(0.01).otherwise(percentile).round(2).alias('payment_per_unit_percentile')