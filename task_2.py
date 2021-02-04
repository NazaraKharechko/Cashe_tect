from functools import lru_cache


class Support_dict(object):
    def __init__(self, arr):
        self.arr = arr

    def get_ranking_names(self):
        x = sorted(self.arr, key=self.arr.get, reverse=True)
        print(x)
        return x

    @lru_cache(maxsize=50)
    def get_average_rank(self):
        v = self.arr.values()
        r = sum(v) / len(v)
        print(f'сума рейтенгу {sum(v)}, а середнє значення рейтенгу => {r}')
        return r


obj = Support_dict({'A': 1, 'B': 2, 'C': 13, 'D': 11, 'E': 4})

obj.get_ranking_names()

obj.get_average_rank()


print(obj.get_average_rank.cache_info())
