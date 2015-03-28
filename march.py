import wolframalpha
import re

app_id = "WTAXGJ-JVYHAYP4EG"
client = wolframalpha.Client(app_id)

results = []
print "Year\t| Low\t| High\t  (averages)"
print "----------------------"
for weather_year in range(1970, 2015):
    res = client.query('temperature in columbus, oh in march {0}'.format(weather_year))
    p = re.compile('\(average low: (\d+) .F  \|  average high: (\d+) .F\).*\n\(March (\d+)\)')
    (low,high,year) = p.search(next(res.results).text).group(1,2,3)
    print "{0}\t| {1}\t| {2}".format(low,high,year)
