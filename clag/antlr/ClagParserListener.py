# Generated from ./clag/antlr/ClagParser.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by ClagParser#agentSection.
    def enterAgentSection(self, ctx:ClagParser.AgentSectionContext):
        pass

    # Exit a parse tree produced by ClagParser#agentSection.
    def exitAgentSection(self, ctx:ClagParser.AgentSectionContext):
        pass


    # Enter a parse tree produced by ClagParser#environmentDef.
    def enterEnvironmentDef(self, ctx:ClagParser.EnvironmentDefContext):
        pass

    # Exit a parse tree produced by ClagParser#environmentDef.
    def exitEnvironmentDef(self, ctx:ClagParser.EnvironmentDefContext):
        pass


    # Enter a parse tree produced by ClagParser#environmentSection.
    def enterEnvironmentSection(self, ctx:ClagParser.EnvironmentSectionContext):
        pass

    # Exit a parse tree produced by ClagParser#environmentSection.
    def exitEnvironmentSection(self, ctx:ClagParser.EnvironmentSectionContext):
        pass


    # Enter a parse tree produced by ClagParser#actionName.
    def enterActionName(self, ctx:ClagParser.ActionNameContext):
        pass

    # Exit a parse tree produced by ClagParser#actionName.
    def exitActionName(self, ctx:ClagParser.ActionNameContext):
        pass


    # Enter a parse tree produced by ClagParser#plan.
    def enterPlan(self, ctx:ClagParser.PlanContext):
        pass

    # Exit a parse tree produced by ClagParser#plan.
    def exitPlan(self, ctx:ClagParser.PlanContext):
        pass


    # Enter a parse tree produced by ClagParser#idList.
    def enterIdList(self, ctx:ClagParser.IdListContext):
        pass

    # Exit a parse tree produced by ClagParser#idList.
    def exitIdList(self, ctx:ClagParser.IdListContext):
        pass


    # Enter a parse tree produced by ClagParser#conditionList.
    def enterConditionList(self, ctx:ClagParser.ConditionListContext):
        pass

    # Exit a parse tree produced by ClagParser#conditionList.
    def exitConditionList(self, ctx:ClagParser.ConditionListContext):
        pass


    # Enter a parse tree produced by ClagParser#contextList.
    def enterContextList(self, ctx:ClagParser.ContextListContext):
        pass

    # Exit a parse tree produced by ClagParser#contextList.
    def exitContextList(self, ctx:ClagParser.ContextListContext):
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