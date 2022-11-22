import csv
import os

def funcSingleHop(ID_NUM, address):
    entire_tracker = []
    try:
        with open(f'{address}\Tracker.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                indentified_infected = row[0]
                contacted_person = int(row[1])
                ctcstart = row[2]
                ctcend = row[3]
                duration = row[4]
                locationNumber = row[5]
                day = row[6]
                indentified_infected_I = row[7]
                contacted_person_I = row[8]
                entire_tracker.append(row)
        csvfile.close()
        save_list = []
        full_list = []
        for x in entire_tracker:
            if int(ID_NUM) == int(x[0]):
                if x[1] not in save_list:
                    save_list.append(int(x[1]))
                    full_list.append(x)
        Sort(full_list)
        return(full_list)
    except:
        pass

    

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: int(x[1]))
    return sub_li


if __name__ == "__main__":
    working_directory = os.getcwd()
    x = funcSingleHop(1,working_directory)
    print(x)