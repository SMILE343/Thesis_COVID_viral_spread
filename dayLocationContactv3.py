
import csv
import os


def singleHopv2(address,peopleNum,numLoc):
    csvwriter = open(f'{address}\Tracker.csv', 'w', encoding='UTF8', newline='')
    new_infections = []
    
    for day in range(50):
        dayInfection = []
        try:
            with open(f'{address}\Day{day}.csv', newline='') as csvfile:
                dayreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in dayreader:
                    person_id = row[0]
                    S = row[1]
                    E = row[2]
                    I = row[3]
                    R = row[4]
                    dayInfection.append([person_id,I])
            csvfile.close()
        except:
            pass
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
            for indentified_infected in range(peopleNum):
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
                        if(contact==1) and indentified_infected!=int(z[0]):
                            for x in dayInfection:
                                if int(x[0]) == int(indentified_infected):
                                    indentified_infected_I = x[1]
                                if int(x[0]) == int(z[0]):
                                    z_infected = x[1]
                            duration = ctcend - ctcstart
                            info = indentified_infected,z[0],ctcstart,ctcend,duration,locationNumber,day, indentified_infected_I, z_infected
                            writing = csv.writer(csvwriter)
                            writing.writerow(info)
                            new_infections.append(z[0])

if __name__ == "__main__":
    working_directory = os.getcwd()
    singleHopv2(working_directory)