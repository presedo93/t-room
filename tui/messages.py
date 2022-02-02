from textual.message import Message
from textual.message_pump import MessagePump


class InputCommand(Message, bubble=True):
    def __init__(self, sender: MessagePump, *, action: str = None, cmd: str = None, val: str = None) -> None:
        super().__init__(sender)
        self.action = action if action is not None else None
        self.cmd = cmd if cmd is not None else None
        self.val = val if val is not None else None

class ConfigCommand(Message, bubble=True):
    def __init__(self, sender: MessagePump, *, cmd: str = None, val: str = None) -> None:
        super().__init__(sender)
        self.cmd = cmd if cmd is not None else None
        self.val = val if val is not None else None
