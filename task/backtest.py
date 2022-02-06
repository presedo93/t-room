from typing import Dict
from backtesting import Strategy


class Backtest:
    def __init__(
        self, symbol: str, limits: Dict, params: Dict, strategy: Strategy
    ) -> None:
        self.symbol = symbol
        self.limits = limits
        self.params = params
        self.strategy = strategy

    # def run(self):
