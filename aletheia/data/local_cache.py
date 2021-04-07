import logging

from aletheia.data import File
from aletheia.data.connectors.azure_datalake_connector import Azure_datalake_connector
import os

CONNECTORS = {
    "DATALAKE": Azure_datalake_connector
}
class LocalCache:
    def __init__(self, location=".", logger=None):
        self.location = location
        self.logger = logger or logging.getLogger('dummy')


    def download(self, file: File, overwrite=False):
        path = os.path.join(self.location, file.id)
        try:
            os.makedirs(path, exist_ok=overwrite)
        except OSError:
            self.logger.debug("File Exists")
            return

        self.logger.info(f"Downloading File: {file.path}")
        con = Azure_datalake_connector()
        con.download(file.path, path)

