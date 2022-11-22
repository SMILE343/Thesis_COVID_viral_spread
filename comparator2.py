import csv


# Effects should be : Change the status of suseptible people to infected in the day file
# open the day file
# Check who is infected
# Run the comparison to tell you who is now infected
# make changes to the day file

# run end of day file

# run data_gen with that number of people
 
arraytracker = []
locationNumber= 0
identifiedPerson = 42
day = 0

S = 0
E = 0
I = 0
R = 0

with open(f'Day{day}.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        person = row[0]
        S = row[1]
        E = row[2]
        I = row[3]
        R = row[4]
        if I > 2:
            arraytracker.append([person,S,E,I,R])
csvfile.close()


try:
    with open(f'Day{day}location{locationNumber}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            person = row[0]
            entrytime = row[1]
            exittime = row[2]
            arraytracker.append([person,entrytime,exittime])
    csvfile.close()
except:
    pass

file2 = open(f"{identifiedPerson}_{locationNumber}.csv","w")

# input person number

# match number and get the timings of that person

# run through the 3 comparisons 

# write out to file if they are contacted and the hours of overlap


identifiedArray = []
print(arraytracker)
for x in arraytracker:
    if x[0] == str(identifiedPerson):
        identifiedArray.append(x)
    print(x)
    print(x[0])
        
for y in identifiedArray:
    I1 = int(y[1])
    I2 = int(y[2])

    for z in arraytracker:
        J1 = int(z[1])
        J2 = int(z[2])
        if(z[0]==identifiedPerson):
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
            print("CONTACT!")
            print(y)
            print(z)
            csvwriter = csv.writer(file2)
            info = identifiedPerson,z[0],ctcstart,ctcend,locationNumber
            csvwriter.writerow(info)
