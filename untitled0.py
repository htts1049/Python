lottos=[44, 1, 0, 0, 31, 25]
win_nums =[31, 10, 45, 1, 6, 19]

cor_min = len(set(lottos)& set(win_nums))
cor_max = cor_min+ lottos.count(0)
rank = {6:1, 5:2, 4:3, 3:4, 2:5}

if cor_min in rank:
    rank_min= rank.get(cor_min)
else:
    rank_min = 6

if cor_max in rank:
    rank_max= rank.get(cor_max)
else :
    rank_max = 6

print(cor_max, cor_min)
print([rank_max, rank_min])