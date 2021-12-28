#fl = open('b.txt', 'a')
#e = input('infor: ')
#y = fl.write(e + '\n')
#with open ('b.txt', 'r') as j:
#    t = j.readlines()
#    print(t)

fl = open('b.txt', 'a')

h = input('header: ')
yr = input('year: ')
tl = input('title: ')
url = input('Address: ')
d = input('date: ')
u = '(' + yr + ')'
e = print(h + ' ' + u + ' ' + tl + ' ' + '[online] ' + 'Address: ' + url + '[accessed: ' + d + ']')


#(h + ' ' + u + ' ' + tl + ' ' + '[online] ' + 'Address: ' + url + '[accessed: ' + d + ']') 


# use this to store all of the references
# ref = this time go for the first version of the code
# maybe make it print out all references at the end
# hint use append module and maybe look in to regex
