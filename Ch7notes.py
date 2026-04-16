#Ch 7 Files

#example = open("file_name", "model") parameters to open a file
                                     #mode is how we want to open a file

f = open("measures.txt", "r") #r means we read the file without editing it

line = f.readline() #only displays single lines in the text file
line = line.rstrip() #gets rid of automatic \n after readline()
print(line)

line = f.readline() #This will read the next line in the file
print(line)

line = f.readlines() #making it plural reads all the lines into a list
print(line)
print(line[0:2]) #because they're lists, we can index
                 #using 0:1 only includes \n, you need 2 to get the next full item

#Exercise
line = f.readlines()
line_list = []

for i in range(len(line)):
    item = line[i].rstrip("\n") #strips all individual items
    line_list.append(item) #appends the stripped item into the list

print(line_list)

#OR
line_list2 = []

for i in line: #works because our line is already a list
    i = i.rstrip("\n")
    line_list2.append(i) #appends the new value in i to the list

print(line_list)

'''#readline, readlines, read, repetition
f = open("measures.txt", "r")

for line in f:
    lines = line.rstrip()
    print(float(lines) + 5) #prints each line as a single item
                            #making it a float lets us treat the items as numbers

#Exercise 2
sum = 0
n = 0

for line in f:
    line = line.rstrip("\n")
    if line != "":
        sum += float(line)
        n += 1
print(round(sum/n, 2))'''

#4 Ways to read a file
f = open("test.txt", 'r') #reading
line = f.readline() #reads one line
line = f.readlines() #reads all lines
line = f.read() #reads the whole file

for i in f:
    i = i.rstrip("\n")
    print(i) #Prints the file through repitition

#Exercise 3
f = open("test.txt", "r")

result = "" #creating an empty string means that we can put the items into a string instead of a list

for line in f:
    clean_line = line.strip("\n")
    if clean_line:
        result += clean_line + " " #concatinates the cleaned line to the result string

print(result)

#Writing to a file
f = open("test.txt", "w") #writing mode
print("Happy","Friday", file = f, sep = "\n") #prints the string to the specified file
                                              #overrides file contents
f.close()

f2 = open("test.txt", 'r')
print(f2.read()) #shows the file has been overwritten

#Creating files
f3 = open("exercise.txt", "w") #creates the exercise file
print("This is an example", file = f3)

#Splitting strings
string = "a-b-c"
output = string.split("-") #splits the items by - and puts them in a list

#Exercise 4
f = open("sales.txt", "r") #opens the file to read
f2 = open("sales.txt", "w") #opens the file to write

for line in f: #for every line in the file
    line = line.rstrip("\n") #the line will have \n stripped
    output = line.split(" ") #and will be split according to their spaces
    print(output) #prints the list output
    print(output, file = f2) #takes the output and prints it to f2

#Append files
f = open("sales.txt", "a")
print("Happy Friday", file = f)

#IDK
'''entry = int(input("A number: "))
num = int(entry)

print(num)'''

#Exercise 5
number = ""
while number.isalpha or len(number) != 1:
    number = input("A number: ")
    if number.isdigit() and len(number) == 1:
        print(number)
        break
    elif number.isalpha() or len(number) != 1:
        print("Please enter a single digit number")

#Try and except
entry = input("A number: ")
try: #if the input can be converted to an int, it'll "try" this part of the code
    num = int(entry)
    print(num)
except: #returns an error message if the input can't be converted to an int
    print("invalid number")

#Exercise 6
try:
    f = open("none.txt", 'r')
    lines = f.readlines()
    print(lines)
except:
    print("File does not exist")

#String vs Tuples
l = ['a', 'b', 'c'] #list values can be changed
print(l)
l[0] = "x"

t = ('a', 'b', 'c')
#t[0] = 'x' tuple values can't be changed

















