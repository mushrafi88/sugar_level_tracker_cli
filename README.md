# sugar_level_tracker_cli

A commandline tool to keep track of your sugar level

The data is stored in .csv format as well as pdf(latex table) 


requirements python pandas package,latex support(especially pdflatex)
```
pip install pandas

```


to run the rofi version
```
./rofi-sugar-level-tracker l6.6
```

to run the cli 
```
./sugar-level.sh f5.8
```

the first string denotes the time and the rest denote sugar level 
for insulin use i6+4 or whatever it is

 | commandline argument | meaning |
| ------ | ------ |
| f5.5 | fasting sugar 5.5 mmol/L |
| b6.2 | 2hours after breakfast 6.2 mmol/L | 
| l6.6 | 2 hours after lunch 6.6 mmol/L|
| d6.6 | 2 hours after dinner 6.6 mmol/L |
| i6+4 | insulin dose and usage time |
