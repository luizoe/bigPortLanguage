# This is a very simple example showing how to use: csv to read, array manipulation, and printing.
import csv


def readToArrData(csvFilePath):
    lineIndex = 0
    dataToRet = []
    with open(csvFilePath, newline='') as csvFileOpened:
        lineReader = csv.reader(csvFileOpened, delimiter=';')
        for line in lineReader:
            for columnData in line:
                dataToRet.append([])
                dataToRet[lineIndex].append(columnData)
            lineIndex = lineIndex + 1
        return dataToRet


def showAsCsvFile(arrData):
    for lineReaded in arrData:
        fullLineText = ""
        for columnReaded in lineReaded:
            fullLineText = fullLineText + columnReaded + ";"
        print(fullLineText)


theParsedData = readToArrData("./data.csv")
print(theParsedData)
showAsCsvFile(theParsedData)
