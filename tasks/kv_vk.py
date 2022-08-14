from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - ключи.
    Например,
    flip_kv_vk({
        'tokyo': 'Токио',
        'moscow': 'Москва',
    }) == {
        'Токио': 'tokyo',
        'Москва': 'moscow',
    }
    """
    res = {}
    for k,v in d.items():
        res[v] = k
        
    return res


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    """
    Функция должна возвращать словарь, в котором в качестве ключей - значения
    переданного словаря, а в качестве значений - массив ключей конфликтующих
    значений.
    Например,
    flip_kv_vk({
        'Санкт-Петербург': '+3',
        'Москва': '+3',
    }) == {
        '+3': ['Москва', 'Санкт-Петербург'],
    }
    """
    res = {}

    for k,v in d.items():
        if v in res:
            if isinstance(res[v],list):
                res[v].append(k)
            else:
                res[v] = [res[v],k]
        else:
            res[v] = [k]

    return res
