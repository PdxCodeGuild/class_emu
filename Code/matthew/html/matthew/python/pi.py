
# have 2 counters - points "inside" the circle and points "outside"
# loop a large number of times (1,000,000)
    # generate a random px, py in the range [0, 1]
    # calculate the distance to px, py from the origin sqrt(px^2+py^2)
    # if the distance is < 1, increment the "inside" counter
    # else, increment the "outside" counter
    # calculate inside/outside*4 or outside/inside*4
    # print it out
import random
import math
counter_inside = 0
counter_outside = 0
n_samples = 1000000000


for i in range(n_samples):
    px = random.random()
    py = random.random()
    distance = math.sqrt(px*px + py*py)
    if distance <= 1:
        counter_inside += 1
    else:
        counter_outside += 1
    if (i%10000 == 0):
        print(f'{round(i/n_samples*100,2)}%')
        pi = counter_inside/(counter_outside + counter_inside)*4
        print(f'{abs(pi-math.pi)/math.pi}%')
