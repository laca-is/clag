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
        4,1,21,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        4,0,29,8,0,11,0,12,0,30,1,1,1,1,1,1,4,1,36,8,1,11,1,12,1,37,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,52,8,2,11,2,12,2,
        53,3,2,56,8,2,1,3,1,3,1,3,4,3,61,8,3,11,3,12,3,62,1,4,1,4,1,4,1,
        4,1,4,4,4,70,8,4,11,4,12,4,71,3,4,74,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,6,1,6,1,6,5,6,86,8,6,10,6,12,6,89,9,6,1,7,1,7,1,7,1,8,1,8,
        1,8,5,8,97,8,8,10,8,12,8,100,9,8,1,9,1,9,1,9,5,9,105,8,9,10,9,12,
        9,108,9,9,1,10,1,10,3,10,112,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,120,8,11,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,
        20,22,24,0,1,2,0,4,4,13,16,126,0,28,1,0,0,0,2,32,1,0,0,0,4,55,1,
        0,0,0,6,57,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,82,1,0,0,0,14,90,
        1,0,0,0,16,93,1,0,0,0,18,101,1,0,0,0,20,111,1,0,0,0,22,113,1,0,0,
        0,24,121,1,0,0,0,26,29,3,2,1,0,27,29,3,6,3,0,28,26,1,0,0,0,28,27,
        1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,1,1,0,0,0,32,
        33,5,1,0,0,33,35,5,20,0,0,34,36,3,4,2,0,35,34,1,0,0,0,36,37,1,0,
        0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,40,5,3,0,0,40,41,
        5,4,0,0,41,56,3,12,6,0,42,43,5,3,0,0,43,44,5,5,0,0,44,45,5,11,0,
        0,45,56,3,12,6,0,46,47,5,12,0,0,47,48,5,2,0,0,48,56,5,20,0,0,49,
        51,5,9,0,0,50,52,3,10,5,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,
        0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,39,1,0,0,0,55,42,1,0,0,0,55,46,
        1,0,0,0,55,49,1,0,0,0,56,5,1,0,0,0,57,58,5,2,0,0,58,60,5,20,0,0,
        59,61,3,8,4,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,
        0,0,0,63,7,1,0,0,0,64,65,5,3,0,0,65,66,5,6,0,0,66,74,3,12,6,0,67,
        69,5,9,0,0,68,70,3,20,10,0,69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,
        0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,64,1,0,0,0,73,67,1,0,0,0,74,9,
        1,0,0,0,75,76,5,20,0,0,76,77,5,7,0,0,77,78,3,16,8,0,78,79,5,8,0,
        0,79,80,3,18,9,0,80,81,5,19,0,0,81,11,1,0,0,0,82,87,5,20,0,0,83,
        84,5,18,0,0,84,86,5,20,0,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,
        0,0,87,88,1,0,0,0,88,13,1,0,0,0,89,87,1,0,0,0,90,91,3,24,12,0,91,
        92,5,20,0,0,92,15,1,0,0,0,93,98,3,14,7,0,94,95,5,18,0,0,95,97,3,
        14,7,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,
        99,17,1,0,0,0,100,98,1,0,0,0,101,106,3,20,10,0,102,103,5,18,0,0,
        103,105,3,20,10,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,
        0,106,107,1,0,0,0,107,19,1,0,0,0,108,106,1,0,0,0,109,112,3,24,12,
        0,110,112,3,22,11,0,111,109,1,0,0,0,111,110,1,0,0,0,112,21,1,0,0,
        0,113,114,5,17,0,0,114,115,5,20,0,0,115,116,3,24,12,0,116,119,5,
        20,0,0,117,118,5,10,0,0,118,120,5,20,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,23,1,0,0,0,121,122,7,0,0,0,122,123,5,20,0,0,123,25,1,
        0,0,0,13,28,30,37,53,55,62,71,73,87,98,106,111,119
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
                     "<INVALID>", "<INVALID>", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "ENVIRONMENT", "THAT", "BELIEVES", 
                      "DESIRES", "PERCEIVES", "WHEN", "THEN", "WITH", "VIA", 
                      "TO", "IN", "ACHIEVE", "ABANDON", "PERCEPT", "CHANGE", 
                      "SEND", "COMMA", "DOT", "ID", "WS" ]

    RULE_system = 0
    RULE_agentDef = 1
    RULE_agentSection = 2
    RULE_environmentDef = 3
    RULE_environmentSection = 4
    RULE_plan = 5
    RULE_idList = 6
    RULE_condition = 7
    RULE_conditionList = 8
    RULE_actionList = 9
    RULE_action = 10
    RULE_sendAction = 11
    RULE_actionType = 12

    ruleNames =  [ "system", "agentDef", "agentSection", "environmentDef", 
                   "environmentSection", "plan", "idList", "condition", 
                   "conditionList", "actionList", "action", "sendAction", 
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
    ACHIEVE=13
    ABANDON=14
    PERCEPT=15
    CHANGE=16
    SEND=17
    COMMA=18
    DOT=19
    ID=20
    WS=21

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4616) != 0)):
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

        def THAT(self):
            return self.getToken(ClagParser.THAT, 0)

        def BELIEVES(self):
            return self.getToken(ClagParser.BELIEVES, 0)

        def idList(self):
            return self.getTypedRuleContext(ClagParser.IdListContext,0)


        def DESIRES(self):
            return self.getToken(ClagParser.DESIRES, 0)

        def TO(self):
            return self.getToken(ClagParser.TO, 0)

        def IN(self):
            return self.getToken(ClagParser.IN, 0)

        def ENVIRONMENT(self):
            return self.getToken(ClagParser.ENVIRONMENT, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def WITH(self):
            return self.getToken(ClagParser.WITH, 0)

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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ClagParser.THAT)
                self.state = 40
                self.match(ClagParser.BELIEVES)
                self.state = 41
                self.idList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(ClagParser.THAT)
                self.state = 43
                self.match(ClagParser.DESIRES)
                self.state = 44
                self.match(ClagParser.TO)
                self.state = 45
                self.idList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(ClagParser.IN)
                self.state = 47
                self.match(ClagParser.ENVIRONMENT)
                self.state = 48
                self.match(ClagParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.match(ClagParser.WITH)
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    self.plan()
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==20):
                        break

                pass


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
            self.state = 57
            self.match(ClagParser.ENVIRONMENT)
            self.state = 58
            self.match(ClagParser.ID)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.environmentSection()
                self.state = 62 
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
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(ClagParser.THAT)
                self.state = 65
                self.match(ClagParser.PERCEIVES)
                self.state = 66
                self.idList()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(ClagParser.WITH)
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 68
                    self.action()
                    self.state = 71 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 253968) != 0)):
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ClagParser.ID)
            self.state = 76
            self.match(ClagParser.WHEN)
            self.state = 77
            self.conditionList()
            self.state = 78
            self.match(ClagParser.THEN)
            self.state = 79
            self.actionList()
            self.state = 80
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
            self.state = 82
            self.match(ClagParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 83
                self.match(ClagParser.COMMA)
                self.state = 84
                self.match(ClagParser.ID)
                self.state = 89
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

        def actionType(self):
            return self.getTypedRuleContext(ClagParser.ActionTypeContext,0)


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
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.actionType()
            self.state = 91
            self.match(ClagParser.ID)
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
            self.state = 93
            self.condition()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
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
            self.state = 101
            self.action()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 102
                self.match(ClagParser.COMMA)
                self.state = 103
                self.action()
                self.state = 108
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
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.actionType()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
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
            self.state = 113
            self.match(ClagParser.SEND)
            self.state = 114
            self.match(ClagParser.ID)
            self.state = 115
            self.actionType()
            self.state = 116
            self.match(ClagParser.ID)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 117
                self.match(ClagParser.VIA)
                self.state = 118
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 122
            self.match(ClagParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





