import os
import random as rn
import shutil

rn.seed(443)
DATA_DIR = 'voice_repo/'
listOfWords = ['backward','bed','bird','cat','dog','down','eight','five','follow','forward','four','go','happy','house','learn','left','nine','no','off','on','one','right','seven','six','stop','three','tree','two','up','visual','wow','yes','zero']


# Number of recordings per word
repoSize = 10000

# Choos small repo or complete
if repoSize < 1500:
    TARGET_DIR = 'mediumRepo'
    for word in listOfWords:
        directory = DATA_DIR + word
        filesInDirectory = os.listdir(directory)
        nbrOfFiles = len(filesInDirectory)
        # First pick by 80%, then split by 50%, and then the rest
        # This makes 80%/10%/10%
        setSizes = {'mTrain': 0.8, 'mTest': 0.1,'mValidation': 0.1}
        for setName, percentage in setSizes.items():
            tmpList = rn.sample(filesInDirectory, int(repoSize*percentage))
            # Copy files
            filesInDirectory = [x for x in filesInDirectory if not x in tmpList]
            #cpFiles = [shutil.copyfile(directory + '/' + y, TARGET_DIR + '/' + setName + '/' + word + '_' + y) for y in tmpList]
else:
    TARGET_DIR = 'fullRepo'
    for word in listOfWords:
        directory = DATA_DIR + word
        filesInDirectory = os.listdir(directory)
        nbrOfFiles = len(filesInDirectory)
        # First pick by 80%, then split by 50%, and then the rest
        # This makes 80%/10%/10%
        setSizes = {'fTrain': 0.8, 'fTest': 0.5,'fValidation': 1.0}
        for setName, percentage in setSizes.items():
            tmpList = rn.sample(filesInDirectory, int(len(filesInDirectory)*percentage))
            # Copy files
            filesInDirectory = [x for x in filesInDirectory if not x in tmpList]
            cpFiles = [shutil.copyfile(directory + '/' + y, TARGET_DIR + '/' + setName + '/' + word + '_' + y) for y in tmpList]

