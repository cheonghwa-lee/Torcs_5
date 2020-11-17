'''
    Generated automatically by Splash Code Generator for source_distance_mid
'''
from std_msgs.msg import Float32
from torcs_interfaces.msg import TORCSSensors

from scl.components import *
from scl.impl.singleton import Singleton

from ..factory.factory_0 import Factory0

class SourceDistanceMid(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="source_distance_mid", factory=Factory0(), mode="Mode A")
    
    def setup(self):
        self.create_subscription(TORCSSensors, "/torcs_sensors_out", self.torcs_sensor_callback, 1)
        self.attach_stream_output_port(msg_type=Float32, channel="source_d")
    
    def run(self):
        pass
    
    def torcs_sensor_callback(self, msg):
        dist_middle = msg.dist_to_middle
        self.get_logger().info("dist_middle: {}".format(dist_middle))
        dist_left = msg.dist_to_left
        dist_right = msg.dist_to_right
        self.get_logger().info("dist_middle: {} {} {}".format(dist_middle, dist_left, dist_right))

        new_msg = Float32()
        new_msg.data = dist_middle
        self.write("source_d", new_msg)
    

