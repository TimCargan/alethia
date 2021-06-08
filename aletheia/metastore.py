from typing import Optional
from google.cloud import firestore
from aletheia.data import Dataset, File
from aletheia.experiment import Experiment


class Metastore:
    """
    MetaStore Interface
    """
    def __init__(self, project="defult", gcp_project=None):
        self._client = firestore.Client(gcp_project)
        self._project_doc = self._client.collection("projects").document(project)
        self.project_root = f"projects/{project}"
        self.project = project

    def _doc(self, path: str) -> firestore.DocumentReference:
        """
        Build a document reference from the project root
        can be used in place of code such us:
         self._project_doc.collection("col").document(id)
         -> self._doc(f"col/{id})
        :param path:
        :return:
        """
        return self._client.document(f"{self.project_root}/{path}")

    def add_metadata(self, name, meta: dict, overwrite: bool = False):
        """
        Add named metadata to the system
        Meta data will be stored in the project db
        Meta data can be any dict object
        :param name: name
        :param meta: Dict metadata to save
        :param overwrite: overwrite existing metadata, default false
        :return:
        """
        files = self._project_doc.collection("metadata")
        doc = files.document(name)
        if doc.get().exists and not overwrite:
            return
        doc.set(meta)

    def get_metadata(self, name: str) -> dict:
        """
        Get metadata by name
        :param name: matadata name
        :return: dict if matadata exists, otherwise None
        """
        md = self._doc(f"metadata/{name}")
        return md.get().to_dict()

    def get_file_by_id(self, id: str) -> File:
        file = self._doc(f"files/{id}").get()
        if file.exists:
            file_dict = file.to_dict()
            return File.from_dict(file_dict)

    def register_file(self, file: File):
        files = self._project_doc.collection("files")
        if files.document(file.id).get().exists:
            return False
        files.add(file.to_dict(), file.id)

    def get_dataset(self, name: str) -> Optional[Dataset]:
        dataset_doc = self._doc(f"datasets/{name}").get()
        if dataset_doc.exists:
            dataset_dict = dataset_doc.to_dict()
            return Dataset.from_dict(dataset_dict)
        return None

    def register_dataset(self, dataset: Dataset) -> bool:
        """
        Register a new dataset in the system
        Split out location and dataset and write them to the database
        If dataset exists, nothing will happen
        :param dataset: Dataset to register
        :return:
        """
        # Split out dataset object
        file = dataset.location
        file_dict = file.to_dict()
        dataset_dict = dataset.to_dict()
        # dataset_proto.file_id = file.id # Don't save file object in top level document

        # Build firestore references
        transaction = self._client.transaction()
        dataset_col = self._project_doc.collection(f"datasets")
        dataset_doc = dataset_col.document(dataset.name)

        # Write to firestore
        @firestore.transactional
        def write_dataset(transaction, dataset):
            # Check if dataset exsits
            if dataset.get(transaction=transaction).exists:
                return False
            transaction.set(dataset, dataset_dict)
            # transaction.set(file, file_dict)
            return True
        return write_dataset(transaction, dataset_doc)

    def get_expr(self, name) -> Experiment:
        exp_doc_ref = self._doc(f"experiments/{name}")
        if not exp_doc_ref.get().exists:
            raise NameError(f'No Experiment with the name \'{name}\' has been run')

        #This should be a readonly version
        return Experiment(name, exp_doc_ref, self)

    def start_expr(self, name, debug:bool=False, **kwargs) -> Experiment:
        """
        Build an new experiment object
        :param name:
        :param debug:
        :param kwargs:
        :return: A context managed experiment
        """
        exp_doc_ref = self._doc(f"experiments/{name}")
        if not debug and exp_doc_ref.get().exists:
            raise NameError(f'An Experiment with the name \'{name}\' has been run')

        exp = Experiment(name, exp_doc_ref, self, debug=debug)
        return exp.start()




