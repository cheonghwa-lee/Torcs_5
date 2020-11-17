'''
    Generated automatically by Splash Code Generator for processing_key
'''
from std_msgs.msg import Float32, Int32

from scl.components import *
from scl.impl.singleton import Singleton

from evdev import *

from ..factory import *

import threading

class ProcessingKey(Component, metaclass=Singleton):
    def __init__(self):
        super().__init__(name="processing_key", factory=None, mode=None)
    
    def setup(self):
        self.attach_stream_output_port(msg_type=Float32, channel="key_x")
        self.attach_stream_output_port(msg_type=Float32, channel="key_theta")
        self.brk_publisher = self.create_publisher(Float32, "brake_command", 1)
        self.gear_publisher = self.create_publisher(Int32, "gear_command", 1)
    
    def task(self):
        dev = InputDevice('/dev/input/event3')
        print(dev)

        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY and event.code == 11:
                if event.value == 1:
                    gear = -1
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 41:
                if event.value == 1:
                    gear = 0
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 2:
                if event.value == 1:
                    gear = 1
                    new_msg = Int32()
                    new_msg.data = gear
                    self.get_logger().info("100: {}".format(gear))
                    self.gear_publisher.publish(new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 3:
                if event.value == 1:
                    gear = 2
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)   
            elif event.type == ecodes.EV_KEY and event.code == 4:
                if event.value == 1:
                    gear = 3
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)    
            elif event.type == ecodes.EV_KEY and event.code == 5:
                if event.value == 1:
                    gear = 4
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)    
            elif event.type == ecodes.EV_KEY and event.code == 6:
                if event.value == 1:
                    gear = 5
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)    
            elif event.type == ecodes.EV_KEY and event.code == 7:
                if event.value == 1:
                    gear = 6
                    new_msg = Int32()
                    new_msg.data = gear
                    self.gear_publisher.publish(new_msg)
            elif event.type == ecodes.EV_KEY and event.code == 103:
                if event.value == 0:
                    accel = 0.0
                    new_msg_acc = Float32()
                    new_msg_acc.data = accel
                    self.get_logger().info("3: {}".format(accel))
                    self.write("key_x", new_msg_acc)
                else:
                    accel = 1.0
                    new_msg_acc = Float32()
                    new_msg_acc.data = accel
                    self.get_logger().info("4: {}".format(accel))
                    self.write("key_x", new_msg_acc)
            elif event.type == ecodes.EV_KEY and event.code == 108:
                if event.value == 0:
                    brake = 0.0
                    new_msg_brk = Float32()
                    new_msg_brk.data = brake
                    self.get_logger().info("1: {}".format(brake))
                    self.brk_publisher.publish(new_msg_brk)
                else:
                    brake = 1.0
                    new_msg_brk = Float32()
                    new_msg_brk.data = brake
                    self.get_logger().info("2: {}".format(brake))
                    self.brk_publisher.publish(new_msg_brk)
            elif event.type == ecodes.EV_KEY and event.code == 105:
                if event.value == 0:
                    steering = 0.0
                    new_msg = Float32()
                    new_msg.data = steering
                    self.write("key_theta", new_msg) 
                else:
                    steering = 0.5
                    new_msg = Float32()
                    new_msg.data = steering
                    self.write("key_theta", new_msg) 
            elif event.type == ecodes.EV_KEY and event.code == 106:
                if event.value == 0:
                    steering = 0.0
                    new_msg = Float32()
                    new_msg.data = steering
                    self.write("key_theta", new_msg) 
                else:
                    steering = -0.5
                    new_msg = Float32()
                    new_msg.data = steering
                    self.write("key_theta", new_msg) 

            elif event.type == ecodes.EV_KEY and event.code == 15 and event.value == 1:
                print("trigger modechange to event_2")
                self.trigger_modechange("factory_0", "event_2")
            elif event.type == ecodes.EV_KEY and event.code == 42 and event.value == 1:
                print("trigger modechange to event_1")
                self.trigger_modechange("factory_0", "event_1")
                
    def run(self):
        thread = threading.Thread(target=self.task)
        thread.start()
                
    
    
    

