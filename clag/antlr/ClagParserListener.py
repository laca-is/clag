# Generated from ClagParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ClagParser import ClagParser
else:
    from ClagParser import ClagParser

# This class defines a complete listener for a parse tree produced by ClagParser.
class ClagParserListener(ParseTreeListener):

    # Enter a parse tree produced by ClagParser#system.
    def enterSystem(self, ctx:ClagParser.SystemContext):
        pass

    # Exit a parse tree produced by ClagParser#system.
    def exitSystem(self, ctx:ClagParser.SystemContext):
        pass


    # Enter a parse tree produced by ClagParser#agentDef.
    def enterAgentDef(self, ctx:ClagParser.AgentDefContext):
        pass

    # Exit a parse tree produced by ClagParser#agentDef.
    def exitAgentDef(self, ctx:ClagParser.AgentDefContext):
        pass


    # Enter a parse tree produced by ClagParser#agentBeliefs.
    def enterAgentBeliefs(self, ctx:ClagParser.AgentBeliefsContext):
        pass

    # Exit a parse tree produced by ClagParser#agentBeliefs.
    def exitAgentBeliefs(self, ctx:ClagParser.AgentBeliefsContext):
        pass


    # Enter a parse tree produced by ClagParser#agentDesires.
    def enterAgentDesires(self, ctx:ClagParser.AgentDesiresContext):
        pass

    # Exit a parse tree produced by ClagParser#agentDesires.
    def exitAgentDesires(self, ctx:ClagParser.AgentDesiresContext):
        pass


    # Enter a parse tree produced by ClagParser#agentPlans.
    def enterAgentPlans(self, ctx:ClagParser.AgentPlansContext):
        pass

    # Exit a parse tree produced by ClagParser#agentPlans.
    def exitAgentPlans(self, ctx:ClagParser.AgentPlansContext):
        pass


    # Enter a parse tree produced by ClagParser#agentCHANNEL.
    def enterAgentCHANNEL(self, ctx:ClagParser.AgentCHANNELContext):
        pass

    # Exit a parse tree produced by ClagParser#agentCHANNEL.
    def exitAgentCHANNEL(self, ctx:ClagParser.AgentCHANNELContext):
        pass


    # Enter a parse tree produced by ClagParser#environmentDef.
    def enterEnvironmentDef(self, ctx:ClagParser.EnvironmentDefContext):
        pass

    # Exit a parse tree produced by ClagParser#environmentDef.
    def exitEnvironmentDef(self, ctx:ClagParser.EnvironmentDefContext):
        pass


    # Enter a parse tree produced by ClagParser#envPerceptions.
    def enterEnvPerceptions(self, ctx:ClagParser.EnvPerceptionsContext):
        pass

    # Exit a parse tree produced by ClagParser#envPerceptions.
    def exitEnvPerceptions(self, ctx:ClagParser.EnvPerceptionsContext):
        pass


    # Enter a parse tree produced by ClagParser#envActions.
    def enterEnvActions(self, ctx:ClagParser.EnvActionsContext):
        pass

    # Exit a parse tree produced by ClagParser#envActions.
    def exitEnvActions(self, ctx:ClagParser.EnvActionsContext):
        pass


    # Enter a parse tree produced by ClagParser#plan.
    def enterPlan(self, ctx:ClagParser.PlanContext):
        pass

    # Exit a parse tree produced by ClagParser#plan.
    def exitPlan(self, ctx:ClagParser.PlanContext):
        pass


    # Enter a parse tree produced by ClagParser#actionDef.
    def enterActionDef(self, ctx:ClagParser.ActionDefContext):
        pass

    # Exit a parse tree produced by ClagParser#actionDef.
    def exitActionDef(self, ctx:ClagParser.ActionDefContext):
        pass


    # Enter a parse tree produced by ClagParser#idList.
    def enterIdList(self, ctx:ClagParser.IdListContext):
        pass

    # Exit a parse tree produced by ClagParser#idList.
    def exitIdList(self, ctx:ClagParser.IdListContext):
        pass


    # Enter a parse tree produced by ClagParser#condition.
    def enterCondition(self, ctx:ClagParser.ConditionContext):
        pass

    # Exit a parse tree produced by ClagParser#condition.
    def exitCondition(self, ctx:ClagParser.ConditionContext):
        pass


    # Enter a parse tree produced by ClagParser#conditionList.
    def enterConditionList(self, ctx:ClagParser.ConditionListContext):
        pass

    # Exit a parse tree produced by ClagParser#conditionList.
    def exitConditionList(self, ctx:ClagParser.ConditionListContext):
        pass


    # Enter a parse tree produced by ClagParser#actionList.
    def enterActionList(self, ctx:ClagParser.ActionListContext):
        pass

    # Exit a parse tree produced by ClagParser#actionList.
    def exitActionList(self, ctx:ClagParser.ActionListContext):
        pass


    # Enter a parse tree produced by ClagParser#action.
    def enterAction(self, ctx:ClagParser.ActionContext):
        pass

    # Exit a parse tree produced by ClagParser#action.
    def exitAction(self, ctx:ClagParser.ActionContext):
        pass


    # Enter a parse tree produced by ClagParser#sendAction.
    def enterSendAction(self, ctx:ClagParser.SendActionContext):
        pass

    # Exit a parse tree produced by ClagParser#sendAction.
    def exitSendAction(self, ctx:ClagParser.SendActionContext):
        pass


    # Enter a parse tree produced by ClagParser#actionType.
    def enterActionType(self, ctx:ClagParser.ActionTypeContext):
        pass

    # Exit a parse tree produced by ClagParser#actionType.
    def exitActionType(self, ctx:ClagParser.ActionTypeContext):
        pass



del ClagParser