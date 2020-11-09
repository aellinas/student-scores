#Algorithm to process a data source

#Import the libraries necessary for the algorithm
import matplotlib.pyplot as plt
import csv
import numpy

#Define the columns in the CSV file
name, science, maths, english, software, network, business, media =[],[],[],[],[],[],[],[]

#Function to welcome and ask the user for their name and validate it
def welcome():
    #A welcome message to the program
    print("This is a program that analyses the results received by students")

    #Asks for  users name and validates it- if alphabetical, continues with program. If not, it will keep looping until a valid name is entered
    #Will keep looping until the expressions evaluate to true
    while True:
        #Asks the user for their name
        userName=input("What is your name?")
        #If the name is alphabetical
        if userName.isalpha():
            #Displays a welcome message, capitalizes the first letter of their name
            print("Welcome", userName.capitalize(),"\n")
            break
        #If the name is not alphabetical
        else:
            #Displays it is an invalid name, user will try again
            print("Invalid name, please try again")

            
#Function for the best subject and score for students
#Function to create the graph that will be plot using the CSV file
def maxAndGraph():
    #Opens the CSV file
    with open("Student Results.csv","r") as csvfile:
        #Reads the file as a CSV file
        global plots
        plots=csv.reader(csvfile, delimiter=',')
        
        #This skips the first row in the CSV file
        global subjectNames
        subjectNames=next(plots)
        print(subjectNames)
        #Parses the file so looks at each row in the file
        global row
        for row in plots:
            global nameRow
            #Assign the name of the row with the index of 
            nameRow=row[0]
            scienceRow=row[1]
            mathsRow=row[2]
            englishRow=row[3]
            softwareRow=row[4]
            networkRow=row[5]
            businessRow=row[6]
            mediaRow=row[7]

            #Create an empty list to append the values to
            allStudentHighest=[]
            global subjectList
            #Create a list with all the subjects and data
            subjectList=[ scienceRow, mathsRow, englishRow, softwareRow, networkRow, businessRow, mediaRow]
            
            #Function to find the subject and mark each student got the highest
            #Finds the maximum value from all of the subjects
            studentMaxval= max([scienceRow, mathsRow,englishRow, softwareRow, networkRow,businessRow,mediaRow], key=float)
            
            #Finds the index of maximum value generated
            studentIndexval=subjectList.index(studentMaxval)
            newStudentindexval=studentIndexval+1

            #Concatenates the value to a string and finds the subject name from the index the value was at
            maximumStudent=nameRow+" maximum score is "+studentMaxval+ " for subject "+ subjectNames[newStudentindexval]
            print(maximumStudent)
            #Appends the string to a list
            allStudentHighest.append(maximumStudent)
            
            #Converts the list to a string
            allStudentHighestL=''.join(allStudentHighest)

            #Opens a file to place the strings 
            files=open("StudentHighest.txt","a")
            #Writes to the file the string with each student and the subject they got the highest in
            files.write("%s \n" %allStudentHighestL)
            files.close()
            
            #Converting the rows/ values from the CSV file to float from strings
            row[1]=float(row[1])
            row[2]=float(row[2])
            row[3]=float(row[3])
            row[4]=float(row[4])
            row[5]=float(row[5])
            row[6]=float(row[6])
            row[7]=float(row[7])
            
            #Beginning of graph code
            #Creation of the 4 subplots
            fig,(ax1,ax2,ax3,ax4, ax5, ax6, ax7)=plt.subplots(7,sharex=True, sharey=True)
        
            #Graph 1 will plot the name and science results
            ax1.plot(name, science)
            #Graph 2 will plot the name and maths results
            ax2.plot(name,maths)
            #Graph 3 will plot the name and english results
            ax3.plot(name,english)
            #Graph 4 will plot the name and software results
            ax4.plot(name,software)
            #Graph 5 will plot the name and network results
            ax5.plot(name,network)
            #Graph 6 will plot the name and business results
            ax6.plot(name,business)
            #Graph 7 will plot the name and media results
            ax7.plot(name,media)
        
            #Appends the values onto the graph
            name.append(row[0])
            science.append(row[1])
            maths.append(row[2])
            english.append(row[3])
            software.append(row[4])
            network.append(row[5])
            business.append(row[6])
            media.append(row[7])
        
            #Assigning the x-axis and y-axis labels
            ax7.set(xlabel="names")
            ax4.set(ylabel="scores")
            
            #Rotates the x-axis by 90 degrees to make it clear 
            plt.xticks(rotation=90)
            
            plt.rcParams.update({'figure.max_open_warning':0})
            #Adds one to the length of the list for names so all CSV data is appended to graph
            allNames=numpy.arange(len(name)+1)
            #Sets the x-axis to add the names at the right positions
            plt.xticks(allNames, name)
        
            #Titles for each graph 
            ax1.set_title("Science results", fontsize="6")
            ax2.set_title("Maths results", fontsize="6")
            ax3.set_title("English results", fontsize="6")
            ax4.set_title("Software results", fontsize="6")
            ax5.set_title("Network results", fontsize="6")
            ax6.set_title("Business results", fontsize="6")
            ax7.set_title("Media results", fontsize="6")
        
            #Changes the size of the subplots so they fit into the area and avoid overlapping 
            fig.tight_layout(pad=0.2)
            
            #Sets the title for all graphs
            fig.suptitle("GRAPHS OF RESULTS FOR EACH TERM",x=0.5, y=1.05)
            
            #Saves the figure
            fig.savefig("graph.png")
        
