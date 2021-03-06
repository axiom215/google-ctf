#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json, tempfile, subprocess, os

with open('metadata.json') as f:
    data = json.load(f)
flag = data['challenge']['flag'].strip()

print "Generating challenge for flag {}...".format(flag)

with open('./challenge/src/flag.txt', 'w') as f:
  f.write(flag)

assert os.system('cd challenge; cargo build --release; cp target/release/{challenge,solve} .; cp solve ../healthcheck') == 0
assert os.system('cp challenge/src/handshake.rs attachments') == 0
