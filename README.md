# Power Grid Monitoring Tool (pgmt)
This is a project repository in Power System which is related to Power Grid Monitoring Tool.

# NTP based Frequency Meter

A power system is continually subjected to disturbances in the form of sudden load and generation changes or faults and tripping of equipment. The disturbances give rise to changes in the system frequency and/or oscillations in the relative frequency, which are observable at various locations in the grid. These are due to the electromechanical dynamics associated with synchronous machines which are interconnected by an ac network. The oscillation frequencies of these “swing modes” typically lie between 0.2-2 Hz. A centre-of-inertia mode which corresponds to overall (i.e. non-relative) frequency movement is observable throughout the grid wherever there is a load genaration imbalance.

### Student Name and Entry Number
* Anjali Yadav 
* Krishna Kumar 
* Parau Majhi 
* Sarita Meena 
* Swaran Pratap Singh 


### Main Componants of Project
* Frequency Measurement Device
* NTP protocol based Client Computer
* Server Computer

This folder contains file realted to last two part of our Term Project.

### Prequisites
* Software: Python ( Library: gspread, time, numpy), Matlab Simulink
* Hardware: Client Computer, Server Computer

### Implementation
1. Run Matlab Simulink model to get data in csv file
2. Keep data in Client Computer
3. To upload data from csv file to server run:
```python3 NTP_Client_to_Server.py```

### Discussion
This folder contains data sets of frequency, program, README.md file, Matlab Simulink Model, key to access and report with future plan. This folder conatins sensitive data, please avoid release at public space.
This project consist of software part and hardware part both. This folder contain material realted to software part and idea of hardware part in report. There are recoded data of frequency save here which we sent to severe, can be be anywhere using client computer on different part of power grid. This will make our life easy by accessing data from anywhere on Real-Time.



#### Thank You ####
