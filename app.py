from flask import Flask
import flask_restless
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)

class IMDBTitleBasics(db.Model):
    """
    Contains the imdb titles information
    """

    __tablename__ = 'imdb_title_basics'

    tconst = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titleType = db.Column(db.String, default='Movie')
    primaryTitle = db.Column(db.String, nullable=False)
    originalTitle = db.Column(db.String, nullable=False)
    isAdult = db.Column(db.Boolean, default=False)
    startYear = db.Column(db.Integer, nullable=False)
    endYear = db.Column(db.String, nullable=True)
    runtimeMinutes = db.Column(db.Integer, nullable=True)
    genres = db.Column(db.String, default='user')
    crew = db.relationship("IMDBTitleCrew", backref="imdb_title_crew", lazy="joined")
    ratings = db.relationship("IMDBTitleRatings", backref="imdb_title_ratings", lazy="joined")

    def __init__(self, title_id, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres):
        self.title_id = title_id
        self.titleType = titleType
        self.primaryTitle = primaryTitle
        self.originalTitle = originalTitle
        self.isAdult = isAdult
        self.startYear = startYear
        self.endYear = endYear
        self.runtimeMinutes = runtimeMinutes
        self.genres = genres
    def __repr__(self):
        return u'<Title {}>'.format(self.primaryTitle)

class IMDBTitleCrew(db.Model):
    """
    Contains the imdb titles information
    """

    __tablename__ = 'imdb_title_crew'

    tconst = db.Column(db.Integer, db.ForeignKey('imdb_title_basics.tconst'), primary_key=True)
    directors = db.Column(db.String, nullable=True)
    writers = db.Column(db.String, nullable=True)
    

    def __init__(self, title_id, directors, writers):
        self.tconst = title_id
        self.directors = directors
        self.writers = writers
    def __repr__(self):
        return u'<Directors {}>'.format(self.directors)


class IMDBTitleRatings(db.Model):
    """
    Contains the imdb titles information
    """

    __tablename__ = 'imdb_title_ratings'

    tconst = db.Column(db.Integer, db.ForeignKey('imdb_title_basics.tconst'), primary_key=True)
    title = db.relationship('IMDBTitleBasics')
    averageRating = db.Column(db.Float, nullable=True)
    numVotes = db.Column(db.Integer, default=0)

    def __init__(self, title_id, directors, writers):
        self.tconst = title_id
        self.directors = directors
        self.writers = writers
    def __repr__(self):
        return u'<Directors {}>'.format(self.directors)

db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(IMDBTitleBasics, methods=['GET', 'POST', 'DELETE'])

app.run()
