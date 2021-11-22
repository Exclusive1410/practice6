#1  Write a Python program to calculate the length of a string.
str = input('Input your string : ')
print('Length of your string is : ', len(str))

print('--------------')

#2  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string.
def string(str):
    if len(str) < 2:
        return ''
    else:
        return str[0:2] + str[-2:]

print(string('w3resource'))
print(string('w3'))
print(string('w'))

print('--------------')

#3 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',except the first char itself. Sample String : 'restart' Expected Result : 'resta$t'
stri = input('Input your string : ')
char = stri[0]
length = len(stri)
stri = stri.replace(char, '$')
stri = char + stri[1:]
print(stri)

print('--------------')

#4 Write a Python function to reverses a string if it's length is a multiple of 4.
rstr = input('Enter string : ')
if len(rstr)%4==0:
 print(rstr[::-1])
else :
 print('Error')

 print('--------------')

 #5 Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Sample Words : red, white, black, red, green, black Expected Result : black, green, red, white,red
comma_sep_words = input('Input comma separated words : ')
words = [word for word in comma_sep_words.split(',')]
print(','.join(sorted(list(set(words)))))