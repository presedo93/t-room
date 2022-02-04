from textual.views import GridView

from tools.utils import open_conf
from tui.widgets.info import Info
from tui.widgets.params import Params
from tui.widgets.status import Status
from tui.widgets.configs import Configs
from tui.widgets.tickers import Tickers
from tui.widgets.selector import Selector


class DashGrid(GridView):
    def on_mount(self) -> None:
        """Make a simple grid arrangement."""

        self.grid.add_column(fraction=1, name="left")
        self.grid.add_column(fraction=1, name="leftcent")
        self.grid.add_column(fraction=2, name="rightcent")
        self.grid.add_column(fraction=2, name="right")

        self.grid.add_row(fraction=1, name="top")
        self.grid.add_row(fraction=1, name="midtop")
        self.grid.add_row(fraction=1, name="middle")
        self.grid.add_row(fraction=1, name="midbot")
        self.grid.add_row(fraction=1, name="bottom")

        self.grid.add_areas(
            configs="left-start|leftcent-end,top",
            central="rightcent-start|right-end,top-start|midbot-end",
            status="left-start|right-end,bottom",
            market="left,middle",
            strategies="leftcent,middle",
            optim="left,midtop",
            forward="leftcent, midtop",
            tickers="left-start|leftcent-end,midbot",
        )

        conf = open_conf("conf/conf.json")

        self.tickers = Tickers()
        self.status = Status()
        self.configs = Configs(conf)
        self.info = Info()
        self.optim = Params("optimize", conf["optimize"])
        self.forward = Params("forward")

        self.grid.place(
            configs=self.configs,
            central=self.info,
            status=self.status,
            tickers=self.tickers,
            market=Selector("markets", conf["brokers"]),
            strategies=Selector("strategies", ["goldencross", "macd+rsi", "bollinger"]),
            optim=self.optim,
            forward=self.forward,
        )
