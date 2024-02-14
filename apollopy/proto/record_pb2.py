# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/record.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/record.proto',
  package='apollo.cyber.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x12proto/record.proto\x12\x12\x61pollo.cyber.proto\"\x96\x02\n\x0bSingleIndex\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.apollo.cyber.proto.SectionType\x12\x10\n\x08position\x18\x02 \x01(\x04\x12\x39\n\rchannel_cache\x18\x65 \x01(\x0b\x32 .apollo.cyber.proto.ChannelCacheH\x00\x12\x42\n\x12\x63hunk_header_cache\x18\x66 \x01(\x0b\x32$.apollo.cyber.proto.ChunkHeaderCacheH\x00\x12>\n\x10\x63hunk_body_cache\x18g \x01(\x0b\x32\".apollo.cyber.proto.ChunkBodyCacheH\x00\x42\x07\n\x05\x63\x61\x63he\"b\n\x10\x43hunkHeaderCache\x12\x16\n\x0emessage_number\x18\x01 \x01(\x04\x12\x12\n\nbegin_time\x18\x02 \x01(\x04\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x04\x12\x10\n\x08raw_size\x18\x04 \x01(\x04\"(\n\x0e\x43hunkBodyCache\x12\x16\n\x0emessage_number\x18\x01 \x01(\x04\"^\n\x0c\x43hannelCache\x12\x16\n\x0emessage_number\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cmessage_type\x18\x03 \x01(\t\x12\x12\n\nproto_desc\x18\x04 \x01(\x0c\"D\n\rSingleMessage\x12\x14\n\x0c\x63hannel_name\x18\x01 \x01(\t\x12\x0c\n\x04time\x18\x02 \x01(\x04\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"\x91\x03\n\x06Header\x12\x15\n\rmajor_version\x18\x01 \x01(\r\x12\x15\n\rminor_version\x18\x02 \x01(\r\x12\x32\n\x08\x63ompress\x18\x03 \x01(\x0e\x32 .apollo.cyber.proto.CompressType\x12\x16\n\x0e\x63hunk_interval\x18\x04 \x01(\x04\x12\x18\n\x10segment_interval\x18\x05 \x01(\x04\x12\x19\n\x0eindex_position\x18\x06 \x01(\x04:\x01\x30\x12\x17\n\x0c\x63hunk_number\x18\x07 \x01(\x04:\x01\x30\x12\x19\n\x0e\x63hannel_number\x18\x08 \x01(\x04:\x01\x30\x12\x15\n\nbegin_time\x18\t \x01(\x04:\x01\x30\x12\x13\n\x08\x65nd_time\x18\n \x01(\x04:\x01\x30\x12\x19\n\x0emessage_number\x18\x0b \x01(\x04:\x01\x30\x12\x0f\n\x04size\x18\x0c \x01(\x04:\x01\x30\x12\x1a\n\x0bis_complete\x18\r \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0e\x63hunk_raw_size\x18\x0e \x01(\x04\x12\x18\n\x10segment_raw_size\x18\x0f \x01(\x04\"A\n\x07\x43hannel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cmessage_type\x18\x02 \x01(\t\x12\x12\n\nproto_desc\x18\x03 \x01(\x0c\"]\n\x0b\x43hunkHeader\x12\x12\n\nbegin_time\x18\x01 \x01(\x04\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x04\x12\x16\n\x0emessage_number\x18\x03 \x01(\x04\x12\x10\n\x08raw_size\x18\x04 \x01(\x04\"@\n\tChunkBody\x12\x33\n\x08messages\x18\x01 \x03(\x0b\x32!.apollo.cyber.proto.SingleMessage\"9\n\x05Index\x12\x30\n\x07indexes\x18\x01 \x03(\x0b\x32\x1f.apollo.cyber.proto.SingleIndex*{\n\x0bSectionType\x12\x12\n\x0eSECTION_HEADER\x10\x00\x12\x18\n\x14SECTION_CHUNK_HEADER\x10\x01\x12\x16\n\x12SECTION_CHUNK_BODY\x10\x02\x12\x11\n\rSECTION_INDEX\x10\x03\x12\x13\n\x0fSECTION_CHANNEL\x10\x04*E\n\x0c\x43ompressType\x12\x11\n\rCOMPRESS_NONE\x10\x00\x12\x10\n\x0c\x43OMPRESS_BZ2\x10\x01\x12\x10\n\x0c\x43OMPRESS_LZ4\x10\x02')
)

_SECTIONTYPE = _descriptor.EnumDescriptor(
  name='SectionType',
  full_name='apollo.cyber.proto.SectionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SECTION_HEADER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECTION_CHUNK_HEADER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECTION_CHUNK_BODY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECTION_INDEX', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECTION_CHANNEL', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1322,
  serialized_end=1445,
)
_sym_db.RegisterEnumDescriptor(_SECTIONTYPE)

