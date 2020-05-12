"""

"""
from powertrain import Powertrain

# Motor pins - maybe look into adding info like this into a config file.
direction_pins = (27, 23, 19, 20)
step_pins = (22, 24, 26, 21)

dexter = Powertrain(direction_pins, step_pins)
dexter.setup()


# Testing objection creation
speed = 80
distance = 0.1
dexter.go('forward', distance, speed, 0.05, True)
dexter.go('backward', distance, speed, 1)
dexter.go('forward', distance, 100, 0.1)
dexter.go('backward', distance, 100, 0.1)
dexter.go('right', distance, speed, 1)
dexter.go('left', distance, speed, 1)
dexter.go_steps('tots_cw', 1066, 0.005, 1)
dexter.go_steps('tots_ccw', 1066,0.005, 1)


GPIO.cleanup()
# for key in dexter.directions.keys():
#     try:
#         dexter.go(key, distance, speed, 1, True)
#     except Exception as error:
#         print(error)


# def listen():
#     while True:
#         'listen out for input direction and speed'
#         choice = input('What directions and how far do you want Dexter to go')
#         break
