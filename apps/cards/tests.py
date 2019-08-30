from django.test import TestCase

# Create your tests here.
if __name__ == '__main__':

    player_dict ={
        10:'WARRIOR',
        9: 'WARLOCK',
        8: 'SHAMAN',
        7: 'ROGUE',
        6: 'PRIEST',
        5: 'PALADIN',
        4: 'MAGE',
        3: 'HUNTER',
        2: 'DRUID',
        0: 'error',
    }


    print(player_dict['2'])