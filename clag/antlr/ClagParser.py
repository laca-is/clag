# Generated from ./clag/antlr/ClagParser.g4 by ANTLR 4.13.2
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
        4,1,28,155,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,4,0,31,8,0,11,0,12,0,32,1,1,1,1,1,1,4,1,38,8,1,11,1,12,1,
        39,1,2,1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,1,2,3,2,51,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,4,2,62,8,2,11,2,12,2,63,3,2,66,8,2,1,3,1,
        3,1,3,4,3,71,8,3,11,3,12,3,72,1,4,1,4,1,4,1,4,1,4,1,4,4,4,81,8,4,
        11,4,12,4,82,3,4,85,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,95,8,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,1,8,
        1,8,1,8,5,8,112,8,8,10,8,12,8,115,9,8,1,9,1,9,1,9,5,9,120,8,9,10,
        9,12,9,123,9,9,1,10,1,10,1,10,5,10,128,8,10,10,10,12,10,131,9,10,
        1,11,1,11,3,11,135,8,11,1,12,1,12,1,12,1,12,1,12,3,12,142,8,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,151,8,13,1,13,1,13,1,13,0,
        0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,0,165,0,30,1,0,0,0,2,
        34,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,84,1,0,0,0,10,86,1,0,0,0,
        12,89,1,0,0,0,14,100,1,0,0,0,16,108,1,0,0,0,18,116,1,0,0,0,20,124,
        1,0,0,0,22,134,1,0,0,0,24,136,1,0,0,0,26,150,1,0,0,0,28,31,3,2,1,
        0,29,31,3,6,3,0,30,28,1,0,0,0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,
        1,0,0,0,32,33,1,0,0,0,33,1,1,0,0,0,34,35,5,1,0,0,35,37,5,27,0,0,
        36,38,3,4,2,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,3,1,0,0,0,41,42,5,5,0,0,42,43,5,11,0,0,43,45,3,14,7,0,44,
        46,5,24,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,66,1,0,0,0,47,48,5,4,
        0,0,48,50,3,14,7,0,49,51,5,24,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,
        66,1,0,0,0,52,53,5,12,0,0,53,54,5,2,0,0,54,66,5,27,0,0,55,56,5,13,
        0,0,56,57,5,14,0,0,57,66,5,27,0,0,58,59,5,9,0,0,59,61,5,15,0,0,60,
        62,3,12,6,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,
        0,0,64,66,1,0,0,0,65,41,1,0,0,0,65,47,1,0,0,0,65,52,1,0,0,0,65,55,
        1,0,0,0,65,58,1,0,0,0,66,5,1,0,0,0,67,68,5,2,0,0,68,70,5,27,0,0,
        69,71,3,8,4,0,70,69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,
        0,0,0,73,7,1,0,0,0,74,75,5,3,0,0,75,76,5,6,0,0,76,85,3,14,7,0,77,
        78,5,9,0,0,78,80,5,16,0,0,79,81,3,10,5,0,80,79,1,0,0,0,81,82,1,0,
        0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,74,1,0,0,0,84,77,
        1,0,0,0,85,9,1,0,0,0,86,87,5,27,0,0,87,88,5,23,0,0,88,11,1,0,0,0,
        89,90,5,27,0,0,90,91,5,7,0,0,91,94,3,16,8,0,92,93,5,9,0,0,93,95,
        3,18,9,0,94,92,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,5,8,0,0,
        97,98,3,20,10,0,98,99,5,23,0,0,99,13,1,0,0,0,100,105,5,27,0,0,101,
        102,5,22,0,0,102,104,5,27,0,0,103,101,1,0,0,0,104,107,1,0,0,0,105,
        103,1,0,0,0,105,106,1,0,0,0,106,15,1,0,0,0,107,105,1,0,0,0,108,113,
        3,26,13,0,109,110,5,22,0,0,110,112,3,26,13,0,111,109,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,17,1,0,0,0,115,113,
        1,0,0,0,116,121,3,26,13,0,117,118,5,22,0,0,118,120,3,26,13,0,119,
        117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,
        19,1,0,0,0,123,121,1,0,0,0,124,129,3,22,11,0,125,126,5,22,0,0,126,
        128,3,22,11,0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,
        130,1,0,0,0,130,21,1,0,0,0,131,129,1,0,0,0,132,135,3,26,13,0,133,
        135,3,24,12,0,134,132,1,0,0,0,134,133,1,0,0,0,135,23,1,0,0,0,136,
        137,5,21,0,0,137,138,5,27,0,0,138,141,3,26,13,0,139,140,5,10,0,0,
        140,142,5,27,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,25,1,0,0,0,
        143,151,5,17,0,0,144,151,5,18,0,0,145,151,5,4,0,0,146,151,5,19,0,
        0,147,151,5,20,0,0,148,149,5,5,0,0,149,151,5,11,0,0,150,143,1,0,
        0,0,150,144,1,0,0,0,150,145,1,0,0,0,150,146,1,0,0,0,150,147,1,0,
        0,0,150,148,1,0,0,0,151,152,1,0,0,0,152,153,5,27,0,0,153,27,1,0,
        0,0,18,30,32,39,45,50,63,65,72,82,84,94,105,113,121,129,134,141,
        150
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
                     "<INVALID>", "<INVALID>", "','", "'.'", "<INVALID>", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "ENVIRONMENT", "THAT", "BELIEVES", 
                      "DESIRES", "PERCEIVES", "WHEN", "THEN", "WITH", "VIA", 
                      "TO", "IN", "USING", "CHANNEL", "PLANS", "ACTIONS", 
                      "ACHIEVE", "ABANDON", "PERCEPT", "CHANGE", "SEND", 
                      "COMMA", "DOT", "AND", "LPAREN", "RPAREN", "ID", "WS" ]

    RULE_system = 0
    RULE_agentDef = 1
    RULE_agentSection = 2
    RULE_environmentDef = 3
    RULE_environmentSection = 4
    RULE_actionName = 5
    RULE_plan = 6
    RULE_idList = 7
    RULE_conditionList = 8
    RULE_contextList = 9
    RULE_actionList = 10
    RULE_action = 11
    RULE_sendAction = 12
    RULE_actionType = 13

    ruleNames =  [ "system", "agentDef", "agentSection", "environmentDef", 
                   "environmentSection", "actionName", "plan", "idList", 
                   "conditionList", "contextList", "actionList", "action", 
                   "sendAction", "actionType" ]

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
    ACTIONS=16
    ACHIEVE=17
    ABANDON=18
    PERCEPT=19
    CHANGE=20
    SEND=21
    COMMA=22
    DOT=23
    AND=24
    LPAREN=25
    RPAREN=26
    ID=27
    WS=28

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
            self.state = 30 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 28
                    self.agentDef()
                    pass
                elif token in [2]:
                    self.state = 29
                    self.environmentDef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32 
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
            self.state = 34
            self.match(ClagParser.AGENT)
            self.state = 35
            self.match(ClagParser.ID)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.agentSection()
                self.state = 39 
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
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ClagParser.DESIRES)
                self.state = 42
                self.match(ClagParser.TO)
                self.state = 43
                self.idList()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 44
                    self.match(ClagParser.AND)


                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(ClagParser.BELIEVES)
                self.state = 48
                self.idList()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==24:
                    self.state = 49
                    self.match(ClagParser.AND)


                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(ClagParser.IN)
                self.state = 53
                self.match(ClagParser.ENVIRONMENT)
                self.state = 54
                self.match(ClagParser.ID)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(ClagParser.USING)
                self.state = 56
                self.match(ClagParser.CHANNEL)
                self.state = 57
                self.match(ClagParser.ID)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.match(ClagParser.WITH)
                self.state = 59
                self.match(ClagParser.PLANS)
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 60
                    self.plan()
                    self.state = 63 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==27):
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
            self.state = 67
            self.match(ClagParser.ENVIRONMENT)
            self.state = 68
            self.match(ClagParser.ID)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.environmentSection()
                self.state = 72 
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

        def ACTIONS(self):
            return self.getToken(ClagParser.ACTIONS, 0)

        def actionName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ActionNameContext)
            else:
                return self.getTypedRuleContext(ClagParser.ActionNameContext,i)


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
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(ClagParser.THAT)
                self.state = 75
                self.match(ClagParser.PERCEIVES)
                self.state = 76
                self.idList()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(ClagParser.WITH)
                self.state = 78
                self.match(ClagParser.ACTIONS)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 79
                    self.actionName()
                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==27):
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


    class ActionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def DOT(self):
            return self.getToken(ClagParser.DOT, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_actionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionName" ):
                listener.enterActionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionName" ):
                listener.exitActionName(self)




    def actionName(self):

        localctx = ClagParser.ActionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ClagParser.ID)
            self.state = 87
            self.match(ClagParser.DOT)
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
        self.enterRule(localctx, 12, self.RULE_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ClagParser.ID)
            self.state = 90
            self.match(ClagParser.WHEN)
            self.state = 91
            self.conditionList()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 92
                self.match(ClagParser.WITH)
                self.state = 93
                self.contextList()


            self.state = 96
            self.match(ClagParser.THEN)
            self.state = 97
            self.actionList()
            self.state = 98
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
        self.enterRule(localctx, 14, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ClagParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 101
                self.match(ClagParser.COMMA)
                self.state = 102
                self.match(ClagParser.ID)
                self.state = 107
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
        self.enterRule(localctx, 16, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.actionType()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 109
                self.match(ClagParser.COMMA)
                self.state = 110
                self.actionType()
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
        self.enterRule(localctx, 18, self.RULE_contextList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.actionType()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 117
                self.match(ClagParser.COMMA)
                self.state = 118
                self.actionType()
                self.state = 123
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
        self.enterRule(localctx, 20, self.RULE_actionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.action()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 125
                self.match(ClagParser.COMMA)
                self.state = 126
                self.action()
                self.state = 131
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
        self.enterRule(localctx, 22, self.RULE_action)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.actionType()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
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
        self.enterRule(localctx, 24, self.RULE_sendAction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(ClagParser.SEND)
            self.state = 137
            self.match(ClagParser.ID)
            self.state = 138
            self.actionType()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 139
                self.match(ClagParser.VIA)
                self.state = 140
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
        self.enterRule(localctx, 26, self.RULE_actionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 143
                self.match(ClagParser.ACHIEVE)
                pass
            elif token in [18]:
                self.state = 144
                self.match(ClagParser.ABANDON)
                pass
            elif token in [4]:
                self.state = 145
                self.match(ClagParser.BELIEVES)
                pass
            elif token in [19]:
                self.state = 146
                self.match(ClagParser.PERCEPT)
                pass
            elif token in [20]:
                self.state = 147
                self.match(ClagParser.CHANGE)
                pass
            elif token in [5]:
                self.state = 148
                self.match(ClagParser.DESIRES)
                self.state = 149
                self.match(ClagParser.TO)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 152
            self.match(ClagParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





