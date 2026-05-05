from clag.antlr.ClagParserListener import ClagParserListener
from clag.models import Agent, Environment, SendAction, GenericAction

class ClagListener(ClagParserListener):
    def __init__(self):
        self.agents = []
        self.envs = []
        self.current_agent = None
        self.current_env = None

    def enterAgentDef(self, ctx):
        if ctx.CREATE():
            # CREATE NUMBER ID AGENTS ...
            count = int(ctx.NUMBER().getText())
            agent_name = ctx.ID().getText()
            self.current_agent = Agent(agent_name)
            self.current_agent.instance_count = count
        else:
            # AGENT ID ...
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
        def parse_value(v):
            if v.NUMBER():
                return v.getText()
            elif v.ANY():
                return "Any"
            elif v.STRING():
                return f'"{v.getText().strip()}"'.replace('""', '"').replace("''", '"')
            else: # ID
                return f'"{v.getText()}"'

        if self.current_agent:
            if ctx.BELIEVES():
                belief_list = []
                if ctx.beliefDefList():
                    for bd in ctx.beliefDefList().beliefDef():
                        name = bd.ID().getText()
                        vals = None
                        if bd.valueList():
                            vals = [parse_value(v) for v in bd.valueList().value()]
                        belief_list.append({'name': name, 'vals': vals})
                self.current_agent.beliefs = belief_list
            elif ctx.DESIRES():
                desire_list = []
                if ctx.goalDefList():
                    for gd in ctx.goalDefList().goalDef():
                        name = gd.ID().getText()
                        vals = None
                        if gd.valueList():
                            vals = [parse_value(v) for v in gd.valueList().value()]
                        desire_list.append({'name': name, 'vals': vals})
                self.current_agent.desires = desire_list
            elif ctx.CHANNEL():
                self.current_agent.channel = ctx.ID().getText()
            elif ctx.ENVIRONMENT():
                self.current_agent.environment = ctx.ID().getText()
            elif ctx.FOCUSING() and ctx.ON():
                self.current_agent.focus_groups = [t.getText() for t in ctx.idList().ID()]
            elif ctx.IGNORING():
                self.current_agent.ignore_groups = [t.getText() for t in ctx.idList().ID()]

    def enterEnvironmentSection(self, ctx):
        if self.current_env:
            if ctx.THAT() and ctx.PERCEIVES():
                self.current_env.perceptions = [t.getText() for t in ctx.idList().ID()]
            elif ctx.WITH() and ctx.ACTIONS():
                # Parse environment actions
                for action_ctx in ctx.actionName():
                    name = action_ctx.ID(0).getText()
                    effect = None
                    target_percept = None
                    if action_ctx.THAT():
                        if action_ctx.REMOVES(): effect = 'remove'
                        elif action_ctx.CREATES(): effect = 'create'
                        elif action_ctx.CHANGES(): effect = 'change'
                        target_percept = action_ctx.ID(1).getText()
                    from clag.models import EnvironmentAction
                    self.current_env.actions.append(EnvironmentAction(name, effect, target_percept))

    def exitEnvironmentSection(self, ctx):
        pass

    def _parse_action(self, action_ctx, default_channel):
        """Parse an action context into an Action object."""
        if action_ctx.sendAction():
            send_ctx = action_ctx.sendAction()
            if send_ctx.EVERYONE():
                receiver = 'broadcast'
                id_offset = 0
            else:
                receiver = send_ctx.ID()[0].getText()
                id_offset = 1

            raw_act = send_ctx.actType().getText().lower().replace(' ', '')
            
            act_map = {
                'tell': 'tell',
                'untell': 'untell',
                'tellhow': 'tellHow',
                'untellhow': 'untellHow',
                'achieve': 'achieve',
                'unachieve': 'unachieve',
                'askone': 'askOne',
                'askall': 'askAll',
                'askhow': 'askHow'
            }
            act_type = act_map.get(raw_act, 'achieve')
            
            content = send_ctx.ID()[id_offset].getText()
            channel = send_ctx.ID()[id_offset + 1].getText() if len(send_ctx.ID()) > id_offset + 1 else default_channel
            return SendAction(receiver, content, act_type, channel)
        elif action_ctx.askAction():
            from clag.models import AskAction
            ask_ctx = action_ctx.askAction()
            if ask_ctx.EVERYONE():
                receiver = 'broadcast'
                id_offset = 0
            else:
                receiver = ask_ctx.ID()[0].getText()
                id_offset = 1
                
            content = ask_ctx.ID()[id_offset].getText()
            wait_reply = ask_ctx.WAIT() is not None
            channel = ask_ctx.ID()[id_offset + 1].getText() if len(ask_ctx.ID()) > id_offset + 1 else default_channel
            
            return AskAction(receiver, content, wait_reply, channel)
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

            conditions = []
            event_change = 'gain'
            for c in ctx.conditionList().actionType():
                text = c.getText().lower()
                if text.startswith('loses'):
                    event_change = 'lose'
                    cond_type = 'believes' if ('believe' in text or 'belief' in text) else 'desires'
                else:
                    if 'believe' in text or 'belief' in text:
                        cond_type = 'believes'
                    elif 'desire' in text:
                        cond_type = 'desires'
                    elif 'achieve' in text:
                        cond_type = 'achieve'
                    else:
                        cond_type = c.getText()
                conditions.append((cond_type, c.ID().getText()))

            context = []
            if ctx.contextList():
                for c in ctx.contextList().actionType():
                    text = c.getText().lower()
                    if 'believe' in text or 'belief' in text:
                        cond_type = 'believes'
                    elif 'desire' in text:
                        cond_type = 'desires'
                    else:
                        cond_type = c.getText()
                    context.append((cond_type, c.ID().getText()))

            plan = {
                "name": ctx.ID().getText(),
                "conditions": conditions,
                "context": context,
                "actions": actions,
                "event_change": event_change
            }
            self.current_agent.plans.append(plan)

    def enterAction(self, ctx):
        if self.current_env:
            action = self._parse_action(ctx, self.current_env.name)
            self.current_env.actions.append(action) 