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


    # Enter a parse tree produced by ClagParser#entity.
    def enterEntity(self, ctx:ClagParser.EntityContext):
        pass

    # Exit a parse tree produced by ClagParser#entity.
    def exitEntity(self, ctx:ClagParser.EntityContext):
        pass


    # Enter a parse tree produced by ClagParser#agent.
    def enterAgent(self, ctx:ClagParser.AgentContext):
        pass

    # Exit a parse tree produced by ClagParser#agent.
    def exitAgent(self, ctx:ClagParser.AgentContext):
        pass


    # Enter a parse tree produced by ClagParser#agent_section.
    def enterAgent_section(self, ctx:ClagParser.Agent_sectionContext):
        pass

    # Exit a parse tree produced by ClagParser#agent_section.
    def exitAgent_section(self, ctx:ClagParser.Agent_sectionContext):
        pass


    # Enter a parse tree produced by ClagParser#beliefs.
    def enterBeliefs(self, ctx:ClagParser.BeliefsContext):
        pass

    # Exit a parse tree produced by ClagParser#beliefs.
    def exitBeliefs(self, ctx:ClagParser.BeliefsContext):
        pass


    # Enter a parse tree produced by ClagParser#desires.
    def enterDesires(self, ctx:ClagParser.DesiresContext):
        pass

    # Exit a parse tree produced by ClagParser#desires.
    def exitDesires(self, ctx:ClagParser.DesiresContext):
        pass


    # Enter a parse tree produced by ClagParser#agent_plans.
    def enterAgent_plans(self, ctx:ClagParser.Agent_plansContext):
        pass

    # Exit a parse tree produced by ClagParser#agent_plans.
    def exitAgent_plans(self, ctx:ClagParser.Agent_plansContext):
        pass


    # Enter a parse tree produced by ClagParser#agent_plan.
    def enterAgent_plan(self, ctx:ClagParser.Agent_planContext):
        pass

    # Exit a parse tree produced by ClagParser#agent_plan.
    def exitAgent_plan(self, ctx:ClagParser.Agent_planContext):
        pass


    # Enter a parse tree produced by ClagParser#condition_list.
    def enterCondition_list(self, ctx:ClagParser.Condition_listContext):
        pass

    # Exit a parse tree produced by ClagParser#condition_list.
    def exitCondition_list(self, ctx:ClagParser.Condition_listContext):
        pass


    # Enter a parse tree produced by ClagParser#condition.
    def enterCondition(self, ctx:ClagParser.ConditionContext):
        pass

    # Exit a parse tree produced by ClagParser#condition.
    def exitCondition(self, ctx:ClagParser.ConditionContext):
        pass


    # Enter a parse tree produced by ClagParser#action.
    def enterAction(self, ctx:ClagParser.ActionContext):
        pass

    # Exit a parse tree produced by ClagParser#action.
    def exitAction(self, ctx:ClagParser.ActionContext):
        pass


    # Enter a parse tree produced by ClagParser#action_list.
    def enterAction_list(self, ctx:ClagParser.Action_listContext):
        pass

    # Exit a parse tree produced by ClagParser#action_list.
    def exitAction_list(self, ctx:ClagParser.Action_listContext):
        pass


    # Enter a parse tree produced by ClagParser#agent_action_type.
    def enterAgent_action_type(self, ctx:ClagParser.Agent_action_typeContext):
        pass

    # Exit a parse tree produced by ClagParser#agent_action_type.
    def exitAgent_action_type(self, ctx:ClagParser.Agent_action_typeContext):
        pass


    # Enter a parse tree produced by ClagParser#environment.
    def enterEnvironment(self, ctx:ClagParser.EnvironmentContext):
        pass

    # Exit a parse tree produced by ClagParser#environment.
    def exitEnvironment(self, ctx:ClagParser.EnvironmentContext):
        pass


    # Enter a parse tree produced by ClagParser#environment_section.
    def enterEnvironment_section(self, ctx:ClagParser.Environment_sectionContext):
        pass

    # Exit a parse tree produced by ClagParser#environment_section.
    def exitEnvironment_section(self, ctx:ClagParser.Environment_sectionContext):
        pass


    # Enter a parse tree produced by ClagParser#perceptions.
    def enterPerceptions(self, ctx:ClagParser.PerceptionsContext):
        pass

    # Exit a parse tree produced by ClagParser#perceptions.
    def exitPerceptions(self, ctx:ClagParser.PerceptionsContext):
        pass


    # Enter a parse tree produced by ClagParser#environment_plans.
    def enterEnvironment_plans(self, ctx:ClagParser.Environment_plansContext):
        pass

    # Exit a parse tree produced by ClagParser#environment_plans.
    def exitEnvironment_plans(self, ctx:ClagParser.Environment_plansContext):
        pass


    # Enter a parse tree produced by ClagParser#env_plan.
    def enterEnv_plan(self, ctx:ClagParser.Env_planContext):
        pass

    # Exit a parse tree produced by ClagParser#env_plan.
    def exitEnv_plan(self, ctx:ClagParser.Env_planContext):
        pass


    # Enter a parse tree produced by ClagParser#env_action_list.
    def enterEnv_action_list(self, ctx:ClagParser.Env_action_listContext):
        pass

    # Exit a parse tree produced by ClagParser#env_action_list.
    def exitEnv_action_list(self, ctx:ClagParser.Env_action_listContext):
        pass


    # Enter a parse tree produced by ClagParser#env_action.
    def enterEnv_action(self, ctx:ClagParser.Env_actionContext):
        pass

    # Exit a parse tree produced by ClagParser#env_action.
    def exitEnv_action(self, ctx:ClagParser.Env_actionContext):
        pass


    # Enter a parse tree produced by ClagParser#env_action_type.
    def enterEnv_action_type(self, ctx:ClagParser.Env_action_typeContext):
        pass

    # Exit a parse tree produced by ClagParser#env_action_type.
    def exitEnv_action_type(self, ctx:ClagParser.Env_action_typeContext):
        pass


    # Enter a parse tree produced by ClagParser#id_list.
    def enterId_list(self, ctx:ClagParser.Id_listContext):
        pass

    # Exit a parse tree produced by ClagParser#id_list.
    def exitId_list(self, ctx:ClagParser.Id_listContext):
        pass



del ClagParser