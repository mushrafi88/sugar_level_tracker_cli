# sugar_level_tracker_cli

A commandline tool to keep track of your sugar level

The data is stored in .csv format as well as pdf(latex table) 


requirements python pandas package,latex support(especially pdflatex)
```
pip install pandas
yay -S texlive-most

```
first cd into the directory
```
git clone https://gitlab.com/mushrafi88/sugar_level_tracker_cli.git
cd sugar_level_tracker_cli
```

to run the rofi version if u have rofi installed
```
./rofi-sugar-level-tracker
```

to run the cli 
```
./sugar-level.sh f5.8
```
to set the name of the patient in pdf edit the sugar_chart.tex

the first string denotes the time and the rest denote sugar level 
for insulin use i6+4 or whatever it is

 | commandline argument | meaning |
| ------ | ------ |
| f5.5 | fasting sugar 5.5 mmol/L |
| b6.2 | 2hours after breakfast 6.2 mmol/L | 
| l6.6 | 2 hours after lunch 6.6 mmol/L|
| d6.6 | 2 hours after dinner 6.6 mmol/L |
| i6+4 | insulin dose and usage time |
