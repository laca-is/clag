class Action:
    def __init__(self, action_type, details=None):
        self.type = action_type  
        self.details = details or {}

class SendAction(Action):
    def __init__(self, receiver, content, act_type, channel):
        super().__init__('send')
        self.details = {
            'receiver': receiver,
            'content': content,
            'act_type': act_type,
            'channel': channel
        }

class AskAction(Action):
    def __init__(self, receiver, content, wait_reply, channel):
        super().__init__('ask')
        self.details = {
            'receiver': receiver,
            'content': content,
            'wait_reply': wait_reply,
            'channel': channel
        }

class GenericAction(Action):
    def __init__(self, action_type, goal):
        super().__init__(action_type.lower())
        self.details = {
            'goal': goal
        }

class Plan:
    def __init__(self, name, conditions=None, context=None, actions=None, event_change='gain'):
        self.name = name
        self.conditions = conditions or [] 
        self.context = context or [] 
        self.actions = actions or []
        self.event_change = event_change 

class Message:
    def __init__(self, receiver, content, protocol):
        self.receiver = receiver
        self.content = content
        self.protocol = protocol

class Agent:
    def __init__(self, name):
        self.name = name
        self.instance_count = 1
        self.beliefs = [] # e.g. [{'name': 'price', 'values': [50, 'USD']}] or [{'name': 'hello', 'values': None}]
        self.desires = []
        self.plans = []
        self.channel = None
        self.environment = None
        self.focus_groups = []
        self.ignore_groups = []

class Environment:
    def __init__(self, name):
        self.name = name
        self.perceptions = []
        self.actions = []

class EnvironmentAction:
    def __init__(self, name, effect=None, target_percept=None):
        self.name = name
        self.effect = effect
        self.target_percept = target_percept