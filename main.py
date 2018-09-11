from time import sleep
import game
from classes import Dot
jimmy = Dot(1)
for x in range(4):
    jimmy.move()
    jimmy.move()
    jimmy.pickUpTrash()
    jimmy.turnRight()