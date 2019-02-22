# Project Phase 1
## Group Member: Bingshiun Low, Irene Chang, Ryan Lata
### Files
#### twitterextract.py
This is a python script adpated from an online resource to connect to the twitter streaming API and pull tweets which are of the English language and have the keyword 'nba' included. The tweets are parsed by python library json which turns the twitter JSON into a python dictionary allowing data access through key value pairs. The hashtags are first extracted first and output is redirected to a text file. The urls are then extracted and redirected into the same text file. 

#### data.txt
This file is the data file where the Twitter urls and hashtags were collected. The file is 1.64MB and contains 63685 hashtags and urls.

#### hadoopwc folder
This contains the output of the word count program run in Hadoop

#### sparkwc.txt
This is the word count file output from Spark

### Commands
##### hdfs wordcount
The data.txt file was imported in hdfs with the following command:
bin/hdfs dfs –copyFromLocal data.txt /rflata/

Hadoop wordcount was run with this command:
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount /rflata/data.txt /rflata/hadoopwc

Spark wordcount was run with this command:
$SPARK_HOME/bin/spark-submit run-example hdfs://localhost:9000/rflata/data.txt > sparkwc.txt

