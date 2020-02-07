import time


def get_time_track(precision):
    def time_track(func):
        def surrogate(*args, **kwargs):
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция работала {elapsed} секунд(ы)')
            return result

        return surrogate

    return time_track


