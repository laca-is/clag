lexer grammar ClagLexer;

AGENT         : 'agent';
BELIEFS       : 'beliefs:';
DESIRES       : 'desires:';
PLANS         : 'plans:';
WHEN          : 'when:';
CONTAINS      : 'contains:';
DO            : 'do';
END           : 'end';
BELIEVE       : 'believe';
DISBELIEVE    : 'disbelieve';
ACHIEVE       : 'achieve';
ABANDON       : 'abandon';

ENVIRONMENT   : 'environment';
PERCEPTIONS   : 'perceptions:';
ACTIONS       : 'actions:';
PERCEPT       : 'percept';
CHANGE        : 'change';

ID            : [a-zA-Z_][a-zA-Z0-9_]*;
COMMA         : ',';
LPAREN        : '(';
RPAREN        : ')';
SEMI          : ';';
WS            : [ \t\r\n]+ -> skip;