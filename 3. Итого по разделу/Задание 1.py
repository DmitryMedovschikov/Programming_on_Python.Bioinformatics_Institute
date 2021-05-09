# Напишите программу, которая принимает на стандартный вход список игр
# футбольных команд с результатом матча и выводит на стандартный вывод
# сводную таблицу результатов всех матчей. За победу команде начисляется 3
# очка, за поражение — 0, за ничью — 1. Формат ввода следующий: В первой
# строке указано целое число nn — количество завершенных игр. После этого
# идет nn строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом: Команда:Всего_игр
# Побед Ничьих Поражений Всего_очков

import itertools

number_of_games = int(input())
games_list = [input().split(';') for game in range(number_of_games)]

teams_in_match = [(game[0], game[2]) for game in games_list]
teams = set(itertools.chain.from_iterable(teams_in_match))
results_dict = {team: [0, 0, 0, 0, 0] for team in teams}

for team_1, goals_1, team_2, goals_2 in games_list:
    results_dict[team_1][0] += 1
    results_dict[team_2][0] += 1
    if int(goals_1) > int(goals_2):
        results_dict[team_1][1] += 1
        results_dict[team_1][4] += 3
        results_dict[team_2][3] += 1
    elif int(goals_1) < int(goals_2):
        results_dict[team_2][1] += 1
        results_dict[team_2][4] += 3
        results_dict[team_1][3] += 1
    elif int(goals_1) == int(goals_2):
        results_dict[team_1][2] += 1
        results_dict[team_1][4] += 1
        results_dict[team_2][2] += 1
        results_dict[team_2][4] += 1

for team in teams:
    print('{}:{}'.format(team, ' '.join(map(str, results_dict[team]))))
