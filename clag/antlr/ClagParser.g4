parser grammar ClagParser;
options { tokenVocab=ClagLexer; }

system: (agentDef | environmentDef)+;

agentDef:
    AGENT ID agentSection+
  | CREATE NUMBER ID AGENTS agentSection+
;
agentSection:
  DESIRES TO goalDefList AND?
  | BELIEVES beliefDefList AND?
  | IN ENVIRONMENT ID AND?
  | FOCUSING ON idList AND?
  | IGNORING idList AND?
  | USING CHANNEL ID AND?
  | WITH PLANS plan+
;

beliefDefList: beliefDef (COMMA beliefDef)*;
beliefDef: ID (IS valueList)?;

goalDefList: goalDef (COMMA goalDef)*;
goalDef: ID (WITH valueList)?;

valueList: value (COMMA value)*;
value: ID | NUMBER | STRING | ANY;

environmentDef: ENVIRONMENT ID environmentSection+;
environmentSection:
    THAT PERCEIVES idList
  | WITH ACTIONS actionName+
;

actionName: ID (THAT (REMOVES | CREATES | CHANGES) ID)? DOT;

plan: ID WHEN conditionList (WITH contextList)? THEN actionList DOT;

idList: ID (COMMA ID)*;
conditionList: actionType (COMMA actionType)*;
contextList: actionType (COMMA actionType)*;
actionList: action (COMMA action)*;
action: 
    actionType
  | sendAction
  | askAction
;

askAction: ASK (ID | EVERYONE) ABOUT ID (AND WAIT)? (VIA ID)?;

sendAction: SEND (ID | EVERYONE) actType ID (VIA ID)?;
actType:
    TELL
  | UNTELL
  | TELL HOW
  | UNTELL HOW
  | ACHIEVE
  | UNACHIEVE
  | ASK ONE
  | ASK ALL
  | ASK HOW
;
actionType: (ACHIEVE | ABANDON | BELIEVES | PERCEPT | CHANGE | DESIRES TO? | LOSES BELIEVES | LOSES DESIRES TO?) ID;