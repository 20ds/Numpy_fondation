"""if -statement"""
a= int(input("Enter a ::"))
if a>10:
    print(f"Hi ,{a} is greater then 10 ")
    if a<20:
        print(f"{a} is lesser then 20")
    else:
        print(f"{a} is greater then 20")
else: 
    print("cant say")
