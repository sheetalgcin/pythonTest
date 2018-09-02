def cntWords(word):
	 list1 = word.split(' ');
	 len1 = len(list1)
	 return len1;


if __name__ == " __main__":main()
word = raw_input("Enter the string")
num = cntWords(word)
print "The number of words {0}".format(num)