SectionType = enum_type_wrapper.EnumTypeWrapper(_SECTIONTYPE)
_COMPRESSTYPE = _descriptor.EnumDescriptor(
  name='CompressType',
  full_name='apollo.cyber.proto.CompressType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMPRESS_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPRESS_BZ2', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPRESS_LZ4', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1447,
  serialized_end=1516,
)
_sym_db.RegisterEnumDescriptor(_COMPRESSTYPE)

CompressType = enum_type_wrapper.EnumTypeWrapper(_COMPRESSTYPE)
SECTION_HEADER = 0
SECTION_CHUNK_HEADER = 1
SECTION_CHUNK_BODY = 2
SECTION_INDEX = 3
SECTION_CHANNEL = 4
COMPRESS_NONE = 0
COMPRESS_BZ2 = 1
COMPRESS_LZ4 = 2



_SINGLEINDEX = _descriptor.Descriptor(
  name='SingleIndex',
  full_name='apollo.cyber.proto.SingleIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='apollo.cyber.proto.SingleIndex.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='apollo.cyber.proto.SingleIndex.position', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_cache', full_name='apollo.cyber.proto.SingleIndex.channel_cache', index=2,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_header_cache', full_name='apollo.cyber.proto.SingleIndex.chunk_header_cache', index=3,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_body_cache', full_name='apollo.cyber.proto.SingleIndex.chunk_body_cache', index=4,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='cache', full_name='apollo.cyber.proto.SingleIndex.cache',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=43,
  serialized_end=321,
)


_CHUNKHEADERCACHE = _descriptor.Descriptor(
  name='ChunkHeaderCache',
  full_name='apollo.cyber.proto.ChunkHeaderCache',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_number', full_name='apollo.cyber.proto.ChunkHeaderCache.message_number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='begin_time', full_name='apollo.cyber.proto.ChunkHeaderCache.begin_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='apollo.cyber.proto.ChunkHeaderCache.end_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_size', full_name='apollo.cyber.proto.ChunkHeaderCache.raw_size', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=421,
)


_CHUNKBODYCACHE = _descriptor.Descriptor(
  name='ChunkBodyCache',
  full_name='apollo.cyber.proto.ChunkBodyCache',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_number', full_name='apollo.cyber.proto.ChunkBodyCache.message_number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=463,
)


_CHANNELCACHE = _descriptor.Descriptor(
  name='ChannelCache',
  full_name='apollo.cyber.proto.ChannelCache',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_number', full_name='apollo.cyber.proto.ChannelCache.message_number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.cyber.proto.ChannelCache.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='apollo.cyber.proto.ChannelCache.message_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_desc', full_name='apollo.cyber.proto.ChannelCache.proto_desc', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=559,
)


_SINGLEMESSAGE = _descriptor.Descriptor(
  name='SingleMessage',
  full_name='apollo.cyber.proto.SingleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_name', full_name='apollo.cyber.proto.SingleMessage.channel_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='apollo.cyber.proto.SingleMessage.time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='apollo.cyber.proto.SingleMessage.content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=629,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='apollo.cyber.proto.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major_version', full_name='apollo.cyber.proto.Header.major_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor_version', full_name='apollo.cyber.proto.Header.minor_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compress', full_name='apollo.cyber.proto.Header.compress', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_interval', full_name='apollo.cyber.proto.Header.chunk_interval', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segment_interval', full_name='apollo.cyber.proto.Header.segment_interval', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_position', full_name='apollo.cyber.proto.Header.index_position', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_number', full_name='apollo.cyber.proto.Header.chunk_number', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_number', full_name='apollo.cyber.proto.Header.channel_number', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='begin_time', full_name='apollo.cyber.proto.Header.begin_time', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='apollo.cyber.proto.Header.end_time', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_number', full_name='apollo.cyber.proto.Header.message_number', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='apollo.cyber.proto.Header.size', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_complete', full_name='apollo.cyber.proto.Header.is_complete', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_raw_size', full_name='apollo.cyber.proto.Header.chunk_raw_size', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segment_raw_size', full_name='apollo.cyber.proto.Header.segment_raw_size', index=14,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=1033,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='apollo.cyber.proto.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apollo.cyber.proto.Channel.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='apollo.cyber.proto.Channel.message_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proto_desc', full_name='apollo.cyber.proto.Channel.proto_desc', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1035,
  serialized_end=1100,
)


_CHUNKHEADER = _descriptor.Descriptor(
  name='ChunkHeader',
  full_name='apollo.cyber.proto.ChunkHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='begin_time', full_name='apollo.cyber.proto.ChunkHeader.begin_time', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='apollo.cyber.proto.ChunkHeader.end_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_number', full_name='apollo.cyber.proto.ChunkHeader.message_number', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_size', full_name='apollo.cyber.proto.ChunkHeader.raw_size', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1102,
  serialized_end=1195,
)


_CHUNKBODY = _descriptor.Descriptor(
  name='ChunkBody',
  full_name='apollo.cyber.proto.ChunkBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='apollo.cyber.proto.ChunkBody.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1197,
  serialized_end=1261,
)


