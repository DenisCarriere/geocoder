.. _wip_guide:

Refactoring guide to support multiple results
=============================================

It basically comes to split the existing classes into two new ones

* `OneResult` handles all the properties of one given result from the provider
* `MultipleResultsQuery` handles the query to the provider, and provides the interface to iterate through the results::

    # from geocoder.base import Base
    #
    # class Baidu(Base):
    #     provider = 'mapquest'
    #     method = 'geocode'
    #
    #     def __init__(self, location, **kwargs):
    #        ...
    #
    #     @property
    #     def lat(self):
    #         return self.parse['location'].get('lat')
    #
    # becomes

    from geocoder.base import OneResult, MultipleResultsQuery

    class BaiduResult(OneResult):

        @property
        def lat(self):
            return self.raw['location'].get('lat')


    class BaiduQuery(MultipleResultsQuery):
        provider = 'mapquest'
        method = 'geocode'

        ...


Changes for `OneResult`
-----------------------

It is important to keep in mind that `OneResult` handles all the properties for **one** given result from the provider. The modifications you will need to do here are the ones that impact **one** result only, not the overall process of the query.

* The JSON returned from the provider moved from `self.parse` to `self.raw`::

    class MapquestResult(OneResult):

        @property
        def lat(self):
            return self.raw['latLng'].get('lat')

        @property
        def lng(self):
            return self.raw['latLng'].get('lng')

    ...

* The constructor `__init__` takes the `json_content` corresponding to this result (and only this one). You might change it before storing it in self.raw::

    class GoogleResult(OneResult):

        def __init__(self, json_content):
            # do some transformation
            ...
            # proceed with super.__init__
            super(GoogleResult, self).__init__(json_content)

or, with Mapbox::

    class MapboxResult(OneResult):

        def __init__(self, json_content):
            super(MapboxResult, self).__init__(json_content)

            for item in json_content.get('context', []):
                if '.' in item['id']:
                    # attribute=country & text=Canada
                    attribute = item['id'].split('.')[0]
                    self.raw[attribute] = item['text']

* the `ok` property should be overridden on the result level when necessary (which is usually the case when you want to reverse)::

    class GoogleReverseResult(GoogleResult):

        @property
        def ok(self):
            return bool(self.address)


Key changes for the Query manager
---------------------------------

Here, it is important to keep in mind that `MultipleResultsQuery` handle the overall process of the query, and stores **all** the results. The responsibilities here are to

#. setup the context correctly
#. make the query with appropriate headers, params
#. parse the response from the provider and create results appropriately

Let's detail those three steps

* (**Setup**) The first modification will be to provide the *metadata* needed for the query, namely:
    * what class to use for the result
    * what url to query
    * which key to use 

::

    class MapquestQuery(MultipleResultsQuery):

        _URL = 'http://www.mapquestapi.com/geocoding/v1/address'
        _RESULT_CLASS = MapquestResult
        _KEY = mapquest_key
        _KEY_MANDATORY = True

    Because the default implementation expects an API Key, you will need to set _KEY_MANDATORY to False if no API Key is required

* (**Query**) In order to make the query: the initialization of the params & headers is not done neither in the constructor anymore but in the appropriated hooks. As you can see, `location` and `provider_key` are passed through::

    def _build_headers(self, provider_key, **kwargs):
        return {
            'referer': 'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'key': provider_key,
            'location': location,
            'maxResults': kwargs.get("maxRows", 1),
            'outFormat': 'json',
        }

* (**Query**) In some cases (e.g reversing), you need more preparation before you can build your headers / params. You would use `_before_initialize` for this, which is called before connecting to the provider. A typical use-case is where `_URL` is dynamic and needs to be extended at runtime::

    class MapboxReverse(MapboxQuery):

        def _before_initialize(self, location, **kwargs):
            self.location = str(Location(location))
            lat, lng = Location(location).latlng
            self.url = self.url.format(lng=lng, lat=lat)


* (**Parsing**) The treatment of the `json_response`, which probably contains multiple results, is not done in the constructor anymore, it is done through the following hooks::

    def _catch_errors(self, json_response):
        if b'The AppKey submitted with this request is invalid' in json_response:
            raise ValueError('MapQuest API Key invalid')

    def _adapt_results(self, json_response):
        results = json_response.get('results', [])
        if results:
            return results[0]['locations']
        return []

* (**Parsing**) In the cases where you are interested in some fields in the `json_response`, additionally to the results, you might want to override `_parse_results`. In which case you should also declare the new attribute in your child class. There is one example with GooglePlaces, where the `next_page_token` interests us::

    class PlacesQuery(MultipleResultsQuery):

        def __init__(self, location, **kwargs):
            super(PlacesQuery, self).__init__(location, **kwargs)
            self.next_page_token = None

        ...

        def _parse_results(self, json_response):
            super(PlacesQuery, self)._parse_results(json_response)

            # store page token if any
            self.next_page_token = json_response.get('next_page_token')


More examples
-------------

Please have a look on the providers already "migrated", like 

* geonames
* bing
* mapbox
* mapquest

The full list is available on the `README <https://github.com/DenisCarriere/geocoder/blob/master/README.md>`_ 
