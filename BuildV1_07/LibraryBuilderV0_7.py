import Tkinter
from Tkinter import Label
import ttk
import time
import threading
import sys
import os
import csv
import math

###############################LibBuilder Functions#################################
def SearchUnknownAlbumPic(Artist, APath):
    #Artist = Artist\ dir level items
    found = False
    TmpPic = ""
    TmpPath = ""
    #Priority of Searches for
    #1-Artist\
    for h in Artist:
        if h[2] == 0: # look for pic files
            if os.path.splitext(h[0])[1] in PicExt:
                TmpPic = h[0]
                TmpPath = APath + slash + TmpPic
                #print CPath + " And "  +  TmpPic
                found = True # cancel other searches
                return (TmpPic, TmpPath)
    #2-Artist\Album\ (s)
    if not found:
        for h in Artist: #loop items in  Artist\ 
            if h[2] == 1: # go into Album\
                for g in h[3]:
                    if g[2] == 0: # look for pic files
                        if os.path.splitext(g[0])[1] in PicExt:
                            TmpPic = g[0]
                            TpmPath = APath + slash + h[0] +  slash + TmpPic
                            found = True # cancel other searches
                            return (TmpPic, TmpPath)
    #3-default.jpg
    if not found:
        TmpPic = DefaultPic
        TmpPath = DefaultPath
        
    return (TmpPic, TmpPath)

def SearchSongPic(Album, BPath, Artist, APath):
    found = False
    TmpPic = ""
    TmpPath = ""
    #Priority of Searches for
    #1-Artist\ItsAlbum
    for h in Album:
        if h[2] == 0: # look for pic files
            if os.path.splitext(h[0])[1] in PicExt: 
                TmpPic = h[0]
                TmpPath = BPath + slash + TmpPic
                found = True # cancel other searches
                #print "1-TmpPic: " + TmpPic
                #print "1-TmpPath " + TmpPath
                return (TmpPic, TmpPath)
    #2-Artist\OtherAlbums
    if not found:
        for h in Artist:
            if h[2] == 1: # look for albums to look for pics files
                for g in h[3]: # go into Album\
                    if g[2] == 0: # look for pic files
                        if os.path.splitext(g[0])[1] in PicExt:
                            TmpPic = g[0]
                            TmpPath = APath + slash + h[0] +  slash +  TmpPic
                            found = True # cancel other searches
                            #print "2-TmpPic: " + TmpPic
                            #print "2-TmpPath " + TmpPath
                            return (TmpPic, TmpPath)                    
    #3-Artist\
    if not found:
        for h in Artist:
            if h[2] == 0: # look pic files
                if os.path.splitext(h[0])[1] in PicExt:
                    TmpPic = h[0]
                    TmpPath = APath + slash + TmpPic
                    found = True # cancel other searches
                    #print "3-TmpPic: " + TmpPic
                    #print "3-TmpPath " + TmpPath
                    return (TmpPic, TmpPath)
    #4-default.jpg
    if not found:
        TmpPic = DefaultPic
        TmpPath = DefaultPath
        #print "4-TmpPic: " + TmpPic
        #print "4-TmpPath " + TmpPath
        

    return (TmpPic, TmpPath)

def UpdateProgress(pcount):
    CurrentProg = float(pcount)/float(tLvItemCnt)
    CurrentPerc = CurrentProg*100
    CurrentPerc = math.floor(CurrentPerc)
    #Update Progress Here
    #print "Updating Progress: " + str(CurrentPerc) + ' %'
    ProgInfo['text'] = 'Write CSV file: ' + str(CurrentPerc) + ' %'
    pb_hD.step(10)
    time.sleep(0.1)
    

def SpecialToCsv(tmpExt):
    OutPath = LibraryPath + slash + 'LibraryWG.csv'
    ProgCnt = 0
    UpCnt = 0
    TenPerc = tLvItemCnt*0.1
    #print ""
    #print ""
    #print "Testing  write findings in LibraryWG.csv file"
    with open (OutPath, 'wb') as f:
        writer = csv.writer(f)
        #loop through  3 Levels of elements
        for i in topLv:
            if i[2] == 0:
                if os.path.splitext(i[0])[1] in  tmpExt:
                    ## Associate Unknown Artist song to a default picture
                    if os.name == "posix":
                        writer.writerow(("Library","UnknownArtist", "UnknownAlbum", str(i[0]), str(i[1]), DefaultPic, DefaultPath))
                    else:
                        writer.writerow(("Library","UnknownArtist", "UnknownAlbum", str(i[0]), str(i[1]).replace("\\","\\\\"), DefaultPic, DefaultPath.replace("\\","\\\\")))
            elif i[2] == 1:
                for e in i[3]:
                    if e[2] == 0:
                        if os.path.splitext(e[0])[1] in  tmpExt:
                            ## Search for Unknown Album song Pic
                            (CurrentPic, CurrentPath) = SearchUnknownAlbumPic(i[3], i[1])
                            if os.name == "posix":
                                writer.writerow(("Library",str(i[0]), "UnknownAlbum",    str(e[0]), str(e[1]), CurrentPic, CurrentPath))
                            else:
                                writer.writerow(("Library",str(i[0]), "UnknownAlbum",    str(e[0]), str(e[1]).replace("\\","\\\\"), CurrentPic, CurrentPath.replace("\\","\\\\")))
                    elif e[2] == 1:
                        for f in e[3]:
                            #Update Progress every 10 songs
                            ProgCnt = ProgCnt + 1
                            UpCnt = UpCnt + 1
                            if ProgCnt > TenPerc:
                                UpdateProgress(UpCnt)
                                ProgCnt = 0
                            if f[2] == 0:
                                if os.path.splitext(f[0])[1] in  tmpExt:
                                    ## Search for Album song Pic

                                    (CurrentPic, CurrentPath) = SearchSongPic(e[3],e[1],i[3], i[1])
                                    #print "Current Pic: " + str(CurrentPic)
                                    #print "Current Path: " + str(CurrentPath)
                                    if os.name == "posix":
                                        writer.writerow(("Library", str(i[0]),str(e[0]), str(f[0]),str(f[1]), CurrentPic, CurrentPath))
                                    else:
                                        writer.writerow(("Library", str(i[0]),str(e[0]), str(f[0]),str(f[1]).replace("\\","\\\\"), CurrentPic, CurrentPath.replace("\\","\\\\")))
    #print ".csv write is done! :" + OutPath




