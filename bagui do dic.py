from operator import itemgetter

times = {'Palmeiras':18,
         'Flamengo': 12,
         'Coritiba': 22}

print(times)
timesnovo = sorted(times.items(), key=itemgetter(1), reverse=True)

print(timesnovo)
# print(type(timesnovo))
# print(timesnovo[1][1])

for i, time in enumerate(timesnovo):
    print(i+1, '-' ,time[0], '-' ,time[1])
# for i in timesnovo:
