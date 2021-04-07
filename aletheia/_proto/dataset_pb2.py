# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _proto/dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _proto import file_pb2 as __proto_dot_file__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='_proto/dataset.proto',
  package='alethaia',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14_proto/dataset.proto\x12\x08\x61lethaia\x1a\x11_proto/file.proto\"\xe5\x02\n\x07\x44\x61taset\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1e\n\x04\x66ile\x18\x03 \x01(\x0b\x32\x0e.alethaia.FileH\x00\x12\x11\n\x07\x66ile_id\x18\x04 \x01(\tH\x00\x12\x31\n\x08\x66\x65\x61tures\x18\x05 \x03(\x0b\x32\x1f.alethaia.Dataset.FeaturesEntry\x12\x0c\n\x04meta\x18\x11 \x01(\t\x12\x18\n\x10split_into_folds\x18\x12 \x01(\x08\x12\x17\n\x0fnumber_of_folds\x18\x13 \x01(\x03\x12\x1e\n\x06source\x18\x19 \x01(\x0b\x32\x0e.alethaia.File\x1a$\n\x04Type\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\r\n\x05\x64type\x18\x02 \x01(\t\x1aG\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.alethaia.Dataset.Type:\x02\x38\x01\x42\n\n\x08locationb\x06proto3'
  ,
  dependencies=[__proto_dot_file__pb2.DESCRIPTOR,])




_DATASET_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='alethaia.Dataset.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape', full_name='alethaia.Dataset.Type.shape', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dtype', full_name='alethaia.Dataset.Type.dtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=326,
)

_DATASET_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='alethaia.Dataset.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='alethaia.Dataset.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='alethaia.Dataset.FeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=399,
)

_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='alethaia.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='alethaia.Dataset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='alethaia.Dataset.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='alethaia.Dataset.file', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_id', full_name='alethaia.Dataset.file_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='alethaia.Dataset.features', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='alethaia.Dataset.meta', index=5,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split_into_folds', full_name='alethaia.Dataset.split_into_folds', index=6,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_of_folds', full_name='alethaia.Dataset.number_of_folds', index=7,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='alethaia.Dataset.source', index=8,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATASET_TYPE, _DATASET_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='location', full_name='alethaia.Dataset.location',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=54,
  serialized_end=411,
)

_DATASET_TYPE.containing_type = _DATASET
_DATASET_FEATURESENTRY.fields_by_name['value'].message_type = _DATASET_TYPE
_DATASET_FEATURESENTRY.containing_type = _DATASET
_DATASET.fields_by_name['file'].message_type = __proto_dot_file__pb2._FILE
_DATASET.fields_by_name['features'].message_type = _DATASET_FEATURESENTRY
_DATASET.fields_by_name['source'].message_type = __proto_dot_file__pb2._FILE
_DATASET.oneofs_by_name['location'].fields.append(
  _DATASET.fields_by_name['file'])
_DATASET.fields_by_name['file'].containing_oneof = _DATASET.oneofs_by_name['location']
_DATASET.oneofs_by_name['location'].fields.append(
  _DATASET.fields_by_name['file_id'])
_DATASET.fields_by_name['file_id'].containing_oneof = _DATASET.oneofs_by_name['location']
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {

  'Type' : _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), {
    'DESCRIPTOR' : _DATASET_TYPE,
    '__module__' : '_proto.dataset_pb2'
    # @@protoc_insertion_point(class_scope:alethaia.Dataset.Type)
    })
  ,

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATASET_FEATURESENTRY,
    '__module__' : '_proto.dataset_pb2'
    # @@protoc_insertion_point(class_scope:alethaia.Dataset.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _DATASET,
  '__module__' : '_proto.dataset_pb2'
  # @@protoc_insertion_point(class_scope:alethaia.Dataset)
  })
_sym_db.RegisterMessage(Dataset)
_sym_db.RegisterMessage(Dataset.Type)
_sym_db.RegisterMessage(Dataset.FeaturesEntry)


_DATASET_FEATURESENTRY._options = None
# @@protoc_insertion_point(module_scope)