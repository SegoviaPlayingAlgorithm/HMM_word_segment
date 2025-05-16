HMM有三个参数A B pi，在训练集有标注的情况下使用频率替代概率即可完成三个参数的估计，具体地：
![微信图片_20250516103257](https://github.com/user-attachments/assets/f0dbbbed-74b1-4128-9dc3-23511cc0166f)
然后用维特比算法计算具有极大似然地隐状态路径，所谓最大路径，本实验中状态有4种，开头B中间M结尾E独立词S
程序中的HMM使用的几个符号对应的numpy数组如下：
![微信图片_20250516103228](https://github.com/user-attachments/assets/f5eaa34c-49ce-4166-b3e8-4f767fab8596)
使用的是pku的分词语料库分为traning和test两部分，test没有标注，所以只能委屈你自己标注一下，然后统计准确率，F1什么的
训练过程预览：
![样本预览和频数统计结果](https://github.com/user-attachments/assets/fc44c23d-f575-4726-8ad8-f31d51820ba8)
分词结果：
![分词结果](https://github.com/user-attachments/assets/a0c3d4c0-eced-40fc-88e8-06bef347e8e7)

