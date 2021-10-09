import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **color):
        self.color = color
        self.contents = list()
        for k, v in self.color.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, number):
        draw = list()
        if number > len(self.contents):
            number = len(self.contents)
        for i in range(number):
            ball = random.choice(self.contents)
            draw.append(ball)
            self.contents.remove(ball)
        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    run = 0
    m = 0
    if num_balls_drawn > len(hat.contents):
        num_balls_drawn = len(hat.contents)

    while num_experiments > run:
        nw_content = hat.contents.copy()
        compare = dict()
        draw = dict()
        balls = list()
        for i in range(num_balls_drawn):
            pick = random.choice(nw_content)
            balls.append(pick)
            nw_content.remove(pick)
        for ball in balls:
            if ball not in draw:
                draw[ball] = 1
            else:
                draw[ball] += 1

        for key in draw:
            if key in expected_balls and draw[key] >= expected_balls[key]:
                compare[key] = draw[key]
        if len(compare) == len(expected_balls):
            m += 1

        run += 1
    prob = m/num_experiments
    return prob


hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
# print(h.draw(3))
probability = experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1},
                         num_balls_drawn=20, num_experiments=100)
print(probability)
