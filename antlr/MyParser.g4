parser grammar MyParser;

options { tokenVocab=MyLexer; }

system: import_stmt* entity*;

import_stmt: IMPORT ID SEMI?;

entity: agent | environment;

// Agent Rules
agent: AGENT ID agent_section*;
agent_section: beliefs | desires | agent_plans;
beliefs: BELIEFS id_list;
desires: DESIRES id_list;
agent_plans: PLANS (agent_plan (COMMA agent_plan)*);

agent_plan: ID LPAREN WHEN action (CONTAINS condition_list)? RPAREN DO action_list END;
condition_list: condition (COMMA condition)*;
condition: agent_action_type ID;
action: agent_action_type ID;
action_list: action (COMMA action)*;
agent_action_type: BELIEVE | DISBELIEVE | ACHIEVE | ABANDON;

// Environment Rules
environment: ENVIRONMENT ID environment_section*;
environment_section: perceptions | environment_plans;
perceptions: PERCEPTIONS id_list;
environment_plans: ACTIONS (env_plan (COMMA env_plan)*);

env_plan: ID DO env_action_list END;
env_action_list: env_action (COMMA env_action)*;
env_action: env_action_type ID;
env_action_type: PERCEPT | CHANGE;

// Common Rules
id_list: ID (COMMA ID)*;