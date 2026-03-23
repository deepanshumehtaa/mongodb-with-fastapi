from typing import *
from pydantic import validator
from ..clients.mongo import RWModel
from ..schemas.bill import StatisticDetail


class StatisticDoc(RWModel):
    """
    Statistics

    Note
    ----
    Divided into two types based on time dimension: annual statistics or monthly statistics

    - Annual statistics:
    - calc_cyc = "year"
    - month = 0
    - records: records for 12 months, key is the month
    - Monthly statistics:
    - calc_cyc = "month"
    - month: the month of the current month
    - records: records the total amount for each day of the current month, key is the day of the month

    Percentage field:

    Tuple[int, float]: The 0th value identifies the id of BillCategory, the value is the percentage, between 0 and 1.
    """
    __collection__ = "book_statistic"

    id: Optional[int]
    statistic_type: str
    calc_cyc: str
    year: int
    month: int = 0

    user_id: int
    book_id: Optional[int]

    expenditure: StatisticDetail = StatisticDetail()
    income: StatisticDetail = StatisticDetail()

    @validator("statistic_type")
    def valid_statistic_type(cls, v) -> str:
        if v in ("book", "account"):
            return v
        raise ValueError(f"Error statistic_type value: {v}")

    @validator("calc_cyc")
    def valid_calc_cyc(cls, v) -> str:
        if v in ("year", "month"):
            return v
        raise ValueError(f"Error calc_cyc value: {v}")
