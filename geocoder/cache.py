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
allowed_output = {'type': 'integer', 'allowed': [0, 1]}

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
schema_output = {
    'json': allowed_output
}


class Cache(object):
    """Cache Object"""

    def __init__(self, db='sqlite:///:memory:'):
        """Create Sqlite Database"""

        engine = create_engine(db)
        self.Session = sessionmaker(bind=engine)

    def insert(self, params):
        """Insert Value into Database"""

        if v.validate(params, schema_insert):
            geocode = Geocode(location=params['location'],
                              provider=params['provider'],
                              method=params['method'],
                              json=json.dumps(params))
            print(geocode.json)
            exit()
            session = self.Session()
            session.add(geocode)
            session.commit()
            return params
        else:
            return v.errors

    def find(self, params):
        """Find item in Database using a JSON Query"""

        if v.validate(params, schema_find):
            session = self.Session()
            query = session.query(Geocode).filter_by(location=params['location'],
                                                     provider=params['provider'],
                                                     method=params['method']).order_by(Geocode.id.desc()).first()
            return json.loads(query.json)
        else:
            return v.errors

if __name__ == '__main__':
    import geocoder
    """
    Simple use
    ==========
    """
    # User Variables
    location = '453 Booth Street, Ottawa'
    
    # Geocode Address
    g = geocoder.bing(location)

    # Create Cache Databse
    cache = Cache()

    # Insert into Database
    cache.insert(g.json)

    # Find results with a Query
    params = {
        'location': location,
        'provider': provider,
        'method': method,
    }
    print(cache.find(params))