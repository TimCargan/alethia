from __future__ import annotations
import uuid
from datetime import datetime
from aletheia.data import Dataset
from contextlib import contextmanager
from google.cloud.firestore import DocumentReference
from google.cloud import firestore


class Experiment:
    RUNNING = "Running"
    COMPLETE = "Complete"
    FAILED = "Failed"

    def __init__(self, name: str, ex_doc: DocumentReference, ms, debug:bool=False, parents:[str]=None):
        if parents is None:
            parents = []
        self._name:str = name
        self._client = ms
        self._doc_ref = ex_doc
        self._debug:bool = debug

        # ID info
        self._parents = parents
        self._parents_path = "/".join(parents)
        self._uuid: str = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{self._parents_path}/{name}"))

        # Rate limit writing
        self._write_blocked:bool = False
        self._write_limit = 5 # Batch updates so we only write updates every 5 seconds
        self._delta: dict = {}
        self._last_update = datetime.now()

        # Keys to save to the document
        self._doc_keys = ["status", "metrics", "hyper_params"]

        self._start_time = None
        self._end_time = None
        self._status = "Unknown"
        self._metrics = {}
        self._hyper_params = None
        self._datasets_used = []


        # Write empty expr to db, creates document
        self._partial_update({"status": self._status})

    def __setattr__(self, key, value):
        """
        This overrides the set att functions of the class
        Enables .asingment notation
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
            self._batch_write({key: value})

    def start_sub_exper(self, run_id=None, collection:str="runs") -> Experiment:
        run_id = run_id if run_id is not None else self._run_id()
        run_col = self._doc_ref.collection(collection)
        run_doc = run_col.document(run_id)
        run = Experiment(run_id, run_doc, self._client, parents=self._parents.append(self._name))
        return run.start()

    @contextmanager
    def start(self):
        try:
            self._start_time = firestore.SERVER_TIMESTAMP
            self._partial_update({"start_time": self.start_time,
                                  "status": self.RUNNING})
            yield self
            self.status = self.COMPLETE
        except Exception as e:
            self.status = self.FAILD
            self.add_metric("Error", str(e))
            raise e
        finally:
            # Write everything to the metastore
            self._end_time = firestore.SERVER_TIMESTAMP
            self._full_write()
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
        :return: The run id, a UUID5 generated using the URL namespace and the path to the experiment
        """
        return self._uuid

    ###################################################################################################
    ###################             Update and DB management                    #######################
    ###################################################################################################

    def _full_write(self):
        """
        Build a dict representation of the experiment and Write the run to the db
        :return:
        """
        d = {k: v for k,v in self.__dict__.items() if k in self._doc_keys and v is not None}
        self._partial_update(d)

    def _flush(self):
        """
        Flush delta dict to the database and update the last write time
        @return:
        """
        self._partial_update(self._delta)
        self._delta = {}
        self._last_update = datetime.now()

    def _batch_write(self, update:dict):
        """
        Batch object updates together so that they can be written as a batch update
        This works by building a dict of updates and only writing if an update comes after the set write limit (default 5 seconds)
        if no other updates are called (and flush is not called) the updates will be written at experiment close
        @param update:
        @return:
        """
        self._delta = self._delta | update
        if (self._last_update - datetime.now()).seconds > self._write_limit:
            self._flush()

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
        self._batch_write({"description": value})

    # TODO: write this to the db when called
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status
        self._batch_write({"status": status})


    # TODO: write this to the db when called
    @property
    def hyper_params(self):
        return self._hyper_params

    @hyper_params.setter
    def hyper_params(self, hps: dict):
        self._hyper_params = hps
        self._batch_write({"hyper_params": hps})

    @property
    def metrics(self):
        return self._metrics
    @metrics.setter
    def metrics(self, value):
        return

    # TODO: write this to the db when called
    def add_metric(self, name: str, value):
        """
        Add a single value to the experiment metrics
        :param name: name of the metric
        :param value: value of the metric
        :return:
        """
        self._metrics[name] = value
        self._batch_write({f"metrics.{name}": value})

    def add_metrics(self, metrics:dict):
        """
        Merge in a dict of metrics
        #TODO Make this a single commit
        :param metrics: dict of metrics to add
        :return:
        """
        for k, v in metrics.items():
            self.add_metric(k,v)

    def add_artifact(self, name: str, path, is_local=True, is_dir=True, upload_file=True):
        pass
