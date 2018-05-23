# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:18:06 2018

@author: Reuben
"""

'''
State machine pattern
----------------
'''

class Light_Conditional():
    ''' Uses conditional logic to toggle the state of the light. '''
    
    def __init__(self):
        self.state = 'off'

    def toggle(self):
        if self.state=='on':
            print('turning off')
            self.state = 'off'
        elif self.state=='off':
            print('turning on')
            self.state = 'on'

class State():
    ''' The state of a light '''
    
    pass

class Off(State):
    ''' Unlit '''
    
    def act(self):
        print('turning on')
        return Light_State_Machine.on

class On(State):
    ''' Shining '''
    
    def act(self):
        print('turning off')
        return Light_State_Machine.off

class Light_State_Machine():
    ''' A super simple state machine illustrate for a light '''
    
    off = Off()
    on = On()
    
    def __init__(self):
        self.state = self.off
        
    def toggle(self):
        self.state = self.state.act()


def demonstrate():
    print('First a light with conditional logic.')
    light_conditional = Light_Conditional()
    light_conditional.toggle()
    light_conditional.toggle()
    light_conditional.toggle()
    light_conditional.toggle()
    
    print('Now a light with a state machine pattern.')
    light_state_machine = Light_State_Machine()
    light_state_machine.toggle()
    light_state_machine.toggle()
    light_state_machine.toggle()
    light_state_machine.toggle()