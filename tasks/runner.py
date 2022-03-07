import asyncio

from textual.widget import Widget

# from tasks.ops.backtest import Backtest
from concurrent.futures import ThreadPoolExecutor
from tui.messages import RunCommand, ProgressCommand


class Runner(Widget):
    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
        self.pool = ThreadPoolExecutor()

    async def on_run(self):
        await asyncio.sleep(1)
        await self.emit(ProgressCommand(self, task="update", status={"back": 1}))

    def run(self, number):
        asyncio.run(self.on_run())

    async def handle_run_command(self, msg: RunCommand) -> None:
        self.pool.map(self.run, range(100))
