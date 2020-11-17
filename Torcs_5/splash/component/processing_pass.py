'''
    Generated automatically by Splash Code Generator for processing_pass
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

from ..factory.factory_0 import Factory0

class ProcessingPass(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="processing_pass", factory=Factory0(), mode="Mode_B")
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="key_x", callback=self.user_callback_1)
        self.attach_stream_input_port(msg_type=Float32, channel="key_theta", callback=self.user_callback_2)
        self.attach_stream_output_port(msg_type=Float32, channel="sink_x")
        self.attach_stream_output_port(msg_type=Float32, channel="sink_theta")
    
    def run(self):
        pass
    
    def user_callback_1(self, msg):
        new_msg = Float32()
        new_msg.data = msg.data
        self.write("sink_x", new_msg)
        
    def user_callback_2(self, msg):
        new_msg = Float32()
        new_msg.data = msg.data
        self.write("sink_theta", new_msg)
        
    
    

