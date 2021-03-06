from shared import db


class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hex_string = db.Column(db.String(4), nullable=False)
    ip_address = db.Column(db.Integer, nullable=False)
    thread = db.Column(db.Integer, db.ForeignKey("thread.id", ondelete="CASCADE"), nullable=False)
    slip = db.Column(db.Integer, db.ForeignKey("slip.id"), nullable=True)
