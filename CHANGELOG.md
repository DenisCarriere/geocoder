# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased] - 2017-09-.. - PR #288 - (coverage 73%)

### Added
- Pretty 'header' in README.md
- Changelog (this file)

### Changed
- refactored canadapost, moving key getter in keys.py
- refactored mapzen
- refactored ottawa
- refactored tomtom
- refactored yandex

### Fixed
- issue #207: tomtom, making use of new API


## [1.31] - 2017-09-6 - PR #286 - (coverage 73%)

### Added
- class attribute `_KEY_MANDATORY` [default to True]

### Changed
- refactored freegeoip, also changed url
- refactored geocodefarm
- refactored ipinfo
- refactored geolytica
- refactored here
- refactored tamu

### Fixed
- PR #287: Allow tamu requests without zip code
- Issue #215: Unofficial endpoint for FreeGeoIP causes intermittent errors


## [1.30] - 2017-08-29 - PR #281

### Changed
- refactored w3w
- refactored ipinfo
- refactored arcgis
- refactored osm

### Fixed
- Issue #154: Add ArcGIS Reverse geocoding
- Issue #279: Google client keys don't get picked up
- Issue #282: Accuracy is always None in 1.29.1 with Google Geocode
- Issue #260: updating what3words provider to use API v2


## [1.29] - 2017-08-22

### Added
- Created refactoring guide


## [1.28] - 2017-08-19

### Added
- Added Baidu reverse and Gaode providers (old style)


## [1.27] - 2017-08-14

### Added
- Adapted doc and test to proximity + BBox


## [1.26] - 2017-08-11
### Added
- `proximity` argument when geocoding with geonames, google, mapbox
- created BBox helper class
- Added Snap

### Changed
- refactored Google
- mapquest
- mapbox
- bing

## [1.25] - 2017-08-04

### Added
- Added documentation on Work In Progress (mutiple results)

### Fixed
- Build passing again


## [1.24] - 2017-08-02 (Coverage 54%)

### Added
- computing coverage in make file

### Changed
- started refactoring to add support for multiple results with geonames. 