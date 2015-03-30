#!/usr/bin/python
# coding: utf8

import json
from sqlalchemy import create_engine
from cerberus import Validator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import sessionmaker

"""
SQL Queries
===========
"""
Base = declarative_base()


class Geocode(Base):
    __tablename__ = 'geocode'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    location = Column(String)
    provider = Column(String)
    method = Column(String)
    json = Column(String)
    geojson = Column(String)
    osm = Column(String)

    def __repr__(self):
        return "<Geocode(location='%s', provider='%s', method='%s')>" % (
               self.location, self.provider, self.method)

    def __getitem__(self, item):
        return self.__dict__.get(item, '')

"""
Schema
======
"""
v = Validator()
v.allow_unknown = True

# Allowed
allowed_method = {'type': 'string', 'allowed': ['geocode', 'reverse']}
allowed_provider = {'type': 'string', 'allowed': ['google', 'bing']}

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
}


class Cache(object):
    """Cache Object"""
    store = {}

    def __init__(self, db='sqlite:///:memory:'):
        """Create Sqlite Database"""

        engine = create_engine(db)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        session = self.Session()
        session.commit()

    def insert(self, g):
        """Insert Value into Database"""

        if v.validate(g.schema, schema_insert):
            geocode = Geocode(location=g.location,
                              provider=g.provider,
                              method=g.method,
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

    def find(self, params, output='json'):
        """Find item in Database using a JSON Query"""

        if v.validate(params, schema_find):
            # Retrieve in memory first
            if json.dumps(params) in self.store:
                return self.store.get(json.dumps(params))[output]
            else:
                # Query Databse
                session = self.Session()
                query = session.query(Geocode).filter_by(
                    location=params['location'],
                    provider=params['provider'],
                    method=params['method']).order_by(Geocode.id.desc()).first()

                # Store in tempory memory
                self.store[json.dumps(params)] = query

                # Return result to user
                return json.loads(query[output])
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
    provider = 'google'
    method = 'geocode'

    # Geocode Address
    g = geocoder.get(location, provider=provider, method=method)

    # Create Cache Databse
    cache = Cache('sqlite:///:memory:')

    # Insert into Database
    cache.insert(g)

    # Find results with a Query
    params = {
        'location': location,
        'provider': provider,
        'method': method,
    }
    out = cache.find(params, output='json')
    print(json.dumps(out, indent=4))
