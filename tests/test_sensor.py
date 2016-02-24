from multiprocessing import Manager

from hamster.sensor import Sensor, StopEvent


def test_sensor_toggle():
    s = Sensor()
    assert not s.state
    s.toggle()
    assert s.state


def test_sensor_stop():
    s = Sensor()
    assert not s.state
    s.stop()
    assert not s.state


def test_sensor_with_queue():
    manager = Manager()
    queue = manager.Queue()
    s = Sensor(queue=queue)
    s.toggle()
    assert not queue.empty()
    assert len(queue.get()) == 3


def test_sensor_stop():
    manager = Manager()
    queue = manager.Queue()
    s = Sensor(queue=queue)
    s.stop()
    assert not queue.empty()
    assert isinstance(queue.get(), StopEvent)


def test_sensor_id():
    s = Sensor(sensor_id=1)
    assert s.sensor_id == 1
