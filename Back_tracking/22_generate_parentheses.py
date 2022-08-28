# back tracking solution
def generateParenthesis(n: int) -> list[str]:
        res = ['()']
        for i in range(1,n):
            new_res = []
            for j in range(len(res)):
                item = [ s for s in res[j] ]
                for k in range(len(item)+1):
                    new_item = item[::]
                    new_item.insert(k,'()')
                    new_item = ''.join(new_item)
                    if new_item not in new_res:
                        new_res.append(new_item)
            res = new_res
        return res




# '(' -> open
# ')' -> close
# max -> max number of a open can appear 

def backtrack(lst, str, open, close, max):
    print(str,lst)
    if len(str) == max*2:
        lst.append(str)
        return
    if open < max:
        backtrack(lst,str+'(',open+1,close,max)
    if close < open:
        backtrack(lst,str+')',open,close+1,max)

def generateParenthesis(n: int) -> list[str]:
    lst = []
    backtrack(lst,'',0,0,n)
    return lst

res = generateParenthesis(3)
print(res)
