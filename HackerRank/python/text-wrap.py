import textwrap

def wrap(string, max_width):
    print(textwrap.wrap(string,7))
    return textwrap.fill(string,max_width)


print(wrap("hi arijit bhai kemon acho? SunlamSunechi valo acho. anondo kor",7))