from app import App
from app.utils import Utils
from app.models.image_file_type import ImageFileType

class Photo:
    def __init__(
        self,
        id: int,
        owner_id: int,
        file_type: ImageFileType
    ):
        self.id = id
        self.owner_id = owner_id
        self.file_type = file_type

    @staticmethod
    def db_fetch_pending() -> list:
        result = []

        cursor = App.instance.db.cursor()

        cursor.execute("SELECT id, owner, file_type FROM photos WHERE sync_status = 'synced' AND processing_status = 'pending' LIMIT 5")

        result = cursor.fetchall()

        photos = []

        for photo in result:
            photos.append(Photo(
                photo[0],
                photo[1],
                ImageFileType[photo[2]]
            ))

        return photos

    def get_file_name(self) -> str:
        return Utils.int_to_16_byte_hex(self.id)

    def __str__(self):
        return ("Photo: {{\n"
            "    id: {},\n"
            "    owner_id: {},\n"
            "    file_type: {}\n"
            "}}").format(
                self.id,
                self.owner_id,
                self.file_type
            )