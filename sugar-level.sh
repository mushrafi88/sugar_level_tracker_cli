#!/bin/bash



#cd ~/sugar_level_tracker_cli
mkdir -p output
#write to csv
python sugar-level.py $a
#write to pdf

python latex.py
python image.py

FILE=sugar_level.png
if [ -f "$FILE" ]; then
  sed -i 's/%//g' sugar_chart.tex
fi  

pdflatex  sugar_chart.tex


#1. read from last line and dunstify
#2. do a backup

\cp {sugar_level.png,sugar_chart.pdf,sugar_chart.csv} output/

notify-send -t 9000 --icon=video-television "sugar_chart updated" 

