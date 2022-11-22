
from asyncio.windows_events import NULL
import csv
from random import randrange
from random import randint
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def randdates(start, end):
    """
    This function will return a random datetime range between two datetime 
    objects.
    """
    firstdate = random_date(start, end)
    secdate = random_date(start, end)

    if firstdate < secdate:
        print(firstdate, secdate)
    else:
        print(secdate, firstdate)

def randTime(t1,t2):
    """
    This function will return a random datetime range between two datetime 
    objects.
    """
    return randint(t1,t2)

def timeRange(t1,t2):
    """
    This function will return a random int range between two int 
    objects.
    """
    x1=randint(t1,t2)
    x2=randint(t1,t2)
    if(x2<x1):
        x3=x1
        x1=x2
        x2=x3
    return x1,x2

def coreData():
    f = open('StartingSample.txt','r')
    f2 = open('StartingSampleLocations.txt','r')
    writetofile = open("demofile2.txt", "w")

    locationarray = []

    f2 = open('StartingSampleLocations.txt','r')
    with f2 as openfileobject:
        count = 0
        for file2line in openfileobject:
            contents = file2line.split(' ')
            numberOfLocationType = int(contents[1])
            locationarray.append(numberOfLocationType)
            count+=1
            if not file2line:
                break
    # ALTER NUMBERS HERE
    maxnum=40
    maxhours=24

    trackerarray = [[[0 for hours in range(maxhours)] for trackers in range(locationarray[x])] for x in range(count)]

    selectedInfection = 1

    S = 0
    E = 0
    I = 0
    R = 0

    day = 0

    currentnum=0

    with open('StartingSample.txt','r') as openfileobject:
        for x in openfileobject:
            y=x.split(',')
            length = len(y)
            unit_no = y[0]
            num_people = int(y[1])
            for thepeople in range(num_people):
                S = 0
                E = 0
                I = 0
                R = 0

                if(currentnum == selectedInfection):
                    S = 0
                    E = 3
                    I = 3
                    R = 0                    
                f = open(f'Day{day}.csv', 'a', encoding='UTF8', newline='')
                writer = csv.writer(f)
                personInfo = currentnum,S,E,I,R
                writer.writerow(personInfo)
                currentnum+=1
                
                for z in range (2,length):
                    edge = y[z].split('-')
                    edge[-1] = edge[-1].strip()
                    pair1 = int(edge[0])
                    pair2 = int(edge[1])
                    sendto=randrange(0,count)
                    for times in range(3):
                        # within the location type
                        withinloc=randrange(0,locationarray[sendto])
                        flag = 0
                        for match in range(pair1,pair2+1):
                            if(trackerarray[sendto][withinloc][match]==maxnum):
                                flag = 1
                        if (flag == 0):
                            for match in range(pair1,pair2+1):
                                trackerarray[sendto][withinloc][match]+=1
                            break
                    
                    t1,t2 = timeRange(pair1,pair2)


                    writetolocation = open(f'Day{day}location{sendto}.csv', 'a', encoding='UTF8', newline='')
                    locationInfo = currentnum, t1, t2
                    writer2 = csv.writer(writetolocation)
                    writer2.writerow(locationInfo)
                    

    f.close()
    writetofile.close()

if __name__ == "__main__":
    coreData()