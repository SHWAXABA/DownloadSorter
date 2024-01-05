#Sorts your downloaded content into appropiate folders
#OBJECTIVES
#1-Create directory creator functions(If directory exist then it ignores the function)
#2-Reads all files in the directory and places them in the appropriate directories(Create function)
# Create a directory for Pictures, Audio, documents and archives
#3-Directories are sorted by creation date(Optional)

import os
import shutil
import sys

#Creates the directories needed
def dirCreate():
    #if statements to check if the directory already exists
    if not os.path.exists('.\Pictures'):
        os.mkdir('Pictures')
    if not os.path.exists('.\Audio'):    
        os.mkdir('Audio')
    if not os.path.exists('.\Documents'):    
        os.mkdir('Documents')
    if not os.path.exists('.\Archives'):    
        os.mkdir('Archives')
    if not os.path.exists('.\Videos'):    
        os.mkdir('Videos')    
    if not os.path.exists('.\Torrents'):  
        os.mkdir('Torrents')        
dirCreate()    

#checks for file types in dictory and places them in to the correct folder
def fileSort():
      for x in os.listdir(): 
        if x.endswith(".txt") or x.endswith(".pdf") or x.endswith(".docx") or x.endswith(".pptx"):
            shutil.move(x,'.\Documents')
        if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg") or x.endswith(".gif"):
            shutil.move(x,'.\Pictures')
        if x.endswith(".mp3") or x.endswith(".wav"):
         shutil.move(x,'.\Audio')
        if x.endswith(".zip") or x.endswith(".rar") or x.endswith(".7zip"):
         shutil.move(x,'.\Archives')  
        if x.endswith(".torrent"):
            shutil.move(x,'.\Torrents') 
        if x.endswith(".mp4") or x.endswith(".mkv") or x.endswith(".avi"):
            shutil.move(x,'.\Videos')      
fileSort()
       
 