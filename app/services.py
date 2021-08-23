from secrets import token_urlsafe
from app import db
from .models import Link


class LinkService():
    @staticmethod
    def create(original_link: str) -> str:
        if Link.is_unique_original_link(original_link):
            short_link = LinkService.generate_short_link()
            link = Link(original_link=original_link, short_link=short_link)
            db.session.add(link)
            db.session.commit()
            return short_link
        return Link.get_by_original_link(original_link).short_link

    @staticmethod
    def get(short_link: str) -> str:
        return Link.get_by_short_link(short_link)

    @staticmethod
    def generate_short_link():
        while True:
            if (link := token_urlsafe(4)) and Link.is_unique_short_link(link):
                return link
