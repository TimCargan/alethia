from google.cloud import storage
from google.cloud.storage.blob import Blob

class GCS_connector:

    def __init__(self):
        self.storage_client = storage.Client("alethea-fcf82")

    def download(self, source, target):
        """

        :param source: gs:// path to file
        :param target: location to download
        :return:
        """
        bucket = self.storage_client.bucket("data")

        blob = Blob.from_string(source)
        blob.download_to_filename(target)