import click

_belief_ctx_types = ['believe', 'disbelieve']
_goal_ctx_types = ['achieve', 'abandon']

def context_type_to_str(context, contextType):
    """Handle context strings from split action/condition components"""
    if contextType in _belief_ctx_types:
        return f'Belief("{context}")'
    if contextType in _goal_ctx_types:
        return f'Goal("{context}")'
    
    click.echo(f'[ERROR] Invalid operation: {contextType} {context}')
    exit()

def conditions_to_str(conditions):
    """Process conditions list of strings (["believe X", "achieve Y"])"""
    if not conditions:
        return ''
    
    processed = []
    for cond in conditions:
        ctx_type, name = cond.split()
        processed.append(context_type_to_str(name, ctx_type))
    
    return f', [{", ".join(processed)}]'

def change_to_srt(contextType, decorator):
    """Map context types to MAS actions"""
    contextType = contextType.lower()
    
    if contextType in ['believe', 'achieve']:
        return 'gain' if decorator else 'add'
    elif contextType in ['disbelieve', 'abandon']:
        return 'lose' if decorator else 'rm'
    
    click.echo(f'[ERROR] Unknown context type: {contextType}')
    exit()