!/bin/bash

clear

echo Set Audio to HeadPhones
amixer cset numid=3 1
echo Switch done
echo
echo StartProgram

java -Xmx256m -jar MusicPlayer.jar
