def letterCombinations(digits: str) -> list[str]:
        digits_dict = dict()
        digits_dict['2'] = ['a','b','c']
        digits_dict['3'] = ['d','e','f']
        digits_dict['4'] = ['g','h','i']
        digits_dict['5'] = ['j','k','l']
        digits_dict['6'] = ['m','n','o']
        digits_dict['7'] = ['p','q','r','s']
        digits_dict['8'] = ['t','u','v']
        digits_dict['9'] = ['w','x','y','z']
        res = []
        for i in range(len(digits)):
            if i == 0:
                res = digits_dict[digits[i]]
            else:
                res = [ res[x]+digits_dict[digits[i]][j] for x in range(len(res)) for j in range(len( digits_dict[digits[i]])) ]
        return res


letterCombinations('23')

