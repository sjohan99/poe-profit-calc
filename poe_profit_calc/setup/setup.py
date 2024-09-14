import logging
import sys

from fastapi import Depends, FastAPI
from poe_profit_calc.fetcher import FileFetcher, HttpFetcher
from poe_profit_calc.prices import Pricer
from poe_profit_calc.setup.logger import LoggingFormatter
from poe_profit_calc.setup.ratelimiting import RateLimiter
from poe_profit_calc.setup.settings import get_settings
from poe_profit_calc.sourcemappings import ENDPOINT_MAPPING, FILE_PATH_MAPPING


class App:
    def __init__(self):
        initialize_logging()
        settings = get_settings()

        if settings.ENV == "prod":
            price_fetcher = Pricer(
                fetcher=HttpFetcher(),
                source_mapping=ENDPOINT_MAPPING,
            )
        else:
            price_fetcher = Pricer(fetcher=FileFetcher(), source_mapping=FILE_PATH_MAPPING)

        rate_limiter = RateLimiter(
            requests_limit=settings.REQUEST_LIMIT_PER_MINUTE, time_window=60, limit_globally=True
        )

        app = FastAPI(dependencies=[Depends(rate_limiter)])
        self.app = app
        self.price_fetcher = price_fetcher
        self.settings = settings
        logging.info(f"Initialized app in {settings.ENV} mode")


def initialize_logging():
    logFormatter = LoggingFormatter()
    logging_handlers = [
        logging.StreamHandler(sys.stdout),
    ]
    for handler in logging_handlers:
        handler.setFormatter(logFormatter)
    logging.basicConfig(level=logging.INFO, handlers=logging_handlers)
