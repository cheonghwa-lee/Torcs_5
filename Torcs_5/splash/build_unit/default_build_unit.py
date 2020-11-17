'''
    Generated automatically by Splash Code Generator for default_build_unit
'''
import rclpy
from rclpy.executors import MultiThreadedExecutor

from scl.link import Link
from scl.build_unit import BuildUnit

from ..component.processing_key import ProcessingKey
from ..component.processing_component_1 import ProcessingComponent1
from ..component.processing_component_2 import ProcessingComponent2
from ..component.sink_accel import SinkAccel
from ..component.sink_steer import SinkSteer
from ..component.processing_pass import ProcessingPass

from ..component.source_linear_x import SourceLinearX
from ..component.source_distance_mid import SourceDistanceMid
from ..component.source_angle_z import SourceAngleZ

from ..component.fusion_1 import Fusion1

from ..stream_port import *

class DefaultBuildUnit(BuildUnit):
    def __init__(self):
        super().__init__()
        processing_key = ProcessingKey()
        processing_key.set_links(links=[Link(StreamPort13(), StreamPort15(), "key_x"), Link(StreamPort14(), StreamPort16(), "key_theta")])
        processing_key.set_build_unit(self)
        processing_key.attach_modechange_output_port("factory_0")
        processing_key.setup()
        self.components.append(processing_key)
        
        processing_component_1 = ProcessingComponent1()
        processing_component_1.set_links(links=[Link(StreamPort3(), StreamPort7(), "fusion1"), Link(StreamPort8(), StreamPort12(), "sink_al_theta")])
        processing_component_1.set_build_unit(self)
        processing_component_1.setup()
        self.components.append(processing_component_1)
        
        processing_component_2 = ProcessingComponent2()
        processing_component_2.set_links(links=[Link(StreamPort0(), StreamPort9(), "source_x"), Link(StreamPort10(), StreamPort11(), "sink_al_x")])
        processing_component_2.set_build_unit(self)
        processing_component_2.setup()
        self.components.append(processing_component_2)
        
        sink_accel = SinkAccel()
        sink_accel.set_links(links=[Link(StreamPort10(), StreamPort11(), "sink_al_x"), Link(StreamPort17(), StreamPort19(), "sink_x")])
        sink_accel.set_build_unit(self)
        sink_accel.setup()
        self.components.append(sink_accel)
        
        sink_steer = SinkSteer()
        sink_steer.set_links(links=[Link(StreamPort8(), StreamPort12(), "sink_al_theta"), Link(StreamPort18(), StreamPort20(), "sink_theta")])
        sink_steer.set_build_unit(self)
        sink_steer.setup()
        self.components.append(sink_steer)
        
        processing_pass = ProcessingPass()
        processing_pass.set_links(links=[Link(StreamPort13(), StreamPort15(), "key_x"), Link(StreamPort14(), StreamPort16(), "key_theta"), Link(StreamPort17(), StreamPort19(), "sink_x"), Link(StreamPort18(), StreamPort20(), "sink_theta")])
        processing_pass.set_build_unit(self)
        processing_pass.setup()
        self.components.append(processing_pass)
        
        source_linear_x = SourceLinearX()
        source_linear_x.set_links(links=[Link(StreamPort0(), StreamPort4(), "source_x"), Link(StreamPort0(), StreamPort9(), "source_x")])
        source_linear_x.set_build_unit(self)
        source_linear_x.setup()
        self.components.append(source_linear_x)
        
        source_distance_mid = SourceDistanceMid()
        source_distance_mid.set_links(links=[Link(StreamPort1(), StreamPort5(), "source_d")])
        source_distance_mid.set_build_unit(self)
        source_distance_mid.setup()
        self.components.append(source_distance_mid)
        
        source_angle_z = SourceAngleZ()
        source_angle_z.set_links(links=[Link(StreamPort2(), StreamPort6(), "source_theta")])
        source_angle_z.set_build_unit(self)
        source_angle_z.setup()
        self.components.append(source_angle_z)
        
        fusion_1 = Fusion1()
        fusion_1.set_links(links=[Link(StreamPort0(), StreamPort4(), "source_x"), Link(StreamPort1(), StreamPort5(), "source_d"), Link(StreamPort2(), StreamPort6(), "source_theta"), Link(StreamPort3(), StreamPort7(), "fusion1")])
        fusion_1.set_build_unit(self)
        fusion_1.set_fusion_rule(fusion_rule={'mandatory_ports': ['stream_port_5', 'stream_port_6'], 'optional_ports': ['stream_port_4'], 'optional_ports_threshold': '0', 'correlation': '100'})
        fusion_1.setup()
        self.components.append(fusion_1)
        

