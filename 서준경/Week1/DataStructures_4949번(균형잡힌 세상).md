```python
sentence = input()
while(sentence != "."):
    li = list()
    result = True
    for i in sentence:
        if (i in '[]()'):
            li.append(i)
    # print(li)
    idx = 0
    while(idx < len(li) - 1):
        if (li[idx] == '(' and li[idx + 1] == ')'):
            del li[idx]
            del li[idx]
            idx = 0
        elif (li[idx] == '[' and li[idx + 1] == ']'):
            del li[idx]
            del li[idx]
            idx = 0
        else:
            idx += 1
    print('yes' if len(li) == 0 else 'no')
    sentence = input()
```
