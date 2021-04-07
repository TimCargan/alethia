from uuid import uuid5, NAMESPACE_URL

from _proto import dataset_pb2
from google.protobuf import json_format
from tensorflow import io
import tensorflow as tf

from data.file import File

TYPES = {
    "int": tf.int64,
    "float": tf.float32,
    "string": tf.string
}

class Dataset:
    def __init__(self, name: str, file: File=None, features:dict={}, meta:str= "",
                 split_into_folds:bool=False, number_of_folds:int=0, **kwargs):
        self.name = name
        self.features = features
        self.meta = meta
        self.location = file

        self.split_into_folds = split_into_folds
        self.number_of_folds = number_of_folds

        self.id = str(uuid5(NAMESPACE_URL, name))

    @staticmethod
    def _make_feature_proto(features: dict):
        """
        Convert features to be used with proto. The conversion maps the "type" dict -> protobuff DataSet.Type()
        :param features: feature dict
        :return: feature dict with proto types
        """
        return {k: dataset_pb2.Dataset.Type(dtype=v["dtype"], shape=v["shape"]) for k, v in features.items()}

    def to_proto(self) -> dataset_pb2.Dataset:
        """
        Make the protobuff version of this class
        :return:
        """
        proto = dataset_pb2.Dataset(
            id=self.id,
            name=self.name,
            features=self._make_feature_proto(self.features), # must be type:{ "str-key": DataSet.Type() msg)
            meta=self.meta,
            split_into_folds = self.split_into_folds,
            number_of_folds = self.number_of_folds
        )
        if self.location:
            proto.file.MergeFrom(self.location.to_proto())
        return proto

    def to_dict(self) -> dict:
        """
        :return: Dict type of class from protobuff
        """
        return self._to_dict(self.to_proto())

    @staticmethod
    def _to_dict(proto: dataset_pb2.Dataset) -> dict:
        return json_format.MessageToDict(proto, including_default_value_fields=True,
                                  preserving_proto_field_name=True)

    @staticmethod
    def from_dict(source: dict):
        source["file"] = File.from_dict(source["file"])
        return Dataset(**source)

    @staticmethod
    def from_proto(proto: dataset_pb2.Dataset):
        return Dataset.from_dict(Dataset._to_dict(proto))

    def get_tf_features_dict(self):
        """
        Gets the feature dict of the dataset for reading as a TFRecord
        :return: {"col", FixedLenFeature(shape, type)
        """
        types = self.features
        features = {}
        for k,v in types:
            features[k] = io.FixedLenFeature(v.shape, TYPES[v.dtype])
        return  features




