# Defining constants.
HIGHEST_NORTH_AMERICA_SCORE = 100
HIGHEST_EUROPE_SCORE = 94.1
HIGHEST_ASIA_SCORE = 89.8
HIGHEST_AUSTRALIA_SCORE = 83.7
HIGHEST_SOUTH_AMERICA_SCORE = 81.6
HIGHEST_AFRICA_SCORE = 77.2


def categorizeTopUni(universityFile):
    # Opening file "TopUni.csv"
    topUni = open(universityFile, "r")

    # Creating lists.
    allTopUniLines = []
    iRankNum = []
    institutionNameNum = []
    countries = []
    nRankNum = []
    scores = []

    # Setting each category into their own list part.
    for topUniLines in topUni:
        topUniLineParts = topUniLines.strip().split(",")
        iRankNum.append(topUniLineParts[0])
        institutionNameNum.append(topUniLineParts[1])
        countries.append(topUniLineParts[2].upper())
        nRankNum.append(topUniLineParts[3])
        other = topUniLineParts[4:7]
        scores.append(topUniLineParts[8])

    # Closing "TopUni.csv".
    topUni.close()

    # Returning each list.
    return (allTopUniLines, countries, iRankNum, institutionNameNum, nRankNum, scores)


def categorizeCapitals(capitalsFile):
    # Opening files "capitals.csv"
    capitals = open(capitalsFile, "r")

    # Creating lists
    capitalNames = []
    capitalCountry = []
    capitalContinents = []

    # Setting each category into their own list part.
    for capitalsLines in capitals:
        capitalsLineParts = capitalsLines.strip().split(",")
        capitalCountry.append(capitalsLineParts[0].upper())
        capitalNames.append(capitalsLineParts[1].upper())
        capitalContinents.append(capitalsLineParts[5].upper())

    # Closing "capitals.csv".
    capitals.close()

    # Returning each list.
    return (capitalNames, capitalCountry, capitalContinents)


def countUni(universityFile):
    # Creating a try and except for opening the file.
    topUni = open(universityFile, "r")

    # Counting the lines in the topUni file while also subtracting 1 for the first line containing the categories.
    count = len(topUni.readlines()) - 1
    topUni.close()

    # Returning the total number of universities.
    return "Total number of universities => %d" % (count)


def availCountriesContinents(universityFile, capitalsFile):
    topUni = open(universityFile, "r")
    # Calling the categorizeCapitals functions.
    (_, capitalCountry, capitalContinents) = categorizeCapitals(capitalsFile)

    # Creating lists.
    countries = []
    continents = []

    # Iterating through the lines in topUni to create a list of countries with no duplicates.
    for topUniLines in topUni:
        topUniLineParts = topUniLines.strip().split(",")
        country = topUniLineParts[2].upper()
        if country not in countries:
            countries.append(country)

    # Iterating through the list of countries to find the position of each country's continent and to return a unique list.
    for i in range(1, len(countries)):
        index = capitalCountry.index(countries[i])
        if capitalContinents[index] not in continents:
            continents.append(capitalContinents[index])
    if "AFRICA" not in continents and "AFRICA" in capitalContinents:
        continents.append("AFRICA")
    elif "SOUTH AMERICA" not in continents and "SOUTH AMERICA" in capitalContinents:
        continents.append("SOUTH AMERICA")

    topUni.close()

    # Creating a cleaner output look.
    availCountries = ", ".join(countries[1:])
    availContinents = ", ".join(continents)

    # Returning the available countries and continents.
    return "Available countries => %s" % availCountries + "\nAvailable continents => %s" % availContinents


