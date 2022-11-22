import csv
from math import floor
import os
from random import random, randrange
from random import randint
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


# Start day file
def startday(day,address,grouping,peopleNum):
    f = open(f'{address}\Day{day}.csv', 'w', encoding='UTF8', newline='')
    currentnum = 0
    for x in range(peopleNum):
        S = 0
        E = 0
        I = 0
        R = 0
        G = randint(0,grouping-1)
        if x==3:
            S = 1
            E = 3
            I = 3
            R = 0
        writer = csv.writer(f)
        personInfo = currentnum,S,E,I,R,G
        writer.writerow(personInfo)
        currentnum+=1
    f.close()


# DayLocation file generation
def dayLocationGen(numloc, day, address):
    inCommunity = []
    group_status = []
    grouping = 3

    with open(f'{address}\Day{day}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            person = row[0]
            S = row[1]
            E = row[2]
            I = row[3]
            R = row[4]
            G = row[5]
            if R == str(0):
                inCommunity.append([person,G])

    csvfile.close()
    locationArrayCounts = [0] *  (numloc+1)
    # print(locationArrayCounts)
    for x in inCommunity:
        pair1 = 9
        pair2 = 21

        # going to different suburbs
        entry_attempts = 0
        while entry_attempts < 3:
            if grouping != 0:
                if randrange(0,100) <= 97:
                    withinloc=randrange(0,numloc)
                    while (withinloc % grouping != int(x[1])):
                        if (withinloc == numloc):
                            withinloc = 0
                        withinloc += 1
                else:
                    withinloc = randrange(0,numloc)
                if locationArrayCounts[withinloc] <=50:
                    locationArrayCounts[withinloc] += 1
                    entry_attempts = 5
                else:
                    entry_attempts += 1
        if entry_attempts == 5:
            t1,t2 = timeRange(pair1,pair2)

            writetolocation = open(f'{address}\Day{day}location{withinloc}.csv', 'a', encoding='UTF8', newline='')
            locationInfo = x[0], t1, t2
            writer2 = csv.writer(writetolocation)
            writer2.writerow(locationInfo)


# Compare and generate day end file
def dayEnd(day,address,infection_chance,incubation_period,numLoc):
    infected = []
    with open(f'{address}\Day{day}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            person = row[0]
            S = row[1]
            E = row[2]
            I = row[3]
            R = row[4]
            G = row[5]
            if int(I) > incubation_period:
                infected.append(person)
    csvfile.close()


    new_infections = []
    for indentified_infected in infected:
        # print(indentified_infected)
        for locationNumber in range(numLoc):
            arraytracker=[]
            try:
                with open(f'{address}\Day{day}location{locationNumber}.csv', newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    for row in spamreader:
                        person = row[0]
                        entrytime = row[1]
                        exittime = row[2]
                        arraytracker.append([person,entrytime,exittime])
                csvfile.close()
            except:
                pass
            # file2 = open(f"{indentified_infected}_{locationNumber}.csv","w")
            identifiedArray = []
            for x in arraytracker:
                if x[0] == str(indentified_infected):
                    identifiedArray.append(x)
                    
            for y in identifiedArray:
                I1 = int(y[1])
                I2 = int(y[2])

                for z in arraytracker:
                    J1 = int(z[1])
                    J2 = int(z[2])
                    if(z[0]==x):
                        continue
                    contact = 0
                    ctcstart = 0
                    ctcend = 0
                    if (I1 <= J1):
                        if(J1 < I2):
                            contact = 1
                            ctcstart = J1
                            if(I2<J2):
                                ctcend = I2
                            else:   
                                ctcend = J2
                    else:
                        if(I1 < J2):
                            contact = 1
                            ctcstart = I1
                            if(I2<J2):
                                ctcend = I2
                            else:
                                ctcend = J2
                    if(contact==1):
                        # csvwriter = csv.writer(file2)
                        # info = indentified_infected,z[0],ctcstart,ctcend,locationNumber
                        # csvwriter.writerow(info)
                        new_infections.append(z[0])
    # print(new_infections)
    with open(f'{address}\Day{day}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #new day
        newday = day + 1
        createNewDay = open(f'{address}\Day{newday}.csv', 'w', encoding='UTF8', newline='')
        #port over values
        for row in spamreader:
            person = row[0]
            S = row[1]
            E = row[2]
            I = row[3]
            R = row[4]
            G = row[5]
            # increment infection day
            if int(I) >= 1:
                E = int(E) + 1
                I = int(I) + 1
            elif int(E) >= 1:
                E = int(E) + 1
            # remove if above 7 days of infection
            if int(I) >= 6+incubation_period:
                R = 1

            # new infections stores everyone in contact
            # only changes if the person is not already infected

            if person in new_infections:
                if int(I) == 0:
                    if randint(0,100) < infection_chance:
                        S = 1
                        if int(E) == 0:
                            E = 1
                        I = 1
                        R = 0
                    else:
                        S = 0
                        E = 1
                        I = 0
                        R = 0
            
            personInfo = person, S, E, I, R, G
            newDayWriter = csv.writer(createNewDay)
            newDayWriter.writerow(personInfo)
    csvfile.close()




def mainGen(address,infection_chance,incubation_period,grouping,peopleNum,daysNum,numLoc):
    day = 0
    #start day
    startday(day, address, grouping,peopleNum)
    #cascade
    for day in range(daysNum):
        dayLocationGen(numLoc,day,address)
        dayEnd(day,address,infection_chance, incubation_period,numLoc)



if __name__ == "__main__":
    working_directory = os.getcwd()
    mainGen(working_directory)