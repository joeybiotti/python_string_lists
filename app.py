word = str(raw_input("Enter a word: "))

if word[::-1] == word:
    print("That word is a palindrome")
else: 
    print("This word ain't no palindrome")