def info(selectedCountry, universityFile, capitalsFile):
    topUni = open(universityFile, "r")
    # Calling the categorizeTopUni and categorizeCapitals functions.
    (allTopUniLines, countries, iRankNum, institutionNameNum, nRankNum, scores) = categorizeTopUni(universityFile)
    (_, capitalCountry, capitalContinents) = categorizeCapitals(capitalsFile)

    # Creating list and defining variables.
    highestContinentScore = []
    countryCount = 0
    totalSelectedCountryScore = 0

    # Find position of selected country.
    countryIndex = countries.index(selectedCountry)
    # Find selected institution using the position of the selected country.
    selectedInstitution = institutionNameNum[countryIndex].upper()

    # Iterate through the lists to find total country score, country count, and the national institution name under certain conditions.
    for i in range(1, len(topUni.readlines())):
        k = countries[i]
        j = nRankNum[i]
        if k.upper() == selectedCountry.upper():
            if j == "1":
                nationalInstitutionName = institutionNameNum[i].upper()
            totalSelectedCountryScore += float(scores[i])
            countryCount += 1

    # Compute average country score.
    averageSelectedCountryScore = totalSelectedCountryScore / countryCount

    # Find selected continent.
    selectedContinent = capitalContinents[capitalCountry.index(selectedCountry)]

    # Find the highest continent score correlating with the selected country.
    if "NORTH AMERICA" == selectedContinent:
        highestContinentScore = HIGHEST_NORTH_AMERICA_SCORE
    elif "EUROPE" == selectedContinent:
        highestContinentScore = HIGHEST_EUROPE_SCORE
    elif "ASIA" == selectedContinent:
        highestContinentScore = HIGHEST_ASIA_SCORE
    elif "AUSTRALIA" == selectedContinent:
        highestContinentScore = HIGHEST_AUSTRALIA_SCORE
    elif "SOUTH AMERICA" == selectedContinent:
        highestContinentScore = HIGHEST_SOUTH_AMERICA_SCORE
    elif "AFRICA" == selectedContinent:
        highestContinentScore = HIGHEST_AFRICA_SCORE

    # Compute relative score.
    relativeScore = averageSelectedCountryScore / highestContinentScore * 100

    topUni.close()

    # Returning international rank with university name, national rank with university name, average score, and relative score.
    return "At international rank => %d the university name is => %s" % (countryIndex, selectedInstitution) + \
           "\nAt national rank => 1 the university name is => %s" % (nationalInstitutionName) + \
           "\nThe average score => %.2f" % averageSelectedCountryScore + \
           "\nThe relative score to the top university in %s is => (%.2f/%.2f) x100" \
           % (selectedContinent, averageSelectedCountryScore, highestContinentScore) + "%" \
           + " = %.2f" % relativeScore + "%"


def capitalInfo(selectedCountry, universityFile, capitalsFile):
    # Opening files "TopUni.csv" and "capitals.csv.
    topUni = open(universityFile, "r")
    capitals = open(capitalsFile, "r")

    # Calling the categorizeTopUni and categorizeCapitals function.
    (capitalNames, capitalCountry, capitalContinents) = categorizeCapitals(capitalsFile)
    (allTopUniLines, _, _, institutionNameNum, _, _) = categorizeTopUni(universityFile)

    # Creating list.
    capitalUniversities = []

    # Finding the country capital using country index.
    countryIndex = capitalCountry.index(selectedCountry)
    selectedCountryCapital = capitalNames[countryIndex].upper()

    # Iterate through the lists to find total capital universities.
    for n in range(1, len(topUni.readlines())):
        k = selectedCountryCapital.upper()
        r = institutionNameNum[n].upper()
        if k in r:
            capitalUniversities.append(r)

    # Creating an empty string for result in the upcoming for loop.
    result = ""
    # Iterate through the length of capital universities to create a clean output.
    for k in range(0, len(capitalUniversities)):
        result += ("\t#%d %s\n" % (k + 1, capitalUniversities[k]))

    # Closing files "TopUni.csv" and "capitals.csv
    topUni.close()
    capitals.close()

    # Returning the capital and the universities that include the capital.
    return "The capital is => %s" % selectedCountryCapital \
           + "\nThe universities that contain the capital name =>" \
           + "\n" + result


def getInformation(selectedCountry, universityFile, capitalsFile):
    # Opening files "TopUni.csv" and "capitals.csv, if they exist.
    try:
        topUni = open(universityFile, "r")
    except FileNotFoundError:
        print("File not found.")
        exit()
    try:
        capitals = open(capitalsFile, "r")
    except FileNotFoundError:
        print("File not found.")
        exit()
    # Uppercase the entry of selectedCountry.
    selectedCountry = selectedCountry.upper()
    # Calling the previously created functions into lines for the output.
    l1 = countUni(universityFile)
    l2To3 = availCountriesContinents(universityFile, capitalsFile)
    l4To7 = info(selectedCountry, universityFile, capitalsFile)
    l8 = capitalInfo(selectedCountry, universityFile, capitalsFile)
    # Opening the "output.txt" file to write inside.
    out = open("output.txt", "w")
    out.write(str(l1))
    out.write("\n")
    out.write(str(l2To3))
    out.write("\n")
    out.write(str(l4To7))
    out.write("\n")
    out.write(str(l8))

    # Closing "output.txt".
    out.close()
    topUni.close()
    capitals.close()
