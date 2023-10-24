def reverse_text(text_as_string):
    n = len (text_as_string)
    while n>0:
        yield text_as_string[n-1]
        n-=1

for char in reverse_text("step"):
    print(char, end= "")