#!/usr/bin/env python3


# returns mean of a list
def getmean(li):
  summe=0
  for item in li:
    summe+=float(item)
  return summe/len(li)


# returns standard deviation
# of a list
def getstddev(li):
  mean = getmean(li)
  squares = []
  for item in li:
    squares.append( (float(item) - mean)**2 )
  variance = getmean(squares)
  return variance**.5


infile=open('../CTA_-_Ridership_-__L__Station_Entries_-_Daily_Totals.csv','r').readlines()[1:]

# filter by weekend only
weekdays_only = [ line for line in infile if line.strip().split(',')[3] == 'W' ]
infile = weekdays_only

# get unique station ids
ids=set()
for line in infile:
  ids.add(line.split(',')[0])

# make a dict with 
# k,v: station_id, list_of_riders
datadict=dict()
for station in ids:
  datadict[station] = []

# populate the dict
for line in infile:
  line = line.strip().split(',')
  datadict[line[0]].append(float(line[-1]))


if __name__ == '__main__':
  # makes a dict of just stddev's
  stddevdict = dict()
  for key in datadict.keys():
    stddevdict[key] = getstddev(datadict[key])

 # makes a dict of just means
  meansdict = dict()
  for key in datadict.keys():
    meansdict[key] = getmean(datadict[key])


  stddevs = [ stddevdict[key] for key in stddevdict.keys() ]
  maxstddev = max(stddevs)

  for k in stddevdict.keys():
    if maxstddev == stddevdict[k]:
      print("The station with the highest weekday standard deviation in ridership is station {}".format(k))
      print("The standard deviation there in riders/day is {}".format(stddevdict[k]))
      print("The mean ridership there in riders/day is {}".format(meansdict[k]))

