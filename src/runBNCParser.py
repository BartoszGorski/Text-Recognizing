from BNC_parser.BNCParser import BNCParser
import sys


parser = BNCParser
parsedDataContainer = []

xmlPath = str()
dataOutputPath = str()

if len(sys.argv) == 3:
    xmlPath = sys.argv[1]
    dataOutputPath = sys.argv[2]

    if xmlPath.find('.xml') != -1:
        parser.parseSingleXML(parsedDataContainer, xmlPath)
    else:
        parser.parseDirectoryXML(parsedDataContainer, xmlPath)

    parser.writeToCsv(parsedDataContainer, dataOutputPath)

elif len(sys.argv) == 2:
    xmlPath = sys.argv[1]

    if xmlPath.find('.xml') != -1:
        parser.parseSingleXML(parsedDataContainer, xmlPath)
    else:
        parser.parseDirectoryXML(parsedDataContainer, xmlPath)

    parser.writeToCsv(parsedDataContainer)

elif len(sys.argv) == 1:
    parser.parseDirectoryXML(parsedDataContainer)
    parser.writeToCsv(parsedDataContainer)

else:
    print("Error! Unrecognized run parameters!")