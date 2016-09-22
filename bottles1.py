def beer_song(num_beers):


    while num_beers > 0:

    #convert to string
        str_number = str(num_beers)

        print(str_number + " bottles of beer on the wall")
        print(str_number + " bottles of beer")
        print("if one of those bottles should happen to fall")
    #convert to string
        num_beers -= 1
        str_number = str(num_beers)
        print(str_number + "bottles of beer on the wall")


beer_song(99)
