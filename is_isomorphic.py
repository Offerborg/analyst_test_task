def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for char_s, char_t in zip(s, t):
        # Проверяем отображение s -> t
        if char_s in map_st:
            if map_st[char_s] != char_t:
                return False
        else:
            map_st[char_s] = char_t

        # Проверяем отображение t -> s (для уникальности замены)
        if char_t in map_ts:
            if map_ts[char_t] != char_s:
                return False
        else:
            map_ts[char_t] = char_s

    return True

# Пример
s = 'paper'
t = 'title'
print(is_isomorphic(s, t))  # True