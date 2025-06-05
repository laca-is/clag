lexer grammar ClagLexer;

AGENT:         [aA]'gent';
ENVIRONMENT:   [eE]'nvironment';
THAT:          [tT]'hat';
BELIEVES:      [bB]'elieves' | [bB]'elieve';
DESIRES:       [dD]'esires';
PERCEIVES:     [pP]'erceives';
WHEN:          [wW]'hen';
THEN:          [tT]'hen';
WITH:          [wW]'ith';
VIA:           [vV]'ia';
TO:            [tT]'o';
IN:            [iI]'n';
USING:         [uU]'sing';
CHANNEL:       [cC]'hannel';
PLANS:         [pP]'lans';
ACTIONS:       [aA]'ctions';

ACHIEVE:       [aA]'chieve';
ABANDON:       [aA]'bandon';
PERCEPT:       [pP]'ercept';
CHANGE:        [cC]'hange';
SEND:          [sS]'end';

COMMA:        ',';
DOT:          '.';
AND:          'and' | 'AND';
LPAREN:       '(';
RPAREN:       ')';
ID:           [a-zA-Z_][a-zA-Z0-9_]*;
WS:           [ \t\r\n]+ -> skip;