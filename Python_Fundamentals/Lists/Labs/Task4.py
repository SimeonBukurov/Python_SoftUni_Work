n = int(input())
word = input()
string = []
for i in range(n):
    current_word = input()
    string.append(i)
print(string)
for i in range(len(string)-1, -1, -1):
    element = string[i]
    if word not in element:
        string.remove(element)
print(string)