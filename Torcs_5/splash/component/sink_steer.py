'''
    Generated automatically by Splash Code Generator for sink_steer
'''
from std_msgs.msg import Float32

from scl.components import *
from scl.impl.singleton import Singleton

class SinkSteer(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="sink_steer", factory=None, mode=None)
    
    def setup(self):
        self.attach_stream_input_port(msg_type=Float32, channel="sink_al_theta", callback=self.user_callback_1)
        self.attach_stream_input_port(msg_type=Float32, channel="sink_theta", callback=self.user_callback_2)
        self.str_publisher = self.create_publisher(Float32, "steering_command", 1)

    def run(self):
        pass
    
    def user_callback_1(self, msg):
        angle_z_command = msg.data
        steering_command = angle_z_command

        if steering_command > 1.0:
            steering = 1.0
        elif steering_command < -1.0:
            steering = -1.0
        else:
            steering = steering_command
        
        # steering = steering_command

        new_msg = Float32()
        new_msg.data = steering
        self.str_publisher.publish(new_msg)
        
    def user_callback_2(self, msg):
        new_msg = Float32()
        new_msg.data = msg.data
        self.str_publisher.publish(new_msg)
        
    
    

