from pyspark import SparkContext
import os
def func(line):
    try:
        return [w.strip() for w in line.split('\t')[0].split(':')]
    except:
        pass
sc=SparkContext('local','meetting')
dir_path=r'E:\大数据\word'
for file in os.listdir(dir_path):
    if file[-3:]=='txt':
        rdd = sc.wholeTextFiles(os.path.join(dir_path,file))
        rdd = rdd.flatMap(lambda item: item[1].split('\r\n')).map(func).filter(lambda x: x)
        # with open(os.path.join(dir_path,file),'r',encoding='utf-8') as r:
        #     datas=r.readlines()
        print(rdd.collect()[2],rdd.collect()[4])

