# Generated from MyParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyParser import MyParser
else:
    from MyParser import MyParser

# This class defines a complete listener for a parse tree produced by MyParser.
class MyParserListener(ParseTreeListener):

    # Enter a parse tree produced by MyParser#system.
    def enterSystem(self, ctx:MyParser.SystemContext):
        pass

    # Exit a parse tree produced by MyParser#system.
    def exitSystem(self, ctx:MyParser.SystemContext):
        pass


    # Enter a parse tree produced by MyParser#import_stmt.
    def enterImport_stmt(self, ctx:MyParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by MyParser#import_stmt.
    def exitImport_stmt(self, ctx:MyParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by MyParser#entity.
    def enterEntity(self, ctx:MyParser.EntityContext):
        pass

    # Exit a parse tree produced by MyParser#entity.
    def exitEntity(self, ctx:MyParser.EntityContext):
        pass


    # Enter a parse tree produced by MyParser#agent.
    def enterAgent(self, ctx:MyParser.AgentContext):
        pass

    # Exit a parse tree produced by MyParser#agent.
    def exitAgent(self, ctx:MyParser.AgentContext):
        pass


    # Enter a parse tree produced by MyParser#agent_section.
    def enterAgent_section(self, ctx:MyParser.Agent_sectionContext):
        pass

    # Exit a parse tree produced by MyParser#agent_section.
    def exitAgent_section(self, ctx:MyParser.Agent_sectionContext):
        pass


    # Enter a parse tree produced by MyParser#beliefs.
    def enterBeliefs(self, ctx:MyParser.BeliefsContext):
        pass

    # Exit a parse tree produced by MyParser#beliefs.
    def exitBeliefs(self, ctx:MyParser.BeliefsContext):
        pass


    # Enter a parse tree produced by MyParser#desires.
    def enterDesires(self, ctx:MyParser.DesiresContext):
        pass

    # Exit a parse tree produced by MyParser#desires.
    def exitDesires(self, ctx:MyParser.DesiresContext):
        pass


    # Enter a parse tree produced by MyParser#agent_plans.
    def enterAgent_plans(self, ctx:MyParser.Agent_plansContext):
        pass

    # Exit a parse tree produced by MyParser#agent_plans.
    def exitAgent_plans(self, ctx:MyParser.Agent_plansContext):
        pass


    # Enter a parse tree produced by MyParser#agent_plan.
    def enterAgent_plan(self, ctx:MyParser.Agent_planContext):
        pass

    # Exit a parse tree produced by MyParser#agent_plan.
    def exitAgent_plan(self, ctx:MyParser.Agent_planContext):
        pass


    # Enter a parse tree produced by MyParser#condition_list.
    def enterCondition_list(self, ctx:MyParser.Condition_listContext):
        pass

    # Exit a parse tree produced by MyParser#condition_list.
    def exitCondition_list(self, ctx:MyParser.Condition_listContext):
        pass


    # Enter a parse tree produced by MyParser#condition.
    def enterCondition(self, ctx:MyParser.ConditionContext):
        pass

    # Exit a parse tree produced by MyParser#condition.
    def exitCondition(self, ctx:MyParser.ConditionContext):
        pass


    # Enter a parse tree produced by MyParser#action.
    def enterAction(self, ctx:MyParser.ActionContext):
        pass

    # Exit a parse tree produced by MyParser#action.
    def exitAction(self, ctx:MyParser.ActionContext):
        pass


    # Enter a parse tree produced by MyParser#action_list.
    def enterAction_list(self, ctx:MyParser.Action_listContext):
        pass

    # Exit a parse tree produced by MyParser#action_list.
    def exitAction_list(self, ctx:MyParser.Action_listContext):
        pass


    # Enter a parse tree produced by MyParser#agent_action_type.
    def enterAgent_action_type(self, ctx:MyParser.Agent_action_typeContext):
        pass

    # Exit a parse tree produced by MyParser#agent_action_type.
    def exitAgent_action_type(self, ctx:MyParser.Agent_action_typeContext):
        pass


    # Enter a parse tree produced by MyParser#environment.
    def enterEnvironment(self, ctx:MyParser.EnvironmentContext):
        pass

    # Exit a parse tree produced by MyParser#environment.
    def exitEnvironment(self, ctx:MyParser.EnvironmentContext):
        pass


    # Enter a parse tree produced by MyParser#environment_section.
    def enterEnvironment_section(self, ctx:MyParser.Environment_sectionContext):
        pass

    # Exit a parse tree produced by MyParser#environment_section.
    def exitEnvironment_section(self, ctx:MyParser.Environment_sectionContext):
        pass


    # Enter a parse tree produced by MyParser#perceptions.
    def enterPerceptions(self, ctx:MyParser.PerceptionsContext):
        pass

    # Exit a parse tree produced by MyParser#perceptions.
    def exitPerceptions(self, ctx:MyParser.PerceptionsContext):
        pass


    # Enter a parse tree produced by MyParser#environment_plans.
    def enterEnvironment_plans(self, ctx:MyParser.Environment_plansContext):
        pass

    # Exit a parse tree produced by MyParser#environment_plans.
    def exitEnvironment_plans(self, ctx:MyParser.Environment_plansContext):
        pass


    # Enter a parse tree produced by MyParser#env_plan.
    def enterEnv_plan(self, ctx:MyParser.Env_planContext):
        pass

    # Exit a parse tree produced by MyParser#env_plan.
    def exitEnv_plan(self, ctx:MyParser.Env_planContext):
        pass


    # Enter a parse tree produced by MyParser#env_action_list.
    def enterEnv_action_list(self, ctx:MyParser.Env_action_listContext):
        pass

    # Exit a parse tree produced by MyParser#env_action_list.
    def exitEnv_action_list(self, ctx:MyParser.Env_action_listContext):
        pass


    # Enter a parse tree produced by MyParser#env_action.
    def enterEnv_action(self, ctx:MyParser.Env_actionContext):
        pass

    # Exit a parse tree produced by MyParser#env_action.
    def exitEnv_action(self, ctx:MyParser.Env_actionContext):
        pass


    # Enter a parse tree produced by MyParser#env_action_type.
    def enterEnv_action_type(self, ctx:MyParser.Env_action_typeContext):
        pass

    # Exit a parse tree produced by MyParser#env_action_type.
    def exitEnv_action_type(self, ctx:MyParser.Env_action_typeContext):
        pass


    # Enter a parse tree produced by MyParser#id_list.
    def enterId_list(self, ctx:MyParser.Id_listContext):
        pass

    # Exit a parse tree produced by MyParser#id_list.
    def exitId_list(self, ctx:MyParser.Id_listContext):
        pass



del MyParser