# Command Line Interface

The command line tool allows you to geocode one or many strings, either
passed as an argument, passed via stdin, or contained in a referenced file.

```bash
$ geocode "Ottawa"
{
  "accuracy": "Rooftop",
  "quality": "PopulatedPlace",
  "lng": -75.68800354003906,
  "status": "OK",
  "locality": "Ottawa",
  "country": "Canada",
  "provider": "bing",
  "state": "ON",
  "location": "Ottawa",
  "address": "Ottawa, ON",
  "lat": 45.389198303222656
}
```

Now, suppose you have a file with two lines, which you want to geocode.

```bash
$ geocode "textfile.txt"
{"status": "OK", "locality": "Ottawa", ...}
{"status": "OK", "locality": "Boston", ...}
```

The output is, by default, sent to stdout, so it can be conveniently parsed
by JSON parsing tools like `jq`.

```bash
$ geocode "textfile.txt" | jq [.lat,.lng,.country] -c
[45.389198303222656,-75.68800354003906,"Canada"]
[42.35866165161133,-71.0567398071289,"United States"]
```

Parsing a batch geocode to CSV can also be done with `jq`. Build your headers first then run the `geocode` application.

```bash
$ echo 'lat,lng,locality' > test.csv
$ geocode cities.txt | jq [.lat,.lng,.locality] -c | jq -r '@csv' >> test.csv
```
