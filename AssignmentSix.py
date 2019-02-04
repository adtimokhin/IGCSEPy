# lists


master_list, male, female, band, dj = [], [], [], [], []


def define_artist(artist):
    artist_type = input("enter artist\'s type")
    if len(artist_type) != 1:
        print("entered type should be one character long")
        define_artist(artist)
    if 'M' == artist_type:
        male.append(artist)
        return
    elif 'F' == artist_type:
        female.append(artist)
        return
    elif 'B' == artist_type:
        band.append(artist)
        return
    elif 'D' == artist_type:
        dj.append(artist)
        return
    else:
        print("entered type of artist was not identified")
        define_artist(artist)
        return


def print_list(name, list):
    print("\n{0} :".format(name))
    if len(list) ==0:
        print("none {0}".format(name.lower()))
        return
    for i in list:
        print(i)


for i in range(10): # number 10 is a number of artists
    name = input("enter an artist name")
    master_list.append(name)
    define_artist(name)


print_list("Male vocalists", male)
print_list("Female vocalists", female)
print_list("Bands", band)
print_list("DJs", dj)
