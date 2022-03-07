import os
import json
import asyncio
import argparse

from datetime import timedelta
from datetime import datetime as dt

from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Dict, List, Tuple


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


def check_folders() -> None:
    """Check if subfolders already exist."""
    if os.path.exists("strategies") is False:
        os.makedirs("strategies", exist_ok=True)


async def run_func_async(
    func: Callable, func_args: List[Any], executor: ThreadPoolExecutor
):
    if asyncio.iscoroutinefunction(func):
        return await func(*func_args)
    else:
        return await asyncio.get_event_loop().run_in_executor(
            func=lambda: func(*func_args), executor=executor
        )
