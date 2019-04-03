#author : Rishab Kharidhi rishab.kharidhi@colorado.edu
#name   : Assignment 2: Password Cracker Project
#purpose: To perform dictionary attacks 
#date   : 02.12.2019
#version: 3.7

import hashlib
import sys
import time

#this is the wordlist that I have built in
snow=['digital','forensics','digitalforensics','professor','aaron','hansen','password','qwerty','admin','aaronhansen','water','waterbottle','medicine','headphones','air','force','airforce','cyber','security','cybersecurity','hacker','attacker','iloveyou','iloveu','light','hi','bye','hey','goodbye','hello','world','helloworld','sign','site','soldier','wrong','username','user','name','national','consider','consumer','digitalevidence','evidence','forensicscientist','scientist','laptop']

#this is the try and except function blocks to check for errors that are possible in this part of the code
try:
    #this function reads the words from the input document and stores them seperately as a list for easier access by the program functions
    def wordlist(docname):
        with open(docname, 'r') as wl:
            w=[]
            words=[]
            for line in wl:
                w.append(line.split())
            for i in range(len(w)):
                words.append(w[i][0])
            return words
except IOError:
    print("The code encountered an error when trying to open the file")
except:
    print("Something went wrong while reading from the file, there was an unexpected error!")

#this is the try and except function blocks to check for errors that are possible in this part of the code
try:
    #this function reads the hashes from the input document containing of hashes and stores them as a list for easier access by the program functions
    def hashlist(hashdocname):
        with open(hashdocname, 'r') as hl:
            h=[]
            hashes=[]
            for line in hl:
                h.append(line.split())
            for i in range(len(h)):
                hashes.append(h[i][0])
            return hashes
except IOError:
    print("The code encountered an error when trying to open the file")
except:
    print("Something went wrong while reading from the file, there was an unexpected error!")

#this function is to check if the document provided by the user is of a .txt format
def extensioncheck(docname):
    extension=docname.split(".")[-1]
    #print(extension)
    if extension == docname:
        print("The document name you have provided has no extension provided")
        sys.exit()
    if extension != 'txt':
        print("The document that you have provided is not a .txt format document, the code is unable to read this file")
        sys.exit()
    if extension == 'txt':
        return
    
#this function reads the built-in wordlist and stores them in another list for use by functions for manipulation and mangling
def snowlist(docname):
    words=[]
    for word in docname:
        words.append(word)
    return words

#this function performs various mangling operations on the words of the list and stores it in the same temporary list that was created by the previous functions
def mangling(words):
    mangledwords=[]
    mangled_flag=0

    #this loop reads the words from the list and appends to another list
    for i in range(len(words)):
        mangledwords.append(words[i])

    #this function performs mangling for the letter a by substituting it with the number 1
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1           
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter e by substituting it with the number 2            
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'e':
                j = '2'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter i by substituting it with the number 3
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'i':
                j = '3'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter o by substituting it with the number 4
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'o':
                j = '4'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter u by substituting it with the number 5
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'u':
                j = '5'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter i by substituting it with the number 1
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'i':
                j = '1'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter e by substituting it with the number 3
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'e':
                j = '3'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter o by substituting it with the number 0
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'o':
                j = '0'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letter s by substituting it with the number $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 's':
                j = '$'
                mangled_flag=1
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the numbers 1,2,3,4,5 and the letter s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters @,2,3,4,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '@'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters 1,3,3,4,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '3'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters 1,2,1,4,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '1'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters 1,2,3,0,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '0'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters @,3,3,4,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '@'
                mangled_flag=1
            if j == 'e':
                j = '3'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters @,2,1,4,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '@'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '1'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters @,2,3,0,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '@'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '0'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters 1,3,1,4,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '3'
                mangled_flag=1
            if j == 'i':
                j = '1'
                mangled_flag=1
            if j == 'o':
                j = '4'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters 1,3,3,0,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '3'
                mangled_flag=1
            if j == 'i':
                j = '3'
                mangled_flag=1
            if j == 'o':
                j = '0'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters 1,2,1,0,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '1'
                mangled_flag=1
            if j == 'e':
                j = '2'
                mangled_flag=1
            if j == 'i':
                j = '1'
                mangled_flag=1
            if j == 'o':
                j = '0'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0

    #this function performs mangling for the letters a,e,i,o,u by substituting it with the characters @,3,1,0,5 and s with $
    for i in range(len(words)):
        mngld=''
        for j in words[i]:
            if j == 'a':
                j = '@'
                mangled_flag=1
            if j == 'e':
                j = '3'
                mangled_flag=1
            if j == 'i':
                j = '1'
                mangled_flag=1
            if j == 'o':
                j = '0'
                mangled_flag=1
            if j == 'u':
                j = '5'
                mangled_flag=1
            if j == 's':
                j = '$'
                mangled_flag=1               
            mngld+=j
        mngld+='123'
        if mangled_flag==1:
            mangledwords.append(mngld)
            mangled_flag=0            

    #this function performs mangling by appending the numbers 123 to the words in the list
    for i in range(len(words)):
        mngld=''
        mngld=words[i]+'123'
        mangledwords.append(mngld)

    for i in range(len(words)):
        mngld=''
        mngld=words[i][::-1]
        mangledwords.append(mngld)
        #print(mngld)
        
    #print(mangledwords)
    return mangledwords


