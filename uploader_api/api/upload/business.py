from uploader_api.database import db
from uploader_api.database.models import UploadIntent


def create_upload_intent(data):
    upload_intent_device = data.get('device')
    upload_intent_date = data.get('date')

    delete_upload_intent(upload_intent_date, upload_intent_device)

    upload_intent = UploadIntent(upload_intent_date, upload_intent_device)
    if upload_intent_date:
        upload_intent.date = upload_intent_date

    db.session.add(upload_intent)
    db.session.commit()
    

def delete_upload_intent(upload_intent_date, upload_intent_device):
    upload_intent = UploadIntent.query.filter(UploadIntent.date == upload_intent_date and 
        UploadIntent.device == upload_intent_device).one_or_none()
    if upload_intent:
        db.session.delete(upload_intent)
        db.session.commit()
