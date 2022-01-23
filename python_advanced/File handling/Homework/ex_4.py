import os


def prepare_result(result):
    result = sorted(result, key=lambda x: (x.split('.')[1], x.split('.')[0]))
    dict_fies = {}
    for el in result:
        if el.split('.')[1] not in dict_fies:
            dict_fies[el.split('.')[1]] = []
        dict_fies[el.split('.')[1]].append(el)

    return dict_fies


file_names = []
for dirpath, dirnames, files in os.walk('./ex_4'):
    for file_name in files:
        file_names.append(file_name)

result_dict = prepare_result(file_names)

with open(fr'C:\Users\{os.getlogin()}\Desktop\report.txt', 'w') as f:
    for k, v in result_dict.items():
        f.writelines(f'.{k}\n')
        for i in range(len(v)):
            f.writelines(f'- - - {v[i]}\n')
