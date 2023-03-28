def outlet():
    n = int(input())
    city_income = map(int, input().split())
    city_education = map(int, input().split())
    city_citizenship = map(int, input().split())
    q = int(input())
    income = map(int, input().split())
    education = map(int, input().split())
    citizenship = map(int, input().split())
    city_dct = {indx: {'city_income': tpl[0], 'city_education': tpl[1], 'city_citizenship': tpl[2]}
                for indx, tpl in enumerate(zip(city_income, city_education, city_citizenship), 1)}
    for indx, tpl in enumerate(zip(income, education, citizenship), 1):
        for key in city_dct:
            if tpl[2] == key and city_dct[key]['city_citizenship'] == 1:
                print(key, end=' ')
                break
            elif tpl[1] == 1 and city_dct[key]['city_income'] <= tpl[0]:
                print(key, end=' ')
                break
            elif tpl[1] == 0 and city_dct[key]['city_education'] == 0 and city_dct[key]['city_income'] <= tpl[0]:
                print(key, end=' ')
                break
        else:
            print(0, end=' ')
