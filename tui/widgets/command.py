from rich import box
from rich.panel import Panel

from textual import events
from textual.keys import Keys
from textual.widget import Widget
from textual.reactive import Reactive

from tui.messages import InputCommand


class Command(Widget):
    has_focus: Reactive[bool] = Reactive(False)
    mouse_over: Reactive[bool] = Reactive(False)
    text: Reactive[str] = Reactive("")

    async def on_focus(self) -> None:
        self.has_focus = True

    async def on_blur(self) -> None:
        self.has_focus = False

    async def on_enter(self) -> None:
        self.mouse_over = True

    async def on_leave(self) -> None:
        self.mouse_over = False

    async def on_key(self, event: events.Key) -> None:
        if event.key == Keys.ControlH:
            self.text = self.text[:-1]
        elif event.key == Keys.Enter:
            t_split = self.text.split()
            t_len = len(t_split)
            if t_len == 1:
                action, cmd, val = t_split[0], None, None
            elif t_len == 2:
                action, cmd, val = t_split[0], t_split[1], None
            elif t_len == 3:
                action, cmd, val = t_split[0], t_split[1], t_split[2]
            else:
                action, cmd, val = None, None, None
            await self.emit(InputCommand(self, action=action, cmd=cmd, val=val))
        elif event.key == Keys.ControlC:
            pass
        else:
            self.text += event.key

    def render(self) -> Panel:
        return Panel(
            f"[b yellow]>>>[/] {self.text}",
            box=box.HEAVY if self.has_focus else box.ROUNDED,
            border_style="green" if self.mouse_over else "blue",
        )
