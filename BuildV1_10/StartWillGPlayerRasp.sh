!/bin/bash
clear

echo Set Audio to HeadPhones
amixer cset numid=3 1
echo Switch done
echo
echo StartProgram
java -jar MusicPlayer.jar
