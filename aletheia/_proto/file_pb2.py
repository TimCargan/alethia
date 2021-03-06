# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aletheia/_proto/file.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='aletheia/_proto/file.proto',
  package='aletheia',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x61letheia/_proto/file.proto\x12\x08\x61letheia\"\xb4\x02\n\x04\x46ile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12+\n\tconnector\x18\x03 \x01(\x0e\x32\x18.aletheia.File.Connector\x12\x11\n\tmime_type\x18\x04 \x01(\t\x12\x14\n\x0cis_directory\x18\x05 \x01(\x08\x12\x0c\n\x04meta\x18\x11 \x01(\t\x12\r\n\x03md5\x18\x12 \x01(\tH\x00\x12\x0e\n\x04sha1\x18\x13 \x01(\tH\x00\x12\x10\n\x06sha256\x18\x14 \x01(\tH\x00\"q\n\tConnector\x12\t\n\x05LOCAL\x10\x00\x12\x13\n\x0f\x41ZURE_DATA_LAKE\x10\x01\x12\x12\n\x0eGCP_FILE_STORE\x10\x02\x12\x0b\n\x07GIT_HUB\x10\x03\x12\x14\n\x10\x41ZURE_DATABRICKS\x10\x04\x12\r\n\tFIRESTORE\x10\x05\x42\n\n\x08\x63hecksumb\x06proto3'
)



_FILE_CONNECTOR = _descriptor.EnumDescriptor(
  name='Connector',
  full_name='aletheia.File.Connector',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AZURE_DATA_LAKE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GCP_FILE_STORE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GIT_HUB', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AZURE_DATABRICKS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIRESTORE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=224,
  serialized_end=337,
)
_sym_db.RegisterEnumDescriptor(_FILE_CONNECTOR)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='aletheia.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='aletheia.File.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='aletheia.File.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connector', full_name='aletheia.File.connector', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='aletheia.File.mime_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_directory', full_name='aletheia.File.is_directory', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='aletheia.File.meta', index=5,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='md5', full_name='aletheia.File.md5', index=6,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sha1', full_name='aletheia.File.sha1', index=7,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sha256', full_name='aletheia.File.sha256', index=8,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FILE_CONNECTOR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='checksum', full_name='aletheia.File.checksum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=41,
  serialized_end=349,
)

_FILE.fields_by_name['connector'].enum_type = _FILE_CONNECTOR
_FILE_CONNECTOR.containing_type = _FILE
_FILE.oneofs_by_name['checksum'].fields.append(
  _FILE.fields_by_name['md5'])
_FILE.fields_by_name['md5'].containing_oneof = _FILE.oneofs_by_name['checksum']
_FILE.oneofs_by_name['checksum'].fields.append(
  _FILE.fields_by_name['sha1'])
_FILE.fields_by_name['sha1'].containing_oneof = _FILE.oneofs_by_name['checksum']
_FILE.oneofs_by_name['checksum'].fields.append(
  _FILE.fields_by_name['sha256'])
_FILE.fields_by_name['sha256'].containing_oneof = _FILE.oneofs_by_name['checksum']
DESCRIPTOR.message_types_by_name['File'] = _FILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'aletheia._proto.file_pb2'
  # @@protoc_insertion_point(class_scope:aletheia.File)
  })
_sym_db.RegisterMessage(File)


# @@protoc_insertion_point(module_scope)
