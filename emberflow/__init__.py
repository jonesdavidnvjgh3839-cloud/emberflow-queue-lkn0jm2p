'''EmberFlow Queue - lightweight in-memory message queue for Python.'''

__version__ = '1.4.2'

class EmberFlowQueue:
    """A minimal in-memory message queue."""
    def __init__(self, backend='memory'):
        self.backend = backend

    def publish(self, message):
        return self.backend
