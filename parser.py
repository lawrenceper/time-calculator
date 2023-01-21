def parser_start_in(n):
    try:
        x = n.strip().split(':')
        y = x[1].split(' ')
        z = (x[0], y[0],y[1])
        if z[2] == 'AM':
            return((int(z[0]), int(z[1]), 0))
        elif z[2] == 'PM':
            return((int(z[0]), int(z[1]), 1))
    except:
        raise Exception('Error: Failed to parse the start time given.')

def parser_end_in(n):
    try:
        x = n.strip().split(':')
        return(x[0], x[1])
    except:
        raise Exception('Error: Failed to parse the end time given.')

def parse_out():
    if len(n) == 2:
        return(f"{n[0]}:{n[1]}")
    elif len(n) == 3:
        if n[2] == 0:
            return(f"{n[0]}:{n[1]} AM")
        elif n[2] == 1:
            return(f"{n[0]}:{n[1]} PM")
    else:
        raise Exception("Error, failed to parse the string.")