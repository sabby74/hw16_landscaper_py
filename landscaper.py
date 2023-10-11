total = 0
day = 0

tools = [
    {
        'name': 'teeth',
        'owned': True,
        'equipped': True,
        'cost': 0,
        'income': 1
    },
    {
        'name': 'rusty scissors',
        'owned': False,
        'equipped': False,
        'cost': 5,
        'income': 5
    },
    {
        'name': 'push lawnmower',
        'owned': False,
        'equipped': False,
        'cost': 25,
        'income': 50
    },
    {
        'name': 'battery-powered lawnmower',
        'owned': False,
        'equipped': False,
        'cost': 250,
        'income': 100
    },
    {
        'name': 'starving students',
        'owned': False,
        'equipped': False,
        'cost': 500,
        'income': 250
    },
]

print()
print('<------------------------LANDSCAPER GAME------------------------>')
print()
print( '                Welcome to the landscaper game!')
print()
print("                       Here's how to play:")
print()
print('1)You start with $0 and a pair of teeth')
print('2)You start by cutting grass with your teeth and make $1 a day.')
print('3)To win you need to own starving students and have $1000')
print("4)You can't buy a tool if you don't have enough money")
print('5)You can only equip one tool at a time')
print('6)You can access your inventory at any time')
print('7)You can only upgrade to the next tool')
print('        --------------------Good luck!--------------------')
print()


def equip(idx):
    eq = int(input('Would you like to equip this item? (1 = Yes, 0 = No): '))
    while eq != 0 and eq != 1:
        eq = int(input('Invalid, please choose 1 or 0: '))
    if eq == 1:
        for tool in tools:
            tool['equipped'] = False
        tools[idx]['equipped'] = True


