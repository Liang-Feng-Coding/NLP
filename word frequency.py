import time

start = time.time()

f1 = open(r"1997.txt", encoding="utf-8")
f2 = open(r"1998.txt", encoding="utf-8")
f3 = open(r"1999.txt", encoding="utf-8")
f4 = open(r"2000.txt", encoding="utf-8")
f5 = open(r"2001.txt", encoding="utf-8")
f6 = open(r"2002.txt", encoding="utf-8")
f7 = open(r"2003.txt", encoding="utf-8")
f8 = open(r"2004.txt", encoding="utf-8")
f9 = open(r"2005.txt", encoding="utf-8")
f10 = open(r"2006.txt", encoding="utf-8")
f11 = open(r"2007.txt", encoding="utf-8")
f12 = open(r"2008.txt", encoding="utf-8")
f13 = open(r"2009.txt", encoding="utf-8")
f14 = open(r"2010.txt", encoding="utf-8")
f15 = open(r"2011.txt", encoding="utf-8")
f16 = open(r"2012.txt", encoding="utf-8")
f17 = open(r"2013.txt", encoding="utf-8")
f18 = open(r"2014.txt", encoding="utf-8")
f19 = open(r"2015.txt", encoding="utf-8")
f20 = open(r"2016.txt", encoding="utf-8")
f21 = open(r"2017.txt", encoding="utf-8")
f22 = open(r"2018.txt", encoding="utf-8")
f23 = open(r"2019.txt", encoding="utf-8")
f24 = open(r"2020.txt", encoding="utf-8")

file1 = f1.readlines()
file2 = f2.readlines()
file3 = f3.readlines()
file4 = f4.readlines()
file5 = f5.readlines()
file6 = f6.readlines()
file7 = f7.readlines()
file8 = f8.readlines()
file9 = f9.readlines()
file10 = f10.readlines()
file11 = f11.readlines()
file12 = f12.readlines()
file13 = f13.readlines()
file14 = f14.readlines()
file15 = f15.readlines()
file16 = f16.readlines()
file17 = f17.readlines()
file18 = f18.readlines()
file19 = f19.readlines()
file20 = f20.readlines()
file21 = f21.readlines()
file22 = f22.readlines()
file23 = f23.readlines()
file24 = f24.readlines()


readline = file1+file2+file3+file4+file5+file6+file7+file8+file9+file10+file11+file12+file13+file14+file15+file16+file17+file18+file19+file20+file21+file22+file23+file24


#print(type(readline))
word = []

for line in readline:
    line = line.lower()
    line = line.replace('\’s',' ')
    line = line.replace('\’',' ')
    line = line.replace('.',' ')
    line = line.replace(':',' ')
    line = line.replace(';',' ')
    line = line.replace('“',' ')
    line = line.replace('”',' ')
    line = line.replace('(',' ')
    line = line.replace(')',' ')
    line = line.replace('|',' ')
    line = line.replace('&',' ')
    line = line.replace('\'s',' ')
    line = line.replace('—',' ')
    line = line.replace('?',' ')
    line = line.replace('-',' ')
    line = line.replace(',',' ')
    line = line.replace('\'',' ')
    line = line.replace('*',' ')
    line = line.replace('!',' ')
    line = line.replace('’s',' ')
    line = line.replace('\/',' ')
    line = line.replace('‘',' ')
    line = line.replace('\"',' ')
    line = line.replace('…',' ')
    line = line.replace(']',' ')
    line = line.replace('[',' ')
    line = line.replace('0',' ')
    line = line.replace('1',' ')
    line = line.replace('2',' ')
    line = line.replace('3',' ')
    line = line.replace('4',' ')
    line = line.replace('5',' ')
    line = line.replace('6',' ')
    line = line.replace('7',' ')
    line = line.replace('8',' ')
    line = line.replace('9',' ')
    line = line.replace('$',' ')
    line = line.replace('@',' ')
    line = line.replace('&',' ')
    line = line.replace('%',' ')
    line = line.replace('#',' ')
    line = line.replace('+',' ')
    line = line.replace('´s',' ')
    line = line.replace('´',' ')
    line = line.replace('/',' ')
    line = line.replace('’',' ')
    line = line.replace('–',' ')
    line = line.replace('\n',' ')
    line = line.replace('{',' ')
    line = line.replace('}',' ')
    line = line.replace('•',' ')
    line = line.replace('�',' ')
    line = line.replace('■',' ')
    line = line.replace('',' ')
    line = line.replace('_____________________________________________',' ')

    
    wo = line.split(' ')
    word.extend(wo)
    
words_dic = {}

for k in word:
    if k in words_dic:
        words_dic[k] += 1     
    else:
        words_dic[k] = 1

words_dic = sorted(words_dic.items(), key=lambda d:d[1], reverse = True)

''' 
with open('my_file.csv', 'w', encoding='utf-8') as f:
    for key, value in words_dic:
        f.write('{0},{1}\n'.format(key, value))
'''
with open('frequency.txt', 'a', encoding='utf-8') as f:
    for key, value in words_dic:
        f.write('{0},{1}\n'.format(key, value))
  
f.close()
end = time.time()
print('duration time is: ', end-start)
