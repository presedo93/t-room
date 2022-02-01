from textual.views import GridView

from textual.widgets import Placeholder

# from tui.widgets.params import Params
from tui.widgets.status import Status

# from tui.widgets.selector import Selector

from tui.widgets.tickers import Tickers

from tui.messages import NewCommand


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
            area1="left-start|leftcent-end,top",
            central="rightcent-start|right-end,top-start|midbot-end",
            status="left-start|right-end,bottom",
            area5="left,middle",
            area6="leftcent,middle",
            area7="left,midtop",
            area8="leftcent, midtop",
            tickers="left-start|leftcent-end,midbot",
        )

        self.tickers = Tickers()
        self.status = Status()

        self.grid.place(
            area1=Placeholder(name="area1"),
            central=Placeholder(name="central"),
            status=self.status,
            tickers=self.tickers,
            area5=Placeholder(name="area5"),
            area6=Placeholder(name="area6"),
            area7=Placeholder(name="area7"),
            area8=Placeholder(name="area8"),
        )

    async def handle_grid_command(self, message: NewCommand) -> None:
        print("ttthereee")
