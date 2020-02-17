#NUMPY CODEBASE

#Counting number of non-zero elements in an array
array = [1, 0, 1, 0, 0, 0, 1]
np.sum([1 for element in array if element != 0 ]) # 3

#Iterating through a dictionary in second line
#Reversing the key and value of each item of a dictionary

tag_fre = {'html':50,'css':74,'ml':65,'go':32}
print({fre:lang for lang,fre in tag_fre.items()}) # => {50: 'html', 74: 'css', 65: 'ml', 32: 'go'}
print({fre:lang for lang,fre in sorted(tag_fre.items(), key = lambda x:x[1])}) # => {32: 'go', 50: 'html', 65: 'ml', 74: 'css'} (sort dictionary by value)
print({fre:lang for lang,fre in sorted(tag_fre.items(), key = lambda x:x[1], reverse = True )})# => {74: 'css', 65: 'ml', 50: 'html', 32: 'go'}

#Add `elements of one list to another list

total_vocab = ['hello', 'hi', 'how', 'you']
new_words = ['i', 'am', 'thank']
total_vocab.extend(new_words)
print(total_vocab)	# ['hello', 'hi', 'how', 'you', 'i', 'am', 'thank']

#Sort tuples based on second parameter

tuple_list = [(0,0.9999),(1,0.707),(2,0.84)]
tuple_list.sort(key = lambda x:x[1] , reverse = True) # Highest value first
print(tuple_list)  # => [(0, 0.9999), (2, 0.84), (1, 0.707)]
#OR
print(sorted(tuple_list , key = lambda x:x[1] , reverse = True)) # => [(0, 0.9999), (2, 0.84), (1, 0.707)]

#Converting one hot vector to a label number

print(np.argmax([0,0,1,0,0])) # 2

# The enumerate() function in Python is commonly used instead of the for loop. That’s because enumerate() can iterate
# over the index of an item, as well as the item itself.Using enumerate() also makes the code cleaner, since you have to
# write fewer lines

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
for month_num, month in enumerate(months, start=1):
  print(month_num ,' ', month)
