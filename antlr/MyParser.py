# Generated from MyParser.g4 by ANTLR 4.13.2
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
        4,1,24,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,5,0,
        54,8,0,10,0,12,0,57,9,0,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,3,2,66,8,
        2,1,3,1,3,1,3,5,3,71,8,3,10,3,12,3,74,9,3,1,4,1,4,1,4,3,4,79,8,4,
        1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,91,8,7,10,7,12,7,94,
        9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,102,8,8,1,8,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,5,9,112,8,9,10,9,12,9,115,9,9,1,10,1,10,1,10,1,11,1,11,1,
        11,1,12,1,12,1,12,5,12,126,8,12,10,12,12,12,129,9,12,1,13,1,13,1,
        14,1,14,1,14,5,14,136,8,14,10,14,12,14,139,9,14,1,15,1,15,3,15,143,
        8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,17,5,17,152,8,17,10,17,12,17,
        155,9,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,165,8,19,10,
        19,12,19,168,9,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,22,5,22,178,
        8,22,10,22,12,22,181,9,22,1,22,0,0,23,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,0,2,1,0,9,12,1,0,16,17,175,0,
        49,1,0,0,0,2,58,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,78,1,0,0,0,10,
        80,1,0,0,0,12,83,1,0,0,0,14,86,1,0,0,0,16,95,1,0,0,0,18,108,1,0,
        0,0,20,116,1,0,0,0,22,119,1,0,0,0,24,122,1,0,0,0,26,130,1,0,0,0,
        28,132,1,0,0,0,30,142,1,0,0,0,32,144,1,0,0,0,34,147,1,0,0,0,36,156,
        1,0,0,0,38,161,1,0,0,0,40,169,1,0,0,0,42,172,1,0,0,0,44,174,1,0,
        0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,
        1,0,0,0,50,55,1,0,0,0,51,49,1,0,0,0,52,54,3,4,2,0,53,52,1,0,0,0,
        54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,1,1,0,0,0,57,55,1,0,
        0,0,58,59,5,18,0,0,59,61,5,19,0,0,60,62,5,23,0,0,61,60,1,0,0,0,61,
        62,1,0,0,0,62,3,1,0,0,0,63,66,3,6,3,0,64,66,3,28,14,0,65,63,1,0,
        0,0,65,64,1,0,0,0,66,5,1,0,0,0,67,68,5,1,0,0,68,72,5,19,0,0,69,71,
        3,8,4,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,7,1,0,0,0,74,72,1,0,0,0,75,79,3,10,5,0,76,79,3,12,6,0,77,79,3,
        14,7,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,9,1,0,0,0,80,
        81,5,2,0,0,81,82,3,44,22,0,82,11,1,0,0,0,83,84,5,3,0,0,84,85,3,44,
        22,0,85,13,1,0,0,0,86,87,5,4,0,0,87,92,3,16,8,0,88,89,5,20,0,0,89,
        91,3,16,8,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,
        0,0,93,15,1,0,0,0,94,92,1,0,0,0,95,96,5,19,0,0,96,97,5,21,0,0,97,
        98,5,5,0,0,98,101,3,22,11,0,99,100,5,6,0,0,100,102,3,18,9,0,101,
        99,1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,22,0,0,104,
        105,5,7,0,0,105,106,3,24,12,0,106,107,5,8,0,0,107,17,1,0,0,0,108,
        113,3,20,10,0,109,110,5,20,0,0,110,112,3,20,10,0,111,109,1,0,0,0,
        112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,19,1,0,0,0,115,
        113,1,0,0,0,116,117,3,26,13,0,117,118,5,19,0,0,118,21,1,0,0,0,119,
        120,3,26,13,0,120,121,5,19,0,0,121,23,1,0,0,0,122,127,3,22,11,0,
        123,124,5,20,0,0,124,126,3,22,11,0,125,123,1,0,0,0,126,129,1,0,0,
        0,127,125,1,0,0,0,127,128,1,0,0,0,128,25,1,0,0,0,129,127,1,0,0,0,
        130,131,7,0,0,0,131,27,1,0,0,0,132,133,5,13,0,0,133,137,5,19,0,0,
        134,136,3,30,15,0,135,134,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,
        0,137,138,1,0,0,0,138,29,1,0,0,0,139,137,1,0,0,0,140,143,3,32,16,
        0,141,143,3,34,17,0,142,140,1,0,0,0,142,141,1,0,0,0,143,31,1,0,0,
        0,144,145,5,14,0,0,145,146,3,44,22,0,146,33,1,0,0,0,147,148,5,15,
        0,0,148,153,3,36,18,0,149,150,5,20,0,0,150,152,3,36,18,0,151,149,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,35,1,
        0,0,0,155,153,1,0,0,0,156,157,5,19,0,0,157,158,5,7,0,0,158,159,3,
        38,19,0,159,160,5,8,0,0,160,37,1,0,0,0,161,166,3,40,20,0,162,163,
        5,20,0,0,163,165,3,40,20,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,
        1,0,0,0,166,167,1,0,0,0,167,39,1,0,0,0,168,166,1,0,0,0,169,170,3,
        42,21,0,170,171,5,19,0,0,171,41,1,0,0,0,172,173,7,1,0,0,173,43,1,
        0,0,0,174,179,5,19,0,0,175,176,5,20,0,0,176,178,5,19,0,0,177,175,
        1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,45,1,
        0,0,0,181,179,1,0,0,0,15,49,55,61,65,72,78,92,101,113,127,137,142,
        153,166,179
    ]

