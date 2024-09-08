## NTP based Frequency Meter ##

# Library require to control Google Sheet at Server
import gspread

# NTP
import time

# Data Management
import numpy as np

# Getting access to Google Sheet using Key which is present in *.json file
gc = gspread.service_account(filename = 'write_your_service_account.json')
# Opening of sheet
wks = gc.open("frequencyMeter").sheet1

# File name of Data Set which contains time and frequency
fileName = "dataSet.csv"

# csv file reader
def csv_reader(fileName):
    # open an existing file for reading -
    data = np.loadtxt(fileName, delimiter=",", dtype=float)
    return data, len(data)


# Reading Data Set
freqData, dataSize = csv_reader(fileName)

start = time.time()
print("Data is ready to send.")
for i in range(100):
    dataToSend = []
    row = 2
    col = 'A'
    location = str(col)+str(row)
    dataToSend = list(freqData[(i*1000):(i+1)*1000, 1])
    for i in range(1000):
        dataToSend[i] = [i+1, float(np.round(dataToSend[i],3))]
    # After this line run, there will be a warning message will be shown, just ignore it
    wks.update(values = dataToSend, range_name = location)
    # It takes 0.5 - 0.7 sec time to upload the data

end = time.time()
print("Time required: ", end-start)

print("Data Send To Server Computer.")

