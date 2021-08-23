from app import db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    original_link = db.Column(db.String(), unique=True)
    short_link = db.Column(db.String(16), unique=True)

    @staticmethod
    def is_unique_original_link(link: str) -> bool:
        return not db.session.query(
            db.exists().where(Link.original_link == link)).scalar()

    @staticmethod
    def is_unique_short_link(link: str) -> bool:
        return not db.session.query(
            db.exists().where(Link.short_link == link)).scalar()

    @staticmethod
    def get_by_short_link(short_link: str):
        return Link.query.filter(Link.short_link == short_link).first()

    @staticmethod
    def get_by_original_link(original_link: str):
        return Link.query.filter(Link.original_link == original_link).first()