class MyParser ( Parser ):

    grammarFileName = "MyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agent'", "'beliefs:'", "'desires:'", 
                     "'plans:'", "'when:'", "'contains:'", "'do'", "'end'", 
                     "'believe'", "'disbelieve'", "'achieve'", "'abandon'", 
                     "'environment'", "'perceptions:'", "'actions:'", "'percept'", 
                     "'change'", "'import'", "<INVALID>", "','", "'('", 
                     "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "BELIEFS", "DESIRES", "PLANS", 
                      "WHEN", "CONTAINS", "DO", "END", "BELIEVE", "DISBELIEVE", 
                      "ACHIEVE", "ABANDON", "ENVIRONMENT", "PERCEPTIONS", 
                      "ACTIONS", "PERCEPT", "CHANGE", "IMPORT", "ID", "COMMA", 
                      "LPAREN", "RPAREN", "SEMI", "WS" ]

    RULE_system = 0
    RULE_import_stmt = 1
    RULE_entity = 2
    RULE_agent = 3
    RULE_agent_section = 4
    RULE_beliefs = 5
    RULE_desires = 6
    RULE_agent_plans = 7
    RULE_agent_plan = 8
    RULE_condition_list = 9
    RULE_condition = 10
    RULE_action = 11
    RULE_action_list = 12
    RULE_agent_action_type = 13
    RULE_environment = 14
    RULE_environment_section = 15
    RULE_perceptions = 16
    RULE_environment_plans = 17
    RULE_env_plan = 18
    RULE_env_action_list = 19
    RULE_env_action = 20
    RULE_env_action_type = 21
    RULE_id_list = 22

    ruleNames =  [ "system", "import_stmt", "entity", "agent", "agent_section", 
                   "beliefs", "desires", "agent_plans", "agent_plan", "condition_list", 
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
    IMPORT=18
    ID=19
    COMMA=20
    LPAREN=21
    RPAREN=22
    SEMI=23
    WS=24

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

        def import_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.Import_stmtContext)
            else:
                return self.getTypedRuleContext(MyParser.Import_stmtContext,i)


        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.EntityContext)
            else:
                return self.getTypedRuleContext(MyParser.EntityContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_system

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSystem" ):
                listener.enterSystem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSystem" ):
                listener.exitSystem(self)




    def system(self):

        localctx = MyParser.SystemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_system)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 46
                self.import_stmt()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==13:
                self.state = 52
                self.entity()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(MyParser.IMPORT, 0)

        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def SEMI(self):
            return self.getToken(MyParser.SEMI, 0)

        def getRuleIndex(self):
            return MyParser.RULE_import_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stmt" ):
                listener.enterImport_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stmt" ):
                listener.exitImport_stmt(self)




    def import_stmt(self):

        localctx = MyParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_import_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MyParser.IMPORT)
            self.state = 59
            self.match(MyParser.ID)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 60
                self.match(MyParser.SEMI)


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
            return self.getTypedRuleContext(MyParser.AgentContext,0)


        def environment(self):
            return self.getTypedRuleContext(MyParser.EnvironmentContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = MyParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entity)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.agent()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
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
            return self.getToken(MyParser.AGENT, 0)

        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def agent_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.Agent_sectionContext)
            else:
                return self.getTypedRuleContext(MyParser.Agent_sectionContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_agent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent" ):
                listener.enterAgent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent" ):
                listener.exitAgent(self)




    def agent(self):

        localctx = MyParser.AgentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_agent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MyParser.AGENT)
            self.state = 68
            self.match(MyParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 69
                self.agent_section()
                self.state = 74
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
            return self.getTypedRuleContext(MyParser.BeliefsContext,0)


        def desires(self):
            return self.getTypedRuleContext(MyParser.DesiresContext,0)


        def agent_plans(self):
            return self.getTypedRuleContext(MyParser.Agent_plansContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_agent_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_section" ):
                listener.enterAgent_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_section" ):
                listener.exitAgent_section(self)




    def agent_section(self):

        localctx = MyParser.Agent_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_agent_section)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.beliefs()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.desires()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
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
            return self.getToken(MyParser.BELIEFS, 0)

        def id_list(self):
            return self.getTypedRuleContext(MyParser.Id_listContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_beliefs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeliefs" ):
                listener.enterBeliefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeliefs" ):
                listener.exitBeliefs(self)




    def beliefs(self):

        localctx = MyParser.BeliefsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_beliefs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MyParser.BELIEFS)
            self.state = 81
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
            return self.getToken(MyParser.DESIRES, 0)

        def id_list(self):
            return self.getTypedRuleContext(MyParser.Id_listContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_desires

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesires" ):
                listener.enterDesires(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesires" ):
                listener.exitDesires(self)




    def desires(self):

        localctx = MyParser.DesiresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_desires)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MyParser.DESIRES)
            self.state = 84
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
            return self.getToken(MyParser.PLANS, 0)

        def agent_plan(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.Agent_planContext)
            else:
                return self.getTypedRuleContext(MyParser.Agent_planContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_agent_plans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_plans" ):
                listener.enterAgent_plans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_plans" ):
                listener.exitAgent_plans(self)




    def agent_plans(self):

        localctx = MyParser.Agent_plansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_agent_plans)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(MyParser.PLANS)

            self.state = 87
            self.agent_plan()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 88
                self.match(MyParser.COMMA)
                self.state = 89
                self.agent_plan()
                self.state = 94
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
            return self.getToken(MyParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MyParser.LPAREN, 0)

        def WHEN(self):
            return self.getToken(MyParser.WHEN, 0)

        def action(self):
            return self.getTypedRuleContext(MyParser.ActionContext,0)


        def RPAREN(self):
            return self.getToken(MyParser.RPAREN, 0)

        def DO(self):
            return self.getToken(MyParser.DO, 0)

        def action_list(self):
            return self.getTypedRuleContext(MyParser.Action_listContext,0)


        def END(self):
            return self.getToken(MyParser.END, 0)

        def CONTAINS(self):
            return self.getToken(MyParser.CONTAINS, 0)

        def condition_list(self):
            return self.getTypedRuleContext(MyParser.Condition_listContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_agent_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_plan" ):
                listener.enterAgent_plan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_plan" ):
                listener.exitAgent_plan(self)




    def agent_plan(self):

        localctx = MyParser.Agent_planContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_agent_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(MyParser.ID)
            self.state = 96
            self.match(MyParser.LPAREN)
            self.state = 97
            self.match(MyParser.WHEN)
            self.state = 98
            self.action()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 99
                self.match(MyParser.CONTAINS)
                self.state = 100
                self.condition_list()


            self.state = 103
            self.match(MyParser.RPAREN)
            self.state = 104
            self.match(MyParser.DO)
            self.state = 105
            self.action_list()
            self.state = 106
            self.match(MyParser.END)
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
                return self.getTypedRuleContexts(MyParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MyParser.ConditionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_condition_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_list" ):
                listener.enterCondition_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_list" ):
                listener.exitCondition_list(self)




    def condition_list(self):

        localctx = MyParser.Condition_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.condition()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 109
                self.match(MyParser.COMMA)
                self.state = 110
                self.condition()
                self.state = 115
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
            return self.getTypedRuleContext(MyParser.Agent_action_typeContext,0)


        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def getRuleIndex(self):
            return MyParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MyParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.agent_action_type()
            self.state = 117
            self.match(MyParser.ID)
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
            return self.getTypedRuleContext(MyParser.Agent_action_typeContext,0)


        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def getRuleIndex(self):
            return MyParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = MyParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.agent_action_type()
            self.state = 120
            self.match(MyParser.ID)
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
                return self.getTypedRuleContexts(MyParser.ActionContext)
            else:
                return self.getTypedRuleContext(MyParser.ActionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_action_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction_list" ):
                listener.enterAction_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction_list" ):
                listener.exitAction_list(self)




    def action_list(self):

        localctx = MyParser.Action_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_action_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.action()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 123
                self.match(MyParser.COMMA)
                self.state = 124
                self.action()
                self.state = 129
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
            return self.getToken(MyParser.BELIEVE, 0)

        def DISBELIEVE(self):
            return self.getToken(MyParser.DISBELIEVE, 0)

        def ACHIEVE(self):
            return self.getToken(MyParser.ACHIEVE, 0)

        def ABANDON(self):
            return self.getToken(MyParser.ABANDON, 0)

        def getRuleIndex(self):
            return MyParser.RULE_agent_action_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgent_action_type" ):
                listener.enterAgent_action_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgent_action_type" ):
                listener.exitAgent_action_type(self)




    def agent_action_type(self):

        localctx = MyParser.Agent_action_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_agent_action_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
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
            return self.getToken(MyParser.ENVIRONMENT, 0)

        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def environment_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.Environment_sectionContext)
            else:
                return self.getTypedRuleContext(MyParser.Environment_sectionContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_environment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironment" ):
                listener.enterEnvironment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironment" ):
                listener.exitEnvironment(self)




    def environment(self):

        localctx = MyParser.EnvironmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_environment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(MyParser.ENVIRONMENT)
            self.state = 133
            self.match(MyParser.ID)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 134
                self.environment_section()
                self.state = 139
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
            return self.getTypedRuleContext(MyParser.PerceptionsContext,0)


        def environment_plans(self):
            return self.getTypedRuleContext(MyParser.Environment_plansContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_environment_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironment_section" ):
                listener.enterEnvironment_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironment_section" ):
                listener.exitEnvironment_section(self)




    def environment_section(self):

        localctx = MyParser.Environment_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_environment_section)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.perceptions()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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
            return self.getToken(MyParser.PERCEPTIONS, 0)

        def id_list(self):
            return self.getTypedRuleContext(MyParser.Id_listContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_perceptions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPerceptions" ):
                listener.enterPerceptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPerceptions" ):
                listener.exitPerceptions(self)




    def perceptions(self):

        localctx = MyParser.PerceptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_perceptions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(MyParser.PERCEPTIONS)
            self.state = 145
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
            return self.getToken(MyParser.ACTIONS, 0)

        def env_plan(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.Env_planContext)
            else:
                return self.getTypedRuleContext(MyParser.Env_planContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_environment_plans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironment_plans" ):
                listener.enterEnvironment_plans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironment_plans" ):
                listener.exitEnvironment_plans(self)




    def environment_plans(self):

        localctx = MyParser.Environment_plansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_environment_plans)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MyParser.ACTIONS)

            self.state = 148
            self.env_plan()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 149
                self.match(MyParser.COMMA)
                self.state = 150
                self.env_plan()
                self.state = 155
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
            return self.getToken(MyParser.ID, 0)

        def DO(self):
            return self.getToken(MyParser.DO, 0)

        def env_action_list(self):
            return self.getTypedRuleContext(MyParser.Env_action_listContext,0)


        def END(self):
            return self.getToken(MyParser.END, 0)

        def getRuleIndex(self):
            return MyParser.RULE_env_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_plan" ):
                listener.enterEnv_plan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_plan" ):
                listener.exitEnv_plan(self)




    def env_plan(self):

        localctx = MyParser.Env_planContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_env_plan)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MyParser.ID)
            self.state = 157
            self.match(MyParser.DO)
            self.state = 158
            self.env_action_list()
            self.state = 159
            self.match(MyParser.END)
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
                return self.getTypedRuleContexts(MyParser.Env_actionContext)
            else:
                return self.getTypedRuleContext(MyParser.Env_actionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_env_action_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_action_list" ):
                listener.enterEnv_action_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_action_list" ):
                listener.exitEnv_action_list(self)




    def env_action_list(self):

        localctx = MyParser.Env_action_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_env_action_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.env_action()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 162
                self.match(MyParser.COMMA)
                self.state = 163
                self.env_action()
                self.state = 168
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
            return self.getTypedRuleContext(MyParser.Env_action_typeContext,0)


        def ID(self):
            return self.getToken(MyParser.ID, 0)

        def getRuleIndex(self):
            return MyParser.RULE_env_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_action" ):
                listener.enterEnv_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_action" ):
                listener.exitEnv_action(self)




    def env_action(self):

        localctx = MyParser.Env_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_env_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.env_action_type()
            self.state = 170
            self.match(MyParser.ID)
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
            return self.getToken(MyParser.PERCEPT, 0)

        def CHANGE(self):
            return self.getToken(MyParser.CHANGE, 0)

        def getRuleIndex(self):
            return MyParser.RULE_env_action_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnv_action_type" ):
                listener.enterEnv_action_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnv_action_type" ):
                listener.exitEnv_action_type(self)




    def env_action_type(self):

        localctx = MyParser.Env_action_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_env_action_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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
                return self.getTokens(MyParser.ID)
            else:
                return self.getToken(MyParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.COMMA)
            else:
                return self.getToken(MyParser.COMMA, i)

        def getRuleIndex(self):
            return MyParser.RULE_id_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_list" ):
                listener.enterId_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_list" ):
                listener.exitId_list(self)




    def id_list(self):

        localctx = MyParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MyParser.ID)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 175
                self.match(MyParser.COMMA)
                self.state = 176
                self.match(MyParser.ID)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