#Function which does statistical calculations- median
def median():
    print("\n Statistical results: \n")
    print("\n Median: \n")
    
    #Calculates the median of each subject and assigns the value to a variable
    scienceMedian=numpy.median(science)
    mathsMedian=numpy.median(maths)
    englishMedian=numpy.median(english)
    softwareMedian=numpy.median(software)
    networkMedian=numpy.median(network)
    businessMedian=numpy.median(business)
    mediaMedian=numpy.median(media)
    
    #Sets a global variable to be used in the whole program
    global medianArray
    #Creation of a median array with all the results of the scores from the subjects
    medianArray=numpy.array([scienceMedian, mathsMedian, englishMedian, softwareMedian, networkMedian, businessMedian, mediaMedian])
    #Output of the median value for each subject
    print("median of science: ",scienceMedian)    
    print("median of maths: ",mathsMedian)
    print("median of english: ",englishMedian)
    print("median of software: ",softwareMedian)
    print("median of network: ",networkMedian)    
    print("median of business: ",businessMedian)
    print("median of media: ",mediaMedian)
    
    #Checks how many subjects got over a certain mark for median statistics
    #Assigns a counter variable 0
    count=0
    #Iterates through each score in the array with median results
    for score in medianArray:
        #If the score is less than 50 (expected result)
        if score<50:
            #Adds one to the count as condition is met
            count=count+1
    if count>0:
        #Displays the count of how many subjects had less than 50
        print(count, "subjects had lower than 50, improvement needed")
    else:
        #If the count is not greater than 0, displays the 0 count 
        print(count, "subjects had lower than 50, no improvement needed")


#Function which does statistical calculations- mean
def mean():
    print("\n Mean: \n")
    
    #Calculates the mean of each subject and assigns the value to a variable
    scienceMean=numpy.mean(science)
    mathsMean=numpy.mean(maths)
    englishMean=numpy.mean(english)
    softwareMean=numpy.mean(software)
    networkMean=numpy.mean(network)
    businessMean=numpy.mean(business)
    mediaMean=numpy.mean(media)
    
    global meanArray
    #Creation of a mean array with all the results of the scores from the subjects
    meanArray=numpy.array([scienceMean, mathsMean, englishMean, softwareMean, networkMean, businessMean, mediaMean])
    #Sends the mean array as an argument to the rounding function to round the values to a decimal place
    rounding(meanArray)
    
    #Output of the mean value for each subject
    print("mean of science: ", roundingValue[0])
    print("mean of maths: ", roundingValue[1])
    print("mean of english: ", roundingValue[2])
    print("mean of software: ", roundingValue[3])
    print("mean of network: ", roundingValue[4])
    print("mean of business: ", roundingValue[5])
    print("mean of media: ", roundingValue[6])  
    
    #Checks how many subjects got over a certain mark for mean statistics
    #Assigns a counter variable 0
    count=0
    #Iterates through each score in the array with mean results
    for score in meanArray:
        #If the score is less than 50 (expected result)
        if score<50:
            #Adds one to the count as condition is met
            count=count+1
    if count>0:
        #Displays the count of how many subjects had less than 50
        print(count, "subjects had lower than 50, improvement needed")
    else:
        #If the count is not greater than 0, displays the 0 count 
        print(count, "subjects had lower than 50, no improvement needed")

    
#Function which does statistical calculations- standard deviation
def standardDeviation():
    print("\n Standard Deviation: \n")
    
    #Calculates the standard deviation of each subject and assigns the value to a variable
    scienceStDeviation=numpy.std(science)
    mathsStDeviation=numpy.std(maths)
    englishStDeviation=numpy.std(english)
    softwareStDeviation=numpy.std(software)
    networkStDeviation=numpy.std(network)
    businessStDeviation=numpy.std(business)
    mediaStDeviation=numpy.std(media)
    
    global stDeviationArray
    #Creation of a standard deviation array with all the results of the scores from the subjects
    stDeviationArray=numpy.array([scienceStDeviation, mathsStDeviation, englishStDeviation, softwareStDeviation,networkStDeviation, businessStDeviation, mediaStDeviation])
    #Sends the standard deviation array as an argument to the rounding function to round the values to a decimal place
    rounding(stDeviationArray)

    #Output of the standard deviation value for each subject
    print("standard deviation of science: ", roundingValue[0])
    print("standard deviation of maths: ", roundingValue[1])
    print("standard deviation of english: ", roundingValue[2])
    print("standard deviation of software: ", roundingValue[3])
    print("standard deviation of network: ", roundingValue[4])
    print("standard deviation of business: ", roundingValue[5])
    print("standard deviation of media: ", roundingValue[6])

    #Saves the arrays that contain the statistical results for each subject in an external text file and adds a title to it
    numpy.savetxt("StatisticalResults.txt",[medianArray,meanArray,stDeviationArray], fmt="%2.1f", delimiter=",", header="STATISTICAL RESULTS- \n 1) Median, 2) Mean, 3) Standard deviation- \n Science, Maths, English, Software, Network, Business, Media")
    
    #Checks how many subjects got over a certain mark for standard deviation statistics
    #Assigns a counter variable 0
    count=0
    #Iterates through each score in the array with standard deviation results
    for score in stDeviationArray:
        #If the score is less than 20 (expected result)
        if score<20:
            #Adds one to the count as condition is met
            count=count+1
        #If the count is greater than 0
    if count>0:
        #Displays the count of how many subjects had less than 20
        print(count, "subjects had lower than 20, improvement needed")
    else:
        #If the count is not greater than 0, displays the 0 count 
        print(count, "subjects had lower than 20, no improvement needed")

    
   
