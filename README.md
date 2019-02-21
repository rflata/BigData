# Project Phase 1

### Files
#### twitterextract.py
This is a python script adpated from an online resource to connect to the twitter streaming API and pull tweets which are of the English language and have the keyword 'nba' included. The tweets are parsed by python library json which turns the twitter JSON into a python dictionary allowing data access through key value pairs. The hashtags are first extracted first and output is redirected to a text file. The urls are then extracted and redirected into the same text file. 

#### data.txt
This file is the data file where the Twitter urls and hashtags were collected. The file is x size and contains x lines.

#### out

### Commands
##### hdfs wordcount
The data.txt file was imported in hdfs with the following command:
bin/hdfs dfs –copyFromLocal data.txt /rflata/

Wordcount was run with this command:
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount /rflata/data.txt /rflata/out
