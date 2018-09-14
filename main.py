from time import sleep
from classes import Dot
jimmy = Dot(1)
bob = Dot(color="blue")
for x in range(4):
    jimmy.move()
    jimmy.move()
    jimmy.pickUpTrash()
    jimmy.turnRight()