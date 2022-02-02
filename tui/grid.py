from textual.views import GridView

from textual.widgets import Placeholder

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
            area7="left,midtop",
            area8="leftcent, midtop",
            tickers="left-start|leftcent-end,midbot",
        )

        self.tickers = Tickers()
        self.status = Status()
        self.configs = Configs()
        self.params = Params()

        self.grid.place(
            configs=self.configs,
            central=self.params,
            status=self.status,
            tickers=self.tickers,
            market=Selector("markets", ["kryptos", "stocks", "futures"]),
            strategies=Selector("strategies", ["goldencross", "macd+rsi", "bollinger"]),
            area7=Placeholder(name="area7"),
            area8=Placeholder(name="area8"),
        )
