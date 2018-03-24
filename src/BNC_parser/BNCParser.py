from xml.dom import minidom
import csv
import os
from BNC_parser.StrDataSample import StrDataSample
  

class BNCParser:
    def parseSingleXML(parsedDataContainer = [], xmlFileName = str()):
        xml = minidom.parse(xmlFileName)
        sentencesList = xml.getElementsByTagName('s')

        for sentence in sentencesList:
            sentenceBuffer = str('')
            if int(sentence.getAttribute('n')) > 2:
                for word in sentence.childNodes:
                    if word.nodeType == minidom.Node.ELEMENT_NODE:
                        try:
                            sentenceBuffer += str(word.firstChild.nodeValue)
                        except Exception:
                            #print("Unknown XML structure! Skipping...")
                            break
                try:
                    sentenceBuffer.encode('ascii')
                except Exception:
                    #print("Non-ASCII string! Skipping...")
                    pass
                else:
                    if len(sentenceBuffer) > 6 and sentenceBuffer.find('(') == -1 and sentenceBuffer.find(')') == -1:      
                        parsedDataContainer.append(StrDataSample(sentenceBuffer))            
            
              
    def parseDirectoryXML(parsedDataContainer = [], directoryName = './BNC_parser/xml/'):
        filesInDirList = os.listdir(directoryName)
        xmlInDirList = []

        for file in filesInDirList:
            if(file.find('.xml') != -1):
                xmlInDirList.append(file)

        xmlListSize = len(xmlInDirList)
        currentFile = 0

        for xml in xmlInDirList:
            currentFile += 1
            BNCParser.parseSingleXML(parsedDataContainer, directoryName + xml)
            print("Parsing progress: ", int((currentFile/xmlListSize)*100), "%")

        print("Done!")


    def writeToCsv(dataContainerToWrite = [], fileName = './output/BNC_parser/BNCorpus.csv', separator = ',', newLine = '\n'):
        with open(fileName, 'w+', newline = newLine) as csvfile:
            csvWriter = csv.writer(csvfile, delimiter = separator, quotechar = '"', quoting = csv.QUOTE_ALL)
            for sample in dataContainerToWrite:
                csvWriter.writerow([sample.sentence, sample.language])

