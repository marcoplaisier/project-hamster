from multiprocessing import Manager

import time

import math
import pytest

from hamster.sensor import SensorManager


@pytest.fixture
def setup():
    manager = Manager()
    queue = manager.Queue()
    sensor_manager = SensorManager(queue)
    return sensor_manager


def test_sensor_manager_init(setup):
    sensor_manager = setup
    assert sensor_manager
    assert not sensor_manager.has_events()
    assert len(list(sensor_manager.get_events())) == 0


def test_sensor_manager(setup):
    sensor_manager = setup
    event = (0, 1, time.clock())
    setup.queue.put(event)
    assert sensor_manager.has_events()
    events = list(sensor_manager.get_events())
    assert len(events) == 1
    assert events[0] == event


def test_rotation(setup):
    sensor_manager = setup
    setup.queue.put((0, 1, time.clock()))
    setup.queue.put((1, 1, time.clock()))
    assert sensor_manager.has_events()
    rotation = sensor_manager.rotation()
    assert rotation == 0.25 * math.pi
