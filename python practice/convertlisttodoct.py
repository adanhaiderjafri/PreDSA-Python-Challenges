# keys = ["name", "age", "city"]
# values = ["Adan", 21, "Karachi"]
def reverseArray(a):
    # Write your code here
    left = 0
    right = len(a)-1
    while  left < right:
        reverseArray[left] ,  reverseArray[right] = reverseArray[right] , reverseArray[left]
        
        
a = [1,2,3,4,5]
print(reverseArray(a))
