from collections import Counter
import numpy as np
string = "吾輩は猫である。名前はまだ無い。"
delimiter=['「','」','・・・',' ']

doublets = list(zip(string[:-1], string[1:]))
doublets = filter((lambda x: not((x[0] in delimiter) or (x[1] in delimiter))), doublets)

triplets = list(zip(string[:-2], string[1:-1], string[2:]))
triplets = filter((lambda x: not((x[0] in delimiter) or (x[1] in delimiter) or (x[2] in delimiter))), triplets)

dict2 = Counter(doublets)
for k,v in sorted(dict2.items(), key=lambda x:x[1], reverse=True)[:50]:
    print(k,v)
dict3 = Counter(triplets)
for k,v in sorted(dict3.items(), key=lambda x:x[1], reverse=True)[:50]:
    print(k,v)
