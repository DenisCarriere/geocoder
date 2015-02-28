# Confidence Score

Based from [OpenCage API](http://geocoder.opencagedata.com/api.html#quickstart)

## Geocoding Confidence

The OpenCage Geocoder will always attempt to find a match for as many parts of a query as it can, but this isn't always possible to do. Where a partial match is made, for example a street name can be matched but a specific house number on that street cannot be matched, the geocoder will still return a result but the granularity of the match will not be as high as if the house number was matched.

The confidence that the geocoder has in a match returned in the confidence field. This contains a value between 0 and 10, where 0 reflects no confidence and 10 reflects high confidence.

Confidence is calculated by measuring the distance in kilometres between the South West and North East corners of each results bounding box; a smaller distance represents a high confidence while a large distance represents a lower confidence.

Please note, you can supply the optional min_confidence parameter (see below).


|Score |       Description          |
|:----:|:---------------------------|
| 10   | less than 0.25 km distance |
| 9    | less than 0.5 km distance  |
| 8    | less than 1 km distance    |
| 7    | less than 5 km distance    |
| 6    | less than 7.5 km distance  |
| 5    | less than 10 km distance   |
| 4    | less than 15 km distance   |
| 3    | less than 20 km distance   |
| 2    | less than 25 km distance   |
| 1    | 25 km or greater distance  |
| 0    | unable to determine a bounding box|