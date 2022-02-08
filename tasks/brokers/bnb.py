import os
import logging
import numpy as np
import pandas as pd

from binance import AsyncClient
from datetime import datetime as dt
from tools.utils import time_period

COLS = ["date", "open", "high", "low", "close", "volume"]
DISCARDED = ["Close_time", "Quote_av", "Trades", "Tb_base_av", "Tb_quote_av", "Ignore"]


async def binance_data(
    symbol: str, interval: str, period: int, save: bool = False
) -> pd.DataFrame:
    start, end = time_period(days=period)
    bn = AsyncClient(
        api_key=os.getenv("BINANCE_API"), api_secret=os.getenv("BINANCE_SECRET")
    )

    lines = await bn.get_historical_klines(symbol, interval, start, end)
    await bn.close_connection()

    data = pd.DataFrame(lines, columns=COLS + DISCARDED, dtype=np.float64).dropna()
    data.drop(columns=DISCARDED, inplace=True)

    data["date"] = data["date"].apply(lambda x: dt.fromtimestamp(x / 1000))
    data.set_index("date", inplace=True)
    data.index = pd.to_datetime(data.index, format="%Y-%m-%d %H:%M:%S")

    if save:
        data.to_csv(f"{symbol}.csv")

    logging.info(f"Fetched {symbol} ({interval}) from {start} to {end}")
    return data


if __name__ == "__main__":
    import asyncio

    logging.basicConfig(
        filename="binance.log", format="%(levelname)s - %(message)s", level=logging.INFO
    )
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(binance_data("BTCUSDT", "1d", 20))
    loop.close()
