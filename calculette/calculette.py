def main():
    with open("input.txt") as f:
        content = f.readlines()

    content = [int(x) for x in content]

    a = 0
    for x in content:
        a = a + x
    
    r = open("result.txt", "w+")
    r.write("result is %s" % a)


if __name__ == "__main__":
    main()