'''
    Generated automatically by Splash Code Generator for source_linear_x
'''
from std_msgs.msg import Float32
from geometry_msgs.msg import TwistStamped

from scl.components import *
from scl.impl.singleton import Singleton

from ..factory.factory_0 import Factory0

class SourceLinearX(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="source_linear_x", factory=Factory0(), mode="Mode A")
    
    def setup(self):
        self.create_subscription(TwistStamped, "/torcs_speed", self.torcs_speed_callback, 1)
        self.attach_stream_output_port(msg_type=Float32, channel="source_x")
    
    def run(self):
        pass
    
    def torcs_speed_callback(self, msg):
        linear_x = msg.twist.linear.x
        new_msg = Float32()
        new_msg.data = linear_x
        self.write("source_x", new_msg)
    

