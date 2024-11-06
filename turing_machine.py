import xml.etree.ElementTree as ET

def load_turing_machine(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    states = {}
    transitions = []

    for state in root.findall(".//state"):
        state_id = state.get('id')
        state_name = state.get('name')
        initial = state.find('initial') is not None
        final = state.find('final') is not None
        states[state_id] = {
            'name': state_name,
            'initial': initial,
            'final': final
        }

    for transition in root.findall(".//transition"):
        from_state = transition.find('from').text
        to_state = transition.find('to').text
        read = transition.find('read').text if transition.find('read').text is not None else ""
        write = transition.find('write').text if transition.find('write').text is not None else ""
        move = transition.find('move').text

        transitions.append({
            'from': from_state,
            'to': to_state,
            'read': read,
            'write': write,
            'move': move
        })

    return states, transitions

def simulate_turing_machine(tape, transitions, states):
    current_state = next(state_id for state_id, info in states.items() if info['initial'])
    tape = list(tape)
    head_position = 0
    flag = False

    while True:
        if head_position >= len(tape):
            tape.append("_")
        symbol = tape[head_position]

        transition = next((t for t in transitions if t['from'] == current_state and t['read'] == symbol), None)
        if not transition:
            break

        tape[head_position] = transition['write']
        current_state = transition['to']

        if transition['move'] == 'R':
            head_position += 1
        elif transition['move'] == 'L':
            head_position -= 1

        if states[current_state]['final']:
            flag = True
            return flag

 
    return flag

def process_string(input_string):
    states, transitions = load_turing_machine("turing_machine_matricula.xml")
    is_valid = simulate_turing_machine(input_string, transitions, states)
    
    if (is_valid):
        return True
    else:
        return False