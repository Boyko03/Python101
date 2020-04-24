def deep_apply(func, data):
    keys = [key for key in data]
    keys.reverse()
    print(keys)

    for key in keys:
        new_key = func(key)
        data[new_key] = data[key]
        data.pop(key)

        if type(data[new_key]) == dict:
            deep_apply(func, data[new_key])
