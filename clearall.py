import os

def clearAllFiles(file_path,days,numLoc):
    # if os.path.isfile(file_path):
    #       os.remove(file_path)
    for day in range(days):
        if os.path.isfile(f"{file_path}\Day{day}.csv"):
            os.remove(f"{file_path}\Day{day}.csv")
        for withinloc in range(numLoc):
            if os.path.isfile(f"{file_path}\Day{day}location{withinloc}.csv"):
                os.remove(f"{file_path}\Day{day}location{withinloc}.csv")

if __name__ == "__main__":
    working_directory = os.getcwd()
    clearAllFiles(working_directory)