# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bfdatafeed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bfgateway_pb2 as bfgateway__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bfdatafeed.proto',
  package='bfdatafeed',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x62\x66\x64\x61tafeed.proto\x12\nbfdatafeed\x1a\x0f\x62\x66gateway.proto\"\x81\x02\n\tBfBarData\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x65xchange\x18\x02 \x01(\t\x12\'\n\x06period\x18\x03 \x01(\x0e\x32\x17.bfdatafeed.BfBarPeriod\x12\x12\n\nactionDate\x18\x04 \x01(\t\x12\x0f\n\x07\x62\x61rTime\x18\x05 \x01(\t\x12\x0e\n\x06volume\x18\x06 \x01(\x05\x12\x14\n\x0copenInterest\x18\x07 \x01(\x01\x12\x12\n\nlastVolume\x18\x08 \x01(\x05\x12\x11\n\topenPrice\x18\t \x01(\x01\x12\x11\n\thighPrice\x18\n \x01(\x01\x12\x10\n\x08lowPrice\x18\x0b \x01(\x01\x12\x12\n\nclosePrice\x18\x0c \x01(\x01\"_\n\x0c\x42\x66GetTickReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x65xchange\x18\x02 \x01(\t\x12\x0e\n\x06toDate\x18\x03 \x01(\t\x12\x0e\n\x06toTime\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x05\"\x87\x01\n\x0b\x42\x66GetBarReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x65xchange\x18\x02 \x01(\t\x12\'\n\x06period\x18\x03 \x01(\x0e\x32\x17.bfdatafeed.BfBarPeriod\x12\x0e\n\x06toDate\x18\x04 \x01(\t\x12\x0e\n\x06toTime\x18\x05 \x01(\t\x12\r\n\x05\x63ount\x18\x06 \x01(\x05\"w\n\x0f\x42\x66\x44\x65leteTickReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x65xchange\x18\x02 \x01(\t\x12\x0e\n\x06toDate\x18\x03 \x01(\t\x12\x0e\n\x06toTime\x18\x04 \x01(\t\x12\x10\n\x08\x66romDate\x18\x05 \x01(\t\x12\x10\n\x08\x66romTime\x18\x06 \x01(\t\"\x9f\x01\n\x0e\x42\x66\x44\x65leteBarReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x65xchange\x18\x02 \x01(\t\x12\'\n\x06period\x18\x03 \x01(\x0e\x32\x17.bfdatafeed.BfBarPeriod\x12\x0e\n\x06toDate\x18\x04 \x01(\t\x12\x0e\n\x06toTime\x18\x05 \x01(\t\x12\x10\n\x08\x66romDate\x18\x06 \x01(\t\x12\x10\n\x08\x66romTime\x18\x07 \x01(\t\"7\n\x13\x42\x66\x44\x65leteContractReq\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08\x65xchange\x18\x02 \x01(\t*\xd1\x02\n\x0b\x42\x66\x42\x61rPeriod\x12\x12\n\x0ePERIOD_UNKNOWN\x10\x00\x12\x0e\n\nPERIOD_S01\x10\x01\x12\x0e\n\nPERIOD_S03\x10\x02\x12\x0e\n\nPERIOD_S05\x10\x03\x12\x0e\n\nPERIOD_S10\x10\x04\x12\x0e\n\nPERIOD_S15\x10\x05\x12\x0e\n\nPERIOD_S30\x10\x06\x12\x0e\n\nPERIOD_M01\x10\x07\x12\x0e\n\nPERIOD_M03\x10\x08\x12\x0e\n\nPERIOD_M05\x10\t\x12\x0e\n\nPERIOD_M10\x10\n\x12\x0e\n\nPERIOD_M15\x10\x0b\x12\x0e\n\nPERIOD_M30\x10\x0c\x12\x0e\n\nPERIOD_H01\x10\r\x12\x0e\n\nPERIOD_H02\x10\x0e\x12\x0e\n\nPERIOD_H03\x10\x0f\x12\x0e\n\nPERIOD_H04\x10\x10\x12\x0e\n\nPERIOD_D01\x10\x11\x12\x0e\n\nPERIOD_W01\x10\x12\x12\x0e\n\nPERIOD_X01\x10\x13\x32\xc3\x05\n\x11\x42\x66\x44\x61tafeedService\x12\x36\n\x04Ping\x12\x15.bfgateway.BfPingData\x1a\x15.bfgateway.BfPingData\"\x00\x12\x38\n\nInsertTick\x12\x15.bfgateway.BfTickData\x1a\x11.bfgateway.BfVoid\"\x00\x12\x37\n\tInsertBar\x12\x15.bfdatafeed.BfBarData\x1a\x11.bfgateway.BfVoid\"\x00\x12@\n\x0eInsertContract\x12\x19.bfgateway.BfContractData\x1a\x11.bfgateway.BfVoid\"\x00\x12>\n\x07GetTick\x12\x18.bfdatafeed.BfGetTickReq\x1a\x15.bfgateway.BfTickData\"\x00\x30\x01\x12<\n\x06GetBar\x12\x17.bfdatafeed.BfGetBarReq\x1a\x15.bfdatafeed.BfBarData\"\x00\x30\x01\x12I\n\x0bGetContract\x12\x1b.bfgateway.BfGetContractReq\x1a\x19.bfgateway.BfContractData\"\x00\x30\x01\x12>\n\nDeleteTick\x12\x1b.bfdatafeed.BfDeleteTickReq\x1a\x11.bfgateway.BfVoid\"\x00\x12<\n\tDeleteBar\x12\x1a.bfdatafeed.BfDeleteBarReq\x1a\x11.bfgateway.BfVoid\"\x00\x12\x46\n\x0e\x44\x65leteContract\x12\x1f.bfdatafeed.BfDeleteContractReq\x1a\x11.bfgateway.BfVoid\"\x00\x12\x32\n\x08\x43leanAll\x12\x11.bfgateway.BfVoid\x1a\x11.bfgateway.BfVoid\"\x00\x42*Z(github.com/sunwangme/bfgo/api/bfdatafeedb\x06proto3')
  ,
  dependencies=[bfgateway__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_BFBARPERIOD = _descriptor.EnumDescriptor(
  name='BfBarPeriod',
  full_name='bfdatafeed.BfBarPeriod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PERIOD_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_S01', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_S03', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_S05', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_S10', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_S15', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_S30', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_M01', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_M03', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_M05', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_M10', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_M15', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_M30', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_H01', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_H02', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_H03', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_H04', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_D01', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_W01', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIOD_X01', index=19, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=885,
  serialized_end=1222,
)
_sym_db.RegisterEnumDescriptor(_BFBARPERIOD)

BfBarPeriod = enum_type_wrapper.EnumTypeWrapper(_BFBARPERIOD)
PERIOD_UNKNOWN = 0
PERIOD_S01 = 1
PERIOD_S03 = 2
PERIOD_S05 = 3
PERIOD_S10 = 4
PERIOD_S15 = 5
PERIOD_S30 = 6
PERIOD_M01 = 7
PERIOD_M03 = 8
PERIOD_M05 = 9
PERIOD_M10 = 10
PERIOD_M15 = 11
PERIOD_M30 = 12
PERIOD_H01 = 13
PERIOD_H02 = 14
PERIOD_H03 = 15
PERIOD_H04 = 16
PERIOD_D01 = 17
PERIOD_W01 = 18
PERIOD_X01 = 19



_BFBARDATA = _descriptor.Descriptor(
  name='BfBarData',
  full_name='bfdatafeed.BfBarData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bfdatafeed.BfBarData.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='bfdatafeed.BfBarData.exchange', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='bfdatafeed.BfBarData.period', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actionDate', full_name='bfdatafeed.BfBarData.actionDate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='barTime', full_name='bfdatafeed.BfBarData.barTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='bfdatafeed.BfBarData.volume', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openInterest', full_name='bfdatafeed.BfBarData.openInterest', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastVolume', full_name='bfdatafeed.BfBarData.lastVolume', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openPrice', full_name='bfdatafeed.BfBarData.openPrice', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='highPrice', full_name='bfdatafeed.BfBarData.highPrice', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lowPrice', full_name='bfdatafeed.BfBarData.lowPrice', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='closePrice', full_name='bfdatafeed.BfBarData.closePrice', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=307,
)


_BFGETTICKREQ = _descriptor.Descriptor(
  name='BfGetTickReq',
  full_name='bfdatafeed.BfGetTickReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bfdatafeed.BfGetTickReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='bfdatafeed.BfGetTickReq.exchange', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toDate', full_name='bfdatafeed.BfGetTickReq.toDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toTime', full_name='bfdatafeed.BfGetTickReq.toTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='bfdatafeed.BfGetTickReq.count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=404,
)


_BFGETBARREQ = _descriptor.Descriptor(
  name='BfGetBarReq',
  full_name='bfdatafeed.BfGetBarReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bfdatafeed.BfGetBarReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='bfdatafeed.BfGetBarReq.exchange', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='bfdatafeed.BfGetBarReq.period', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toDate', full_name='bfdatafeed.BfGetBarReq.toDate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toTime', full_name='bfdatafeed.BfGetBarReq.toTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='bfdatafeed.BfGetBarReq.count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=542,
)


_BFDELETETICKREQ = _descriptor.Descriptor(
  name='BfDeleteTickReq',
  full_name='bfdatafeed.BfDeleteTickReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bfdatafeed.BfDeleteTickReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='bfdatafeed.BfDeleteTickReq.exchange', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toDate', full_name='bfdatafeed.BfDeleteTickReq.toDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toTime', full_name='bfdatafeed.BfDeleteTickReq.toTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromDate', full_name='bfdatafeed.BfDeleteTickReq.fromDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromTime', full_name='bfdatafeed.BfDeleteTickReq.fromTime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=663,
)


_BFDELETEBARREQ = _descriptor.Descriptor(
  name='BfDeleteBarReq',
  full_name='bfdatafeed.BfDeleteBarReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bfdatafeed.BfDeleteBarReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='bfdatafeed.BfDeleteBarReq.exchange', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='period', full_name='bfdatafeed.BfDeleteBarReq.period', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toDate', full_name='bfdatafeed.BfDeleteBarReq.toDate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toTime', full_name='bfdatafeed.BfDeleteBarReq.toTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromDate', full_name='bfdatafeed.BfDeleteBarReq.fromDate', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromTime', full_name='bfdatafeed.BfDeleteBarReq.fromTime', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=825,
)


_BFDELETECONTRACTREQ = _descriptor.Descriptor(
  name='BfDeleteContractReq',
  full_name='bfdatafeed.BfDeleteContractReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='bfdatafeed.BfDeleteContractReq.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='bfdatafeed.BfDeleteContractReq.exchange', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=882,
)

_BFBARDATA.fields_by_name['period'].enum_type = _BFBARPERIOD
_BFGETBARREQ.fields_by_name['period'].enum_type = _BFBARPERIOD
_BFDELETEBARREQ.fields_by_name['period'].enum_type = _BFBARPERIOD
DESCRIPTOR.message_types_by_name['BfBarData'] = _BFBARDATA
DESCRIPTOR.message_types_by_name['BfGetTickReq'] = _BFGETTICKREQ
DESCRIPTOR.message_types_by_name['BfGetBarReq'] = _BFGETBARREQ
DESCRIPTOR.message_types_by_name['BfDeleteTickReq'] = _BFDELETETICKREQ
DESCRIPTOR.message_types_by_name['BfDeleteBarReq'] = _BFDELETEBARREQ
DESCRIPTOR.message_types_by_name['BfDeleteContractReq'] = _BFDELETECONTRACTREQ
DESCRIPTOR.enum_types_by_name['BfBarPeriod'] = _BFBARPERIOD

BfBarData = _reflection.GeneratedProtocolMessageType('BfBarData', (_message.Message,), dict(
  DESCRIPTOR = _BFBARDATA,
  __module__ = 'bfdatafeed_pb2'
  # @@protoc_insertion_point(class_scope:bfdatafeed.BfBarData)
  ))
_sym_db.RegisterMessage(BfBarData)

BfGetTickReq = _reflection.GeneratedProtocolMessageType('BfGetTickReq', (_message.Message,), dict(
  DESCRIPTOR = _BFGETTICKREQ,
  __module__ = 'bfdatafeed_pb2'
  # @@protoc_insertion_point(class_scope:bfdatafeed.BfGetTickReq)
  ))
_sym_db.RegisterMessage(BfGetTickReq)

BfGetBarReq = _reflection.GeneratedProtocolMessageType('BfGetBarReq', (_message.Message,), dict(
  DESCRIPTOR = _BFGETBARREQ,
  __module__ = 'bfdatafeed_pb2'
  # @@protoc_insertion_point(class_scope:bfdatafeed.BfGetBarReq)
  ))
_sym_db.RegisterMessage(BfGetBarReq)

BfDeleteTickReq = _reflection.GeneratedProtocolMessageType('BfDeleteTickReq', (_message.Message,), dict(
  DESCRIPTOR = _BFDELETETICKREQ,
  __module__ = 'bfdatafeed_pb2'
  # @@protoc_insertion_point(class_scope:bfdatafeed.BfDeleteTickReq)
  ))
_sym_db.RegisterMessage(BfDeleteTickReq)

BfDeleteBarReq = _reflection.GeneratedProtocolMessageType('BfDeleteBarReq', (_message.Message,), dict(
  DESCRIPTOR = _BFDELETEBARREQ,
  __module__ = 'bfdatafeed_pb2'
  # @@protoc_insertion_point(class_scope:bfdatafeed.BfDeleteBarReq)
  ))
_sym_db.RegisterMessage(BfDeleteBarReq)

BfDeleteContractReq = _reflection.GeneratedProtocolMessageType('BfDeleteContractReq', (_message.Message,), dict(
  DESCRIPTOR = _BFDELETECONTRACTREQ,
  __module__ = 'bfdatafeed_pb2'
  # @@protoc_insertion_point(class_scope:bfdatafeed.BfDeleteContractReq)
  ))
_sym_db.RegisterMessage(BfDeleteContractReq)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z(github.com/sunwangme/bfgo/api/bfdatafeed'))
import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaBfDatafeedServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InsertTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InsertBar(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def InsertContract(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetBar(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetContract(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteTick(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteBar(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteContract(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CleanAll(self, request, context):
    raise NotImplementedError()

class BetaBfDatafeedServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def Ping(self, request, timeout):
    raise NotImplementedError()
  Ping.future = None
  @abc.abstractmethod
  def InsertTick(self, request, timeout):
    raise NotImplementedError()
  InsertTick.future = None
  @abc.abstractmethod
  def InsertBar(self, request, timeout):
    raise NotImplementedError()
  InsertBar.future = None
  @abc.abstractmethod
  def InsertContract(self, request, timeout):
    raise NotImplementedError()
  InsertContract.future = None
  @abc.abstractmethod
  def GetTick(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetBar(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def GetContract(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def DeleteTick(self, request, timeout):
    raise NotImplementedError()
  DeleteTick.future = None
  @abc.abstractmethod
  def DeleteBar(self, request, timeout):
    raise NotImplementedError()
  DeleteBar.future = None
  @abc.abstractmethod
  def DeleteContract(self, request, timeout):
    raise NotImplementedError()
  DeleteContract.future = None
  @abc.abstractmethod
  def CleanAll(self, request, timeout):
    raise NotImplementedError()
  CleanAll.future = None

def beta_create_BfDatafeedService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  request_deserializers = {
    ('bfdatafeed.BfDatafeedService', 'CleanAll'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'DeleteBar'): bfdatafeed_pb2.BfDeleteBarReq.FromString,
    ('bfdatafeed.BfDatafeedService', 'DeleteContract'): bfdatafeed_pb2.BfDeleteContractReq.FromString,
    ('bfdatafeed.BfDatafeedService', 'DeleteTick'): bfdatafeed_pb2.BfDeleteTickReq.FromString,
    ('bfdatafeed.BfDatafeedService', 'GetBar'): bfdatafeed_pb2.BfGetBarReq.FromString,
    ('bfdatafeed.BfDatafeedService', 'GetContract'): bfgateway_pb2.BfGetContractReq.FromString,
    ('bfdatafeed.BfDatafeedService', 'GetTick'): bfdatafeed_pb2.BfGetTickReq.FromString,
    ('bfdatafeed.BfDatafeedService', 'InsertBar'): bfdatafeed_pb2.BfBarData.FromString,
    ('bfdatafeed.BfDatafeedService', 'InsertContract'): bfgateway_pb2.BfContractData.FromString,
    ('bfdatafeed.BfDatafeedService', 'InsertTick'): bfgateway_pb2.BfTickData.FromString,
    ('bfdatafeed.BfDatafeedService', 'Ping'): bfgateway_pb2.BfPingData.FromString,
  }
  response_serializers = {
    ('bfdatafeed.BfDatafeedService', 'CleanAll'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'DeleteBar'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'DeleteContract'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'DeleteTick'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'GetBar'): bfdatafeed_pb2.BfBarData.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'GetContract'): bfgateway_pb2.BfContractData.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'GetTick'): bfgateway_pb2.BfTickData.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'InsertBar'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'InsertContract'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'InsertTick'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'Ping'): bfgateway_pb2.BfPingData.SerializeToString,
  }
  method_implementations = {
    ('bfdatafeed.BfDatafeedService', 'CleanAll'): face_utilities.unary_unary_inline(servicer.CleanAll),
    ('bfdatafeed.BfDatafeedService', 'DeleteBar'): face_utilities.unary_unary_inline(servicer.DeleteBar),
    ('bfdatafeed.BfDatafeedService', 'DeleteContract'): face_utilities.unary_unary_inline(servicer.DeleteContract),
    ('bfdatafeed.BfDatafeedService', 'DeleteTick'): face_utilities.unary_unary_inline(servicer.DeleteTick),
    ('bfdatafeed.BfDatafeedService', 'GetBar'): face_utilities.unary_stream_inline(servicer.GetBar),
    ('bfdatafeed.BfDatafeedService', 'GetContract'): face_utilities.unary_stream_inline(servicer.GetContract),
    ('bfdatafeed.BfDatafeedService', 'GetTick'): face_utilities.unary_stream_inline(servicer.GetTick),
    ('bfdatafeed.BfDatafeedService', 'InsertBar'): face_utilities.unary_unary_inline(servicer.InsertBar),
    ('bfdatafeed.BfDatafeedService', 'InsertContract'): face_utilities.unary_unary_inline(servicer.InsertContract),
    ('bfdatafeed.BfDatafeedService', 'InsertTick'): face_utilities.unary_unary_inline(servicer.InsertTick),
    ('bfdatafeed.BfDatafeedService', 'Ping'): face_utilities.unary_unary_inline(servicer.Ping),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_BfDatafeedService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfdatafeed_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  import bfgateway_pb2
  request_serializers = {
    ('bfdatafeed.BfDatafeedService', 'CleanAll'): bfgateway_pb2.BfVoid.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'DeleteBar'): bfdatafeed_pb2.BfDeleteBarReq.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'DeleteContract'): bfdatafeed_pb2.BfDeleteContractReq.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'DeleteTick'): bfdatafeed_pb2.BfDeleteTickReq.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'GetBar'): bfdatafeed_pb2.BfGetBarReq.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'GetContract'): bfgateway_pb2.BfGetContractReq.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'GetTick'): bfdatafeed_pb2.BfGetTickReq.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'InsertBar'): bfdatafeed_pb2.BfBarData.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'InsertContract'): bfgateway_pb2.BfContractData.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'InsertTick'): bfgateway_pb2.BfTickData.SerializeToString,
    ('bfdatafeed.BfDatafeedService', 'Ping'): bfgateway_pb2.BfPingData.SerializeToString,
  }
  response_deserializers = {
    ('bfdatafeed.BfDatafeedService', 'CleanAll'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'DeleteBar'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'DeleteContract'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'DeleteTick'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'GetBar'): bfdatafeed_pb2.BfBarData.FromString,
    ('bfdatafeed.BfDatafeedService', 'GetContract'): bfgateway_pb2.BfContractData.FromString,
    ('bfdatafeed.BfDatafeedService', 'GetTick'): bfgateway_pb2.BfTickData.FromString,
    ('bfdatafeed.BfDatafeedService', 'InsertBar'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'InsertContract'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'InsertTick'): bfgateway_pb2.BfVoid.FromString,
    ('bfdatafeed.BfDatafeedService', 'Ping'): bfgateway_pb2.BfPingData.FromString,
  }
  cardinalities = {
    'CleanAll': cardinality.Cardinality.UNARY_UNARY,
    'DeleteBar': cardinality.Cardinality.UNARY_UNARY,
    'DeleteContract': cardinality.Cardinality.UNARY_UNARY,
    'DeleteTick': cardinality.Cardinality.UNARY_UNARY,
    'GetBar': cardinality.Cardinality.UNARY_STREAM,
    'GetContract': cardinality.Cardinality.UNARY_STREAM,
    'GetTick': cardinality.Cardinality.UNARY_STREAM,
    'InsertBar': cardinality.Cardinality.UNARY_UNARY,
    'InsertContract': cardinality.Cardinality.UNARY_UNARY,
    'InsertTick': cardinality.Cardinality.UNARY_UNARY,
    'Ping': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'bfdatafeed.BfDatafeedService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)