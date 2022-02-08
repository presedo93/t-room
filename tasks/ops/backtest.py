from typing import Dict, List
from backtesting import Strategy
from tasks.ops.task import Task


class Backtest(Task):
    def __init__(
        self,
        symbol: str,
        tickers: List[str],
        limits: Dict,
        params: Dict,
        strategy: Strategy,
    ) -> None:
        super().__init__()
        self.symbol = symbol
        self.tickers = tickers

        self.limits = limits
        self.params = params

        self.strategy = strategy

    def run(self):
        for t in self.tickers:
            self.step(t)

    async def step(self, tick: str):
        import asyncio

        asyncio.sleep(1)
