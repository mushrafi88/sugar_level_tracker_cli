#!/bin/bash



#cd $HOME/sugar_level_tracker_cli
mkdir -p output
#write to csv
python sugar-level.py $1
#write to pdf

python latex.py
python image.py
pdflatex sugar_chart.tex

\cp {sugar_level.png,sugar_chart.pdf,sugar_chart.csv} output/

notify-send -t 9000 --icon=video-television "sugar_chart updated" 

