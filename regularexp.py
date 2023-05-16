'''
in python regular expression is used to find the required word from a text.to used regular exp we should import as import re

'''
import re
pattern=r"[A-Z]rax"
text= "hello whats up its me ram bhanu from olangchunggola and whats about you.peter quill, drax,groot,yondu,ranon,ego,thanos"
res=re.search(pattern,text)
print(res)

