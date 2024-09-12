import click

_belief_ctx_types = ['acreditar', 'desacreditar']
_goal_ctx_types = ['cumprir', 'abandonar']

def context_type_to_str(context, contextType):
    if contextType in _belief_ctx_types:
        return f'Belief("{context}")'
    if contextType in _goal_ctx_types:
        return f'Goal("{context}")'
    
    click.echo(f'[ERROR] Invalid operation: {contextType} {context}')
    exit()

def conditions_to_str(conditions):
    conditions = ', '.join([context_type_to_str(condition.name, condition.ctxType) for condition in conditions])
    return f', [{conditions}]'
        
def change_to_srt(contextType, decorator):
    if contextType == _belief_ctx_types[0] or contextType == _goal_ctx_types[0]:
        return 'gain' if decorator else 'add'
    else:
        return 'lose' if decorator else 'rm'
    
