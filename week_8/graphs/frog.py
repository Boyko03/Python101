def ready(frogs):
    index = frogs.index('_')
    left = frogs[:index]
    if '>' in left:
        return False
    else:
        right = frogs[index:]
        if '<' in right:
            return False

    return True


def add(frogs, solution):
    solution.insert(0, f"{''.join(frogs)}\n")


def swap_frogs(new_frogs, x):
    index = new_frogs.index('_')

    tmp = new_frogs[index + x]
    new_frogs[index + x] = new_frogs[index]
    new_frogs[index] = tmp


def frog_jump(frogs, x):
        new_frogs = frogs[:]
        swap_frogs(new_frogs, x)

        return new_frogs


def jump(frogs, solution):
    if ready(frogs):
        solution += [f'{"".join(frogs)}\n']
        return 1

    to_str = ''.join(frogs).split('_')
    if to_str[0] != '' and to_str[0][-1] == '>':
        new_frogs = frog_jump(frogs, -1)
        if jump(new_frogs, solution):
            add(frogs, solution)
            return True

    if len(to_str[0]) > 1 and to_str[0][-2] == '>':
        new_frogs = frog_jump(frogs, -2)
        if jump(new_frogs, solution):
            add(frogs, solution)
            return True

    if to_str[1] != '' and to_str[1][0] == '<':
        new_frogs = frog_jump(frogs, 1)
        if jump(new_frogs, solution):
            add(frogs, solution)
            return True

    if len(to_str[1]) > 1 and to_str[1][1] == '<':
        new_frogs = frog_jump(frogs, 2)
        if jump(new_frogs, solution):
            add(frogs, solution)
            return True

    return False


def verify(frogs):
    if frogs.count('_') != 1:
        raise ValueError('Invalid input')

    if frogs.count('>') == 0 or frogs.count('<') == 0:
        raise ValueError('Invalid input')

    if frogs.count('>') != frogs.count('<'):
        raise ValueError('Invalid input.')

    for frog in frogs:
        if frog not in ['>', '_', '<']:
            raise ValueError('Invalid input.')


def frog(frogs):
    solution = []
    verify(frogs)
    frogs = [frog for frog in frogs]
    jump(frogs, solution)

    print(''.join(solution))
