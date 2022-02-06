import os
import logging
import pandas as pd

from tools.utils import time_period
from alpha_vantage.async_support.timeseries import TimeSeries


COLS = ["open", "high", "low", "close", "volume"]

async def alpha_vantage_data(
    symbol: str, interval: str, period: int, save: bool = False
) -> pd.DataFrame:
    ts = TimeSeries(key=os.getenv("ALPHA_VANTAGE_API"), output_format="pandas", indexing_type="date")
    match interval:
        case "1m" | "5m" | "15m" | "30m" | "60m":
            data, _ = await ts.get_intraday(symbol, f"{interval}in", outputsize="full")
        case "1d":
            data, _ = await ts.get_daily(symbol, outputsize="full")
        case "1w":
            data, _ = await ts.get_weekly(symbol)
        case "1M":
            data, _ = await ts.get_monthly(symbol)
        case _:
            logging.warning(f"({interval}) is not correct. Retrieving 1d as default.")
            data, _ = await ts.get_daily(symbol, outputsize="full")
    await ts.close()

    data.columns = COLS
    start, end = time_period(days=period)
    data = data.sort_index().loc[start:end]

    if save:
        data.to_csv(f"{symbol}.csv")

    logging.info(f"Fetched {symbol} ({interval}) from {start} to {end}")
    return data


if __name__ == "__main__":
    import asyncio
    logging.basicConfig(
        filename="alpha.log", format="%(levelname)s - %(message)s", level=logging.INFO
    )
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(alpha_vantage_data("AAPL", "1d", 10))
    loop.close()
