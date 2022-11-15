from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os
import easygui
import time

#Boilerplate code, valid file types & processing function
validExt = [".mp4",".avi",".ogv",".webm",".mkv"]
title = "EasyConcat v0.2"

def processclips():
    startTime = time.time()
    finalclip = concatenate_videoclips(clips)
    finalclip.write_videofile(folder + "\\" + outputfile + extension, write_logfile=True)
    endTime = time.time()
    textToDisplay = str(len(clips)) + " clips processed in " + str(round(endTime-startTime,1)) + " seconds\n Keep the log file?"
    keep = easygui.buttonbox(textToDisplay, title, ["No", "Yes"])

    if keep == "No":
        os.remove(folder + "\\" + outputfile + extension + ".log")
    
    textToDisplay = "Process more files?"
    output = easygui.buttonbox(textToDisplay, title, ["Finish", "Go Again"])

    if output == "Finish":
        ret = True
    
    else:
        ret = False

    return ret

while True:
    # Gets Parameters
    cont = False
    prefix = ""
    textToDisplay = "Please give the full folder path as copied from Explorer\nE.G: C:\\Users\\bea\\Music"
    while cont == False:
        #easygui multienterbox, defines list of parameters and text to display
        parameters = ["Folder Path", "Output File Name", "Output Extension"]
        defaults = ["","",".mp4"]
        input = easygui.multenterbox(prefix + textToDisplay,title,parameters,defaults)
        folder = input[0]
        outputfile = input[1]
        extension = input[2]
        files = os.listdir(folder)
        #data sanitisation, if folder doesn't exist, file already exists, or if extension is invalid it will add a prefix to display
        if os.path.exists(folder) == False:
            prefix = "Failed to find supplied folder\n"
        elif validExt.count(extension) == 0:
            prefix = "Extension provided invalid\n"
        elif files.count(outputfile+extension) != 0:
            prefix = "Cannot over-write file, please choose a different filename\n"
        else:
            #everything is all good
            cont = True

    #Defines arrays for testing
    clips = []
    failedFiles = []
    errors = False

    #Tests each file in the list to confirm if it is a video file we can process
    for file in files:
        #Gets file extension
        tmp = file.split(".")
        ext = "." + str(tmp.pop())
        #Counts instances of extension in the validExt array
        extCount = validExt.count(ext)
        #If not found, errors = true & appends failedFiles with the file name
        if extCount == 0:
            errors = True
            failedFiles.append(file)
        else:
            #Adds the file to the clips array for processing
            clips.append(VideoFileClip(folder + "\\" + file))

    if errors == True:
        errorCount = len(failedFiles)
        textToDisplay = str(errorCount) + " files did not match the valid extensions. Do you wish to proceed?"
        result = easygui.buttonbox(textToDisplay, title, ["Cancel", "What Files?", "Proceed"])
        if result == "What Files?":
            formattedFiles = ""
            for file in failedFiles:
                formattedFiles = formattedFiles + "\n" + file
            textToDisplay = "The following files failed:\n" + formattedFiles
            result = easygui.buttonbox(textToDisplay, title, ["Cancel", "Proceed"])
        
        if result == "Proceed":
            brk = processclips()
    else:
        brk = processclips()

    if brk == True:
        break


#removes log files from working directory
yee = os.listdir(os.curdir)
for f in yee:
    if f.endswith(".log"):
        os.remove(f)