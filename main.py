import os

import pandas as pd
import numpy as np
import logging
import unittest
import argparse

from log_config import setup_logging
from data_handling import DataHandler

from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.gofplots import qqplot
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.seasonal import seasonal_decompose

from tqdm import tqdm
from itertools import product
from typing import Union

import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import warnings

warnings.filterwarnings('ignore')

def setup_logging(level):
    """
    Set up logging with a specified level.
    """
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {level}')
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def configure_parser():
    """
    Configures and returns an argparse.ArgumentParser instance for command-line arguments.

    :returns parser:
    """
    arg_parser = argparse.ArgumentParser(description="Initial Data Processing")

    arg_parser.add_argument("--log-level", dest="log_level", default="DEBUG",
                            help="Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    arg_parser.add_argument("--file-path", default="/dev/transport_data.csv",
                            help="Path to the .csv file, if different from /dev/transport-data.csv")

    return arg_parser


def main(args):
    """
    Main function that initializes the data handler [...] operations

    :return:
    """

    try:
        handle_data = DataHandler(args.file_path)
        logging.debug("Test")
    except FileNotFoundError as e:
        logging.error(e)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    """
    Optional command line commands for passing.
    """
    parser = configure_parser()
    args = parser.parse_args()
    setup_logging(args.log_level)
    main(args)
