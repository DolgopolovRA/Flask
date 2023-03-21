from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import ArticleSchema
from blog.models.database import db
from blog.models import Article, Author
from combojsonapi.event.resource import EventsResource


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }

class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter(Article.author_id == kwargs["id"]).count()}

class ArticleDetail(ResourceDetail):
    events = AuthorDetailEvents
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
