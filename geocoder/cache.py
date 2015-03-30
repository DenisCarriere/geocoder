#!/usr/bin/python
# coding: utf8

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

    def __init__(self, db='sqlite:///:memory:'):
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

        # Save values into Database
        session = self.Session()
        session.add(geocode)
        session.commit()
        return values

    def find(self, location, provider='bing', output='json', **kwargs):
        """Find item in Database using a JSON Query"""

        # Query Databse
        session = self.Session()
        query = session.query(Geocode).filter_by(
            location=location,
            provider=provider,
            **kwargs).order_by(Geocode.id.desc()).first()

        # Return result to user in JSON format
        if query:
            return json.loads(query[output])
        return {}

if __name__ == '__main__':
    import geocoder

    """
    How to Use
    ==========
    """
    # User Variables
    location = 'Orleans, Ottawa'

    # Geocode Address
    g = geocoder.bing(location)

    # Create Cache Databse
    cache = Cache('sqlite:///:memory:')

    # Insert into Database
    values = {
        'location': location,
        'provider': 'bing',
        'lat': 45.34,
        'lng': -75.123
    }
    cache.insert(g)

    # Find results with a Query
    print(cache.find(location))
