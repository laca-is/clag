parser grammar ClagParser;
options { tokenVocab=ClagLexer; }

system: (agentDef | environmentDef)+;

agentDef: AGENT ID agentSection+;
agentSection:
    THAT BELIEVES idList
  | THAT DESIRES TO idList
  | IN ENVIRONMENT ID
  | WITH plan+
;

environmentDef: ENVIRONMENT ID environmentSection+;
environmentSection:
    THAT PERCEIVES idList
  | WITH action+
;

plan: ID WHEN conditionList THEN actionList DOT;

idList: ID (COMMA ID)*;
condition: actionType ID;
conditionList: condition (COMMA condition)*;
actionList: action (COMMA action)*;
action: 
    actionType
  | sendAction
;

sendAction: SEND ID actionType ID (VIA ID)?;
actionType: (ACHIEVE | ABANDON | BELIEVES | PERCEPT | CHANGE) ID;