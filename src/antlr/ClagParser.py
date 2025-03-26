# Generated from ClagParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,168,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,1,1,1,3,1,53,8,
        1,1,2,1,2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,1,3,1,3,3,3,66,8,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,7,
        1,7,1,7,1,7,1,7,1,7,3,7,87,8,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,
        8,97,8,8,10,8,12,8,100,9,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,
        1,11,5,11,111,8,11,10,11,12,11,114,9,11,1,12,1,12,1,13,1,13,1,13,
        5,13,121,8,13,10,13,12,13,124,9,13,1,14,1,14,3,14,128,8,14,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,5,16,137,8,16,10,16,12,16,140,9,16,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,5,18,150,8,18,10,18,12,18,
        153,9,18,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,21,5,21,163,8,21,10,
        21,12,21,166,9,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,0,2,1,0,9,12,1,0,16,17,159,0,47,1,0,0,
        0,2,52,1,0,0,0,4,54,1,0,0,0,6,65,1,0,0,0,8,67,1,0,0,0,10,70,1,0,
        0,0,12,73,1,0,0,0,14,80,1,0,0,0,16,93,1,0,0,0,18,101,1,0,0,0,20,
        104,1,0,0,0,22,107,1,0,0,0,24,115,1,0,0,0,26,117,1,0,0,0,28,127,
        1,0,0,0,30,129,1,0,0,0,32,132,1,0,0,0,34,141,1,0,0,0,36,146,1,0,
        0,0,38,154,1,0,0,0,40,157,1,0,0,0,42,159,1,0,0,0,44,46,3,2,1,0,45,
        44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,
        0,49,47,1,0,0,0,50,53,3,4,2,0,51,53,3,26,13,0,52,50,1,0,0,0,52,51,
        1,0,0,0,53,3,1,0,0,0,54,55,5,1,0,0,55,59,5,18,0,0,56,58,3,6,3,0,
        57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,5,1,0,
        0,0,61,59,1,0,0,0,62,66,3,8,4,0,63,66,3,10,5,0,64,66,3,12,6,0,65,
        62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,7,1,0,0,0,67,68,5,2,0,
        0,68,69,3,42,21,0,69,9,1,0,0,0,70,71,5,3,0,0,71,72,3,42,21,0,72,
        11,1,0,0,0,73,77,5,4,0,0,74,76,3,14,7,0,75,74,1,0,0,0,76,79,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,79,77,1,0,0,0,80,81,
        5,18,0,0,81,82,5,20,0,0,82,83,5,5,0,0,83,86,3,20,10,0,84,85,5,6,
        0,0,85,87,3,16,8,0,86,84,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,
        89,5,21,0,0,89,90,5,7,0,0,90,91,3,22,11,0,91,92,5,8,0,0,92,15,1,
        0,0,0,93,98,3,18,9,0,94,95,5,19,0,0,95,97,3,18,9,0,96,94,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,17,1,0,0,0,100,98,
        1,0,0,0,101,102,3,24,12,0,102,103,5,18,0,0,103,19,1,0,0,0,104,105,
        3,24,12,0,105,106,5,18,0,0,106,21,1,0,0,0,107,112,3,20,10,0,108,
        109,5,19,0,0,109,111,3,20,10,0,110,108,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,23,1,0,0,0,114,112,1,0,0,0,115,116,
        7,0,0,0,116,25,1,0,0,0,117,118,5,13,0,0,118,122,5,18,0,0,119,121,
        3,28,14,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,
        1,0,0,0,123,27,1,0,0,0,124,122,1,0,0,0,125,128,3,30,15,0,126,128,
        3,32,16,0,127,125,1,0,0,0,127,126,1,0,0,0,128,29,1,0,0,0,129,130,
        5,14,0,0,130,131,3,42,21,0,131,31,1,0,0,0,132,133,5,15,0,0,133,138,
        3,34,17,0,134,135,5,19,0,0,135,137,3,34,17,0,136,134,1,0,0,0,137,
        140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,33,1,0,0,0,140,138,
        1,0,0,0,141,142,5,18,0,0,142,143,5,7,0,0,143,144,3,36,18,0,144,145,
        5,8,0,0,145,35,1,0,0,0,146,151,3,38,19,0,147,148,5,19,0,0,148,150,
        3,38,19,0,149,147,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,
        1,0,0,0,152,37,1,0,0,0,153,151,1,0,0,0,154,155,3,40,20,0,155,156,
        5,18,0,0,156,39,1,0,0,0,157,158,7,1,0,0,158,41,1,0,0,0,159,164,5,
        18,0,0,160,161,5,19,0,0,161,163,5,18,0,0,162,160,1,0,0,0,163,166,
        1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,43,1,0,0,0,166,164,1,
        0,0,0,13,47,52,59,65,77,86,98,112,122,127,138,151,164
    ]

