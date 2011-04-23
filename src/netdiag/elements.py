#!bin/py
# -*- coding: utf-8 -*-

import re
import sys
import blockdiag.elements
from blockdiag.elements import *
from blockdiag.utils.XY import XY


class Diagram(blockdiag.elements.Diagram):
    def __init__(self):
        super(Diagram, self).__init__()

        self.orientation = 'portrait'
        self.span_height = 120
        self.networks = []


class DiagramNode(blockdiag.elements.DiagramNode):
    def __init__(self, id):
        super(DiagramNode, self).__init__(id)

        self.address = {}
        self.networks = []

    def set_attributes(self, network, attrs):
        for attr in attrs:
            if attr.name == 'address':
                self.address[network] = unquote(attr.value)
            else:
                self.set_attribute(attr)


class NodeGroup(blockdiag.elements.NodeGroup):
    def __init__(self, id):
        super(NodeGroup, self).__init__(id)

        self.address = None
