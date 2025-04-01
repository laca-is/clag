parser grammar ClagParser;

options { tokenVocab=ClagLexer; }

system: (agentDef | environmentDef)+;

agentDef: AGENT ID thatClause+;
thatClause:
    THAT BELIEVES idList AND?       #agentBeliefs
  | THAT DESIRES TO idList AND?        #agentDesires
  | WITH PLANS plan+          #agentPlans
  | USING CHANNEL ID               #agentCHANNEL
;

environmentDef: ENVIRONMENT ID thatEnvClause+;
thatEnvClause:
    THAT PERCEIVES idList AND?      #envPerceptions
  | WITH ACTIONS actionDef+   #envActions
;

plan: ID WHEN conditionList THEN actionList DOT;
actionDef: DO ID actionList DOT;

idList: ID (COMMA ID)*;
condition: actionType ID;
conditionList: condition (COMMA condition)*;
actionList: action (COMMA action)*;
action: 
    actionType ID
  | sendAction
;

sendAction: SEND ID actionType ID (VIA ID)?;
actionType: ACHIEVE | ABANDON | BELIEVES | DISBELIEVE | PERCEPT | CHANGE;