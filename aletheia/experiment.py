from datetime import datetime

from data import Dataset
from contextlib import contextmanager
from google.cloud.firestore import DocumentReference
from google.cloud import firestore


class Experiment:
    def __init__(self, name: str, ex_doc: DocumentReference, ms, debug:bool=False, **kwargs):
        self._name = name
        self._client = ms
        self._doc_ref = ex_doc
        self._write_blocked = False
        self._debug = debug

        # Keys to save to the document
        self._doc_keys = ["status", "metrics", "hyper_params"]

        self._start_time = None
        self._end_time = None
        self._status = "Unknown"
        self._metrics = {}
        self._hyper_params = None
        self._datasets_used = []

        # Write empty expr to db, creates document
        self._doc_ref.set({"status": self._status})

    def __setattr__(self, key, value):
        """
        This overides the set att functions of the class
        Eables .asingment notation
        :param key:
        :param value:
        :return:
        """
        if key[:1] == "_":  # Private keys can be set without issue
            super().__setattr__(key, value)
        else:
            #TODO: check types are db safe here
            self._doc_keys.append(key)
            super().__setattr__(key, value)
            self._partial_update({key: value})

    def start_sub_exper(self, run_id=None, collection:str="runs"):
        run_id = run_id if run_id is not None else self._run_id()
        run_col = self._doc_ref.collection(collection)
        run_doc = run_col.document(run_id)
        run = Experiment(run_id, run_doc, self._client)
        return run.start()

    @contextmanager
    def start(self):
        try:
            self._start_time = firestore.SERVER_TIMESTAMP
            self._partial_update({"start_time": self.start_time})
            self.status = "Running"
            yield self
            self.status = "Complete"
        except Exception as e:
            self.status = "Failed"
            self.add_metric("Error", str(e))
            raise e
        finally:
            # Write everything to the metastore
            self._full_write()
            self._end_time = firestore.SERVER_TIMESTAMP
            self._partial_update({"end_time": self.end_time})

    def using_dataset(self, name):
        """
        Track that a dataset has been used
        :param name:
        :return:
        """
        self._datasets_used += [name]
        self._partial_update({"datasets_used": firestore.ArrayUnion([name])})

    def load_dataset(self, name) -> Dataset:
        """
        Load the dataset from the metastore
        Track that the dataset has been used
        :param name:
        :return: dataset
        """
        ds = self._client.get_dataset(name)
        if ds:
            self.using_dataset(name)
            return ds

    def _run_id(self) -> str:
        """
        Make a new run id
        TODO: make this better, for now just the time
        :return: a run id
        """
        return str(datetime.now())

    def _full_write(self):
        """
        Write the run to the db, its stupid
        :return:
        """
        d = {k: v for k,v in self.__dict__.items() if k in self._doc_keys and v is not None}
        self._doc_ref.update(d)

    def _partial_write(self):
        """
        Unimplemented
        :return:
        """
        self._full_write()
        pass

    def _partial_update(self, update: dict):
        """
        Update the given values in the dict
        :param update: values to update, use dot notation to update maps e,g `map.key` otherwise the map will be overwritten
        :return:
        """
        if not self._write_blocked:
            self._doc_ref.update(update)

    @property
    def datasets_used(self):
        return self._datasets_used
    @datasets_used.setter
    def datasets_used(self, value):
        return

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        return

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        return

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value:str):
        self._description = value
        self._partial_update({"description": value})

    # TODO: write this to the db when called
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status
        self._partial_update({"status": status})


    # TODO: write this to the db when called
    @property
    def hyper_params(self):
        return self._hyper_params

    @hyper_params.setter
    def hyper_params(self, hps: dict):
        self._hyper_params = hps
        self._partial_update({"hyper_params": hps})

    @property
    def metrics(self):
        return self._metrics
    @metrics.setter
    def metrics(self, value):
        return

    # TODO: write this to the db when called
    def add_metric(self, name: str, value):
        self._metrics[name] = value
        self._partial_update({f"metrics.{name}": value})

    def add_artifact(self, name: str, path, is_local=True, is_dir=True, upload_file=True):
        pass
