def deep_update(data, key, val):
    if key in data:
        data[key] = val

    for k in data:
        if type(data[k]) == dict:
            deep_update(data[k], key, val)
