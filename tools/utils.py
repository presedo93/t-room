import os
import json
import argparse

from typing import Dict, Tuple
from datetime import timedelta
from datetime import datetime as dt


def str2bool(v: str) -> bool:
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


def open_conf(conf_path: str) -> Dict:
    with open(os.path.join(os.getcwd(), conf_path), "r") as f:
        conf = json.load(f)

    return conf


def time_period(days: int = 0, offset: int = 0) -> Tuple[str, str]:
    end = dt.today() - timedelta(days=offset)
    start = end - timedelta(days=days)
    return start.strftime("%Y-%b-%d %H:%M:%S"), end.strftime("%Y-%b-%d %H:%M:%S")