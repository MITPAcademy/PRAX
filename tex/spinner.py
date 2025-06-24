import threading
import time

class Spinner:
    spinner_cycle = ['|', '/', '-', '\\']
    def __init__(self, message="Processing..."):
        self.stop_running = False
        self.message = message
        self._thread = None

    def start(self):
        def spin():
            idx = 0
            while not self.stop_running:
                print(f"\r{self.message} {self.spinner_cycle[idx % 4]}", end='', flush=True)
                idx += 1
                time.sleep(0.13)
            print('\r' + ' ' * (len(self.message) + 4) + '\r', end='', flush=True)

        self._thread = threading.Thread(target=spin)
        self._thread.start()

    def stop(self):
        self.stop_running = True
        if self._thread is not None:
            self._thread.join()