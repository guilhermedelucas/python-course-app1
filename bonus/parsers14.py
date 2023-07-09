def parse(feet_inches_arg):
    parts = feet_inches_arg.split(' ')
    feet_local = float(parts[0])
    inches_local = float(parts[1])
    return {"feet": feet_local, "inches": inches_local}