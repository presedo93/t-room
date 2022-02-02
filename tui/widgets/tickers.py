from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.console import RenderableType

from textual import events
from textual.widget import Widget
from textual.reactive import Reactive


class Tickers(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    color: Reactive[str] = Reactive("blue")

    def __init__(self) -> None:
        self.tickers = ["BTCUSD", "ETHUSD", "ADABTC", "SHIBUSDT"] * 10
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

    def on_key(self, event: events.Keys) -> None:
        if event.key == "up":
            self.tickers.pop(0)
        self.refresh()

    def render(self) -> RenderableType:
        table = Table(box=None, expand=True, padding=(1, 0, 0, 0), show_header=False)

        table.add_column(justify="center", no_wrap=True)
        table.add_column(justify="center", no_wrap=True)
        table.add_column(justify="center", no_wrap=True)

        t_len = len(self.tickers)
        for i in range(0, t_len, 3):
            r1 = self.tickers[i] if i < t_len else ""
            r1 = f"[black on {self.color}]{r1}[/]" if i == 0 else r1
            r2 = self.tickers[i + 1] if i + 1 < t_len else ""
            r3 = self.tickers[i + 2] if i + 2 < t_len else ""
            table.add_row(r1, r2, r3)

        return Panel(
            table,
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title="Tickers to process",
        )
