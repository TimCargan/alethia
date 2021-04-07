from abc import ABC, abstractmethod

class StorageConnector(ABC):
    @abstractmethod
    def exisit(self, path):
        pass
    @abstractmethod
    def download(self, source, target):
        pass
    @abstractmethod
    def upload(self, source, target):
        pass