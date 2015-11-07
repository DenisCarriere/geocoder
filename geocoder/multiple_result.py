#!/usr/bin/python
# coding: utf8

import geocoder
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, Boolean, Sequence
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class Geocode(Base):
    """SQLAlchemy Schema"""
    __tablename__ = 'geocode'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    location = Column(String)
    provider = Column(String)
    method = Column(String)
    ok = Column(Boolean)
    lat = Column(Float)
    lng = Column(Float)
    status = Column(String)
    json = Column(String)

    def __repr__(self):
        return "<Geocode(location='%s', provider='%s', method='%s')>" % (
               self.location, self.provider, self.method)

    def __getitem__(self, item):
        return self.__dict__.get(item, '')


class Cache(object):
    """Cache Object"""

    def __init__(self, db='sqlite:///.geocoder.db'):
        """Create Sqlite Database"""
        engine = create_engine(db)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        session = self.Session()
        session.commit()

    def insert(self, values):
        """Insert Geocoder Object into Database"""

        # Detect if data is a Geocoder class
        if hasattr(values, 'json'):
            values = values.json

        geocode = Geocode(location=values['location'],
                          provider=values['provider'],
                          lat=values.get('lat'),
                          lng=values.get('lng'),
                          method=values.get('method'),
                          ok=values.get('ok'),
                          status=values.get('status'),
                          json=json.dumps(values))
                          # All values in here
        # Save values into Database
        session = self.Session()
        session.add(geocode)
        session.commit()
        return values

    def find(self, location, provider, output='json', **kwargs):
        """Find item in Database using a JSON Query"""

        # Query Databse
        session = self.Session()
        query = session.query(Geocode).filter_by(
            location=location,
            provider=provider,
            **kwargs).order_by(Geocode.id.asc()).all()

        # Return result to user in JSON format
        if query:
            return query
        return []

def MultiQueries(location,provider,results):
    """
    How to Use
    ==========
    """
    # User Variables
    location = location
    results = results
    provider = provider

    # Create Cache Databse
    cache = Cache()
    query = cache.find(location,provider)
    if not query:
        for result in xrange(1,results+1):
        # Geocode Address
            g = geocoder.mapzen(location,result=result)
        # Insert into Database
            if g.json:
                cache.insert(g)
            else:
                return [g]
        # Find all results with a query
        query = cache.find(location,provider)
    return query

if __name__ == '__main__':
    query = MultiQueries('Sea','mapzen',10)
    for result in query:
        print(result.json)
