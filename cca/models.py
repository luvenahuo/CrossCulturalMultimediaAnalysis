from datetime import datetime
from time import time
from flask import current_app

from cca import app, db

# class Common(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     src_id = db.Column(db.Integer, db.ForeignKey('commits.id'))
#     commit_src = db.relationship('Commits', backref=db.backref('common_src', lazy=True))
#     dest_id = db.Column(db.Integer, db.ForeignKey('commits.id'))
#     commit_dest = db.relationship('Commits', backref=db.backref('common_dest', lazy=True))

common = db.Table(
    'common',
    db.Column('src_id', db.Integer, db.ForeignKey('commits.id')),
    db.Column('dest_id', db.Integer, db.ForeignKey('commits.id'))
)

class Commits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.String(8))
    affinity_id = db.Column(db.Integer, db.ForeignKey('affinity.id'))
    affinity = db.relationship('Affinity', backref=db.backref('commits', lazy=True))
    message = db.Column(db.String(4096))
    video_date = db.Column(db.DateTime)

    commonality = db.relationship(
        'Commits', secondary=common,
        primaryjoin=(common.c.src_id == id),
        secondaryjoin=(common.c.dest_id == id),
        backref=db.backref('common', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Commits {} {} {}>'.format(self.id, self.index, self.affinity_id)
    
    def add_common(self, commit):
        if not self.is_common(commit):
            self.commonality.append(commit)

    def is_common(self, commit):
        return self.commonality.filter(
            common.c.src_id == commit.id).count() > 0

    def get_common(self):
        commonality = Commits.query.join(common, (common.c.dest_id == Commits.id)).filter(common.c.src_id==self.id)
        
        return commonality

class Tags(db.Model):
    id =     id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(140))
    commit_id = db.Column(db.Integer, db.ForeignKey('commits.id'))
    commit = db.relationship('Commits', backref=db.backref('tags', lazy=True))

    def __repr__(self):
        return '<Tags {}>'.format(self.commit_id)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(140))
    commit_id = db.Column(db.Integer, db.ForeignKey('commits.id'))
    commit = db.relationship('Commits', backref=db.backref('image', lazy=True))
    def __repr__(self):
        return '<Images {}>'.format(self.commit_id)

class Affinity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))

    def __repr__(self):
        return '<Affinity {}>'.format(self.name)
