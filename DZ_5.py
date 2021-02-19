from random import randint
import copy

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

funny_words_list = [nouns, adverbs, adjectives]

def get_jokes(n: int, rep_word_flag = False, fwl=funny_words_list) -> list:
    fwl = copy.deepcopy(fwl)
    if n > len(fwl[0]) and rep_word_flag is False:
        return "От такого большого количетсва оригинальных шуток Вы рискуете умереть от смеха!"
    result = []
    for i in range(n):
        joke = []
        for l in fwl:
            index = randint(0, len(l)-1)
            if rep_word_flag:
                joke.append(l[index])
            else:
                joke.append(l.pop(index))
        result.append(" ".join(joke))
    return result

print(get_jokes(4))
print(get_jokes(6))
print(get_jokes(10, True))