# Copyright (c) Alibaba, Inc. and its affiliates.

from .convert import convert_hf2mcore, convert_mcore2hf
from .patcher import patch_megatron_tokenizer
from .utils import adapter_state_dict_context, prepare_mcore_model
