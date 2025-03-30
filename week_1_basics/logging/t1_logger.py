import logging
from random import randint, uniform
from functools import wraps
import time


class Logger:

    def __init__(self, func):
        self._func = func
        self._logger = logging.getLogger(func.__name__)
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        res = self._func(*args, **kwargs)  # Decide type of log message by this value
        exec_time = time.time() - start_time

        match exec_time:
            case exec_time if exec_time < 0.02:
                self._logger.info(f"Time of execution: {exec_time}")
            case exec_time if exec_time < 0.04:
                self._logger.warning(f"Time of execution: {exec_time}")
            case exec_time if exec_time < 0.048:
                self._logger.error(f"Time of execution: {exec_time}")
            case _:
                self._logger.critical(f"Time of execution: {exec_time}")


@Logger
def func():
    time.sleep(uniform(0.01, 0.06))
    return randint(1, 1000)

@Logger
def func_manual(a: float, b: float) -> int:
    time.sleep(uniform(a, b))
    return randint(1, 1000)


logging.basicConfig(
    filename="t1.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger_obj = Logger(func)

nums = [func() for i in range(25)]
nums2 = [func_manual(0.001, 0.03) for i in range(50)]