_INDEX = _descriptor.Descriptor(
  name='Index',
  full_name='apollo.cyber.proto.Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='indexes', full_name='apollo.cyber.proto.Index.indexes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1263,
  serialized_end=1320,
)

_SINGLEINDEX.fields_by_name['type'].enum_type = _SECTIONTYPE
_SINGLEINDEX.fields_by_name['channel_cache'].message_type = _CHANNELCACHE
_SINGLEINDEX.fields_by_name['chunk_header_cache'].message_type = _CHUNKHEADERCACHE
_SINGLEINDEX.fields_by_name['chunk_body_cache'].message_type = _CHUNKBODYCACHE
_SINGLEINDEX.oneofs_by_name['cache'].fields.append(
  _SINGLEINDEX.fields_by_name['channel_cache'])
_SINGLEINDEX.fields_by_name['channel_cache'].containing_oneof = _SINGLEINDEX.oneofs_by_name['cache']
_SINGLEINDEX.oneofs_by_name['cache'].fields.append(
  _SINGLEINDEX.fields_by_name['chunk_header_cache'])
_SINGLEINDEX.fields_by_name['chunk_header_cache'].containing_oneof = _SINGLEINDEX.oneofs_by_name['cache']
_SINGLEINDEX.oneofs_by_name['cache'].fields.append(
  _SINGLEINDEX.fields_by_name['chunk_body_cache'])
_SINGLEINDEX.fields_by_name['chunk_body_cache'].containing_oneof = _SINGLEINDEX.oneofs_by_name['cache']
_HEADER.fields_by_name['compress'].enum_type = _COMPRESSTYPE
_CHUNKBODY.fields_by_name['messages'].message_type = _SINGLEMESSAGE
_INDEX.fields_by_name['indexes'].message_type = _SINGLEINDEX
DESCRIPTOR.message_types_by_name['SingleIndex'] = _SINGLEINDEX
DESCRIPTOR.message_types_by_name['ChunkHeaderCache'] = _CHUNKHEADERCACHE
DESCRIPTOR.message_types_by_name['ChunkBodyCache'] = _CHUNKBODYCACHE
DESCRIPTOR.message_types_by_name['ChannelCache'] = _CHANNELCACHE
DESCRIPTOR.message_types_by_name['SingleMessage'] = _SINGLEMESSAGE
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['ChunkHeader'] = _CHUNKHEADER
DESCRIPTOR.message_types_by_name['ChunkBody'] = _CHUNKBODY
DESCRIPTOR.message_types_by_name['Index'] = _INDEX
DESCRIPTOR.enum_types_by_name['SectionType'] = _SECTIONTYPE
DESCRIPTOR.enum_types_by_name['CompressType'] = _COMPRESSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SingleIndex = _reflection.GeneratedProtocolMessageType('SingleIndex', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEINDEX,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.SingleIndex)
  ))
_sym_db.RegisterMessage(SingleIndex)

ChunkHeaderCache = _reflection.GeneratedProtocolMessageType('ChunkHeaderCache', (_message.Message,), dict(
  DESCRIPTOR = _CHUNKHEADERCACHE,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.ChunkHeaderCache)
  ))
_sym_db.RegisterMessage(ChunkHeaderCache)

ChunkBodyCache = _reflection.GeneratedProtocolMessageType('ChunkBodyCache', (_message.Message,), dict(
  DESCRIPTOR = _CHUNKBODYCACHE,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.ChunkBodyCache)
  ))
_sym_db.RegisterMessage(ChunkBodyCache)

ChannelCache = _reflection.GeneratedProtocolMessageType('ChannelCache', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELCACHE,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.ChannelCache)
  ))
_sym_db.RegisterMessage(ChannelCache)

SingleMessage = _reflection.GeneratedProtocolMessageType('SingleMessage', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEMESSAGE,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.SingleMessage)
  ))
_sym_db.RegisterMessage(SingleMessage)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.Header)
  ))
_sym_db.RegisterMessage(Header)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(
  DESCRIPTOR = _CHANNEL,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.Channel)
  ))
_sym_db.RegisterMessage(Channel)

ChunkHeader = _reflection.GeneratedProtocolMessageType('ChunkHeader', (_message.Message,), dict(
  DESCRIPTOR = _CHUNKHEADER,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.ChunkHeader)
  ))
_sym_db.RegisterMessage(ChunkHeader)

ChunkBody = _reflection.GeneratedProtocolMessageType('ChunkBody', (_message.Message,), dict(
  DESCRIPTOR = _CHUNKBODY,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.ChunkBody)
  ))
_sym_db.RegisterMessage(ChunkBody)

Index = _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), dict(
  DESCRIPTOR = _INDEX,
  __module__ = 'proto.record_pb2'
  # @@protoc_insertion_point(class_scope:apollo.cyber.proto.Index)
  ))
_sym_db.RegisterMessage(Index)


# @@protoc_insertion_point(module_scope)
