import argparse
import functools
import json
import tqdm
from azure.datalake.store import core, lib, multithread
import os
import glob
import enlighten
# from aletheia.data.connectors.connector import StorageConnector


class Azure_datalake_connector():
    def __init__(self):
        with open("./adls.key") as f:
            adls_info = json.load(f)
        self.adl = core.AzureDLFileSystem(lib.auth(**adls_info), store_name=adls_info["store_name"])

    def exists(self, path):
        """
        See if file exists at given path
        :param path: path
        :return: Bool (True if file exits)
        """
        return self.adl.exists(path)

    def download(self, source, target):
        os.makedirs(target, exist_ok=True)
        pbar = enlighten.Counter()

        progres = tqdm.tqdm(unit_scale=True, unit='B', unit_divisor=1024)
        multithread.ADLDownloader(self.adl, source, target, 5, 2**24, overwrite=True,
                                  progress_callback=functools.partial(self._prog, progres))


    def upload(self, source, target):
        progres = tqdm.tqdm(unit_scale=True, unit='B', unit_divisor=1024)
        multithread.ADLUploader(self.adl, target, source, 10, overwrite=True,
                                progress_callback=functools.partial(self._prog, progres))

    def _prog(self, p, curr, total):
        p.total = total
        p.update(curr - p.n)

