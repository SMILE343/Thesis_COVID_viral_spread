import csv
import os

def multiHop(address):
    entire_tracker = []
    with open(f'{address}\Tracker.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            indentified_infected = row[0]
            contacted_person = row[1]
            ctcstart = row[2]
            ctcend = row[3]
            duration = row[4]
            locationNumber = row[5]
            day = row[6]
            indentified_infected_I = row[7]
            contacted_person_I = row[8]
            entire_tracker.append(row)
    csvfile.close()
    return entire_tracker

# add person to queue
# while queue:
    # pop person
    # check against tracker
    # only accept those before the day selected
    # add those that are in direct contact across all days if they arent already in the queue

def breadthFirst(entire_tracker,person_to_track,current_day,incubation_period):
    queue = []
    visited = []
    infected_list = []
    queue.append([person_to_track,current_day,24,0])
    curr_count = 0
    while queue and curr_count < 3:
        # get the first path from the queue
        # print(visited)
        # print(queue)
        # print(infected_list)
        current_person = queue.pop(0)
        visited.append(current_person)
        curr_count = int(current_person[3]) + 1
        # get the last node from the path
        for entry in entire_tracker:
            # person match and before day
            if int(entry[0]) == int(current_person[0]) and int(entry[6]) < int(current_day):
                # check if they are infected
                if int(entry[8]) > incubation_period:
                    infected_list.append([entry[1],entry[6],entry[2],curr_count])
                    print(f"{current_person}, Infected person:{entry[1]}, Day: {entry[6]}, time: {entry[2]}:00, {curr_count}")
                else:
                    marker = 0
                    for nodes in visited:
                        if [entry[1],entry[6],entry[2]] == [nodes[0],nodes[1],nodes[2]]:
                            marker = 1
                    for nodes2 in queue:
                        if [entry[1],entry[6],entry[2]] == [nodes2[0],nodes2[1],nodes2[2]]:
                            marker = 1
                    if marker == 0:
                        queue.append([entry[1],entry[6],entry[2],curr_count])
            # if same day make sure before time
            if int(entry[0]) == int(current_person[0]) and int(entry[6]) == int(current_day) and int(entry[2]) < int(current_person[2]):
                # check if they are infected
                if int(entry[8]) > incubation_period:
                    infected_list.append([entry[1],entry[6],entry[2],curr_count])
                    print(f"{current_person}, Infected person:{entry[1]}, Day: {entry[6]}, time: {entry[2]}:00, {curr_count}")
                else:
                    marker = 0
                    for nodes in visited:
                        if [entry[1],entry[6],entry[2]] == [nodes[0],nodes[1],nodes[2]]:
                            marker = 1
                    for nodes2 in queue:
                        if [entry[1],entry[6],entry[2]] == [nodes2[0],nodes2[1],nodes2[2]]:
                            marker = 1
                    if marker == 0:
                        queue.append([entry[1],entry[6],entry[2],curr_count])
        if infected_list:
            break
    return infected_list

if __name__ == "__main__":
    person_to_track = int(input('Enter individual to track:'))
    day_to_start = int(input('Enter day:'))

    working_directory = os.getcwd()
    entire_tracker = multiHop(working_directory)
    current_day = day_to_start
    breadthFirst(entire_tracker,person_to_track,current_day)

