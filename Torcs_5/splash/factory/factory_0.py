'''
    Generated automatically by Splash Code Generator for factory_0
'''
from scl.factory import Factory

class Factory0(Factory):
    def __init__(self):
        super().__init__(name="factory_0", parent=None, mode="")
        self.set_mode_configuration({'initial_mode': 'Mode A', 'mode_list': [{'name': 'Mode A', 'events': [{'name': 'event_1', 'next_mode': 'Mode A', 'output_internal_data_items': False}, {'name': 'event_2', 'next_mode': 'Mode_B', 'output_internal_data_items': False}]}, {'name': 'Mode_B', 'events': [{'name': 'event_1', 'next_mode': 'Mode A', 'output_internal_data_items': False}, {'name': 'event_2', 'next_mode': 'Mode_B', 'output_internal_data_items': False}]}]})

