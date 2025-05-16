from pysbd import Segmenter
import numpy as np
from HMMwordsegment import HMM_w_s

segmenter = Segmenter()
sentences=[]
with open('pku_test.utf8',encoding='utf-8') as file:
    for line in file:
        for s in segmenter.segment(line):
            sentences.append(s)
#使用pysbd库进行分句，分词是分句的下游任务

model=HMM_w_s
npz=np.load("param.npz")
A=npz["arr_0"]
B=npz["arr_1"]
pi=npz["arr_2"]
for i in range(10):
    print(sentences[i])
    print(model.getpos(sentences[i],A,B,pi))
    print("-------------------------------")
