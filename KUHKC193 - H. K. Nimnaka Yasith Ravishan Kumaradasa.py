# Name: H. K. Nimnaka Yasith Ravishan Kumaradasa
# Student ID: KUHKC193
# Subject: CSP1150A

import random

candidate_words = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED',
                   'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED',
                   'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER',
                   'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER',
                   'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN',
                   'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER',
                   'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER',
                   'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER',
                   'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER',
                   'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER',
                   'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR',
                   'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']

#One of the word is the password from this candidate words.

word_count = (random.sample(candidate_words, 8))
password = random.choice(word_count)

print("          ...................................................")
print()
print("\t        - Welcome to the Guess The Word Game -")
print("\t                     *********")
print("          ...................................................")
print()
Guesses = 3
won = False

while Guesses >= 0:
    print("Password is one of these words")
    print('\t...........')
    print()
    print('0'')', word_count[0])
    print('1'')', word_count[1])
    print('2'')', word_count[2])
    print('3'')', word_count[3])
    print('4'')', word_count[4])
    print('5'')', word_count[5])
    print('6'')', word_count[6])
    print('7'')', word_count[7])
    print()

    list1 = []
    for ch in password:
        list1.append(ch[0:])
    # print the count1's part

    print('Guesses Remaining: ', Guesses + 1, 'Terms')

    Guess_Words = int(input('---> Enter Your Guess Here (Enter 0-7): '))
    Guess_Word = word_count[Guess_Words - 1]

    list2 = []
    for sh in Guess_Word:
        list2.append(sh[0:])
    # print the count2's part

    count = 0
    if list1[0] == list2[0]:
        count += 1
    if list1[1] == list2[1]:
        count += 1
    if list1[2] == list2[2]:
        count += 1
    if list1[3] == list2[3]:
        count += 1
    if list1[4] == list2[4]:
        count += 1
    if list1[5] == list2[5]:
        count += 1

    if list1 != list2:
        if Guesses == 3:
            print('BLOCKS')
        else:
            print('STREAKS')
        print('Your Password is Incorrect')
        print(count,'/6 Correct')
        print()
    else:
        print()
        print('CLEARS')
        print('Password is Correct.')
        print()
        print('\tCongratulations!! You Won The Game.')
        break
    Guesses = Guesses - 1
else:
    print('\tYou Loose, Better Luck Next Time!!!.')

    


    
