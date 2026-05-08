import numpy as np
def get_error(steps):
    return -5 * steps + 100

#testing the function with 10steps
steps_input = 10
current_error=get_error(steps_input)

print(f"Error after {steps_input} steps: {current_error}")

#example seeing how error decreases over time
for s in range(0,21,5):
    print(f"At step {s:2},the error is {get_error(s)}")