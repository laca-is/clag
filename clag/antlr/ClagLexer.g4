lexer grammar ClagLexer;

AGENT:         'agent' | 'Agent';
ENVIRONMENT:   'environment' | 'Environment';
THAT:          'that' | 'That';
BELIEVES:      'believes' | 'Believes' | 'believe' | 'Believe';
DESIRES:       'desires' | 'Desires';
WHEN:          'when' | 'When';
IF:            'if' | 'If';
THEN:          'then' | 'Then';
DO:            'do' | 'Do';
PERCEIVES:     'perceives' | 'Perceives';
HAS:           'has' | 'Has';
WITH:          'with' | 'With';
AND:           'and' | 'And';
PLANS:         'plans' | 'Plans';
ACTIONS:       'actions' | 'Actions';
USING:         'using' | 'Using';
CAN:           'can' | 'Can';
VIA:           'via' | 'Via';

ACHIEVE:       'achieve' | 'Achieve' | 'achieves' | 'Achieves';
ABANDON:       'abandon' | 'Abandon';
DISBELIEVE:    'disbelieve' | 'Disbelieve';
PERCEPT:       'percept' | 'Percept';
CHANGE:        'change' | 'Change';

SEND:          'send' | 'Send';
RECEIVE:       'receive' | 'Receive';
MESSAGE:       'message' | 'Message';
TO:            'to' | 'To';
FROM:          'from' | 'From';
BROADCAST:     'broadcast' | 'Broadcast';
CHANNEL:      'channel' | 'Channel';

COMMA:        ',';
DOT:          '.';
ID:           [a-zA-Z_][a-zA-Z0-9_]*;
WS:           [ \t\r\n]+ -> skip;