#this function performs the comparision of the hashes of the words from the list created by the mangling functions to the hashes from the input hash list
def passwordcheck_list(mangledwords,hashlist):
    list_flag=1
    for i in mangledwords:
        hash1=hashlib.md5(i.encode())
        hash2=hash1.hexdigest()
        for j in hashlist:
            if hash2 == j:
                print("A Password found, it is ",i)
                list_flag=0
    return list_flag

#this function performs the comparision of the hashes of the words from the list created by the mangling functions to the hash that was input by the user
def passwordcheck_hash(mangledwords,inputhash):
    for i in mangledwords:
        #print(i)
        hash1=hashlib.md5(i.encode())
        hash2=hash1.hexdigest()
        if hash2 == inputhash:
            print("The password has been cracked, it is ",i)
            return 0


try:
    #this is the main part of the loop, that takes input from the user regarding what sort of password cracking task they want to perform
    choice_flag=1
    while choice_flag==1:
        cracked_flag=1
        choice=str(input("Do you want to check the password against a\n 1)hash-wordlist\n \t or\n 2)just a hash\n"))

        #this choice is if the user wants to check the password against a hash-wordlist
        if choice == '1':
            hashdocname=str(input("Enter the name of the hash-wordlist document in .txt format\n"))
            extensioncheck(hashdocname)
            hashes=hashlist(hashdocname)
            option=str(input("Do you want to \n 1)Use the build-in wordlist\n \t or \n 2)Provide your own wordlist\n"))
            if option == '1':
                words=snowlist(snow)
            if option == '2':
                docname=str(input("Enter the name of the wordlist document .txt format\n"))
                extensioncheck(docname)
                words=wordlist(docname)
            if option != '1' and option != '2':
                print("Invalid word list choice")
            mangledlist=mangling(words)
            cracked_flag=passwordcheck_list(mangledlist,hashes)
            if cracked_flag != 0:
                print("Sorry, the password was not found in the wordlist, please use a different wordlist")
            choice_flag=0
            sys.exit()


        #this choice is if the user wants to check the password against a hash input
        if choice == '2':
            hashinput=str(input("Enter the hash of the password to be cracked\n"))
            option=str(input("Do you want to \n 1)Use the build-in wordlist\n \t or \n 2)Provide your own wordlist\n"))
            if option == '1':
                words=snowlist(snow)
            if option == '2':
                docname=str(input("Enter the name of the wordlist document .txt format\n"))
                extensioncheck(docname)
                words=wordlist(docname)
            if option != '1' and option != '2':
                print("Invalid word list choice")
            mangledlist=mangling(words)
            cracked_flag=passwordcheck_hash(mangledlist,hashinput)
            if cracked_flag != 0:
                print("Sorry, the password was not found in the wordlist, please use a different wordlist")
            choice_flag=0
            sys.exit()


        else:
            print("Invalid choice")
            choice_flag=1

except FileNotFoundError:
    print("The document name that you have entered does not exist, please try again with the proper name")
except ValueError:
    print("The code encountered an error in passing an argument to a function")
except EOFError:
    print("There was an error encountered when taking an input from you. Sorry, please try again!")
##except IOError:
##    print("The code encountered an error when trying to open the file")
except KeyboardInterrupt:
    print("You have over-ridden the processing of this code and cancelled the password cracking operation. Bye!")
except NameError:
    print("You have entered an invalid input, please try again properly!")
#except:
 #   print("Oops sorry, the code ran into some unexpected error!")
