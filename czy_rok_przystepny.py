def czyPrzestepny(rok):
    return (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0)

first_data = czyPrzestepny(2000)
second_data = czyPrzestepny(2002)

print(first_data)
print(second_data)