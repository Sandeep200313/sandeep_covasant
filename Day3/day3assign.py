#Q1

input = [1,2,3, [1,2,3,[3,4],2]]
def flatten(input):
    res=[]
    for ele in input:
        if type(ele)==type(1):
            res.append(ele)
        else:
            res+=flatten(ele)
            
    return res
res=flatten(input)
print(res)


#Q2
#convert(x)          Converts like below 
#                   input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
#                  output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]

lst=[[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
def convert(lst):
    if type(lst)==type('a'):
        return [int(n) for n in lst.strip("()").split(",")]
        
    elif type(lst)==type([]):
        return [convert(item) for item in lst]
        
    return lst
res=convert(lst)
print(res)