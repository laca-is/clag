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
        4,1,34,144,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,4,0,31,8,0,11,0,12,0,32,1,1,1,1,1,1,4,1,38,8,1,11,1,12,1,
        39,1,2,1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,1,2,1,2,1,2,3,2,53,8,2,1,2,
        1,2,1,2,4,2,58,8,2,11,2,12,2,59,1,2,1,2,1,2,3,2,65,8,2,1,3,1,3,1,
        3,4,3,70,8,3,11,3,12,3,71,1,4,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,1,4,
        4,4,83,8,4,11,4,12,4,84,3,4,87,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,1,8,
        1,8,1,8,1,9,1,9,1,9,5,9,115,8,9,10,9,12,9,118,9,9,1,10,1,10,1,10,
        5,10,123,8,10,10,10,12,10,126,9,10,1,11,1,11,1,11,1,11,3,11,132,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,140,8,12,1,13,1,13,1,13,
        0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,1,2,0,4,4,19,23,147,
        0,30,1,0,0,0,2,34,1,0,0,0,4,64,1,0,0,0,6,66,1,0,0,0,8,86,1,0,0,0,
        10,88,1,0,0,0,12,95,1,0,0,0,14,100,1,0,0,0,16,108,1,0,0,0,18,111,
        1,0,0,0,20,119,1,0,0,0,22,131,1,0,0,0,24,133,1,0,0,0,26,141,1,0,
        0,0,28,31,3,2,1,0,29,31,3,6,3,0,30,28,1,0,0,0,30,29,1,0,0,0,31,32,
        1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,1,1,0,0,0,34,35,5,1,0,0,35,
        37,5,33,0,0,36,38,3,4,2,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,
        0,0,39,40,1,0,0,0,40,3,1,0,0,0,41,42,5,3,0,0,42,43,5,4,0,0,43,45,
        3,14,7,0,44,46,5,13,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,65,1,0,0,
        0,47,48,5,3,0,0,48,49,5,5,0,0,49,50,5,27,0,0,50,52,3,14,7,0,51,53,
        5,13,0,0,52,51,1,0,0,0,52,53,1,0,0,0,53,65,1,0,0,0,54,55,5,12,0,
        0,55,57,5,14,0,0,56,58,3,10,5,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,
        1,0,0,0,59,60,1,0,0,0,60,65,1,0,0,0,61,62,5,16,0,0,62,63,5,30,0,
        0,63,65,5,33,0,0,64,41,1,0,0,0,64,47,1,0,0,0,64,54,1,0,0,0,64,61,
        1,0,0,0,65,5,1,0,0,0,66,67,5,2,0,0,67,69,5,33,0,0,68,70,3,8,4,0,
        69,68,1,0,0,0,70,71,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,7,1,0,
        0,0,73,74,5,3,0,0,74,75,5,10,0,0,75,77,3,14,7,0,76,78,5,13,0,0,77,
        76,1,0,0,0,77,78,1,0,0,0,78,87,1,0,0,0,79,80,5,12,0,0,80,82,5,15,
        0,0,81,83,3,12,6,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,
        85,1,0,0,0,85,87,1,0,0,0,86,73,1,0,0,0,86,79,1,0,0,0,87,9,1,0,0,
        0,88,89,5,33,0,0,89,90,5,6,0,0,90,91,3,18,9,0,91,92,5,8,0,0,92,93,
        3,20,10,0,93,94,5,32,0,0,94,11,1,0,0,0,95,96,5,9,0,0,96,97,5,33,
        0,0,97,98,3,20,10,0,98,99,5,32,0,0,99,13,1,0,0,0,100,105,5,33,0,
        0,101,102,5,31,0,0,102,104,5,33,0,0,103,101,1,0,0,0,104,107,1,0,
        0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,15,1,0,0,0,107,105,1,0,0,
        0,108,109,3,26,13,0,109,110,5,33,0,0,110,17,1,0,0,0,111,116,3,16,
        8,0,112,113,5,31,0,0,113,115,3,16,8,0,114,112,1,0,0,0,115,118,1,
        0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,19,1,0,0,0,118,116,1,0,
        0,0,119,124,3,22,11,0,120,121,5,31,0,0,121,123,3,22,11,0,122,120,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,21,1,
        0,0,0,126,124,1,0,0,0,127,128,3,26,13,0,128,129,5,33,0,0,129,132,
        1,0,0,0,130,132,3,24,12,0,131,127,1,0,0,0,131,130,1,0,0,0,132,23,
        1,0,0,0,133,134,5,24,0,0,134,135,5,33,0,0,135,136,3,26,13,0,136,
        139,5,33,0,0,137,138,5,18,0,0,138,140,5,33,0,0,139,137,1,0,0,0,139,
        140,1,0,0,0,140,25,1,0,0,0,141,142,7,0,0,0,142,27,1,0,0,0,16,30,
        32,39,45,52,59,64,71,77,84,86,105,116,124,131,139
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "AGENT", "ENVIRONMENT", "THAT", "BELIEVES", 
                      "DESIRES", "WHEN", "IF", "THEN", "DO", "PERCEIVES", 
                      "HAS", "WITH", "AND", "PLANS", "ACTIONS", "USING", 
                      "CAN", "VIA", "ACHIEVE", "ABANDON", "DISBELIEVE", 
                      "PERCEPT", "CHANGE", "SEND", "RECEIVE", "MESSAGE", 
                      "TO", "FROM", "BROADCAST", "CHANNEL", "COMMA", "DOT", 
                      "ID", "WS" ]

    RULE_system = 0
    RULE_agentDef = 1
    RULE_thatClause = 2
    RULE_environmentDef = 3
    RULE_thatEnvClause = 4
    RULE_plan = 5
    RULE_actionDef = 6
    RULE_idList = 7
    RULE_condition = 8
    RULE_conditionList = 9
    RULE_actionList = 10
    RULE_action = 11
    RULE_sendAction = 12
    RULE_actionType = 13

    ruleNames =  [ "system", "agentDef", "thatClause", "environmentDef", 
                   "thatEnvClause", "plan", "actionDef", "idList", "condition", 
                   "conditionList", "actionList", "action", "sendAction", 
                   "actionType" ]

    EOF = Token.EOF
    AGENT=1
    ENVIRONMENT=2
    THAT=3
    BELIEVES=4
    DESIRES=5
    WHEN=6
    IF=7
    THEN=8
    DO=9
    PERCEIVES=10
    HAS=11
    WITH=12
    AND=13
    PLANS=14
    ACTIONS=15
    USING=16
    CAN=17
    VIA=18
    ACHIEVE=19
    ABANDON=20
    DISBELIEVE=21
    PERCEPT=22
    CHANGE=23
    SEND=24
    RECEIVE=25
    MESSAGE=26
    TO=27
    FROM=28
    BROADCAST=29
    CHANNEL=30
    COMMA=31
    DOT=32
    ID=33
    WS=34

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

        def thatClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ThatClauseContext)
            else:
                return self.getTypedRuleContext(ClagParser.ThatClauseContext,i)


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
                self.thatClause()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 69640) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThatClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ClagParser.RULE_thatClause

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AgentDesiresContext(ThatClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ClagParser.ThatClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THAT(self):
            return self.getToken(ClagParser.THAT, 0)
        def DESIRES(self):
            return self.getToken(ClagParser.DESIRES, 0)
        def TO(self):
            return self.getToken(ClagParser.TO, 0)
        def idList(self):
            return self.getTypedRuleContext(ClagParser.IdListContext,0)

        def AND(self):
            return self.getToken(ClagParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentDesires" ):
                listener.enterAgentDesires(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentDesires" ):
                listener.exitAgentDesires(self)


    class AgentBeliefsContext(ThatClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ClagParser.ThatClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THAT(self):
            return self.getToken(ClagParser.THAT, 0)
        def BELIEVES(self):
            return self.getToken(ClagParser.BELIEVES, 0)
        def idList(self):
            return self.getTypedRuleContext(ClagParser.IdListContext,0)

        def AND(self):
            return self.getToken(ClagParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentBeliefs" ):
                listener.enterAgentBeliefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentBeliefs" ):
                listener.exitAgentBeliefs(self)


    class AgentPlansContext(ThatClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ClagParser.ThatClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(ClagParser.WITH, 0)
        def PLANS(self):
            return self.getToken(ClagParser.PLANS, 0)
        def plan(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.PlanContext)
            else:
                return self.getTypedRuleContext(ClagParser.PlanContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentPlans" ):
                listener.enterAgentPlans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentPlans" ):
                listener.exitAgentPlans(self)


    class AgentCHANNELContext(ThatClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ClagParser.ThatClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def USING(self):
            return self.getToken(ClagParser.USING, 0)
        def CHANNEL(self):
            return self.getToken(ClagParser.CHANNEL, 0)
        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgentCHANNEL" ):
                listener.enterAgentCHANNEL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgentCHANNEL" ):
                listener.exitAgentCHANNEL(self)



    def thatClause(self):

        localctx = ClagParser.ThatClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_thatClause)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ClagParser.AgentBeliefsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ClagParser.THAT)
                self.state = 42
                self.match(ClagParser.BELIEVES)
                self.state = 43
                self.idList()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 44
                    self.match(ClagParser.AND)


                pass

            elif la_ == 2:
                localctx = ClagParser.AgentDesiresContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(ClagParser.THAT)
                self.state = 48
                self.match(ClagParser.DESIRES)
                self.state = 49
                self.match(ClagParser.TO)
                self.state = 50
                self.idList()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 51
                    self.match(ClagParser.AND)


                pass

            elif la_ == 3:
                localctx = ClagParser.AgentPlansContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(ClagParser.WITH)
                self.state = 55
                self.match(ClagParser.PLANS)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 56
                    self.plan()
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==33):
                        break

                pass

            elif la_ == 4:
                localctx = ClagParser.AgentCHANNELContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.match(ClagParser.USING)
                self.state = 62
                self.match(ClagParser.CHANNEL)
                self.state = 63
                self.match(ClagParser.ID)
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

        def thatEnvClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ThatEnvClauseContext)
            else:
                return self.getTypedRuleContext(ClagParser.ThatEnvClauseContext,i)


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
            self.state = 66
            self.match(ClagParser.ENVIRONMENT)
            self.state = 67
            self.match(ClagParser.ID)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.thatEnvClause()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==12):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThatEnvClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ClagParser.RULE_thatEnvClause

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EnvActionsContext(ThatEnvClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ClagParser.ThatEnvClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WITH(self):
            return self.getToken(ClagParser.WITH, 0)
        def ACTIONS(self):
            return self.getToken(ClagParser.ACTIONS, 0)
        def actionDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClagParser.ActionDefContext)
            else:
                return self.getTypedRuleContext(ClagParser.ActionDefContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvActions" ):
                listener.enterEnvActions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvActions" ):
                listener.exitEnvActions(self)


    class EnvPerceptionsContext(ThatEnvClauseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ClagParser.ThatEnvClauseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THAT(self):
            return self.getToken(ClagParser.THAT, 0)
        def PERCEIVES(self):
            return self.getToken(ClagParser.PERCEIVES, 0)
        def idList(self):
            return self.getTypedRuleContext(ClagParser.IdListContext,0)

        def AND(self):
            return self.getToken(ClagParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnvPerceptions" ):
                listener.enterEnvPerceptions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnvPerceptions" ):
                listener.exitEnvPerceptions(self)



    def thatEnvClause(self):

        localctx = ClagParser.ThatEnvClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_thatEnvClause)
        self._la = 0 # Token type
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = ClagParser.EnvPerceptionsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(ClagParser.THAT)
                self.state = 74
                self.match(ClagParser.PERCEIVES)
                self.state = 75
                self.idList()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 76
                    self.match(ClagParser.AND)


                pass
            elif token in [12]:
                localctx = ClagParser.EnvActionsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(ClagParser.WITH)
                self.state = 80
                self.match(ClagParser.ACTIONS)
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 81
                    self.actionDef()
                    self.state = 84 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9):
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
            self.state = 88
            self.match(ClagParser.ID)
            self.state = 89
            self.match(ClagParser.WHEN)
            self.state = 90
            self.conditionList()
            self.state = 91
            self.match(ClagParser.THEN)
            self.state = 92
            self.actionList()
            self.state = 93
            self.match(ClagParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(ClagParser.DO, 0)

        def ID(self):
            return self.getToken(ClagParser.ID, 0)

        def actionList(self):
            return self.getTypedRuleContext(ClagParser.ActionListContext,0)


        def DOT(self):
            return self.getToken(ClagParser.DOT, 0)

        def getRuleIndex(self):
            return ClagParser.RULE_actionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionDef" ):
                listener.enterActionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionDef" ):
                listener.exitActionDef(self)




    def actionDef(self):

        localctx = ClagParser.ActionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_actionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ClagParser.DO)
            self.state = 96
            self.match(ClagParser.ID)
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
            while _la==31:
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
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.actionType()
            self.state = 109
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
        self.enterRule(localctx, 18, self.RULE_conditionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.condition()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 112
                self.match(ClagParser.COMMA)
                self.state = 113
                self.condition()
                self.state = 118
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
            self.state = 119
            self.action()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 120
                self.match(ClagParser.COMMA)
                self.state = 121
                self.action()
                self.state = 126
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


        def ID(self):
            return self.getToken(ClagParser.ID, 0)

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
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 19, 20, 21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.actionType()
                self.state = 128
                self.match(ClagParser.ID)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
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
            self.state = 133
            self.match(ClagParser.SEND)
            self.state = 134
            self.match(ClagParser.ID)
            self.state = 135
            self.actionType()
            self.state = 136
            self.match(ClagParser.ID)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 137
                self.match(ClagParser.VIA)
                self.state = 138
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

        def ACHIEVE(self):
            return self.getToken(ClagParser.ACHIEVE, 0)

        def ABANDON(self):
            return self.getToken(ClagParser.ABANDON, 0)

        def BELIEVES(self):
            return self.getToken(ClagParser.BELIEVES, 0)

        def DISBELIEVE(self):
            return self.getToken(ClagParser.DISBELIEVE, 0)

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
        self.enterRule(localctx, 26, self.RULE_actionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16252944) != 0)):
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





