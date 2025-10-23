from marshmallow import Schema, fields
from sqlalchemy import Column, String
from blacklists.src.models.model import Model, Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Blacklist(Model, Base):
    __tablename__ = 'blacklists'

    email = Column(String(120), unique=True, nullable=False)
    app_uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    blocked_reason = Column(String(255))
    ip = Column(String(20), nullable=False)

    def __init__(self, email, app_uuid, blocked_reason, ip):
        Model.__init__(self)
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip = ip

# Especificación de los campos que estarán presentes al serializar el objeto como JSON
class BlacklistSchema(Schema):
    id = fields.UUID()
    email = fields.String()
    app_uuid = fields.UUID()
    blocked_reason = fields.String()
    ip = fields.String()
    createdAt = fields.DateTime()
