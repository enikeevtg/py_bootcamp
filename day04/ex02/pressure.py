import random
import time


def emit_gel(step: int):
    pressure = 50
    sign = step / abs(step)
    while True:
        step_ = random.randint(min(0, step), max(0, step))
        pressure += step_
        sign = yield pressure
        step = sign * abs(step)
        yield


def valve():
    step = 21
    generator = emit_gel(step)
    sign = 1
    while True:
        current_pressure = next(generator)
        print(current_pressure)

        if current_pressure > 90 or current_pressure < 10:
            generator.close()
            break

        if current_pressure < 20:
            sign = 1
        elif current_pressure > 80:
            sign = -1
        generator.send(sign)
        time.sleep(0.1)


if __name__ == "__main__":
    valve()
