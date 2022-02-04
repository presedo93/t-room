import logging
import numpy as np
import pandas as pd

from datetime import datetime
from binance import Client

from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

from typing import Tuple

COLS = ["Date", "Open", "High", "Low", "Close", "Volume"]
DISCARD = ["Close_time", "Quote_av", "Trades", "Tb_base_av", "Tb_quote_av", "Ignore"]


def time_period(
    days: int = 0, secs: int = 0, days_off: int = 0, secs_off: int = 0
) -> Tuple[str, str]:
    start = end = dt.today() - relativedelta(days=days_off, seconds=secs_off)
    start -= relativedelta(days=days, seconds=secs)
    return start.strftime("%d %b %Y %H:%M:%S"), end.strftime("%d %b %Y %H:%M:%S")


def binance_data(
    bclient: Client, symbol: str, interval: str, period: int, save: bool = False
) -> pd.DataFrame:
    start, end = time_period(days=period)

    klines = bclient.get_historical_klines(symbol, interval, start, end)
    data = pd.DataFrame(klines, columns=COLS + DISCARD, dtype=np.float64).dropna()
    data.drop(columns=DISCARD, inplace=True)

    data["Date"] = data["Date"].apply(lambda x: datetime.fromtimestamp(x / 1000))
    data.set_index("Date", inplace=True)
    data.index = pd.to_datetime(data.index, format="%Y-%m-%d %H:%M:%S")

    logging.info(f"Fetched {symbol} ({interval}) from {start} to {end}")

    if save:
        data.to_csv(f"{symbol}.csv")

    return data


if __name__ == "__main__":
    import os

    logging.basicConfig(
        filename="binance.log", format="%(levelname)s - %(message)s", level=logging.INFO
    )

    client = Client(
        api_key=os.getenv("BINANCE_API"), api_secret=os.getenv("BINANCE_SECRET")
    )
    binance_data(client, "BTCUSDT", "1d", 20, save=True)
