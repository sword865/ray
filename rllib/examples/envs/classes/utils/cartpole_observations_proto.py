# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cartpole_observations.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x63\x61rtpole_observations.proto"]\n\x13\x43\x61rtPoleObservation\x12\r\n\x05x_pos\x18\x01 \x01(\x01\x12\x0f\n\x07x_veloc\x18\x02 \x01(\x01\x12\x11\n\tangle_pos\x18\x03 \x01(\x01\x12\x13\n\x0b\x61ngle_veloc\x18\x04 \x01(\x01\x62\x06proto3'  # noqa
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "cartpole_observations_proto", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_CARTPOLEOBSERVATION"]._serialized_start = 31
    _globals["_CARTPOLEOBSERVATION"]._serialized_end = 124
# @@protoc_insertion_point(module_scope)
