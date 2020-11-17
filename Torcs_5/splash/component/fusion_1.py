'''
    Generated automatically by Splash Code Generator for fusion_1
'''
from std_msgs.msg import Int32, Float32

from scl.components import *
from scl.impl.singleton import Singleton

from ..factory.factory_0 import Factory0

class Fusion1(FusionOperator, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="fusion_1", factory=Factory0(), mode="Mode A")
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="source_x")
        self.attach_stream_input_port(msg_type=Float32, channel="source_d")
        self.attach_stream_input_port(msg_type=Float32, channel="source_theta")
        self.attach_stream_output_port(channel="fusion1")
    
    def run(self):
        pass
    
    

