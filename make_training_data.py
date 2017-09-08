import glob
import random
import gzip

doc_dirs=glob.glob("doc_ngrams/*")
random.shuffle(doc_dirs)

for doc_dir in doc_dirs:
    doc_num=doc_dir.split("/")[-1]
    with gzip.open(doc_dir+"/biarcs.txt.gz","rt",encoding="utf-8") as barcs:
        for line in barcs:
            cols=line.split("\t")
            assert len(cols)==3
            ngram=cols[1].replace(" ","_")
            print(int(doc_num),ngram,sep="\t")
            


