############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        # initializing the attributes of the object of the class
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # this method updates the pairings attribute
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    # list of objects
    all_melon_types = []

    # instantiate melon type objects
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberry')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, 'Yellow watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types



def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print("{} pairs with".format(melon.name))
        for pairing in melon.pairings:
            print('- {}'.format(pairing))
        print()

    return

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # looping for code
    melon_type_dict = {}

    for melon in melon_types:
        melon_type_dict[melon.code] = melon

    return melon_type_dict
    

# print_pairing_info(make_melon_types())
# print(make_melon_type_lookup(make_melon_types()))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods
    def __init__(self, type_melon, shape_rating, color_rating, harvested_from, 
                 harvested_by):
        self.type_melon = type_melon
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Sellable if color and shape rating > 5 and didn't come from field 3"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3:
            return True
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    
    # when this fx is called, we are inputing the melon types dictionary
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons_list = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]
    return melons_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable():
            print('Harvested by {} from Field # {} CAN BE SOLD'.format(melon.harvested_by, melon.harvested_from))
        else:
            print('Harvested by {} from Field # {} NOT SELLABLE'.format(melon.harvested_by, melon.harvested_from))

# get_sellability_report(make_melons(make_melon_type_lookup(make_melon_types())))

melon_code_dict = make_melon_type_lookup(make_melon_types())

print(make_melons(make_melon_types()))


