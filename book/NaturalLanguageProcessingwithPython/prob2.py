def q1():
    list_str = ["lion", "dog", "cat"]
    print(list_str + list_str)
    print(list_str*2)
    print(list_str[1])
    print(list_str[0:1])
    print(sorted(list_str))

from nltk.corpus import gutenberg
def q2():
    word_list = gutenberg.words('austen-persuasion.txt')
    print(len(word_list))
    print(len(set(word_list)))

def q3():
    pass

if __name__=='__main__':
    #q1()
    #q2()
