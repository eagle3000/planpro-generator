import uuid
import math

class Edge(object):

    def __init__(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b
        self.geo_edge_uuid = str(uuid.uuid4())
        self.top_edge_uuid = str(uuid.uuid4())

    def is_node_connected(self, other_node):
        return self.node_a == other_node or self.node_b == other_node

    def get_other_node(self, node):
        if self.node_a == node:
            return self.node_b
        return self.node_a

    def get_uuids(self):
        return [self.geo_edge_uuid, self.top_edge_uuid]

    def get_length(self):
        return 2 * 6371000 * math.asin(
            math.pi/180*math.sqrt(
                math.pow(math.sin((math.pi/180*(self.node_b.x - self.node_a.x))/2),2)+
                math.cos(math.pi/180*self.node_a.x)*
                math.cos(math.pi/180*self.node_b.x)*
                math.pow(math.sin((math.pi/180*(self.node_b.y - self.node_a.y))/2),2)
            )
        )
