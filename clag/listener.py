from clag.antlr.ClagParserListener import ClagParserListener
from clag.models import Agent, Environment, SendAction, GenericAction

class ClagListener(ClagParserListener):
    def __init__(self):
        self.agents = []
        self.envs = []
        self.current_agent = None
        self.current_env = None

    def enterAgentDef(self, ctx):
        self.current_agent = Agent(ctx.ID().getText())

    def exitAgentDef(self, ctx):
        self.agents.append(self.current_agent)
        self.current_agent = None

    def enterEnvironmentDef(self, ctx):
        self.current_env = Environment(ctx.ID().getText())

    def exitEnvironmentDef(self, ctx):
        self.envs.append(self.current_env)
        self.current_env = None

    def enterAgentSection(self, ctx):
        if self.current_agent:
            if ctx.BELIEVES():
                self.current_agent.beliefs = [t.getText() for t in ctx.idList().ID()]
            elif ctx.DESIRES():
                self.current_agent.desires = [t.getText() for t in ctx.idList().ID()]
            elif ctx.CHANNEL():
                self.current_agent.channel = ctx.ID().getText()
            elif ctx.ENVIRONMENT():
                self.current_agent.environment = ctx.ID().getText()

    def enterEnvironmentSection(self, ctx):
        if self.current_env:
            if ctx.THAT() and ctx.PERCEIVES():
                self.current_env.perceptions = [t.getText() for t in ctx.idList().ID()]
            elif ctx.WITH() and ctx.ACTIONS():
                # Parse environment actions
                for action_ctx in ctx.actionName():
                    self.current_env.actions.append(action_ctx.ID().getText())

    def exitEnvironmentSection(self, ctx):
        pass

    def _parse_action(self, action_ctx, default_protocol):
        """Parse an action context into an Action object."""
        if action_ctx.sendAction():
            send_ctx = action_ctx.sendAction()
            receiver = send_ctx.ID()[0].getText()
            content = send_ctx.actionType().getText()
            protocol = send_ctx.ID()[1].getText() if len(send_ctx.ID()) > 1 else default_protocol
            return SendAction(receiver, content, protocol)
        else:  # actionType
            action_type = action_ctx.actionType()
            # Get the action type (ACHIEVE, ABANDON, BELIEVES, etc.)
            action_type_name = next(
                (name for name in dir(action_type) if name in ['ACHIEVE', 'ABANDON', 'BELIEVES', 'PERCEPT', 'CHANGE', 'DESIRES'] 
                 and getattr(action_type, name)()),
                'ACHIEVE'  # Default to ACHIEVE if no specific type found
            )
            return GenericAction(action_type_name, action_type.ID().getText())

    def enterPlan(self, ctx):
        if self.current_agent:
            actions = [self._parse_action(action_ctx, self.current_agent.channel) 
                      for action_ctx in ctx.actionList().action()]

            plan = {
                "name": ctx.ID().getText(),
                "conditions": [(c.getText(), c.ID().getText()) for c in ctx.conditionList().actionType()],
                "context": [(c.getText(), c.ID().getText()) for c in ctx.contextList().actionType()] if ctx.contextList() else [],
                "actions": actions
            }
            self.current_agent.plans.append(plan)

    def enterAction(self, ctx):
        if self.current_env:
            action = self._parse_action(ctx, self.current_env.name)
            self.current_env.actions.append(action) 