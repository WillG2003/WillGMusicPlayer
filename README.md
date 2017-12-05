# WillGMusicPlayer
music player for .mp3, .wav, .flac

Basic Java Music Player for .mp3, .wav, and .flac files Uses the following java libs: 
-jaudiotagger-2.0.3.jar 
-jflac-1.3
-jdk1.4.jar 
-jflac-1.3.jar 
-jl1.0.1.jar 
-mp3plugin.jar 
-mp3spi1.9.5.jar 
-opencsv-3.8.jar 
-tritonus_share-0.3.6.jar

Requires the installation of -Python 2.7 -JDK 8 (JDK 7 is also fine)

Installation Notes: 
1-Download git pkg
2-copy paste LibraryBuilderV0_7.py into MediaLibraryFolder\

Use in Windows:
1-Run StartWillGPlayerGUI.bat (or StartWillGPlayerCmd.bat for debug with console).This launches the player.
2-Goto Options Tab->Library and click "Update Path" and navigate to your MediaLibraryFolder.
3-Click "Analyse Library" and the python LibraryBuilder will generate a Library.csv file and populate the Player Tab interface
  with your music.
4-Click "Save Options" to save the location of the generated Library.csv and MediaLibraryFolder Locations.
  This allows the library to be autoloaded at the next program start up.
  
5-Go back to the Player tab and select a playlist to make (Rap, Punk, Metal, or Rock).

6-Building a playlist:

  6-1:Right Click an Artists to add all artist's songs to the current playlist
  
  6-2:Right Click an Artist's album to add the album's songs to the selected playlist
  
  6-3:Right Click a Song to add it to the current  playlist
  
  6-4:Click "Save PlayList" to save a playlist for further use
  
  
7-Double-Click a Song in the populated playlist(the selected entry will turn red).

8-Click Play to start the song
   
