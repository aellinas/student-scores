# Student-scores


## **Project**
The algorithm is used to process a data source. It parses an external CSV file which contains data records of 60 students with their name and marks up to 100 for 7 subjects (Science, Maths, English, Software, Network, Business, Media). This data will be transformed into-
  1)	Plotted graphs for each subject
  2)	Statistical data including median, mean and standard deviation, whether the scores are reaching an expected result and the subjects with the best statistic
  3)	The subject and mark each student got the highest in



![image](https://user-images.githubusercontent.com/73494385/97219375-d5524e00-17c1-11eb-9639-1ffd55ad2359.png)

## **Reason**
The program can be used for-
* A visual or statistical representation of the difference in marks between students and subjects
* Viewing the trend in marks for the students and subjects
* Viewing the personal best for students (the subject and mark) 


## **Output**
This is the intended output once the program is run- 
1)	7 subplots (1 for each subject) combined into a single graph
2)	StatisticalResults text file- contains the median, mean and standard deviation of each subject and the maximum/minimum values of these
3)	StudentHighest text file- contains the student name, score and subject they got the highest in  


## **Maintenance**
The graphs and statistical results are generated through parsing the CSV file therefore, data can be changed in the CSV file without changing the code. 
