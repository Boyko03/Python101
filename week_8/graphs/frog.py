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


def add(new_frogs, solution, frogs):
    if jump(new_frogs, solution):
        solution.insert(0, f"{''.join(frogs)}\n")
        return True

    return False


def frog_jump(new_frogs, u_index):
        index = new_frogs.index('_')

        tmp = new_frogs[index + u_index]
        new_frogs[index + u_index] = new_frogs[index]
        new_frogs[index] = tmp


def jump(frogs, solution):
    if ready(frogs):
        solution += [f'{"".join(frogs)}\n']
        return 1

    to_str = ''.join(frogs).split('_')
    if to_str[0] != '' and to_str[0][-1] == '>':
        new_frogs = frogs[:]
        frog_jump(new_frogs, -1)

        if add(new_frogs, solution, frogs):
            return True

    if to_str[0] != '' and len(to_str[0]) > 1 and to_str[0][-2] == '>':
        new_frogs = frogs[:]
        frog_jump(new_frogs, -2)

        if add(new_frogs, solution, frogs):
            return True

    if to_str[1] != '' and to_str[1][0] == '<':
        new_frogs = frogs[:]
        frog_jump(new_frogs, 1)

        if add(new_frogs, solution, frogs):
            return True

    if to_str[1] != '' and len(to_str[1]) > 1 and to_str[1][1] == '<':
        new_frogs = frogs[:]
        frog_jump(new_frogs, 2)

        if add(new_frogs, solution, frogs):
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
