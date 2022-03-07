from textual.message import Message
from textual.message_pump import MessagePump
from typing import Dict, List


class InputCommand(Message, bubble=True):
    def __init__(
        self, sender: MessagePump, *, action: str = None, cmd: List = None
    ) -> None:
        super().__init__(sender)
        self.action = action
        self.cmd = cmd


class ParamsCommand(Message, bubble=True):
    def __init__(self, sender: MessagePump, *, params: Dict = None) -> None:
        super().__init__(sender)
        self.params = params


class RunCommand(Message, bubble=True):
    def __init__(
        self, sender: MessagePump, *, task: str = None, params: Dict = None
    ) -> None:
        super().__init__(sender)
        self.task = task
        self.params = params


class ProgressCommand(Message, bubble=True):
    def __init__(
        self, sender: MessagePump, *, task: str = None, status: Dict = None
    ) -> None:
        super().__init__(sender)
        self.task = task
        self.status = status