#Function that finds the subject with the best statistics
def subjectHighest():
    print("\n Best values: \n ")
    
    #Rounds the arrays to 1 decimal place
    rounding([medianArray, meanArray, stDeviationArray])
    #Assigns the first index which is median array from the rounding function
    medianArrayRounded=roundingValue[0]
    #Assigns the second index which is mean array from the rounding function
    meanArrayRounded=roundingValue[1]
    #Assigns the third index which is standard deviation array from the rounding function
    stDeviationArrayRounded=roundingValue[2]
    totalArray=numpy.array([medianArrayRounded, meanArrayRounded, stDeviationArrayRounded])
        
    #Finds the maximum value in the median array
    maxValueMedian=numpy.amax(medianArrayRounded)
    #Converting the maximum value to a list so other commands can be executed on data
    maxMedianList=maxValueMedian.tolist()
    #Convert the rounded median array to a list 
    medianList=medianArrayRounded.tolist()
    #Find the index of where the maximum value is in the median array
    medianIndex=medianList.index(maxMedianList)
    medianIndex=medianIndex+1
    #Find the subject that had the maximum score using the lists and index of the max value
    subjectMax=subjectNames[medianIndex]
    maxMedian="max value of median is "+ str(maxMedianList) +" which is subject "+ subjectMax
    print(maxMedian)
    
    #Finds the maximum value in the mean array
    maxValueMean=numpy.amax(meanArrayRounded)
    #Converting the maximum value to a list so other commands can be executed on data
    maxMeanList=maxValueMean.tolist()
    #Convert the rounded mean array to a list
    meanList=meanArrayRounded.tolist()
    #Find the index of where the maximum value is in the mean array
    meanIndex=meanList.index(maxMeanList)
    #Align the index from the arrays to the subject list
    meanIndex=meanIndex+1
    #Find the subject that had the maximum score using the lists and index of the max value
    subjectMax=subjectNames[meanIndex]
    maxMean="max value of mean is "+ str(maxMeanList) +" which is subject "+ subjectMax
    print(maxMean)
    
    #Finds the lowest value in the standard deviation array
    lowValueStDeviation=numpy.amin(stDeviationArrayRounded)
    #Converting the minimum value to a list so other commands can be executed on data
    minStdDeviationList=lowValueStDeviation.tolist()
    #Convert the rounded standard deviation array to a list
    stDeviationList=stDeviationArrayRounded.tolist()
    #Find the index of where the minimum value is in the standard deviation array
    stDeviationIndex=stDeviationList.index(minStdDeviationList)
    stDeviationIndex=stDeviationIndex+1
    #Find the subject that had the minimum score using the lists and index of the max value
    subjectMax=subjectNames[stDeviationIndex]
    minStDeviation="min value of standard deviation is "+ str(minStdDeviationList) +" which is subject "+ subjectMax
    print(minStDeviation)
    
    #Open the file in append mode that has the statistical results
    file=open("StatisticalResults.txt","a")
    file.write("\nMaximum and minimum values- \n")
    #Write to the file the maximum value of median and the subject this was
    file.write(maxMedian+"\n")
    #Write to the file the maximum value of mean and the subject this was
    file.write(maxMean+"\n")
    #Write to the file the minimum value of standard deviation and the subject this was
    file.write(minStDeviation+"\n")
    file.close()
    
#Rounding function to round the arrays to one decimal place, takes arrays passed as a parameter
def rounding(array):
    global roundingValue
    #Rounds the array that has been passed through the parameter to one decimal place
    roundingValue=numpy.round(array, 1)
    

#Calls the welcome function       
welcome()
#Calls the graph plotting function
maxAndGraph()
#Calls the statistical calculation median function
median()    
#Calls the statistical calculation mean function
mean()
#Calls the statistical calculation standard deviation function
standardDeviation()
#Calls the subject highest function
subjectHighest()