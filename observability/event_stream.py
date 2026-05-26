# observability/event_stream.py
import queue
import threading
import time

class EventStream:
    """
    Handles asynchronous event streaming for system monitoring.
    """
    _event_queue = queue.Queue()

    @classmethod
    def emit(cls, event_type: str, data: dict):
        """
        Emits an event to the stream for processing.
        """
        cls._event_queue.put({"type": event_type, "payload": data})

    @classmethod
    def start_consumer(cls):
        """
        Starts a background thread to process events.
        """
        def process():
            while True:
                event = cls._event_queue.get()
                # Here we could stream to external tools (Elastic, Datadog, etc.)
                print(f"[STREAM] Processing event: {event['type']}")
                cls._event_queue.task_done()
        
        thread = threading.Thread(target=process, daemon=True)
        thread.start()