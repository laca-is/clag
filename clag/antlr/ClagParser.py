# Generated from clag/antlr/ClagParser.g4 by ANTLR 4.13.2
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
        4,1,25,149,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        4,0,29,8,0,11,0,12,0,30,1,1,1,1,1,1,4,1,36,8,1,11,1,12,1,37,1,2,
        1,2,1,2,1,2,3,2,44,8,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,4,2,60,8,2,11,2,12,2,61,3,2,64,8,2,1,3,1,3,1,3,
        4,3,69,8,3,11,3,12,3,70,1,4,1,4,1,4,1,4,1,4,4,4,78,8,4,11,4,12,4,
        79,3,4,82,8,4,1,5,1,5,1,5,1,5,1,5,3,5,89,8,5,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,5,6,98,8,6,10,6,12,6,101,9,6,1,7,1,7,1,7,5,7,106,8,7,10,
        7,12,7,109,9,7,1,8,1,8,1,8,5,8,114,8,8,10,8,12,8,117,9,8,1,9,1,9,
        1,9,5,9,122,8,9,10,9,12,9,125,9,9,1,10,1,10,3,10,129,8,10,1,11,1,
        11,1,11,1,11,1,11,3,11,136,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,145,8,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,
        20,22,24,0,0,160,0,28,1,0,0,0,2,32,1,0,0,0,4,63,1,0,0,0,6,65,1,0,
        0,0,8,81,1,0,0,0,10,83,1,0,0,0,12,94,1,0,0,0,14,102,1,0,0,0,16,110,
        1,0,0,0,18,118,1,0,0,0,20,128,1,0,0,0,22,130,1,0,0,0,24,144,1,0,
        0,0,26,29,3,2,1,0,27,29,3,6,3,0,28,26,1,0,0,0,28,27,1,0,0,0,29,30,
        1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,1,1,0,0,0,32,33,5,1,0,0,33,
        35,5,24,0,0,34,36,3,4,2,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,
        0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,40,5,5,0,0,40,41,5,11,0,0,41,43,
        3,12,6,0,42,44,5,23,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,64,1,0,0,
        0,45,46,5,4,0,0,46,48,3,12,6,0,47,49,5,23,0,0,48,47,1,0,0,0,48,49,
        1,0,0,0,49,64,1,0,0,0,50,51,5,12,0,0,51,52,5,2,0,0,52,64,5,24,0,
        0,53,54,5,13,0,0,54,55,5,14,0,0,55,64,5,24,0,0,56,57,5,9,0,0,57,
        59,5,15,0,0,58,60,3,10,5,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,
        0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,39,1,0,0,0,63,45,1,0,0,0,63,50,
        1,0,0,0,63,53,1,0,0,0,63,56,1,0,0,0,64,5,1,0,0,0,65,66,5,2,0,0,66,
        68,5,24,0,0,67,69,3,8,4,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,
        0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,73,5,3,0,0,73,74,5,6,0,0,74,82,
        3,12,6,0,75,77,5,9,0,0,76,78,3,20,10,0,77,76,1,0,0,0,78,79,1,0,0,
        0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,72,1,0,0,0,81,75,
        1,0,0,0,82,9,1,0,0,0,83,84,5,24,0,0,84,85,5,7,0,0,85,88,3,14,7,0,
        86,87,5,9,0,0,87,89,3,16,8,0,88,86,1,0,0,0,88,89,1,0,0,0,89,90,1,
        0,0,0,90,91,5,8,0,0,91,92,3,18,9,0,92,93,5,22,0,0,93,11,1,0,0,0,
        94,99,5,24,0,0,95,96,5,21,0,0,96,98,5,24,0,0,97,95,1,0,0,0,98,101,
        1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,13,1,0,0,0,101,99,1,0,0,
        0,102,107,3,24,12,0,103,104,5,21,0,0,104,106,3,24,12,0,105,103,1,
        0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,15,1,0,
        0,0,109,107,1,0,0,0,110,115,3,24,12,0,111,112,5,21,0,0,112,114,3,
        24,12,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,
        1,0,0,0,116,17,1,0,0,0,117,115,1,0,0,0,118,123,3,20,10,0,119,120,
        5,21,0,0,120,122,3,20,10,0,121,119,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,19,1,0,0,0,125,123,1,0,0,0,126,129,3,
        24,12,0,127,129,3,22,11,0,128,126,1,0,0,0,128,127,1,0,0,0,129,21,
        1,0,0,0,130,131,5,20,0,0,131,132,5,24,0,0,132,135,3,24,12,0,133,
        134,5,10,0,0,134,136,5,24,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,
        23,1,0,0,0,137,145,5,16,0,0,138,145,5,17,0,0,139,145,5,4,0,0,140,
        145,5,18,0,0,141,145,5,19,0,0,142,143,5,5,0,0,143,145,5,11,0,0,144,
        137,1,0,0,0,144,138,1,0,0,0,144,139,1,0,0,0,144,140,1,0,0,0,144,
        141,1,0,0,0,144,142,1,0,0,0,145,146,1,0,0,0,146,147,5,24,0,0,147,
        25,1,0,0,0,18,28,30,37,43,48,61,63,70,79,81,88,99,107,115,123,128,
        135,144
    ]

