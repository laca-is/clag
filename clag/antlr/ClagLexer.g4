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

ACHIEVE:       [aA]'chieve';
ABANDON:       [aA]'bandon';
PERCEPT:       [pP]'ercept';
CHANGE:        [cC]'hange';
SEND:          [sS]'end';

COMMA:        ',';
DOT:          '.';
ID:           [a-zA-Z_][a-zA-Z0-9_]*;
WS:           [ \t\r\n]+ -> skip;