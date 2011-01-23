# Copyright (C) 2011 by Henrik Gustafsson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

class Store:

    def __init__(self):
        pass

    def partition(self, key):
        return Partition(key)

    def propose(self, key, value, callback):
        self.partition(key).propose(key, value, callback)

class ChannelManager:
    pass

class Node(ChannelManager):
    pass

class Partition:

    queue = []

    def __init__(self, key):
        self.key = key

    def propose(self, key, value, callback):
        self.queue.append((key, value, callback))

class PartionNode:

    map = {}

    def ack(self, id):
        pass

    def propose(self, key, value, callback):
        map[key] = value
        callback()

class Leader(PartionNode):
    pass

class Follower(PartionNode):
    pass


