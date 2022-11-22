

import os
import matplotlib.pyplot as plt
import csv
def graphVisual(address,Sus,Exp,Inf,Rem,grp1_dis,grp2_dis,grp3_dis,grp4_dis):
    S_array = []
    E_array = []
    I_array = []
    R_array = []
    day_array = []

    newgroup = []

    grouping = 3

    for groups in range(grouping):
        newgroup.append(0)
        newgroup[groups]=[]
    

    for day in range(50):
        try:
            with open(f'{address}\Day{day}.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                S_count = 0
                E_count = 0
                I_count = 0
                R_count = 0
                group0_count = 0
                group1_count = 0
                group2_count = 0

                for row in spamreader:
                    person = row[0]
                    S = row[1]
                    E = row[2]
                    I = row[3]
                    R = row[4]
                    G = row[5]
                    if (int(S) == 0):
                        S_count += 1
                    if (int(E) >= 1):
                        E_count += 1
                    if (int(I) >= 1):
                        I_count += 1
                    if (int(R) >= 1):
                        R_count += 1

                    
                    if int(G) == 0 and (int(I) >= 1):
                        group0_count += 1
                    if int(G) == 1 and (int(I) >= 1):
                        group1_count += 1
                    if int(G) == 2 and (int(I) >= 1):
                        group2_count += 1

                S_array.append(S_count)
                E_array.append(E_count)
                I_array.append(I_count)
                R_array.append(R_count)
                newgroup[0].append(group0_count)
                newgroup[1].append(group1_count)
                newgroup[2].append(group2_count)

                # group0.append(group0_count)
                # group1.append(group1_count)
                # group2.append(group2_count)
                day_array.append(day)
            csvfile.close()
        except:
            pass
    # plotting the points
    if Sus == 1:
        plt.plot(day_array, S_array, label = "Susceptible")
    if Exp == 1:
        plt.plot(day_array, E_array, label = "Exposed")
    if Inf == 1:
        plt.plot(day_array, I_array, label = "Infected")
    if Rem == 1:
        plt.plot(day_array, R_array, label = "Removed")
    if grp1_dis == 1:
        plt.plot(day_array, newgroup[0], label = "group 1")
    if grp2_dis == 1:
        plt.plot(day_array, newgroup[1], label = "group 2")
    if grp3_dis == 1:
        plt.plot(day_array, newgroup[2], label = "group 3")
    if grp4_dis == 1:
        plt.plot(day_array, newgroup[3], label = "group 4")  

    print(grp3_dis)
        

    # naming the x axis
    plt.xlabel('Days')
    # naming the y axis
    plt.ylabel('Number of people')
    
    # giving a title to my graph
    plt.title('Infection Tracker')
    plt.legend()
    # function to show the plot
    plt.show()


if __name__ == "__main__":
    working_directory = os.getcwd()
    graphVisual(working_directory)