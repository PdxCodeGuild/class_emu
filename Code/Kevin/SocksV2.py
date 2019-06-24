import random


ankles, crews, calfs, thighs = 0, 0, 0, 0
a_pair, cr_pair, ca_pair, t_pair = 0, 0, 0, 0

black_ankle, black_crew, black_calf, black_thigh = 0, 0, 0, 0
white_ankle, white_crew, white_calf, white_thigh = 0, 0, 0, 0
blue_ankle, blue_crew, blue_calf, blue_thigh = 0, 0, 0, 0
red_ankle, red_crew, red_calf, red_thigh = 0, 0, 0, 0

ba_pair, bc_pair, bcalf_pair, bt_pair = 0, 0, 0, 0
wa_pair, wc_pair, wcalf_pair, wt_pair = 0, 0, 0, 0
blua_pair, bluc_pair, blucalf_pair, blut_pair = 0, 0, 0, 0
ra_pair, rc_pair, rcalf_pair, rt_pair = 0, 0, 0, 0

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue', 'red'] 

socks = []
for i in range(100):
    tu_socks = (random.choice(sock_colors), random.choice(sock_types))
    socks.append(tu_socks)
socks.sort()
#print(socks)




def count_socks(socks, color, type):
    count = 0
    for i in range(len(socks)):
        if socks[i][0] == color and socks[i][1] == type:
            count += 1
    return count

print(count_socks(socks, 'black', 'crew'))

for i in range(len(socks)):
    if socks[i][0] == 'black':
        if socks[i][1] == 'ankle':
            black_ankle += 1
            ba_pair = black_ankle // 2
        elif socks[i][1] == 'crew':
            black_crew += 1
            bc_pair = black_crew // 2
        elif socks[i][1] == 'calf':
            black_calf += 1
            bc_pair = black_calf // 2
        elif socks[i][1] == 'thigh':
            black_thigh +=1
            bt_pair = black_thigh // 2
    elif socks[i][0] == 'white':
        if socks[i][1] == 'ankle':
            white_ankle += 1
            wa_pair = white_ankle // 2
        elif socks[i][1] == 'crew':
            white_crew += 1
            wc_pair = white_crew // 2
        elif socks[i][1] == 'calf':
            white_calf += 1
            wc_pair = white_calf // 2
        elif socks[i][1] == 'thigh':
            white_thigh +=1
            wt_pair = white_thigh // 2
    elif socks[i][0] == 'blue':
        if socks[i][1] == 'ankle':
            blue_ankle += 1
            blua_pair = blue_ankle // 2
        elif socks[i][1] == 'crew':
            blue_crew += 1
            bluc_pair = blue_crew // 2
        elif socks[i][1] == 'calf':
            blue_calf += 1
            bluc_pair = blue_calf // 2
        elif socks[i][1] == 'thigh':
            blue_thigh +=1
            blut_pair = blue_thigh // 2
    if socks[i][0] == 'red':
        if socks[i][1] == 'ankle':
            red_ankle += 1
            ra_pair = red_ankle // 2
        elif socks[i][1] == 'crew':
            red_crew += 1
            rc_pair = red_crew // 2
        elif socks[i][1] == 'calf':
            red_calf += 1
            rc_pair = red_calf // 2
        elif socks[i][1] == 'thigh':
            red_thigh +=1
            rt_pair = red_thigh // 2        
    
print(f"\nBlack:\nAnkle: {black_ankle}\nCrew: {black_crew}\nCalf: {black_calf}\nThigh: {black_thigh}")
print(f"\nWhite:\nAnkle: {white_ankle}\nCrew: {white_crew}\nCalf: {white_calf}\nThigh: {white_thigh}")                 
print(f"\nBlue:\nAnkle: {blue_ankle}\nCrew: {blue_crew}\nCalf: {blue_calf}\nThigh: {blue_thigh}")                 
print(f"\nRed:\nAnkle: {red_ankle}\nCrew: {red_crew}\nCalf: {red_calf}\nThigh: {red_thigh}")                 
                 
#         ankles += 1
#         a_pair = ankles // 2
#     elif socks[i] == 'crew':
#         crews += 1
#         cr_pair = crews // 2
#     elif socks[i] == 'calf':
#         calfs += 1
#         ca_pair = calfs // 2
#     elif socks[i] == 'thigh':
#         thighs += 1
#         t_pair = thighs // 2
# print(f"\nAnkles: {ankles}\nCrews: {crews}\nCalfs: {calfs}\nThighs: {thighs}")
# print(f"\nAnkle pairs: {a_pair}\nCrew pairs: {cr_pair}\nCalf pairs: {ca_pair}\nThigh pairs: {t_pair}")