from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.console import RenderableType
from rich.progress import Progress, BarColumn, TimeRemainingColumn

from textual.widget import Widget
from textual.reactive import Reactive


class Status(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    color: Reactive[str] = Reactive("blue")
    bar: Reactive[Progress] = Reactive(
        Progress(
            "[progress.description]{task.description}",
            BarColumn(bar_width=160),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
        )
    )

    async def on_mount(self) -> None:
        self.backtest = self.bar.add_task("backtest", total=100)
        self.optimize = self.bar.add_task("optimize", total=100)
        self.forward = self.bar.add_task("forward", total=100)
        self.set_interval(0.1, self.refresh)

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

    # async def handle_grid_command(self, message: NewCommand) -> None:
        # self.bar.update(self.backtest, advance=2)

    def render(self) -> RenderableType:
        return Panel(
            Align.center(self.bar, vertical="middle"),
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title="Tasks status",
        )
