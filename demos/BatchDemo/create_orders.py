# Create an order every minute, writing to file.
import random
import time
import threading

WRITE_TIME_IN_SECONDS = 1
file_path = 'pending_orders.txt'

items = [
    "Edible water bottles",
    "Hoverboard shoes",
    "Solar-powered flashlight",
    "Portable inflatable sauna",
    "Miniature fog machine",
    "LED light-up plant bonsai",
    "Voice-activated trash can",
    "Self-stirring coffee mug",
    "Banana-shaped umbrella",
    "Digital pet rock"
]

def write_to_file( file_path, value ):
    with open( file_path, 'a' ) as file:
        file.write(value + '\n')
        file.flush()


# Clear the existing file.
with open( file_path, 'w' ) as file:
    pass

order_number = 0
while True:
    # Mike forgot to quit the program.
    # Let's not run it forever...
    if order_number > 99:
        break;

    write_to_file(file_path, str(order_number)
        + ': ' +items[random.randint(0,9)])
    order_number += 1
    time.sleep(WRITE_TIME_IN_SECONDS)