###############################Progress Bar Functions###############################
#Define your Progress Bar function, 
def GuiBar(root):   
    root.title('Library Builder V-0.7')
    root.geometry('450x150')
    global ft    
    ft = ttk.Frame()
    ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    global pb_hD # make progress bar global
    pb_hD = ttk.Progressbar(ft, orient='horizontal',  mode='determinate')#variable=valeur,
    pb_hD.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
    global ProgInfo # make ProgInfo
    ProgInfo = Label(root, text='Progress Info')
    ProgInfo.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.BOTTOM)
    root.mainloop()
    #Quit Root
    root.quit()

# Define the process of unknown duration with root as one of the input And once done, add root.quit() at the end.
def BuildLib(root):
    
    time.sleep(0.5) # wait for  pb_hD() to be created before running thread
    
    #Check OS
    global slash #make slash a global variable
    if os.name == "posix":
        #print "posix"
        slash = "/"
    else:
        #print "Windows"
        slash = "\\"
    
    #print 'Calculating Library Analysis...'
    pb_hD.config(mode='indeterminate')
    ProgInfo['text'] = 'Calculating Library Analysis'
    pb_hD.start()
    time.sleep(2)

    #1-Get Library path in 1st arg--> indeterminate pbar
    ProgInfo['text'] = '1-Check LibraryPath'
    time.sleep(1)
    global LibraryPath # make LibraryPath global
    LibraryPath = sys.argv[1]
    #print ""
    #print "LibraryPath: " + LibraryPath
    #G:\Music"
    #C:\Users\Marie-Noelle\Desktop\William\Music

    #2-Get Extensions --> indeterminate pbar
    ProgInfo['text'] = '2-Analyse Extensions'
    time.sleep(1)
    Eargs = sys.argv[2:]
    #print ""
    #print "Get Extension Arguments: " + str(Eargs)

    
    #3-Analyse all music file extensions --> indeterminate pbar
    ProgInfo['text'] = '3-Analyse music extensions'
    time.sleep(1)
    global MusExt # make MusExt[] global
    MusExt = []
    #print ""
    #print "MusRef: " + str(MusRef)    
    for mx in Eargs:
        if mx in MusRef:
            #print "mx: " + str(mx)
            MusExt.append(mx)
    #print "MusExt: " + str(MusExt)
    


    #4-Get all Picture file extensions --> indeterminate pbar
    ProgInfo['text'] = '4-Analyse picture extensions'
    time.sleep(1)
    global PicExt # make PicExt[] global
    PicExt = []
    #print ""
    #print "PicRef: " + str(PicRef)
    for px in Eargs:
        if px in PicRef:
            #print "px: " + str(px)
            PicExt.append(px)
    #print "PicExt: " + str(PicExt)
    #print ""

    #5-Get File Structure Analysis --> indeterminate pbar
    ProgInfo['text'] = '5-File Structure Analysis'
    time.sleep(1)
    global DefaultPic # make DefaultPic global
    DefaultPic = "default.jpg"
    global DefaultPath # make DefaultPath global
    DefaultPath = LibraryPath + slash + DefaultPic
    global CurrentPic # make CurrentPic global
    CurrentPic = ""
    global CurrentPath # make CurrentPath global
    CurrentPath = ""
    
    #get dirs
    fLvitems = os.listdir(LibraryPath)
    #Hold lists  of tupled lists
    global topLv # make topLv[] global
    topLv = []

    totfLvdir = 0
    totfLvfile = 0
    totsLvdir = 0
    totsLvfile = 0
    tottLvdir = 0
    tottLvfile = 0

    fLvCnt = 0
    sLvCnt = 0
    tLvCnt = 0

    fLvItemCnt = 0
    sLvItemCnt = 0
    global tLvItemCnt # make tLvItemCnt global
    tLvItemCnt = 0
    totItemCnt = 0
    
    global UpdateTrigS # make update trig Start global
    UpdateTrigS = False
    global UpdateTrigE # make update trig End global
    UpdateTrigE = False
    
    #mark 0 = file
    #mark 1 = folder
    #print ""	
    #print ""
    #print "List Directory in " + LibraryPath
    for fLv in fLvitems:
        #reset cnt 2nd and third
        sLvCnt = 0
        tLvCnt = 0
        PathfLv = LibraryPath + slash + fLv
        if os.path.isfile(PathfLv):
            ##print "  " + fLv
            topLv.append((fLv,PathfLv, 0))
            totfLvfile = totfLvfile + 1
            fLvCnt = fLvCnt + 1
            fLvItemCnt = fLvItemCnt + 1
        elif os.path.isdir(PathfLv):
            ##print "  " + PathfLv
            topLv.append((fLv,PathfLv, 1, []))
            totfLvdir = totfLvdir + 1
            fLvCnt = fLvCnt + 1
            fLvItemCnt = fLvItemCnt + 1
            sLvitems = os.listdir(PathfLv)
            for sLv in sLvitems:
                tLvCnt = 0
                PathsLv = PathfLv + slash + sLv
                if os.path.isfile(PathsLv):
                    #print "    " + sLv
                    topLv[fLvCnt-1][3].append((sLv, PathsLv,0)) ## add 2nd lv file to 1st lev tuple, mark 0
                    totsLvfile = totsLvfile + 1
                    sLvCnt = sLvCnt + 1
                    sLvItemCnt = sLvItemCnt + 1
                elif os.path.isdir(PathsLv):
                    #print "    " + PathsLv 
                    topLv[fLvCnt-1][3].append((sLv, PathsLv, 1, [])) ## add 2nd lv dir + [] to 1st lev tuple, mark 1
                    totsLvdir = totsLvdir + 1
                    sLvCnt = sLvCnt + 1
                    sLvItemCnt = sLvItemCnt + 1
                    tLvitems = os.listdir(PathsLv)
                    for tLv in tLvitems:
                        #print "      " + tLv
                        PathtLv = PathsLv + slash + tLv
                        if os.path.isfile(PathtLv):
                            topLv[fLvCnt-1][3][sLvCnt-1][3].append((tLv,PathtLv,0))
                            tottLvfile = tottLvfile + 1
                            tLvCnt = tLvCnt + 1
                            tLvItemCnt = tLvItemCnt + 1
                        elif os.path.isdir(PathtLv):
                            topLv[fLvCnt-1][3][sLvCnt-1][3].append((tLv,PathtLv,1))
                            tLvCnt = tLvCnt + 1
                            tottLvdir = tottLvdir + 1
                            tLvItemCnt = tLvItemCnt + 1
    totItemCnt = fLvItemCnt + sLvItemCnt + tLvItemCnt
    #print "Search Details:"
    #print "  First Level directories: " + str(totfLvdir)
    #print "  First Level files      : "	+ str(totfLvfile)	
    #print "  First Level items      : "	+ str(fLvItemCnt)	
    #print "  	2nd   Level directories: " + str(totsLvdir)
    #print "  	2nd   Level files      : "	+ str(totsLvfile)
    #print "  	2nd   Level items      : "	+ str(sLvItemCnt)
    #print "  		Third Level directories: " + str(tottLvdir)
    #print "  		Third Level files      : "	+ str(tottLvfile)
    #print "  		Third Level items      : "	+ str(tLvItemCnt)
    #print ""
    #print "Total Item Count: " + str(totItemCnt)
    pb_hD.stop()
    
    #6-Write CSV file
    pb_hD.config(mode='determinate')
    ProgInfo['text'] = '6-Write CSV file'
    time.sleep(1)
    SpecialToCsv(MusExt)
    
    #7-Success!
    ProgInfo['text'] = '7-Success'
    print 'Success'
    time.sleep(1)
   
    #Destroy GUI objects and quit root
    pb_hD.destroy()
    ProgInfo.destroy()    
    root.quit()

#Now define our Main Functions, which will first define root,
# then call for call for "BuildLib(root)" --- that's your progressbar,
# and then call for thread1 simultaneously which will  execute your BuildLib() process
def Main():
    #global root
    root = Tkinter.Tk()
    LibThread=threading.Thread(target=BuildLib, args=(root,))
    LibThread.start()
    GuiBar(root)  # This will block while the mainloop runs
   
##################################Start of Script (set Global variables here)########################
# Args{ScripName, LibraryPath, Ext[[MusExt], [PicExt]]}
# Outputs --> Success or failure message
# Extensions
BaseRef = [".mp3", ".MP3", ".wav", ".WAV", ".flac", ".FLAC", ".png", ".jpg", ".JPEG"]
MusRef = [".mp3", ".MP3", ".wav", ".WAV", ".flac", ".FLAC"]
PicRef = [".png", ".jpg", ".JPEG"]
    
#Run the functions by calling our Main() function,
if __name__ == '__main__':
    Main()
    
    
