#file i/0 

# f=open("gh.txt","r")
# # data=f.read()
# # print(data)
# # print(type(data))

# line1=f.readline()#read line by line
# print(line1)

# line2=f.readline()
# print(line2)
# # f.close()

# in case both read and read line is applised then terminal will show blank spaces are raed func

# f=open("gh.txt","a") append will add data on next line
# # f=open("gh.txt","w") w will over right the data
# f.write("\nafter that me")
# f.write("yuor me")


#read the article given
# f=open("gh.txt","w+") # w + will truncate the file data with abc and terminal willread blanks becuse pointer is on blank
# # f=open("gh.txt","r+")
# # f.write("abc") #r+ modes moves the circur after abc and sytem will read from that point

# f.write("abc")
# l=f.read()
# print(l)

# f=open("gh.txt","a+") no truncate but curser is at blank
# f.write("abc")
# l=f.read()

# print(l)

#syntax
# with open("gh.txt","r") as f:#with syntax close is not required 

#     l=f.read()
#     print(l)

# DELETING A FILE

#pip intall file_name
# import os
# os.remove("gh.txt")


# with open("practice.txt","w") as f:
    
    # l=f.write("hi everyone we are learning file io\nwelcome to jumanji \nhello world")


# with open("practice.txt","r") as  f:

#     data=f.read()
# new_data=data.replace("jumanji","python")
# print(new_data)


# with open("practice.txt","w") as f:
#     f.write(new_data)


# k="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if data.find(k):
#         print("exists")
    





# def check_for_line(line_no):
#     word="learning"
#     data= True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
                
#                 return line_no
#             line_no=line_no+1
    
#     return 2
# k=check_for_line()
# # if k ==-1:
#     print(f"the word 'learning' first appears on {k}")
# else:
#     print("you are a nerd")




# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     # print(data)
    


# num=""
# for i in range(len(data)):
        
#         if(data[i])==",":
#             print(int(num))
#             num=""
#         else:
#             num=num+data[i]

# num=data.split(",")
# for val in num:
        
#         if int(val)%2==0:
#             print(count)
#             count+=1
