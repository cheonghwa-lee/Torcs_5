'''
    Generated automatically by Splash Code Generator for stream_port_0
'''
from scl.channel import StreamOutputPort
from ..component.source_linear_x import SourceLinearX

class StreamPort0(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_0", parent=SourceLinearX())

'''
    Generated automatically by Splash Code Generator for stream_port_1
'''
from scl.channel import StreamOutputPort
from ..component.source_distance_mid import SourceDistanceMid

class StreamPort1(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_1", parent=SourceDistanceMid())

'''
    Generated automatically by Splash Code Generator for stream_port_2
'''
from scl.channel import StreamOutputPort
from ..component.source_angle_z import SourceAngleZ

class StreamPort2(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_2", parent=SourceAngleZ())

'''
    Generated automatically by Splash Code Generator for stream_port_3
'''
from scl.channel import StreamOutputPort
from ..component.fusion_1 import Fusion1

class StreamPort3(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_3", parent=Fusion1())

'''
    Generated automatically by Splash Code Generator for stream_port_4
'''
from scl.channel import StreamInputPort
from ..component.fusion_1 import Fusion1

class StreamPort4(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_4", parent=Fusion1())

'''
    Generated automatically by Splash Code Generator for stream_port_5
'''
from scl.channel import StreamInputPort
from ..component.fusion_1 import Fusion1

class StreamPort5(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_5", parent=Fusion1())

'''
    Generated automatically by Splash Code Generator for stream_port_6
'''
from scl.channel import StreamInputPort
from ..component.fusion_1 import Fusion1

class StreamPort6(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_6", parent=Fusion1())

'''
    Generated automatically by Splash Code Generator for stream_port_7
'''
from scl.channel import StreamInputPort
from ..component.processing_component_1 import ProcessingComponent1

class StreamPort7(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_7", parent=ProcessingComponent1())

'''
    Generated automatically by Splash Code Generator for stream_port_8
'''
from scl.channel import StreamOutputPort
from ..component.processing_component_1 import ProcessingComponent1

class StreamPort8(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_8", parent=ProcessingComponent1())

'''
    Generated automatically by Splash Code Generator for stream_port_9
'''
from scl.channel import StreamInputPort
from ..component.processing_component_2 import ProcessingComponent2

class StreamPort9(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_9", parent=ProcessingComponent2())

'''
    Generated automatically by Splash Code Generator for stream_port_10
'''
from scl.channel import StreamOutputPort
from ..component.processing_component_2 import ProcessingComponent2

class StreamPort10(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_10", parent=ProcessingComponent2())

'''
    Generated automatically by Splash Code Generator for stream_port_11
'''
from scl.channel import StreamInputPort
from ..component.sink_accel import SinkAccel

class StreamPort11(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_11", parent=SinkAccel())

'''
    Generated automatically by Splash Code Generator for stream_port_12
'''
from scl.channel import StreamInputPort
from ..component.sink_steer import SinkSteer

class StreamPort12(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_12", parent=SinkSteer())

'''
    Generated automatically by Splash Code Generator for stream_port_13
'''
from scl.channel import StreamOutputPort
from ..component.processing_key import ProcessingKey

class StreamPort13(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_13", parent=ProcessingKey())

'''
    Generated automatically by Splash Code Generator for stream_port_14
'''
from scl.channel import StreamOutputPort
from ..component.processing_key import ProcessingKey

class StreamPort14(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_14", parent=ProcessingKey())

'''
    Generated automatically by Splash Code Generator for stream_port_15
'''
from scl.channel import StreamInputPort
from ..component.processing_pass import ProcessingPass

class StreamPort15(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_15", parent=ProcessingPass())

'''
    Generated automatically by Splash Code Generator for stream_port_16
'''
from scl.channel import StreamInputPort
from ..component.processing_pass import ProcessingPass

class StreamPort16(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_16", parent=ProcessingPass())

'''
    Generated automatically by Splash Code Generator for stream_port_17
'''
from scl.channel import StreamOutputPort
from ..component.processing_pass import ProcessingPass

class StreamPort17(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_17", parent=ProcessingPass())

'''
    Generated automatically by Splash Code Generator for stream_port_18
'''
from scl.channel import StreamOutputPort
from ..component.processing_pass import ProcessingPass

class StreamPort18(StreamOutputPort):
    def __init__(self):
        super().__init__(name="stream_port_18", parent=ProcessingPass())

'''
    Generated automatically by Splash Code Generator for stream_port_19
'''
from scl.channel import StreamInputPort
from ..component.sink_accel import SinkAccel

class StreamPort19(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_19", parent=SinkAccel())

'''
    Generated automatically by Splash Code Generator for stream_port_20
'''
from scl.channel import StreamInputPort
from ..component.sink_accel import SinkAccel

class StreamPort20(StreamInputPort):
    def __init__(self):
        super().__init__(name="stream_port_20", parent=SinkAccel())