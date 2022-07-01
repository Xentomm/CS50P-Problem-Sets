def main():
    ans = input("File name: ").lower().split(sep = '.')
    check(ans[1])

def check(a):
    if a == "gif":
        print("image/gif")
    elif a == "jpg" or a == "jpeg":
        print("image/jpeg")
    elif a == "png":
        print("image/png")
    elif a == "pdf":
        print("application/pdf")
    elif a == "txt":
        print("text/plain")
    elif a == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

main()