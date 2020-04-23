def deep_find_all_bfs(data, key):
    def bfs(datas, key, found):
        new_datas = []
        for data in datas:
            if key in data:
                found.append(data[key])

            for k in data:
                if type(data[k]) == dict:
                    new_datas += [{key: data[k][key]} for key in data[k]]

        if new_datas != []:
            bfs(new_datas, key, found)

        return found

    return bfs([{k: data[k]} for k in data], key, [])


def deep_find_all_dfs(data, key):
    def dfs(data, key, found):
        if key in data:
            found.append(data[key])

        for k in data:
            if type(data[k]) == dict:
                dfs(data[k], key, found)

        return found

    return dfs(data, key, [])
