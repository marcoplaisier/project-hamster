import time
from queue import Queue, Empty


class StopEvent:
    pass


class Sensor(object):
    def __init__(self, sensor_id=0, queue=None):
        self.sensor_id = sensor_id
        self.queue = queue
        self.state = False

    def toggle(self):
        if self.queue:
            self.queue.put((self.sensor_id, self.state, time.clock()))
        self.state = not self.state

    def stop(self):
        self.state = None
        if self.queue:
            self.queue.put(StopEvent())


class SensorManager(object):
    def __init__(self, queue):
        self.queue = queue

    def has_events(self):
        return not self.queue.empty()

    def get_events(self):
        not_done = True
        while not_done:
            try:
                event = self.queue.get_nowait()
            except Empty:
                not_done = True
                event = None

            if event and not isinstance(event, StopEvent):
                yield event
            else:
                raise StopIteration
