"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
 contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use
 of "and" when writing out numbers is in compliance with British usage.
"""

number_words = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty",
                "sixty", "seventy", "eighty", "ninety"]


def transcriptinferieur100(n):
    if n < 21:
        return number_words[n-1]
    elif n < 30:
       return number_words[19] + number_words[n-20-1]
    elif n == 30:
        return number_words[20]
    elif n < 40:
        return number_words[20] + number_words[n-30-1]
    elif n == 40:
        return number_words[21]
    elif n < 50:
        return number_words[21] + number_words[n-40-1]
    elif n == 50:
        return number_words[22]
    elif n < 60:
        return number_words[22] + number_words[n-50-1]
    elif n == 60:
        return number_words[23]
    elif n < 70:
       return number_words[23] + number_words[n-60-1]
    elif n == 70:
        return number_words[24]
    elif n < 80:
        return number_words[24] + number_words[n-70-1]
    elif n == 80:
        return number_words[25]
    elif n < 90:
        return number_words[25] + number_words[n-80-1]
    elif n == 90:
        return number_words[26]
    else:
        return number_words[26] + number_words[n-90-1]

def transcriptsuperieur100(n):
    if n % 100 == 0:
        return number_words[int(str(n)[0]) - 1] + "hundred"
    else:
        return number_words[int(str(n)[0])-1] + "hundred" +"and" + transcriptinferieur100(int(str(n)[1:]))

def counttranscript():
    numberletters = 0
    for n in range(1,1001):
        if n < 100:
            numberletters += len(transcriptinferieur100(n))
            print(n, transcriptinferieur100(n), len(transcriptinferieur100(n)))
        elif n < 1000:
            numberletters += len(transcriptsuperieur100(n))
            print(n, transcriptsuperieur100(n), len(transcriptsuperieur100(n)))
        else:
            numberletters += len("one"+"thousand")
            print(n, "onethousand", len("one"+"thousand"))
    return(numberletters)