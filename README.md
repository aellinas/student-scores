# Student-scores

## **Contents**
1) [Project](#Project)
2) [Aim](#Aim)
3) [Requirements](#Requirements)
4) [Instructions](#Instructions)
5) [Output](#Output)
6) [Maintenance](#Maintenance)


## **Project**
The algorithm is used to process a data source. It parses an external CSV file which contains data records of 60 students with their name and marks up to 100 for 7 subjects (Science, Maths, English, Software, Network, Business, Media). This data will be transformed into-
  1)	Plotted graphs for each subject
  2)	Statistical data including median, mean and standard deviation, whether the scores are reaching an expected result and the subjects with the best statistic
  3)	The subject and mark each student got the highest in

![image](https://user-images.githubusercontent.com/73494385/97221358-ac7f8800-17c4-11eb-89f3-d24751005060.png)


## **Aim**
The program can be used for-
* A visual or statistical representation of the difference in marks between students and subjects
* Viewing the trend in marks for the students and subjects
* Viewing the personal best for students (the subject and mark) 

## **Requirements**
conda >=4.9.1 || Python >=3.6 
- Refer to [requirements.txt](requirements.txt) for further requirements
- To install requirements use 'pip install -r requirements.txt' on the command line in the directory where the file has been downloaded

## **Instructions**
How to use the program-
1) Press the button 'Code' then 'Download ZIP' - this downloads all the files in the repository (requirements.txt,Student Results.csv, Student Scores.py) 
2) Extract the contents and install the requirements.txt file 
3) Run the code in either Anaconda Spyder/ Python
4) The console will display the rows, the subjects and marks in which the student got the highest in, statistical results, best values for the statistics
5) The graphical plot is generated (if used Anaconda Spyder- Plots subsection), saved to device as PNG file and two external text files produced

## **Output**
This is the output once the program is run- 
1)	7 subplots (1 for each subject) combined into a single graph- saved as 'graph.png' on device // 'Plots' subsection on Anaconda Spyder
2)	StatisticalResults text file- contains the median, mean and standard deviation of each subject and the maximum/minimum values of these
3)	StudentHighest text file- contains the student name, score and subject they got the highest in  
(These are saved to the file which contains the code)

## **Maintenance**
The graphs and statistical results are generated through parsing the CSV file therefore, data can be changed in the CSV file without changing the code. 
