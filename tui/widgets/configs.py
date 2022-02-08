from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.pretty import Pretty
from rich.console import Group
from rich.console import RenderableType

from typing import Dict, List
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
    cash: Reactive[float] = Reactive(0.0)
    commission: Reactive[float] = Reactive(0.0)
    price_limit: Reactive[float] = Reactive(0.0)
    str_ticker: Reactive[str] = Reactive("")

    interval: Reactive[List] = Reactive([])
    period: Reactive[List] = Reactive([])

    def __init__(self, conf: Dict) -> None:
        self.conf = conf
        super().__init__()

    def on_mount(self) -> None:
        self.cash = self.conf["cash"]
        self.commission = self.conf["commission"]

        self.price_limit = self.conf["price_limit"]
        self.str_ticker = self.conf["str_ticker"]

        self.interval = self.conf["interval"]
        self.period = self.conf["period"]

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
        match msg.cmd:
            case ["workers", val]:
                self.workers = int(val)
            case ["store", val]:
                self.store = str2bool(val)
            case ["cash", val]:
                self.cash = float(val)
            case ["commission", val]:
                self.commission = float(val)
            case ["price_limit", val]:
                self.price_limit = float(val)
            case ["str_ticker", val]:
                self.str_ticker = str(val)
            case ["intervals", *val]:
                self.interval = val
            case ["periods", *val]:
                print(val)
                self.period = val
        self.refresh()

    def render(self) -> RenderableType:
        table1 = Table(
            box=None,
            style=self.color,
            expand=True,
            title_style="bold",
            padding=(0, 0, 0, 0),
            show_header=False,
        )

        table1.add_column(justify="center", style=self.color)
        table1.add_column(justify="center", style="white")
        table1.add_column(justify="center", style=self.color)
        table1.add_column(justify="center", style="white")

        table1.add_row("Workers:", f"{self.workers}", "Store in DB:", f"{self.store}")
        table1.add_row(
            "Cash:", f"{self.cash}", "Commission:", f"{self.commission*100}%"
        )
        table1.add_row(
            "Max. Price:",
            f"{self.price_limit}",
            "Name in ticker:",
            f"{self.str_ticker}",
        )

        table2 = Table(
            box=None,
            style=self.color,
            expand=True,
            title_style="bold",
            padding=(0, 0, 0, 0),
            show_header=False,
        )

        table2.add_column(justify="center", style=self.color)
        table2.add_column(justify="center", style="white")

        table2.add_row("Intervals:", Pretty(self.interval))
        table2.add_row("Periods:", Pretty(self.period))

        group = Group(table1, table2)

        return Panel(
            Align.center(group, vertical="middle"),
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title="run parameters",
        )
