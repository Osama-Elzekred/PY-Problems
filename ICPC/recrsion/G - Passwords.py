

def cin(n):
    # function that woks equally to doing cin >> n
    try:
        n[0] = int(input())
        if n[0] == 0:
            return False
        return True
    except:
        return False


def solve(words, rules):

    nums = [i for i in range(10)]

    def createpass(rule_idx, st, rule):
        if rule_idx == len(rule):
            return st

        if rule[rule_idx] == '#':
            for word in words:
                p = createpass(rule_idx+1, st+word, rule)
                if p:
                    print(p)

        if rule[rule_idx] == '0':
            for num in nums:
                p = createpass(rule_idx+1, st+str(num), rule)
                if p:
                    print(p)

    # def generateWord(idx):
    #     while(idx<len(words)):

    #       return words[idx]
    # def generateNum(idx):
    #   pass
    for rule in rules:
        print("--")
        createpass(0, "", rule)


n = [0]
while(cin(n)):
    words = [input() for i in range(n[0])]
    r = int(input())
    rules = [input() for i in range(r)]
    solve(words, rules)
