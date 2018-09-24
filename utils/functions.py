
# 加密方式
import random


def get_ticket():
    s = 'sadafdwqffgfhytuyk432646'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)
    return ticket