class ClagParser ( Parser ):

    grammarFileName = "ClagParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agent'", "'beliefs:'", "'desires:'", 
                     "'plans:'", "'when:'", "'contains:'", "'do'", "'end'", 
                     "'believe'", "'disbelieve'", "'achieve'", "'abandon'", 
                     "'environment'", "'perceptions:'", "'actions:'", "'percept'", 
                     "'change'", "<INVALID>", "','", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "BELIEFS", "DESIRES", "PLANS", 
                      "WHEN", "CONTAINS", "DO", "END", "BELIEVE", "DISBELIEVE", 
                      "ACHIEVE", "ABANDON", "ENVIRONMENT", "PERCEPTIONS", 
                      "ACTIONS", "PERCEPT", "CHANGE", "ID", "COMMA", "LPAREN", 
                      "RPAREN", "SEMI", "WS" ]

    RULE_system = 0
    RULE_entity = 1
    RULE_agent = 2
    RULE_agent_section = 3
    RULE_beliefs = 4
    RULE_desires = 5
    RULE_agent_plans = 6
    RULE_agent_plan = 7
    RULE_condition_list = 8
    RULE_condition = 9
    RULE_action = 10
    RULE_action_list = 11
    RULE_agent_action_type = 12
    RULE_environment = 13
    RULE_environment_section = 14
    RULE_perceptions = 15
    RULE_environment_plans = 16
    RULE_env_plan = 17
    RULE_env_action_list = 18
    RULE_env_action = 19
    RULE_env_action_type = 20
    RULE_id_list = 21

    ruleNames =  [ "system", "entity", "agent", "agent_section", "beliefs", 
                   "desires", "agent_plans", "agent_plan", "condition_list", 
                   "condition", "action", "action_list", "agent_action_type", 
                   "environment", "environment_section", "perceptions", 
                   "environment_plans", "env_plan", "env_action_list", "env_action", 
                   "env_action_type", "id_list" ]

    EOF = Token.EOF
    AGENT=1
    BELIEFS=2
    DESIRES=3
    PLANS=4
    WHEN=5
    CONTAINS=6
    DO=7
    END=8
    BELIEVE=9
    DISBELIEVE=10
    ACHIEVE=11
    ABANDON=12
    ENVIRONMENT=13
    PERCEPTIONS=14
    ACTIONS=15
    PERCEPT=16
    CHANGE=17
    ID=18
    COMMA=19
    LPAREN=20
    RPAREN=21
    SEMI=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SystemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.EntityContext)
            else:
                return self.getTypedRuleContext(ClagParser.EntityContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_system

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem" ):
                listener.enterSystem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem" ):
                listener.exitSystem(self)




    def system(self):

        localctx = ClagParser.SystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_system)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==13:
                self.state = 44
                self.entity()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agent(self):
            return self.getTypedRuleContext(ClagParser.AgentContext,0)


        def environment(self):
            return self.getTypedRuleContext(ClagParser.EnvironmentContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = ClagParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entity)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.agent()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.environment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENT(self):
            return self.getToken(ClagParser.AGENT, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def agent_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.Agent_sectionContext)
            else:
                return self.getTypedRuleContext(ClagParser.Agent_sectionContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_agent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent" ):
                listener.enterAgent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent" ):
                listener.exitAgent(self)




    def agent(self):

        localctx = ClagParser.AgentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_agent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ClagParser.AGENT)
            self.state = 55
            self.match(ClagParser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 56
                self.agent_section()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Agent_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def beliefs(self):
            return self.getTypedRuleContext(ClagParser.BeliefsContext,0)


        def desires(self):
            return self.getTypedRuleContext(ClagParser.DesiresContext,0)


        def agent_plans(self):
            return self.getTypedRuleContext(ClagParser.Agent_plansContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_agent_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_section" ):
                listener.enterAgent_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_section" ):
                listener.exitAgent_section(self)




    def agent_section(self):

        localctx = ClagParser.Agent_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_agent_section)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.beliefs()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.desires()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.agent_plans()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeliefsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BELIEFS(self):
            return self.getToken(ClagParser.BELIEFS, 0)

        def id_list(self):
            return self.getTypedRuleContext(ClagParser.Id_listContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_beliefs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeliefs" ):
                listener.enterBeliefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeliefs" ):
                listener.exitBeliefs(self)




    def beliefs(self):

        localctx = ClagParser.BeliefsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_beliefs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ClagParser.BELIEFS)
            self.state = 68
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DesiresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESIRES(self):
            return self.getToken(ClagParser.DESIRES, 0)

        def id_list(self):
            return self.getTypedRuleContext(ClagParser.Id_listContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_desires

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesires" ):
                listener.enterDesires(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesires" ):
                listener.exitDesires(self)




    def desires(self):

        localctx = ClagParser.DesiresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_desires)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ClagParser.DESIRES)
            self.state = 71
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Agent_plansContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLANS(self):
            return self.getToken(ClagParser.PLANS, 0)

        def agent_plan(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.Agent_planContext)
            else:
                return self.getTypedRuleContext(ClagParser.Agent_planContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_agent_plans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_plans" ):
                listener.enterAgent_plans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_plans" ):
                listener.exitAgent_plans(self)




    def agent_plans(self):

        localctx = ClagParser.Agent_plansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_agent_plans)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(ClagParser.PLANS)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 74
                self.agent_plan()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Agent_planContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ClagParser.LPAREN, 0)

        def WHEN(self):
            return self.getToken(ClagParser.WHEN, 0)

        def action(self):
            return self.getTypedRuleContext(ClagParser.ActionContext,0)


        def RPAREN(self):
            return self.getToken(ClagParser.RPAREN, 0)

        def DO(self):
            return self.getToken(ClagParser.DO, 0)

        def action_list(self):
            return self.getTypedRuleContext(ClagParser.Action_listContext,0)


        def END(self):
            return self.getToken(ClagParser.END, 0)

        def CONTAINS(self):
            return self.getToken(ClagParser.CONTAINS, 0)

        def condition_list(self):
            return self.getTypedRuleContext(ClagParser.Condition_listContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_agent_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_plan" ):
                listener.enterAgent_plan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_plan" ):
                listener.exitAgent_plan(self)




    def agent_plan(self):

        localctx = ClagParser.Agent_planContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_agent_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ClagParser.ID)
            self.state = 81
            self.match(ClagParser.LPAREN)
            self.state = 82
            self.match(ClagParser.WHEN)
            self.state = 83
            self.action()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 84
                self.match(ClagParser.CONTAINS)
                self.state = 85
                self.condition_list()


            self.state = 88
            self.match(ClagParser.RPAREN)
            self.state = 89
            self.match(ClagParser.DO)
            self.state = 90
            self.action_list()
            self.state = 91
            self.match(ClagParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ConditionContext)
            else:
                return self.getTypedRuleContext(ClagParser.ConditionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_condition_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_list" ):
                listener.enterCondition_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_list" ):
                listener.exitCondition_list(self)




    def condition_list(self):

        localctx = ClagParser.Condition_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.condition()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 94
                self.match(ClagParser.COMMA)
                self.state = 95
                self.condition()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agent_action_type(self):
            return self.getTypedRuleContext(ClagParser.Agent_action_typeContext,0)


        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ClagParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.agent_action_type()
            self.state = 102
            self.match(ClagParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agent_action_type(self):
            return self.getTypedRuleContext(ClagParser.Agent_action_typeContext,0)


        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = ClagParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.agent_action_type()
            self.state = 105
            self.match(ClagParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Action_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ActionContext)
            else:
                return self.getTypedRuleContext(ClagParser.ActionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_action_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction_list" ):
                listener.enterAction_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction_list" ):
                listener.exitAction_list(self)




    def action_list(self):

        localctx = ClagParser.Action_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_action_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.action()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 108
                self.match(ClagParser.COMMA)
                self.state = 109
                self.action()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Agent_action_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BELIEVE(self):
            return self.getToken(ClagParser.BELIEVE, 0)

        def DISBELIEVE(self):
            return self.getToken(ClagParser.DISBELIEVE, 0)

        def ACHIEVE(self):
            return self.getToken(ClagParser.ACHIEVE, 0)

        def ABANDON(self):
            return self.getToken(ClagParser.ABANDON, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_agent_action_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_action_type" ):
                listener.enterAgent_action_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_action_type" ):
                listener.exitAgent_action_type(self)




    def agent_action_type(self):

        localctx = ClagParser.Agent_action_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_agent_action_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvironmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENVIRONMENT(self):
            return self.getToken(ClagParser.ENVIRONMENT, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def environment_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.Environment_sectionContext)
            else:
                return self.getTypedRuleContext(ClagParser.Environment_sectionContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_environment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironment" ):
                listener.enterEnvironment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironment" ):
                listener.exitEnvironment(self)




    def environment(self):

        localctx = ClagParser.EnvironmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_environment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ClagParser.ENVIRONMENT)
            self.state = 118
            self.match(ClagParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 119
                self.environment_section()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Environment_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def perceptions(self):
            return self.getTypedRuleContext(ClagParser.PerceptionsContext,0)


        def environment_plans(self):
            return self.getTypedRuleContext(ClagParser.Environment_plansContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_environment_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironment_section" ):
                listener.enterEnvironment_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironment_section" ):
                listener.exitEnvironment_section(self)




    def environment_section(self):

        localctx = ClagParser.Environment_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_environment_section)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.perceptions()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.environment_plans()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PerceptionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCEPTIONS(self):
            return self.getToken(ClagParser.PERCEPTIONS, 0)

        def id_list(self):
            return self.getTypedRuleContext(ClagParser.Id_listContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_perceptions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerceptions" ):
                listener.enterPerceptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerceptions" ):
                listener.exitPerceptions(self)




    def perceptions(self):

        localctx = ClagParser.PerceptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_perceptions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ClagParser.PERCEPTIONS)
            self.state = 130
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Environment_plansContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIONS(self):
            return self.getToken(ClagParser.ACTIONS, 0)

        def env_plan(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.Env_planContext)
            else:
                return self.getTypedRuleContext(ClagParser.Env_planContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_environment_plans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironment_plans" ):
                listener.enterEnvironment_plans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironment_plans" ):
                listener.exitEnvironment_plans(self)




    def environment_plans(self):

        localctx = ClagParser.Environment_plansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_environment_plans)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ClagParser.ACTIONS)

            self.state = 133
            self.env_plan()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 134
                self.match(ClagParser.COMMA)
                self.state = 135
                self.env_plan()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Env_planContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def DO(self):
            return self.getToken(ClagParser.DO, 0)

        def env_action_list(self):
            return self.getTypedRuleContext(ClagParser.Env_action_listContext,0)


        def END(self):
            return self.getToken(ClagParser.END, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_env_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_plan" ):
                listener.enterEnv_plan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_plan" ):
                listener.exitEnv_plan(self)




    def env_plan(self):

        localctx = ClagParser.Env_planContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_env_plan)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ClagParser.ID)
            self.state = 142
            self.match(ClagParser.DO)
            self.state = 143
            self.env_action_list()
            self.state = 144
            self.match(ClagParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Env_action_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def env_action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.Env_actionContext)
            else:
                return self.getTypedRuleContext(ClagParser.Env_actionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_env_action_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_action_list" ):
                listener.enterEnv_action_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_action_list" ):
                listener.exitEnv_action_list(self)




    def env_action_list(self):

        localctx = ClagParser.Env_action_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_env_action_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.env_action()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 147
                self.match(ClagParser.COMMA)
                self.state = 148
                self.env_action()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Env_actionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def env_action_type(self):
            return self.getTypedRuleContext(ClagParser.Env_action_typeContext,0)


        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_env_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_action" ):
                listener.enterEnv_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_action" ):
                listener.exitEnv_action(self)




    def env_action(self):

        localctx = ClagParser.Env_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_env_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.env_action_type()
            self.state = 155
            self.match(ClagParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Env_action_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCEPT(self):
            return self.getToken(ClagParser.PERCEPT, 0)

        def CHANGE(self):
            return self.getToken(ClagParser.CHANGE, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_env_action_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_action_type" ):
                listener.enterEnv_action_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_action_type" ):
                listener.exitEnv_action_type(self)




    def env_action_type(self):

        localctx = ClagParser.Env_action_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_env_action_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.ID)
            else:
                return self.getToken(ClagParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)




    def id_list(self):

        localctx = ClagParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ClagParser.ID)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 160
                self.match(ClagParser.COMMA)
                self.state = 161
                self.match(ClagParser.ID)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





