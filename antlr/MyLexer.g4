lexer grammar MyLexer;

// Agent Keywords
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

// Environment Keywords
ENVIRONMENT   : 'environment';
PERCEPTIONS   : 'perceptions:';
ACTIONS       : 'actions:';
PERCEPT       : 'percept';
CHANGE        : 'change';

// System Keywords
IMPORT        : 'import';

// Common Tokens
ID            : [a-zA-Z_][a-zA-Z0-9_]*;
COMMA         : ',';
LPAREN        : '(';
RPAREN        : ')';
SEMI          : ';';
WS            : [ \t\r\n]+ -> skip;