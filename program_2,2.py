#continuation of program_2
import program_2
start_speed = 0
car = program_2.Car(start_speed, 'Toyota', 2010)
change_speed = 5
print('Starting speed:', car.get_speed())
for x in range(0,5):
    car.accelerate(change_speed)
    print('Speed:', car.get_speed())
for y in range(0,3):
    car.brake(change_speed)
    print('Speed:', car.get_speed())