class ClagParser ( Parser ):

    grammarFileName = "ClagParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "ENVIRONMENT", "THAT", "BELIEVES", 
                      "DESIRES", "PERCEIVES", "WHEN", "THEN", "WITH", "VIA", 
                      "TO", "IN", "USING", "CHANNEL", "PLANS", "ACHIEVE", 
                      "ABANDON", "PERCEPT", "CHANGE", "SEND", "COMMA", "DOT", 
                      "AND", "ID", "WS" ]

    RULE_system = 0
    RULE_agentDef = 1
    RULE_agentSection = 2
    RULE_environmentDef = 3
    RULE_environmentSection = 4
    RULE_plan = 5
    RULE_idList = 6
    RULE_conditionList = 7
    RULE_contextList = 8
    RULE_actionList = 9
    RULE_action = 10
    RULE_sendAction = 11
    RULE_actionType = 12

    ruleNames =  [ "system", "agentDef", "agentSection", "environmentDef", 
                   "environmentSection", "plan", "idList", "conditionList", 
                   "contextList", "actionList", "action", "sendAction", 
                   "actionType" ]

    EOF = Token.EOF
    AGENT=1
    ENVIRONMENT=2
    THAT=3
    BELIEVES=4
    DESIRES=5
    PERCEIVES=6
    WHEN=7
    THEN=8
    WITH=9
    VIA=10
    TO=11
    IN=12
    USING=13
    CHANNEL=14
    PLANS=15
    ACHIEVE=16
    ABANDON=17
    PERCEPT=18
    CHANGE=19
    SEND=20
    COMMA=21
    DOT=22
    AND=23
    ID=24
    WS=25

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

        def agentDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.AgentDefContext)
            else:
                return self.getTypedRuleContext(ClagParser.AgentDefContext,i)


        def environmentDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.EnvironmentDefContext)
            else:
                return self.getTypedRuleContext(ClagParser.EnvironmentDefContext,i)


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
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 26
                    self.agentDef()
                    pass
                elif token in [2]:
                    self.state = 27
                    self.environmentDef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGENT(self):
            return self.getToken(ClagParser.AGENT, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def agentSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.AgentSectionContext)
            else:
                return self.getTypedRuleContext(ClagParser.AgentSectionContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_agentDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentDef" ):
                listener.enterAgentDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentDef" ):
                listener.exitAgentDef(self)




    def agentDef(self):

        localctx = ClagParser.AgentDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_agentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ClagParser.AGENT)
            self.state = 33
            self.match(ClagParser.ID)
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.agentSection()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12848) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgentSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESIRES(self):
            return self.getToken(ClagParser.DESIRES, 0)

        def TO(self):
            return self.getToken(ClagParser.TO, 0)

        def idList(self):
            return self.getTypedRuleContext(ClagParser.IdListContext,0)


        def AND(self):
            return self.getToken(ClagParser.AND, 0)

        def BELIEVES(self):
            return self.getToken(ClagParser.BELIEVES, 0)

        def IN(self):
            return self.getToken(ClagParser.IN, 0)

        def ENVIRONMENT(self):
            return self.getToken(ClagParser.ENVIRONMENT, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def USING(self):
            return self.getToken(ClagParser.USING, 0)

        def CHANNEL(self):
            return self.getToken(ClagParser.CHANNEL, 0)

        def WITH(self):
            return self.getToken(ClagParser.WITH, 0)

        def PLANS(self):
            return self.getToken(ClagParser.PLANS, 0)

        def plan(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.PlanContext)
            else:
                return self.getTypedRuleContext(ClagParser.PlanContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_agentSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentSection" ):
                listener.enterAgentSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentSection" ):
                listener.exitAgentSection(self)




    def agentSection(self):

        localctx = ClagParser.AgentSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_agentSection)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ClagParser.DESIRES)
                self.state = 40
                self.match(ClagParser.TO)
                self.state = 41
                self.idList()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 42
                    self.match(ClagParser.AND)


                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(ClagParser.BELIEVES)
                self.state = 46
                self.idList()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 47
                    self.match(ClagParser.AND)


                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(ClagParser.IN)
                self.state = 51
                self.match(ClagParser.ENVIRONMENT)
                self.state = 52
                self.match(ClagParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.match(ClagParser.USING)
                self.state = 54
                self.match(ClagParser.CHANNEL)
                self.state = 55
                self.match(ClagParser.ID)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.match(ClagParser.WITH)
                self.state = 57
                self.match(ClagParser.PLANS)
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 58
                    self.plan()
                    self.state = 61 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==24):
                        break

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


    class EnvironmentDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENVIRONMENT(self):
            return self.getToken(ClagParser.ENVIRONMENT, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def environmentSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.EnvironmentSectionContext)
            else:
                return self.getTypedRuleContext(ClagParser.EnvironmentSectionContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_environmentDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironmentDef" ):
                listener.enterEnvironmentDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironmentDef" ):
                listener.exitEnvironmentDef(self)




    def environmentDef(self):

        localctx = ClagParser.EnvironmentDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_environmentDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ClagParser.ENVIRONMENT)
            self.state = 66
            self.match(ClagParser.ID)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.environmentSection()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnvironmentSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THAT(self):
            return self.getToken(ClagParser.THAT, 0)

        def PERCEIVES(self):
            return self.getToken(ClagParser.PERCEIVES, 0)

        def idList(self):
            return self.getTypedRuleContext(ClagParser.IdListContext,0)


        def WITH(self):
            return self.getToken(ClagParser.WITH, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ActionContext)
            else:
                return self.getTypedRuleContext(ClagParser.ActionContext,i)


        def getRuleIndex(self):
            return ClagParser.RULE_environmentSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvironmentSection" ):
                listener.enterEnvironmentSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvironmentSection" ):
                listener.exitEnvironmentSection(self)




    def environmentSection(self):

        localctx = ClagParser.EnvironmentSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_environmentSection)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(ClagParser.THAT)
                self.state = 73
                self.match(ClagParser.PERCEIVES)
                self.state = 74
                self.idList()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(ClagParser.WITH)
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 76
                    self.action()
                    self.state = 79 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2031664) != 0)):
                        break

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


    class PlanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def WHEN(self):
            return self.getToken(ClagParser.WHEN, 0)

        def conditionList(self):
            return self.getTypedRuleContext(ClagParser.ConditionListContext,0)


        def THEN(self):
            return self.getToken(ClagParser.THEN, 0)

        def actionList(self):
            return self.getTypedRuleContext(ClagParser.ActionListContext,0)


        def DOT(self):
            return self.getToken(ClagParser.DOT, 0)

        def WITH(self):
            return self.getToken(ClagParser.WITH, 0)

        def contextList(self):
            return self.getTypedRuleContext(ClagParser.ContextListContext,0)


        def getRuleIndex(self):
            return ClagParser.RULE_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan" ):
                listener.enterPlan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan" ):
                listener.exitPlan(self)




    def plan(self):

        localctx = ClagParser.PlanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ClagParser.ID)
            self.state = 84
            self.match(ClagParser.WHEN)
            self.state = 85
            self.conditionList()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 86
                self.match(ClagParser.WITH)
                self.state = 87
                self.contextList()


            self.state = 90
            self.match(ClagParser.THEN)
            self.state = 91
            self.actionList()
            self.state = 92
            self.match(ClagParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
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
            return ClagParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)




    def idList(self):

        localctx = ClagParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ClagParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 95
                self.match(ClagParser.COMMA)
                self.state = 96
                self.match(ClagParser.ID)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ActionTypeContext)
            else:
                return self.getTypedRuleContext(ClagParser.ActionTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_conditionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionList" ):
                listener.enterConditionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionList" ):
                listener.exitConditionList(self)




    def conditionList(self):

        localctx = ClagParser.ConditionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.actionType()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 103
                self.match(ClagParser.COMMA)
                self.state = 104
                self.actionType()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ActionTypeContext)
            else:
                return self.getTypedRuleContext(ClagParser.ActionTypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.COMMA)
            else:
                return self.getToken(ClagParser.COMMA, i)

        def getRuleIndex(self):
            return ClagParser.RULE_contextList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContextList" ):
                listener.enterContextList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContextList" ):
                listener.exitContextList(self)




    def contextList(self):

        localctx = ClagParser.ContextListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_contextList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.actionType()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 111
                self.match(ClagParser.COMMA)
                self.state = 112
                self.actionType()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionListContext(ParserRuleContext):
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
            return ClagParser.RULE_actionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionList" ):
                listener.enterActionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionList" ):
                listener.exitActionList(self)




    def actionList(self):

        localctx = ClagParser.ActionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_actionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.action()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 119
                self.match(ClagParser.COMMA)
                self.state = 120
                self.action()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def actionType(self):
            return self.getTypedRuleContext(ClagParser.ActionTypeContext,0)


        def sendAction(self):
            return self.getTypedRuleContext(ClagParser.SendActionContext,0)


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
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.actionType()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.sendAction()
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


    class SendActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEND(self):
            return self.getToken(ClagParser.SEND, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ClagParser.ID)
            else:
                return self.getToken(ClagParser.ID, i)

        def actionType(self):
            return self.getTypedRuleContext(ClagParser.ActionTypeContext,0)


        def VIA(self):
            return self.getToken(ClagParser.VIA, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_sendAction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSendAction" ):
                listener.enterSendAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSendAction" ):
                listener.exitSendAction(self)




    def sendAction(self):

        localctx = ClagParser.SendActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sendAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ClagParser.SEND)
            self.state = 131
            self.match(ClagParser.ID)
            self.state = 132
            self.actionType()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 133
                self.match(ClagParser.VIA)
                self.state = 134
                self.match(ClagParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def ACHIEVE(self):
            return self.getToken(ClagParser.ACHIEVE, 0)

        def ABANDON(self):
            return self.getToken(ClagParser.ABANDON, 0)

        def BELIEVES(self):
            return self.getToken(ClagParser.BELIEVES, 0)

        def PERCEPT(self):
            return self.getToken(ClagParser.PERCEPT, 0)

        def CHANGE(self):
            return self.getToken(ClagParser.CHANGE, 0)

        def DESIRES(self):
            return self.getToken(ClagParser.DESIRES, 0)

        def TO(self):
            return self.getToken(ClagParser.TO, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_actionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionType" ):
                listener.enterActionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionType" ):
                listener.exitActionType(self)




    def actionType(self):

        localctx = ClagParser.ActionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_actionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 137
                self.match(ClagParser.ACHIEVE)
                pass
            elif token in [17]:
                self.state = 138
                self.match(ClagParser.ABANDON)
                pass
            elif token in [4]:
                self.state = 139
                self.match(ClagParser.BELIEVES)
                pass
            elif token in [18]:
                self.state = 140
                self.match(ClagParser.PERCEPT)
                pass
            elif token in [19]:
                self.state = 141
                self.match(ClagParser.CHANGE)
                pass
            elif token in [5]:
                self.state = 142
                self.match(ClagParser.DESIRES)
                self.state = 143
                self.match(ClagParser.TO)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 146
            self.match(ClagParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





