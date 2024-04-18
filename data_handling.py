import pandas as pd
import logging
import os


class DataHandler:
    """
    Manage loading data
    Aggregating on a monthly basis
    Visualising

    """

    def __init__(self, file_name: str):
        """
        Class to handle data loading and basic processing.
        """
        self.file_name = file_name
        self.transport_data = None
        self.logger = logging.getLogger(__name__)
        self.check_file_exists()

    def check_file_exists(self):
        """
        Checks if the file exists at the given path.
        Raises FileNotFoundError if the file does not exist.
        """
        if not os.path.isfile(self.file_name):
            self.logger.error(f"File not found: {self.file_name}")
            raise FileNotFoundError(f"File not found: {self.file_name}")
        else:
            self.logger.info(f"File exists: {self.file_name}")
            self.load_data()

    def load_data(self):
        """
        Loads data from CSV to DataFrame
        """
        try:
            self.transport_data = pd.read_csv(self.file_name)
            self.logger.info("Dataset loaded successfully.")
        except pd.errors.ParserError as e:
            self.logger.error(f"Error parsing the file: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            raise