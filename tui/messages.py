from textual.message import Message
from textual.message_pump import MessagePump
from typing import List


class InputCommand(Message, bubble=True):
    def __init__(
        self, sender: MessagePump, *, action: str = None, cmd: List = None
    ) -> None:
        super().__init__(sender)
        self.action = action
        self.cmd = cmd


class ConfigCommand(Message, bubble=True):
    def __init__(self, sender: MessagePump, *, cmd: List = None) -> None:
        super().__init__(sender)
        self.cmd = cmd
