def main():
    import statistics #importing module

    file=open("avocado.csv") #opening file
    lines=file.readlines() #reading lines
    file.close()#closing file
    data=[]#declaring variable
    for line in lines:
        data.append(line.split(','))#adding raw data to variables

    def readAndComputeMean_SM(col):
        place=data[0].index(col) #finding position of given column
        col_data=[]#declaring new variable
        for line in data[1:]:
            col_data.append(float(line[place].strip()))#retrieving column data,strip to separate columns
        avg=statistics.mean(col_data)#built-in function to find mean
        return avg

    #repeating same path for standard deviation and median
    def readAndComputeSD_SM(col):
        place=data[0].index(col)
        col_data=[]
        for line in data[1:]:
            col_data.append(float(line[place].strip()))
        sd=statistics.pstdev(col_data)
        return sd

    def readAndComputeMedian_SM(col):
        place=data[0].index(col)
        col_data=[]
        for line in data[1:]:
            col_data.append(float(line[place].strip()))
        median=statistics.median(col_data)
        return median

    def readAndComputeMean_HG(col):
        place=data[0].index(col)
        Sum=0
        for line in data[1:]:
            Sum+=float(line[place].strip())#adding column values to Sum variable
        avg=Sum/(len(data)-1) #finding mean using formula
        return avg

    def readAndComputeSD_HG(col):
        place=data[0].index(col)
        Sum=0
        var=0
        avg=0
        for line in data[1:]:
            Sum+=float(line[place].strip())
        avg=Sum/(len(data)-1)
        for line in data[1:]:
            var+=(float(line[place].strip())-avg)**2 # subtracting mean from column values\
            #taking square, and add them to variable
        std=(var/(len(data)-1))**0.5 #std formula from statistics
        return std
            
    def readAndComputeMedian_HG(col):
        place=data[0].index(col)
        r1=[float(line[place]) for line in data[1:]]
        n=len(r1)
        r1.sort()# sorting column data
        if n%2==0:
            m1=r1[n//2]# finding two middle numbers and divide to 2
            m2=r1[n//2-1]
            median=(m1+m2)/2
        else:
            median=r1[n//2]
        return median

    def readAndComputeMean_MML(col):
        place=data[0].index(col)#memoryless, or laziness, using list and mapping functions
        return statistics.mean(list(map(float,list(line[place]\
                                                   for line in data[1:]))))

    def readAndComputeSD_MML(col):
        place=data[0].index(col)
        return statistics.pstdev(list(map(float,list(line[place]\
                                                   for line in data[1:])))) 
            
    def readAndComputeMedian_MML(col):
        place=data[0].index(col)
        return statistics.median(list(map(float,list(line[place] \
                                                     for line in data[1:]))))

    mean_SM=readAndComputeMean_SM("Total Volume")
    sd_SM=readAndComputeSD_SM("Total Volume")
    median_SM=readAndComputeMedian_SM("Total Volume")
    mean_HG=readAndComputeMean_HG("Total Volume")
    sd_HG=readAndComputeSD_HG("Total Volume")
    median_HG=readAndComputeMedian_HG("Total Volume")
    mean_MML=readAndComputeMean_MML("Total Volume")
    sd_MML=readAndComputeSD_MML("Total Volume")
    median_MML=readAndComputeMedian_MML("Total Volume")

    print("\t\t\tUsing Statistic Module")
    print(" Mean: ",mean_SM,"\n","Std: ",sd_SM,"\n","Median: "\
          ,median_SM)
    print("\t\t\tUsing Homegrown code")
    print(" Mean: ",mean_HG,"\n","Std: ",sd_HG,"\n","Median: "\
          ,median_HG)
    print("\t\t\tWithout Memory")
    print(" Mean: ",mean_MML,"\n","Std: ",sd_MML,"\n","Median: "\
          ,median_MML)

if __name__=="__main__":
    print("problem_2.py is being run directly")
