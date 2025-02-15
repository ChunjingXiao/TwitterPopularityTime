# -*- coding: utf-8 -*-

# input: pairwiseRankDataTest
# classLabel globleFeature #user #items userFeature itemFeature1 itemFeature2
# 1	0	1	2	2:1	170:1	180:-1
# 0	0	1	2	2:1	523:1	533:-1
# 1	0	1	2	3:1	123:1	133:-1

# input2: pred.txt
# 0.421134
# 0.401046
# 0.663426

# output: 
# userID	#tweet	posRatio	Accuracy	sensitivity	specificity	gMean
# 142977623	16	0.3125	0.5	0.8	0.3636	0.5393
# 13877002	1	-1	-1	-1	-1	-1
# 28179079	1	-1	-1	-1	-1	-1


import sys
import datetime
import math

def printTime(beginTime):
    endTime = datetime.datetime.now() #calculate time
    print ("------------consumed-----------time-----------begin-----------")
    print ("consumed time:" + str(endTime - beginTime) )
    print ("------------consumed-----------time-----------end-------------")
    
def readUserId(inFile3):
    try:
        fin = open(inFile3)
        for current in fin:
            data = current.replace('\n','')
            curL = data.split('\t')
            userId = curL[0]
            return userId
    except:
        return '0000'
    
def readTestPred(inFile1,inFile2,userId,output):
    fin = open(inFile1,"r")   # pairwiseRankDataTest
    
    lineLabel = {} # lineLabel[lineCount] = [label]
    rowCount = 0
    positiveSample = 0
    negativeSample = 0
    for current in fin:
        rowCount += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        classLabel = float(curL[0])        
        if(classLabel <= 0):
            lineLabel[rowCount] = 0
            negativeSample += 1
        else:
            lineLabel[rowCount] = 1
            positiveSample += 1
        
    fin2 = open(inFile2,"r") # pred.txt
    count2 = 0
    correctCount = 0
    positivePred = 0
    negativePred = 0
    for current in fin2:
        count2 += 1
        data = current.replace('\n','')
        curL = data.split('\t')
        classLabel = float(curL[0])        
        if(classLabel < 0.5):   # if classLabel < 0.5, then negative 0
            predictLable = 0
            if( lineLabel[count2] == predictLable):
                negativePred += 1
                correctCount += 1
        else:
            predictLable = 1
            if( lineLabel[count2] == predictLable):
                positivePred += 1
                correctCount += 1

    if(count2 == 0):
        print '----------------' + str(userId) + '------is 0000---------------------------'
        return
    accurate = round(correctCount/float(count2),4)
    posRatio = round(positiveSample/float(rowCount),4)
    if(positiveSample == 0):  # then negativeSample must > 0
        sensitivity = -1*round(negativePred/float(negativeSample),4)
        specificity = round(negativePred/float(negativeSample),4)
        gMean = round(negativePred/float(negativeSample),4)
    elif(negativeSample == 0): # then positiveSample must > 0
        sensitivity = round(positivePred/float(positiveSample),4)
        specificity = -1*round(positivePred/float(positiveSample),4)
        gMean =  round(positivePred/float(positiveSample),4)
    else:
        sensitivity = round(positivePred/float(positiveSample),4)
        specificity = round(negativePred/float(negativeSample),4)
        gMean =  round(math.sqrt(sensitivity * specificity),4)
    '''
    if(count2 == 0 or positiveSample == 0 or  negativeSample == 0):
        accurate = -1
        posRatio = -1 
        sensitivity = -1
        specificity = -1
        gMean = -1
    else:
        accurate = round(correctCount/float(count2),4)
        posRatio = round(positiveSample/float(rowCount),4)
        
        sensitivity = round(positivePred/float(positiveSample),4)
        specificity = round(negativePred/float(negativeSample),4)
        gMean =  round(math.sqrt(sensitivity * specificity),4)
    '''
    print 'Accuracy--------' + str(accurate) + '--------'
    
    
    fout = open(output,'a')
    fout.write(userId +'\t'+ str(rowCount) +'\t'+ str(posRatio) +'\t'+ str(accurate)+'\t'+ str(sensitivity)+'\t'+ str(specificity)+'\t'+ str(gMean)+'\n')
    
    '''
    if(count >= 10):
        posRatio = round(positive/float(count),4)
        if( posRatio >= 0.4 and posRatio <= 0.6):    
            pass
    '''
    
    
        
def main(argv):
    inFile1 = argv[1]  # pairwiseRankDataTest 
    inFile2 = argv[2]  # pred.txt
    inFile3 = argv[3]  # SelectUserOne
    output = argv[4]   # computeSensitivityTxt
    reload(sys)
    sys.setdefaultencoding('utf-8')
    beginTime = datetime.datetime.now() 

    
    userId = readUserId(inFile3)
    readTestPred(inFile1,inFile2,userId,output)
    
    #printTime(beginTime)       
    #print "\a"
    #print 'finish' 

if __name__ == "__main__":
    #ִmain fuction
    main(sys.argv)
    
    