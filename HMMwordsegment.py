import numpy as np

pos2idx={'B':0,'M':1,'E':2,'S':3}
idx2pos={0:'B',1:'M',2:'E',3:'S'}
A=np.ones([4,4])/1e100
B=np.ones([4,65536])/1e100
pi=np.ones([4,1])/1e100

class HMM_w_s():
    def show():
        global A
        print(A)
    def train(txtfile,para_path):#训练文本路径和参数存储路径
        num_line=0
        global A,B,pi
        with open(txtfile,encoding='utf-8') as txt:
            for line in txt:
                num_line+=1
                states=[]#states是一个句子每个字的标注，即每个字的BMES标签
                sentence=""#去空格的句子
                words=line.strip().split() #剥落空格后拆分成词的list
                for i in range(len(words)):
                    sentence+=words[i]
                    if(len(words[i])>1):
                        states.append('B')
                        for j in range(len(words[i])-2):
                            states.append('M')
                        states.append('E')
                    else:
                        states.append('S')
                for i in range(len(states)):
                    if(i==0):
                        pi[pos2idx[states[0]]][0]+=1
                    else:
                        A[pos2idx[states[i-1]]][pos2idx[states[i]]]+=1
                        B[pos2idx[states[i]]] [ord(sentence[i])]+=1
                if(num_line<=5):
                    print("展示第"+str(num_line)+"个样本的标注，分词，标注的数字索引，")
                    print(states)
                    print(words)
        print("频数统计：","转移频数",A,"状态表现出某种观测的频数",B,"初始状态频数",pi)
        # 用频率替代概率（极大似然理论、大数定律?其实这个做法小学生都会，我觉得不用解释的那么高大上）
        for i in range(4):
            Arowsum=A[i].sum()
            A[i]=np.log(A[i]/Arowsum)
            Browsum=B[i].sum()
            B[i]=np.log(B[i]/Browsum)
            pisum=pi.sum()
            pi=np.log(pi/pisum)
        np.savez(para_path,A,B,pi)
    def getpos(sentence,A,B,pi):#文本，参数
        #利用维特比算法计算最优路径
        n=len(sentence)
        delta=np.zeros([4,n])
        psi=np.zeros([4,n])
        for i in range(n):
            if(i==0):
                delta[:,0]=pi[:,0]+B[:,ord(sentence[0])]
            else:
                for j in range(4):
                    maxi=np.argmax(delta[:,i-1]+A[:,j])
                    psi[j][i]=maxi
                    delta[j][i]=delta[maxi][i-1]+A[maxi][j]+B[j][ord(sentence[i])]
        pos=""
        posi=int(np.argmax(delta[:,n-1]))
        pos+=" | "+idx2pos[posi]+":"+sentence[n-1]
        for i in range(n-1):
            posi=int(psi[posi][n-1-i])#加强制转换是因为argmax得到的psi居然是浮点类型的
            pos+=" | "+idx2pos[posi]+":"+sentence[n-2-i]
        return pos[::-1] #翻转pos得到正确标注



                        
                    
                        
                
            
