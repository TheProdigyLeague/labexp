# Copyright 1999-2015 Alibaba Group Holding Ltd.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding=utf-8
import hashlib
import hmac

from webullsdkcore.compat import ensure_string
from webullsdkcore.compat import ensure_bytes
from webullsdkcore.compat import b64_encode_bytes


def get_sign_string(source, secret):
    source = ensure_bytes(source)
    secret = ensure_bytes(secret)
    h = hmac.new(secret, source, hashlib.sha1)
    signature = ensure_string(b64_encode_bytes(h.digest()).strip())
    return signature


def get_signer_name():
    return "HMAC-SHA1"


def get_signer_version():
    return "1.0"


def get_signer_type():
    return ""