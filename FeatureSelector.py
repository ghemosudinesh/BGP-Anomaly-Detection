import csv
import decimal
import pandas

#columns to include
columnsToInclude = 10;

#selected Columns for fisher selector
selectedColumns = [];


def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

with open('prefix hijax rc004.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    negativeData = [];
    positiveData = [];

    theta = [0]*37;
    sortedTheta = [0]*37;
    gama = -0.5;
    beta = 0;
    sumOfNegative = [0]*37;
    sumOfPositive = [0]*37;
    squareOfData = [0]*37;
    sumOfData = [0]*37;
    lengthOfData = 0;
    lengthOfPositive = len(positiveData);
    lengthOfNegative = len(negativeData);

    
    for row in csv_reader:
        lengthOfData = lengthOfData + 1;
        for i in range(37) :
            sumOfData[i] = float(sumOfData[i]) + float(row[i]);
            squareOfData[i] = float(squareOfData[i]) + ( float(row[i]) * float(row[i]) ) ;
        if(row[37] == '-1'):
            negativeData.append(row);
        else:
            positiveData.append(row);

    for i in range(37) :
        for neg in negativeData:
            sumOfNegative[i] = float(sumOfNegative[i]) + float(neg[i]);
        for pos in positiveData:
            sumOfPositive[i] = float(sumOfPositive[i]) + float(pos[i]);
          

    for i in range(37) :
        
        firstDivision = (1/lengthOfData);
        firstSubDivision1 = ( 1/len(sumOfNegative) );
        firstSubDivision2 = ( 1/len(sumOfPositive) );

        secondDivision = ( gama/lengthOfData );

        squareLength = (lengthOfData * lengthOfData);
        thirdDivision = ( (gama-1)/squareLength );

        firstSubPortion1 = ( firstSubDivision1 * sumOfNegative[i] );
        firstSubPortion2 = ( firstSubDivision2 * sumOfPositive[i] );

        firstPortion = ( firstSubPortion1 + firstSubPortion2);

        secondPortion = secondDivision * squareOfData[i];

        thirdPortion = thirdDivision * sumOfData[i];

        theta[i] = firstDivision * (firstPortion - secondPortion + thirdPortion );

    

    sortedTheta = sorted(theta, reverse = True);
    print(theta);
    print('sortedTheta:::');
    print(sortedTheta);
    
    #search for top including columns
    for i in range(columnsToInclude):
        for j in range(37):
            if(theta[j] == sortedTheta[i]):
               selectedColumns.append(j);

    selectedColumns.append(37);

    #sort selected columns
    sortedSelectedColumns = sorted(selectedColumns,reverse = False);
    print('selectedColumns::');
    print(sortedSelectedColumns);

with open('prefix hijax rc004.csv') as csv_file:
    csv_data = pandas.read_csv(csv_file, usecols = sortedSelectedColumns);
    #line_count = 0;
    print(csv_data);
    city = pandas.DataFrame(csv_data);
    city.to_csv('writeData.csv');


        

    

    
               
        
        
     
        
