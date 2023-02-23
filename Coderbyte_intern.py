def StringChallenge(strParam):
    nums = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    operators = ["minus", "plus"]
    temp = 0
    nums_keys = list(nums.keys())
    resultstr = ""
    n1, n2 = 0, 0
    next_operation = 0
    for i in range(len(strParam)+1):
        test = strParam[temp:i]
        if test in nums_keys:
            resultstr += str(nums[strParam[temp:i]])
            temp = i
            if i == len(strParam):
                if next_operation != 0:
                    n2 = int(resultstr)
                    resultstr = ""

                if next_operation == 1:
                    n1 = n1+n2
                    n2 = 0
                if next_operation == 2:
                    n1 = n1-n2
                    n2 = 0

        if test == "plus":
            if next_operation != 0:
                n2 = int(resultstr)
                resultstr = ""

                if next_operation == 1:
                    n1 = n1+n2
                    n2 = 0
                if next_operation == 2:
                    n1 = n1-n2
                    n2 = 0
            if len(resultstr) != 0:
                n1 = int(resultstr)
                resultstr = ""
            next_operation = 1
            temp = i
        if test == "minus":
            if next_operation != 0:
                n2 = int(resultstr)
                resultstr = ""

                if next_operation == 1:
                    n1 = n1+n2
                    n2 = 0
                if next_operation == 2:
                    n1 = n1-n2
                    n2 = 0

            if len(resultstr) != 0:
                n1 = int(resultstr)
                resultstr = ""
            next_operation = 2
            temp = i
    print(n1)
    # code goes here
    return Convert_to_string(n1)


def Convert_to_string(n):
    nums = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
            "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    nums_keys = list(nums.keys())
    result_str = ""
    if n < 0:
        result_str += "negative"

    num = str(n)
    for i in num:
        if i in nums_keys:
            result_str += nums[i]
    return result_str


# keep this function call here
print(StringChallenge(input()))
# 1. For input "foursixminustwotwoplusonezero" the output was incorrect. The correct output is threefour

# 2. For input "twoplustwoplusthree" the output was incorrect. The correct output is seven
#
# 3. For input "twoplustwoplusthreeminusseven" the output was incorrect. The correct output is zero
#
# 4. For input "eightplustwominusfive" the output was incorrect. The correct output is five
#
# 5. For input "twotwothreepluseightseven" the output was incorrect. The correct output is threeonezero
#
# 6. For input "oneminusoneminusone" the output was incorrect. The correct output is negativeone
#
