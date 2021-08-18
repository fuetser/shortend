from app import db
from .models import Link


class LinkService():
    @staticmethod
    def create(original_link: str, short_link: str):
        link = Link(original_link=original_link, short_link=short_link)
        db.session.add(link)
        db.session.commit()

    @staticmethod
    def get(short_link: str) -> str:
        return Link.get(short_link).original_link
