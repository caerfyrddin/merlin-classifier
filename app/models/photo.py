from app import App

class Photo:
    def __init__(
        self,
        id,
        owner_id,
        processing_status,
        created_at,
        modified_at
    ):
        self.id = id
        self.owner_id = owner_id
        self.processing_status = processing_status
        self.created_at = created_at
        self.modified_at = modified_at

    @staticmethod
    def db_fetch_pending() -> list:
        result = []

        cursor = App.instance.db.cursor()

        cursor.execute("SELECT * FROM photos WHERE sync_status = 'synced' AND processing_status = 'pending'")

        result = cursor.fetchall()

        return result