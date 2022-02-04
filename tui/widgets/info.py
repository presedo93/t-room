from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.console import RenderableType

from textual.widget import Widget
from textual.reactive import Reactive


class Info(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)

    def __init__(self) -> None:
        super().__init__()

    async def on_focus(self) -> None:
        self.has_focus = True

    async def on_blur(self) -> None:
        self.has_focus = False

    async def on_enter(self) -> None:
        self.mouse_over = True

    async def on_leave(self) -> None:
        self.mouse_over = False

    def render(self) -> RenderableType:
        text = """\
Welcome to t-room, the backtesting tui!
    Are you ready to do some
          simulations?
        """
        return Panel(
            Align.center(Text(text, "b green" if self.mouse_over else "b blue"), vertical="middle"),
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title="parameters",
        )
