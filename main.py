

germany_males = [
  1759155,
  1753582,
  1791604,
  2000873,
  2144613,
  2522689,
  2484654,
  2442247,
  2335539,
  3108115,
  3574731,
  3185065,
  2649114,
  2270878,
  1736102,
  3815241]

germany_females = [
  1668224,
  1663249,
  1697303,
  1908819,
  2077483,
  2457963,
  2437668,
  2424908,
  2309166,
  3037162,
  3467097,
  3169989,
  2743333,
  2442225,
  1972407,
  5542819]


india_males = [
  61917556,
  61998098,
  62172011,
  62051890,
  59827896,
  55312148,
  51825020,
  48131760,
  44241036,
  39354854,
  32879891,
  26797259,
  21048863,
  15690047,
  10906951,
  11240803]

india_females = [
  54981938,
  54683905,
  54732361,
  54635318,
  52948119,
  49979399,
  47784588,
  45014795,
  42034977,
  37986002,
  32034808,
  26461589,
  21170943,
  16261149,
  11875730,
  13954207]

germany_total = 80594017
india_total = 1281935911

print("------GERMANY MALES------")
i = 0;
for person in germany_males:
  out = str(person/germany_total)
  out = out[0:6]
  out = out[0:out.find(".")] + out[out.find(".")+1:len(out)]
  out = out[0:3] + '.' + out[3:len(out)]
  out = out[2:len(out)] + "%"
  if i == 0 or i == 5:
    print(str(i) + "-" + str(i+4)+ '  : ' + out)
  if i != 75 and i > 5:
    print(str(i) + "-" + str(i+4)+ ': ' + out)
  if i == 75:
    print(str(i) + "+  : " + out)
  i = i + 5
print("")
print("")

print("------GERMANY FEMALES------")
i = 0;
for person in germany_females:
  out = str(person/germany_total)
  out = out[0:6]
  out = out[0:out.find(".")] + out[out.find(".")+1:len(out)]
  out = out[0:3] + '.' + out[3:len(out)]
  out = out[2:len(out)]+ "%"
  if i == 0 or i == 5:
    print(str(i) + "-" + str(i+4)+ '  : ' + out)
  if i != 75 and i > 5:
    print(str(i) + "-" + str(i+4)+ ': ' + out)
  if i == 75:
    print(str(i) + "+  : " + out)
  i = i + 5
print("")
print("")

print("------INDIA MALES------")
i = 0;
for person in india_males:
  out = str(person/india_total)
  out = out[0:6]
  out = out[0:out.find(".")] + out[out.find(".")+1:len(out)]
  out = out[0:3] + '.' + out[3:len(out)]
  out = out[2:len(out)]+ "%"
  if i == 0 or i == 5:
    print(str(i) + "-" + str(i+4)+ '  : ' + out)
  if i != 75 and i > 5:
    print(str(i) + "-" + str(i+4)+ ': ' + out)
  if i == 75:
    print(str(i) + "+  : " + out)
  i = i + 5
print("")
print("")

print("------INDIA FEMALES------")
i = 0;
for person in india_females:
  out = str(person/india_total)
  out = out[0:6]
  out = out[0:out.find(".")] + out[out.find(".")+1:len(out)]
  out = out[0:3] + '.' + out[3:len(out)]
  out = out[2:len(out)]+ "%"
  if i == 0 or i == 5:
    print(str(i) + "-" + str(i+4)+ '  : ' + out)
  if i != 75 and i > 5:
    print(str(i) + "-" + str(i+4)+ ': ' + out)
  if i == 75:
    print(str(i) + "+  : " + out)
  i = i + 5