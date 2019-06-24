import random


ankles, crews, calfs, thighs = 0, 0, 0, 0
a_pair, cr_pair, ca_pair, t_pair = 0, 0, 0, 0
sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = []
for i in range(100):
    socks.append(random.choice(sock_types))
socks.sort()
print(socks)

for i in range(len(socks)):
    if socks[i] == 'ankle':
        ankles += 1
        a_pair = ankles // 2
    elif socks[i] == 'crew':
        crews += 1
        cr_pair = crews // 2
    elif socks[i] == 'calf':
        calfs += 1
        ca_pair = calfs // 2
    elif socks[i] == 'thigh':
        thighs += 1
        t_pair = thighs // 2
print(f"\nAnkles: {ankles}\nCrews: {crews}\nCalfs: {calfs}\nThighs: {thighs}")
print(f"\nAnkle pairs: {a_pair}\nCrew pairs: {cr_pair}\nCalf pairs: {ca_pair}\nThigh pairs: {t_pair}")