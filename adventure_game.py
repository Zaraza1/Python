name = input('Type in your name : ')
print('Welcome', name, 'to this adventure!')
answer = input('You are on a road, it has come to an end... you can turn right or left. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come to a river, you can walk around it or swim across... Type walk to walk and swim to swim? ')
    if answer == 'swim':
        print('You have tried to swim across and were eaten by an alligator...')
    elif answer == 'walk':
        answer = input('After walking for many miles, you find a small hut. Do you enter or continue walking? Type enter to enter or continue to keep walking: ')
        if answer == 'enter':
            print('You enter the hut and find supplies and a map. You use them to find your way home. You Win!')
        elif answer == 'continue':
            print('You continued walking, became hopelessly lost, and never found your way out. You lose.')
        else:
            print('Not a valid option')
    else:
        print('Not a valid option')

elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back? Type in: cross or back.. ')
    if answer == 'back':
        print('You go back and notice a hidden path that was not visible before. Do you take it? Yes or No: ')
        if answer.lower() == 'yes':
            print('The hidden path leads you to a beautiful village where you are welcomed and find a new home. You Win!')
        elif answer.lower() == 'no':
            print('You missed your chance to escape the forest. Night falls, and you are lost forever. You lose.')
        else:
            print('Not a valid option')
    elif answer == 'cross':
        answer = input('You crossed the bridge and meet a stranger... Do you talk to them? Yes or No: ')
        if answer == 'yes':
            print('You talked to the stranger and he gave you a treasure map. Following it, you find gold and make it home rich. You Win!')
        elif answer == 'no':
            print('You ignore the stranger and continue your way. Eventually, you find a road leading home. You Win, but you always wonder about the stranger.')
        else:
            print('Not a valid option')
    else:
        print('Not a valid option')
else:
    print('Not a valid option')

print('Thank you for playing', name, '!')
