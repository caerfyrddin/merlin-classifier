

import logging
import threading
import time

log = logging.getLogger('app')

class Dispatcher:
    def __init__(self):
        self.running = False

    def process_pending_images(self):
        log.debug('Started dispatch')
        i = 0

        while i < 8:
            print(i)

            i += 1

            time.sleep(2)
            
        log.debug('Ended dispatch')
        self.running = False

    def run(self):
        if self.running:
            log.debug('Dispatch already started')
            return

        self.running = True

        thread = threading.Thread(target = self.process_pending_images)
        thread.start()

        return