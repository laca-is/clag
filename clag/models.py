class Action:
    def __init__(self, action_type, details=None):
        self.type = action_type  
        self.details = details or {}

class SendAction(Action):
    def __init__(self, receiver, content, protocol):
        super().__init__('send')
        self.details = {
            'receiver': receiver,
            'content': content,
            'protocol': protocol
        }

class GenericAction(Action):
    def __init__(self, action_type, goal):
        super().__init__(action_type.lower())
        self.details = {
            'goal': goal
        }

class Plan:
    def __init__(self, name, conditions=None, context=None, actions=None):
        self.name = name
        self.conditions = conditions or [] 
        self.context = context or [] 
        self.actions = actions or [] 

class Message:
    def __init__(self, receiver, content, protocol):
        self.receiver = receiver
        self.content = content
        self.protocol = protocol

class Agent:
    def __init__(self, name):
        self.name = name
        self.beliefs = []
        self.desires = []
        self.plans = []
        self.channel = None
        self.environment = None

class Environment:
    def __init__(self, name):
        self.name = name
        self.perceptions = []
        self.actions = []