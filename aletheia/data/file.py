from enum import Enum

from _proto import file_pb2
from google.protobuf import json_format
from uuid import uuid5, NAMESPACE_URL


class File:
    """
    Supported data storage connectors i.e where the file lives
    """
    CONNECTORS = Enum('CONNECTORS', file_pb2.File.Connector.items())

    def __init__(self, path, connector: CONNECTORS, mime_type: str = "", meta="", is_directory=None):
        self.path = path
        self.connector = connector
        self.mime_type = mime_type
        self.meta = meta
        self.is_directory = is_directory
        if is_directory is None:
            self.is_directory = path[-1] in ["/", "\\"]

        self.id = str(uuid5(NAMESPACE_URL, path))

    def to_proto(self):
        """
        Make the protobuff version of this class
        :return:
        """
        proto = file_pb2.File(
            id=self.id,
            path=self.path,
            connector=self.connector.value,
            mime_type=self.mime_type,
            meta=self.meta,
            is_directory=self.is_directory
        )
        return proto

    def to_dict(self):
        """
        :return: Dict type of class from protobuff
        """
        return json_format.MessageToDict(self.to_proto(), including_default_value_fields=True, preserving_proto_field_name=True)

    @staticmethod
    def from_proto(proto:file_pb2.File):
        """
        Build File from proto object `file_pb2.File` object
        :param proto: protobuff file (file_pb2.File)
        :return: File object
        """

        f = File(path=proto.path, connector=File.CONNECTORS(proto.connector),
                 mime_type=proto.mime_type, meta=proto.meta,
                 is_directory=proto.is_directory)
        f.id = proto.id
        return f

    @staticmethod
    def from_dict(source:dict):
        """
        Build File from dict
        :param source: dict
        :return: File object
        """
        proto = json_format.ParseDict(source, file_pb2.File())
        return File.from_proto(proto)
