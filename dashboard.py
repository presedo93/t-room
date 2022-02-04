from textual.app import App
from textual.reactive import Reactive

from tui.grid import DashGrid
from tui.messages import InputCommand
from tui.widgets.header import Header
from tui.widgets.command import Command


class Dashboard(App):
    show_runner: Reactive[bool] = Reactive(False)

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("ctrl+b", "toggle_runner", "Toggle Runner")
        await self.bind("ctrl+c", "quit", "Quit")

    def watch_show_runner(self, show_runner: bool) -> None:
        """Called when show_runner changes."""
        self.runner.animate("visible", True if show_runner else False)

    def action_toggle_runner(self) -> None:
        """Called when user hits 'b' key."""
        self.show_runner = not self.show_runner

    async def handle_input_command(self, msg: InputCommand) -> None:
        if msg.action == "config":
            await self.grid.configs.post_message(InputCommand(self, cmd=msg.cmd, val=msg.val))

    async def on_mount(self) -> None:
        self.grid = DashGrid()
        await self.view.dock(Header(), edge="top", size=3)
        await self.view.dock(Command(), edge="bottom", size=3)
        await self.view.dock(self.grid, edge="top")

        # Runner
        # self.runner = Runner()
        # await self.view.dock(self.runner, edge="left", z=1)
        # self.runner.visible = False

Dashboard.run()