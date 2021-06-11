import random

# target = "My father’s family name being Pirrip, and my Christian name Philip, my infant tongue could make of both names nothing longer or more explicit than Pip. So, I called myself Pip, and came to be called Pip. I give Pirrip as my father’s family name, on the authority of his tombstone and my sister — Mrs. Joe Gargery, who married the blacksmith. As I never saw my father or my mother, and never saw any likeness of either of them (for their days were long before the days of photographs), my first fancies regarding what they were like, were unreasonably derived from their tombstones. The shape of the letters on my father’s, gave me an odd idea that he was a square, stout, dark man, with curly black hair. From the character and turn of the inscription, “Also Georgiana Wife of the Above,” I drew a childish conclusion that my mother was freckled and sickly. To five little stone lozenges, each about a foot and a half long, which were arranged in a neat row beside their grave, and were sacred to the memory of five little brothers of mine — who gave up trying to get a living, exceedingly early in that universal struggle — I am indebted for a belief I religiously entertained that they had all been born on their backs with their hands in their trousers—pockets, and had never taken them out in this state of existence. Ours was the marsh country, down by the river, within, as the river wound, twenty miles of the sea. My first most vivid and broad impression of the identity of things, seems to me to have been gained on a memorable raw afternoon towards evening. At such a time I found out for certain, that this bleak place overgrown with nettles was the churchyard; and that Philip Pirrip, late of this parish, and also Georgiana wife of the above, were dead and buried; and that Alexander, Bartholomew, Abraham, Tobias, and Roger, infant children of the aforesaid, were also dead and buried; and that the dark flat wilderness beyond the churchyard, intersected with dykes and mounds and gates, with scattered cattle feeding on it, was the marshes; and that the low leaden line beyond, was the river; and that the distant savage lair from which the wind was rushing, was the sea; and that the small bundle of shivers growing afraid of it all and beginning to cry, was Pip."

target = "I never go back on my word, because that is my Ninja way."

tempTarget = ""
for character in target:
    if character == '”':
        tempTarget += '\"'
    elif character == "’":
        tempTarget += '\''
    else:
        tempTarget += character

target = tempTarget

characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?\";—!():"


def makeList():
    # returns a list with the same number of characters as the target
    charList = []
    for i in range(len(target)):
        charList.append(random.choice(characters))  # grabs a random character from the character's string
    return charList


def score(myList):
    # returns an integer denoting how many matches the random string has with the target string
    matches = 0
    for i in range(len(target)):
        if myList[i] == target[i]:
            matches += 1
    return matches


def mutate(myList):
    newList = list(myList)  # copies the contents of myList into newList, instead of linking the two together

    randomLetter = random.choice(characters)  # returns a random character
    randomIndex = random.randint(0, len(target) - 1)  # returns a random index
    newList[randomIndex] = randomLetter

    return newList


random.seed()

bestList = makeList()  # bestList is the initial condition list
bestScore = score(bestList)  # the best score is also another initial condition

guesses = 0

while True:
    guess = mutate(bestList)  # mutate() operatees on the initial condition
    guessScore = score(guess)
    # print(guessScore)
    guesses += 1

    if guessScore <= bestScore:
        continue

    print(''.join(guess), guessScore, guesses)

    if guessScore == len(target):
        break

    bestList = list(guess)
    bestScore = guessScore
