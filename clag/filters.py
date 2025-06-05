import click

_belief_ctx_types = ['believe', 'disbelieve']
_goal_ctx_types = ['achieve', 'abandon']

def data_type_to_str(data):
    """Handle context strings from split action/condition components"""
    if isinstance(data, list):
        return ', '.join(data_type_to_str(item) for item in data)
    
    if isinstance(data, tuple):
        ctx, name = data
        if hasattr(ctx, 'BELIEVES') and ctx.BELIEVES():
            return f'Belief("{name}")'
        elif hasattr(ctx, 'DESIRES') and ctx.DESIRES():
            return f'Goal("{name}")'
        return f'"{name}"'
    
    return str(data)

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

def trim(value):
    """Remove leading and trailing whitespace"""
    return value.strip()