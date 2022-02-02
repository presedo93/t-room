from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.console import RenderableType

from textual.widget import Widget
from textual.reactive import Reactive

from tools.utils import str2bool
from tui.messages import InputCommand


class Configs(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    color: Reactive[str] = Reactive("blue")

    workers: Reactive[int] = Reactive(0)
    store: Reactive[bool] = Reactive(False)

    def __init__(self) -> None:
        super().__init__(name=None)

    async def on_focus(self) -> None:
        self.has_focus = True

    async def on_blur(self) -> None:
        self.has_focus = False

    async def on_enter(self) -> None:
        self.mouse_over = True
        self.color = "green"

    async def on_leave(self) -> None:
        self.mouse_over = False
        self.color = "blue"

    async def handle_input_command(self, msg: InputCommand) -> None:
        if msg.cmd.lower() == "workers":
            self.workers = int(msg.val)
        elif msg.cmd.lower() == "store":
            self.store = str2bool(msg.val)

    def render(self) -> RenderableType:
        table = Table(
            box=box.SIMPLE,
            expand=True,
            title_style="bold",
            padding=(0, 0, 0, 0),
            show_header=False,
        )

        table.add_column(justify="center", style=self.color)
        table.add_column(justify="center", style=self.color)
        table.add_column(justify="center", style=self.color)
        table.add_column(justify="center", style=self.color)

        table.add_row("Workers:", f"{self.workers}", "Store in DB:", f"{self.store}")

        return Panel(
            table,
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title="run parameters",
        )
