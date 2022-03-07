from textual.app import App
from textual.reactive import Reactive

from tui.grid import DashGrid
from tasks.runner import Runner
from tui.widgets.header import Header
from tui.widgets.command import Command

from tools.utils import check_folders
from tui.messages import InputCommand, RunCommand, ProgressCommand


class Dashboard(App):
    show_runner: Reactive[bool] = Reactive(False)

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("ctrl+c", "quit", "Quit")

    async def handle_input_command(self, msg: InputCommand) -> None:
        if msg.action == "config":
            await self.grid.configs.post_message(InputCommand(self, cmd=msg.cmd))
        if msg.action == "tickers":
            await self.grid.tickers.post_message(InputCommand(self, cmd=msg.cmd))
        elif msg.action == "start":
            await self.runner.post_message(
                RunCommand(self, task="back", params=self.grid.conf)
            )

    async def handle_progress_command(self, msg: ProgressCommand) -> None:
        if msg.task == "update":
            await self.grid.status.post_message(
                ProgressCommand(self, status=msg.status)
            )

    async def on_mount(self) -> None:
        check_folders()
        self.grid = DashGrid()
        self.runner = Runner()
        await self.view.dock(Header(), edge="top", size=3)
        await self.view.dock(Command(), edge="bottom", size=3)
        await self.view.dock(self.grid, edge="top")
        await self.view.dock(self.runner)


Dashboard.run(log="textual.log")
