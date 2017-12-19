import populartimes

yourapikey = 'AIzaSyDphmhbitcDQZYu5BG3_uEiKHWOKcsAtLY'
yourapikey2 = ' AIzaSyAJXHl_sPypFNdtsiOWgVqMLICyzL-NcX4 '

#germanbars = populartimes.get(yourapikey2, ["bar"], (48.132986, 11.566126), (48.142199, 11.580047))
rogers = populartimes.get(yourapikey2, ["bar"], (42.0033745,-87.6797645), (42.019816,-87.660634))
len(rogers)
print(rogers)

fnew = open('rogers-bars.txt', 'w')
for item in rogers:
    fnew.write("%s\n" % item)
fnew.close()
