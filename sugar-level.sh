#!/bin/bash



cd $HOME/sugar_level_tracker_cli

#write to csv
python sugar-level.py $1
#write to pdf

python latex.py

pdflatex sugar_chart.tex


notify-send -t 9000 --icon=video-television "sugar_chart updated" 

