from multiprocessing import Manager

import time

from hamster.sensor import SensorManager


def test_sensor_manager_init():
    manager = Manager()
    queue = manager.Queue()
    sensor_manager = SensorManager(queue)
    assert sensor_manager
    assert not sensor_manager.has_events()
    assert len(list(sensor_manager.get_events())) == 0


def test_sensor_manager():
    manager = Manager()
    queue = manager.Queue()
    sensor_manager = SensorManager(queue=queue)
    event = (0, 1, time.clock())
    queue.put(event)
    assert sensor_manager.has_events()
    events = list(sensor_manager.get_events())
    assert len(events) == 1
    assert events[0] == event
