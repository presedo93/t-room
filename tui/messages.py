from textual.message import Message
from textual.message_pump import MessagePump


class NewCommand(Message, bubble=True):
    def __init__(self, sender: MessagePump, receiver: str, cmd: str) -> None:
        super().__init__(sender)
        self.receiver = receiver
        self.cmd = cmd


class GridCommand(Message, bubble=True):
    def __init__(self, sender: MessagePump, receiver: str, cmd: str) -> None:
        super().__init__(sender)
        self.receiver = receiver
        self.cmd = cmd
