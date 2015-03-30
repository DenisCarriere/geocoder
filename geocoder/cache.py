#!/usr/bin/python
# coding: utf8

import json
from cerberus import Validator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker

"""
SQLAlchemy Schema
=================
"""
Base = declarative_base()


class Geocode(Base):
    __tablename__ = 'geocode'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    location = Column(String)
    provider = Column(String)
    method = Column(String)
    ok = Column(String)
    status = Column(String)
    json = Column(String)
    geojson = Column(String)
    osm = Column(String)

    def __repr__(self):
        return "<Geocode(location='%s', provider='%s', method='%s')>" % (
               self.location, self.provider, self.method)

    def __getitem__(self, item):
        return self.__dict__.get(item, '')

"""
Validator Schema
================
"""
v = Validator()
v.allow_unknown = True

# Allowed
allowed_method = {'type': 'string', 'allowed': ['geocode', 'reverse']}
allowed_provider = {'type': 'string', 'allowed': ['google', 'bing']}
allowed_output = {'type': 'string', 'allowed': ['json', 'osm', 'geojson']}

# Schemas
schema_insert = {
    'location': {'type': 'string'},
    'provider': allowed_provider,
    'method': allowed_method,
    'json': {'type': 'dict'}
}

schema_find = {
    'location': {'type': 'string'},
    'provider': allowed_provider,
    'method': allowed_method,
    'output': allowed_output,
}


class Cache(object):
    """Cache Object

    |Params   |Description       |Default            |
    |:--------|:-----------------|:------------------|
    |db       |SQLAlchemy DB     |sqlite:///:memory: |
    |location |Query Location    |                   |
    |provider |Geocoder Provider |bing               |
    |method   |Geocoder Method   |geocode            |
    |output   |json/geojson/osm  |json               |

    """

    def __init__(self, db='sqlite:///:memory:'):
        """Create Sqlite Database"""

        engine = create_engine(db)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        session = self.Session()
        session.commit()

    def insert(self, g):
        """Insert Geocoder Object into Database"""

        params = {
            'location': g.location,
            'provider': g.provider,
            'method': g.method,
        }

        if v.validate(params, schema_insert):
            geocode = Geocode(location=g.location,
                              provider=g.provider,
                              method=g.method,
                              ok=g.ok,
                              status=g.status,
                              json=json.dumps(g.json),
                              geojson=json.dumps(g.geojson),
                              osm=json.dumps(g.osm))

            session = self.Session()
            session.add(geocode)
            session.commit()
            return g.json
        else:
            print('WARNING: %s' % (json.dumps(v.errors)))
            return {}

    def find(self, location, **kwargs):
        """Find item in Database using a JSON Query"""

        params = {
            'location': location,
            'provider': kwargs.get('provider', 'bing'),
            'method': kwargs.get('method', 'geocode'),
            'output': kwargs.get('output', 'json'),
        }

        if v.validate(params, schema_find):
            # Query Databse
            session = self.Session()
            query = session.query(Geocode).filter_by(
                location=params['location'],
                provider=params['provider'],
                method=params['method']).order_by(Geocode.id.desc()).first()

            # Return result to user in JSON
            if query:
                out = query[params['output']]
                return json.loads(out)
            else:
                return {}
        else:
            print('WARNING: %s' % (json.dumps(v.errors)))
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
    cache.insert(g)

    # Find results with a Query
    print(cache.find(location, output='json'))
