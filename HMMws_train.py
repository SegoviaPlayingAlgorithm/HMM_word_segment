from pysbd import Segmenter
import numpy as np
import HMMwordsegment
from HMMwordsegment import HMM_w_s,A,B,pi

model=HMM_w_s
model.train("pku_training.utf8","param.npz")





