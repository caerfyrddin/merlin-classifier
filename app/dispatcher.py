import logging
import threading

from app.models.photo import Photo

log = logging.getLogger('app')

class Dispatcher:
    def __init__(self):
        self.running = False

    def process_pending_images(self):
        log.debug('Started dispatch')

        while True:
            photos = Photo.db_fetch_pending()

            if len(photos) == 0:
                break

            for photo in photos:
                pass

                # Detect faces

                # for face in faces:

                    # Generate embedding

                    # class = Classify

                    # photo.addClass

                    # Update mean embedding

            break
            
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