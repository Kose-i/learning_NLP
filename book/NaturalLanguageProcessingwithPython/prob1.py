
def q1():
    print( 12 / (4+1) )

def q2():
    print(26**100)

from nltk.book import *
def q3():
    print(['Monty', 'Python']*20)
    print(3*sent1)

def q4():
    print(len(text2))
    print(len(set(text2)))

def q5():
    print("fiction: romance")

def q6():
    text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

def q7():
    print(text5.collocations())

def q8():
    print(set(text4))
    print(len(set(text4)))

def q9():
    my_string = 'My String'
    print(my_string)
    print(my_string + my_string)
    print(my_string*3)
    print(' '.join([my_string, my_string]))
    print((my_string+' ')*3)

def q10():
    my_sent = ["My", "sent"]
    str_my_sent = ' '.join(my_sent)
    print(str_my_sent)
    same_list = str_my_sent.split(' ')
    print(same_list)

def q11():
    phrase1 = ['hoge']
    phrase2 = ['huga', 'fuga']
    print(len(phrase1 + phrase2))
    print(len(phrase1) + len(phrase2))

def q12():
    str_a = "Monty Python"
    list_str_b = ["Monty","Python"]
    print(str_a[6:12])
    print(list_str_b[1])

def q13():
    print(sent1[1][1])
    print(sent1[1])

def q14():
    print(sent3)
    print(sent3[1])
    print(sent3[5])
    print(sent3[8])

def q15():
    dict_list = list()
    for word in set(text5):
        if len(word) > 0 and word[0] == 'b':
            dict_list.append(word)
    dict_list.sort()
    print(dict_list)

def q16():
    range_ten = range(10)
    print(range_ten)
    range_ten_to_twenty = range(10, 20)
    print(range_ten_to_twenty)
    range_ten_to_twenty_every_two = range(10, 20, 2)
    print(range_ten_to_twenty_every_two)
    range_ten_to_twenty_every_minus_two = range(10, 20, -2)
    print(range_ten_to_twenty_every_minus_two)

def q17():
    sunset_idx = text9.index("sunset")
    first_idx = sunset_idx
    end_idx = sunset_idx
    while text9[first_idx] != '.':
        first_idx -= 1
    while text9[end_idx] != '.':
        end_idx += 1
    print(' '.join(text9[first_idx+1:end_idx+1]))

def q18():
    sent_list =      sent1
    sent_list.extend(sent2)
    sent_list.extend(sent3)
    sent_list.extend(sent4)
    sent_list.extend(sent5)
    sent_list.extend(sent6)
    sent_list.extend(sent7)
    sent_list.extend(sent8)
    token_count = len(sent_list)
    word_count  = len(set(sent_list))
    print(token_count / word_count)

def q19():
    q19_a = sorted(set([w.lower() for w in text1])) 
    q19_b = sorted([w.lower() for w in set(text1)])
    print(len(q19_a))
    print(len(q19_b))

def q20():
    words = ["Abc", "ABC", "..?"]
    for e in words:
        if e.isupper():
            print(e+".isupper()")
        if not e.islower():
            print("not"+e+"islower()")

def q21():
    print(text2[-2]+' '+text2[-1])

def q22():
    is_words = [len(w)==4 for w in set(text5)]
    words = list()
    for i,w in enumerate(set(text5)):
        if is_words[i]:
            words.append(w)
    print(words)
    words.sort(key=FreqDist)

def q23():
    for word in text6:
        if word.isupper():
            print(word)

def q24():
    for word in text7:
        if len(word)>=3 and word[-3:] == "ize":
            if word.count("z") >= 1: #and word.count("pt") >= 1:
                print(word)

if __name__=='__main__':
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    #q7()
    #q8()
    #q9()
    #q10()
    #q11()
    #q12()
    #q13()
    #q14()
    #q15()
    #q16()
    #q17()
    #q18()
    #q19()
    #q20()
    #q21()
    #q22()
    #q23()
    q24()
