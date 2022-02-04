from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.console import RenderableType

from textual.widget import Widget
from textual.reactive import Reactive

from typing import Dict


class Params(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    params: Reactive[Dict] = Reactive({})

    def __init__(self, field: str, params: Dict | None = None) -> None:
        super().__init__()
        self.field = field
        self.params = params

    async def on_focus(self) -> None:
        self.has_focus = True

    async def on_blur(self) -> None:
        self.has_focus = False

    async def on_enter(self) -> None:
        self.mouse_over = True

    async def on_leave(self) -> None:
        self.mouse_over = False

    def render(self) -> RenderableType:
        if self.params is not None:
            rend = self.create_table(self.params)
        else:
            rend = Align.center(Text(f"No {self.field} params", style="green" if self.mouse_over else "blue"), vertical="middle")

        return Panel(
            rend,
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title=self.field,
        )

    def create_table(self, params: Dict) -> Table:
        table = Table(
            show_header=False,
            box=None,
            border_style="green" if self.mouse_over else "blue",
            show_lines=True,
            title_style="bold",
        )

        table.add_column(justify="center")
        for k, v in params.items():
            table.add_row(f"{k}", style="green" if self.mouse_over else "blue")
            table.add_row(f"{v}")

        return table
