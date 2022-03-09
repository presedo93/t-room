import asyncio

from textual.widget import Widget

# from tasks.ops.backtest import Backtest
from concurrent.futures import ProcessPoolExecutor
from tui.messages import RunCommand, ProgressCommand


class Runner(Widget):
    def __init__(self, name: str | None = None) -> None:
        super().__init__(name)
        self.pool = ProcessPoolExecutor()
        self.loop = asyncio.get_event_loop()

    @staticmethod
    def run(number):
        asyncio.run(on_run())

    async def handle_run_command(self, msg: RunCommand) -> None:
        tasks = [
            self.loop.run_in_executor(self.pool, Runner.run, i) for i in range(100)
        ]
        for fs in asyncio.as_completed(tasks):
            # Waits for the finalization of the method and gets the value.
            _ = await fs
            # Update the progress bar
            await self.emit(ProgressCommand(self, task="update", status={"back": 1}))


async def on_run():
    sum([i * i for i in range(int(1e7))])
