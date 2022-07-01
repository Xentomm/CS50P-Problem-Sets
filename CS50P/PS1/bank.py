import re
def main():
    answer = input().lower()
    new_ans = re.split(',| ', answer)
    print(new_ans)
    money(new_ans[0])

def money(ans):
    if (ans == "hello"):
        print("$0")
    elif(ans[0] == "h"):
        print("$20")
    else:
        print("$100")

main()
