import populartimes

yourapikey = 'AIzaSyDphmhbitcDQZYu5BG3_uEiKHWOKcsAtLY'
yourapikey2 = 'AIzaSyAJXHl_sPypFNdtsiOWgVqMLICyzL-NcX4'


def poptester(locname, key, type, lower, upper):
    loc = populartimes.get(key, type, lower, upper)
    print('There are '+str(len(loc))+' items from your request\n')
    print('Result below:\n')
    print(loc)
    with open(locname + '.txt', 'w') as fnew:
        for item in loc:
            fnew.write('%s\n' % item)


poptester("rogersbar", yourapikey, ['bar'], (42.0033745,-87.6797645), (42.019816,-87.660634))
poptester("rogersall", yourapikey, [''], (42.0033745,-87.6797645), (42.019816,-87.660634))
#poptester("germanbars", yourapikey, [], (42.0033745,-87.6797645), (42.019816,-87.660634))
