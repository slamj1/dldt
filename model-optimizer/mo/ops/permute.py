"""
 Copyright (c) 2018 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import networkx as nx

from mo.front.common.partial_infer.transpose import transpose_infer
from mo.front.extractor import attr_getter
from mo.ops.op import Op


class Permute(Op):
    op = 'Permute'
    enabled = False

    def __init__(self, graph: nx.MultiDiGraph, attrs: dict):
        super().__init__(graph, {
            'order': None,
            'type': __class__.op,
            'op': __class__.op,
            'infer': self.infer,
        }, attrs)

    def supported_attrs(self):
        return [('order', lambda node: attr_getter(node, 'order'))]

    @staticmethod
    def infer(*args, **kwargs):
        return transpose_infer(*args, **kwargs)