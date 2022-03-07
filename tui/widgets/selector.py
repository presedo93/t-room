from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.console import RenderableType

from textual import events
from textual.widget import Widget
from textual.reactive import Reactive
from typing import Dict


class Selector(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    color: Reactive[str] = Reactive("blue")

    def __init__(self, field: str, config: Dict) -> None:
        self.field = field
        self.config = config
        self.el = config[field]
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
            self.el = [self.el[1], *self.el[2:], self.el[0]]
        elif event.key == "down":
            self.el = [self.el[-1], *self.el[0:-1]]
        self.config[self.field] = self.el
        self.refresh()

    def render(self) -> RenderableType:
        table = Table(
            box=box.SIMPLE,
            expand=True,
            title_style="bold",
            padding=(0, 0, 0, 0),
            show_header=False,
        )

        table.add_column(justify="center")

        for i, e in enumerate(self.el):
            table.add_row(
                e,
                style=f"black on {self.color}" if i == 0 else "white",
                end_section=True,
            )

        return Panel(
            table,
            border_style="green" if self.mouse_over else "blue",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            title=self.field,
        )
