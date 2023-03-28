def outlet():
    n = int(input())
    city_income = map(int, input().split())
    city_education = map(int, input().split())
    city_citizenship = map(int, input().split())
    q = int(input())
    income = map(int, input().split())
    education = map(int, input().split())
    citizenship = map(int, input().split())
    city_dct_educ = {}
    city_dct_no_educ = {}
    lst = []
    for indx, tpl in enumerate(zip(city_income, city_education, city_citizenship), 1):
        if tpl[1] == 0:
            city_dct_educ[indx] = {
                'city_income': tpl[0], 'city_education': tpl[1], 'city_citizenship': tpl[2]}
            city_dct_no_educ[indx] = {
                'city_income': tpl[0], 'city_education': tpl[1], 'city_citizenship': tpl[2]}
        elif tpl[1] == 1:
            city_dct_educ[indx] = {
                'city_income': tpl[0], 'city_education': tpl[1], 'city_citizenship': tpl[2]}

    for indx, tpl in enumerate(zip(income, education, citizenship), 1):
        if tpl[1] == 1:
            for key in city_dct_educ:
                if tpl[0] >= city_dct_educ[key]['city_income']:
                    lst.append(key)
                    break
                elif key == tpl[2] and city_dct_educ[key]['city_citizenship'] == 1:
                    lst.append(key)
                    break
            else:
                lst.append(0)
        elif tpl[1] == 0 and tpl[2] != 0:
            if city_dct_educ[tpl[2]]['city_citizenship'] == 1:
                for key in city_dct_no_educ:
                    if key < tpl[2]:
                        if tpl[0] >= city_dct_no_educ[key]['city_income']:
                            lst.append(key)
                            break
                    elif key >= tpl[2]:
                        lst.append(tpl[2])
                        break

            elif city_dct_educ[tpl[2]]['city_citizenship'] == 0:
                for key in city_dct_no_educ:
                    if tpl[0] >= city_dct_no_educ[key]['city_income']:
                        lst.append(key)
                        break
                else:
                    lst.append(0)
        elif tpl[1] == 0 and tpl[2] == 0:
            for key in city_dct_no_educ:
                if tpl[0] >= city_dct_no_educ[key]['city_income']:
                    lst.append(key)
                    break
            else:
                lst.append(0)
    return lst


print(*outlet())
