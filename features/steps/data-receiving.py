import time
from multiprocessing import Manager

from behave import *

from hamster.sensor import Sensor, SensorManager

use_step_matcher("parse")


@given("two sensors")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    manager = Manager()
    queue = manager.Queue()
    context.queue = queue
    context.sensors = []
    context.sensors.append(Sensor(sensor_id=0, queue=queue))
    context.sensors.append(Sensor(sensor_id=1, queue=queue))
    context.sensor_manager = SensorManager(queue)


@given("sensor {number} is {state}")
def step_impl(context, number, state):
    """
    :type context: behave.runner.Context
    """
    sensor_id = int(number) - 1
    sensor_state = True if state == "High" else False
    context.sensors[sensor_id].state = sensor_state


@when("sensor {number} goes {state}")
def step_impl(context, number, state):
    """
    :type context: behave.runner.Context
    """
    sensor_id = int(number) - 1
    context.sensors[sensor_id].toggle()


@then("the sensor manager returns {amount} transition")
def step_impl(context, amount):
    """
    :type context: behave.runner.Context
    """
    for sensor in context.sensors:
        sensor.stop()

    assert context.sensor_manager.has_events()
    events = context.sensor_manager.get_events()
    event_list = list(events)
    assert len(event_list) == int(amount)
