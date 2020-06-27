day = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}
gifts = {
    1: "a Partridge in a Pear Tree.",
    2: "two Turtle Doves,",
    3: "three French Hens,",
    4: "four Calling Birds,",
    5: "five Gold Rings,",
    6: "six Geese-a-Laying,",
    7: "seven Swans-a-Swimming,",
    8: "eight Maids-a-Milking,",
    9: "nine Ladies Dancing,",
    10: "ten Lords-a-Leaping,",
    11: "eleven Pipers Piping,",
    12: "twelve Drummers Drumming,"
}


def recite(start_verse, end_verse):
    if end_verse < start_verse:
        raise ValueError('End verse must be greater than start verse')
    lyrics = []
    running_verse = start_verse
    while True:
        verse = ["On the {} day of Christmas my true love gave to me:".format(day[running_verse])]
        for i in range(running_verse, 0, -1):
            if running_verse != 1 and i == 1:
                verse.append('and')
            verse.append(gifts[i])
        lyrics.append(' '.join(verse))
        if running_verse == end_verse:
            break
        else:
            running_verse += 1
    return lyrics

