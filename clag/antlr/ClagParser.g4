parser grammar ClagParser;
options { tokenVocab=ClagLexer; }

system: (agentDef | environmentDef)+;

agentDef: AGENT ID agentSection+;
agentSection:
  DESIRES TO idList AND?
  | BELIEVES idList AND?
  | IN ENVIRONMENT ID
  | USING CHANNEL ID
  | WITH PLANS plan+
;

environmentDef: ENVIRONMENT ID environmentSection+;
environmentSection:
    THAT PERCEIVES idList
  | WITH ACTIONS actionName+
;

actionName: ID DOT;

plan: ID WHEN conditionList (WITH contextList)? THEN actionList DOT;

idList: ID (COMMA ID)*;
conditionList: actionType (COMMA actionType)*;
contextList: actionType (COMMA actionType)*;
actionList: action (COMMA action)*;
action: 
    actionType
  | sendAction
;

sendAction: SEND ID actionType (VIA ID)?;
actionType: (ACHIEVE | ABANDON | BELIEVES | PERCEPT | CHANGE | DESIRES TO) ID;