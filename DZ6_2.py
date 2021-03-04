from DZ6_1 import get_res_tuple


def get_statistic(log_list: list):
    """
    Рассчитываает основные статистические характеристики запросов
    :param log_list: Список кортежей из первой задачи
    :return: Словарь с описательными статистиками {
    "count_of_uniq_IP": Количество уникальных запросов,
    "rms": СКО количества запросов с одного адреса,
    "mean_val": среднее количество запросов,
    "max_req": максимальное количество запросов,
    "min_req": минимальное количество запросов}
    """
    req_counter = {}
    for line in log_list:
        key = line[0]
        req_counter[key] = req_counter.get(key, 0) + 1

    val = req_counter.values()
    meanVal = sum(val) / len(val)
    sum_of_sq = 0
    for v in val:
        sum_of_sq += (v - meanVal) ** 2
    rms = (sum_of_sq / (len(val) - 1)) ** 0.5
    return {"count_of_uniq_IP": len(val), "rms": rms, "mean_val": meanVal, "max_req": max(val), "min_req": min(val)}


def chekSPAMers(log_list: list, stat={}):
    """
    Проверяет список кортежей на наличие спамеров, исходя из того, что количество запросов с одного адреса -
    нормально распределенная случайная величина
    :param log_list: Список кортежей из первой задачи
    :param stat: Словарь со статистиками если был посчитан ранее
    :return: Словарь со спамерами {"IP адрес" : количество сделанных запросов}
    """
    if len(stat) == 0:
        stat = get_statistic(log_list)
    req_counter = {}
    for line in log_list:
        key = line[0]
        req_counter[key] = req_counter.get(key, 0) + 1
    limit_of_req = round(stat["mean_val"] + 3*stat["rms"])
    return {k: v for k, v in req_counter.items() if v > limit_of_req}


if __name__ == "__main__":
    log_list = get_res_tuple()
    print(f"Всего запросов на сервер: {len(log_list)}")

    stat = get_statistic(log_list)
    print("Запосов с уникальных IP адресов:", stat["count_of_uniq_IP"])
    print("Среднее количество запросов:", round(stat["mean_val"]))
    print("Минимальное количество запросов:", stat["min_req"])
    print("Максимальное количество запросов:", stat["max_req"])

    spamers = chekSPAMers(log_list, stat)
    print("Потенциальные спамеры:")
    for k, v in spamers.items():
        print(f"\tIP SPAMера {k}, количество сделанных запросов: {v}")
    print(f"Всего СПАМЕРов: {len(spamers)}")
    print(f"Всего СПАМ запросов: {sum(spamers.values())}")
    print("Процент СПАМ запросов:", round(sum(spamers.values()) / len(log_list) * 100), "\b%")
