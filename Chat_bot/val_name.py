value = {"USD": ["доллар", "$", "dollar"], "RUB": ["руб", "rubl"], "EUR": ["евро", "euro"]}


def chek(val):
    for key in value:
        for j in value[key]:
            if j.upper() in val:
                return key
    return val
