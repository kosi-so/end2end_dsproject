import os
import urllib.request as request
from src.ds_project import logger
import zipfile
from src.ds_project.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    # Download Zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url= self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with follwing features: \n{headers}")

        else:
            logger.info("File already exists")

    # Extract zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
