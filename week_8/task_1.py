def deep_find_bfs(data, key):
    def bfs(datas, key):
        new_datas = []
        for data in datas:
            if key in data:
                return data[key]

            for k in data:
                if type(data[k]) == dict:
                    new_datas += [{key: data[k][key]} for key in data[k]]

        return bfs(new_datas, key)

    return bfs([{k: data[k]} for k in data], key)


def deep_find_dfs(data, key):
    if key in data:
        return data[key]

    for k in data:
        if type(data[k]) == dict:
            return deep_find_dfs(data[k], key)
