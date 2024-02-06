# authors: Alex Leung & Jose Tellez & Yu-Shiuan Lin

#
# data of countries and capitals
#
# this is a tuple of lists. each element of the tuple is a list of two strings: a country and its capital city
#
countries_and_capitals = (
    ['Afghanistan', 'Kabul'], ['Albania', 'Tirana (Tirane)'], ['Algeria', 'Algiers'], ['Andorra', 'Andorra la Vella'],
    ['Angola', 'Luanda'], ['Antigua and Barbuda', "Saint John's"], ['Argentina', 'Buenos Aires'],
    ['Armenia', 'Yerevan'],
    ['Australia', 'Canberra'], ['Austria', 'Vienna'], ['Azerbaijan', 'Baku'], ['Bahamas', 'Nassau'],
    ['Bahrain', 'Manama'],
    ['Bangladesh', 'Dhaka'], ['Barbados', 'Bridgetown'], ['Belarus', 'Minsk'], ['Belgium', 'Brussels'],
    ['Belize', 'Belmopan'], ['Benin', 'Porto Novo'], ['Bhutan', 'Thimphu'], ['Bolivia', 'Sucre'],
    ['Bosnia and Herzegovina', 'Sarajevo'], ['Botswana', 'Gaborone'], ['Brazil', 'Brasilia'],
    ['Brunei', 'Bandar Seri Begawan'], ['Bulgaria', 'Sofia'], ['Burkina Faso', 'Ouagadougou'], ['Burundi', 'Gitega'],
    ['Cambodia', 'Phnom Penh'], ['Cameroon', 'Yaounde'], ['Canada', 'Ottawa'], ['Cape Verde', 'Praia'],
    ['Central African Republic', 'Bangui'], ['Chad', "N'Djamena"], ['Chile', 'Santiago'], ['China', 'Beijing'],
    ['Colombia', 'Bogota'], ['Comoros', 'Moroni'], ['Congo, Democratic Republic of the', 'Kinshasa'],
    ['Congo, Republic of the', 'Brazzaville'], ['Costa Rica', 'San Jose'],
    ["Cote d'Ivoire (Ivory Coast)", 'Yamoussoukro'],
    ['Croatia', 'Zagreb'], ['Cuba', 'Havana'], ['Cyprus', 'Nicosia'], ['Czech Republic (Czechia)', 'Prague'],
    ['Denmark', 'Copenhagen'], ['Djibouti', 'Djibouti'], ['Dominica', 'Roseau'],
    ['Dominican Republic', 'Santo Domingo'],
    ['East Timor', 'Dili'], ['Ecuador', 'Quito'], ['Egypt', 'Cairo'], ['El Salvador', 'San Salvador'],
    ['England', 'London'], ['Equatorial Guinea', 'Malabo'], ['Eritrea', 'Asmara'], ['Estonia', 'Tallinn'],
    ['Eswatini (Swaziland)', 'Mbabana'], ['Ethiopia', 'Addis Ababa'], ['Federated States of Micronesia', 'Palikir'],
    ['Fiji', 'Suva'], ['Finland', 'Helsinki'], ['France', 'Paris'], ['Gabon', 'Libreville'], ['Gambia', 'Banjul'],
    ['Georgia', 'Tbilisi'], ['Germany', 'Berlin'], ['Ghana', 'Accra'], ['Greece', 'Athens'],
    ['Grenada', "Saint George's"],
    ['Guatemala', 'Guatemala City'], ['Guinea', 'Conakry'], ['Guinea-Bissau', 'Bissau'], ['Guyana', 'Georgetown'],
    ['Haiti', 'Port au Prince'], ['Honduras', 'Tegucigalpa'], ['Hungary', 'Budapest'], ['Iceland', 'Reykjavik'],
    ['India', 'New Delhi'], ['Indonesia', 'Jakarta'], ['Iran', 'Tehran'], ['Iraq', 'Baghdad'], ['Ireland', 'Dublin'],
    ['Israel', 'Jerusalem'], ['Italy', 'Rome'], ['Jamaica', 'Kingston'], ['Japan', 'Tokyo'], ['Jordan', 'Amman'],
    ['Kazakhstan', 'Nur-Sultan'], ['Kenya', 'Nairobi'], ['Kiribati', 'Tarawa Atoll'], ['Kosovo', 'Pristina'],
    ['Kuwait', 'Kuwait City'], ['Kyrgyzstan', 'Bishkek'], ['Laos', 'Vientiane'], ['Latvia', 'Riga'],
    ['Lebanon', 'Beirut'],
    ['Lesotho', 'Maseru'], ['Liberia', 'Monrovia'], ['Libya', 'Tripoli'], ['Liechtenstein', 'Vaduz'],
    ['Lithuania', 'Vilnius'], ['Luxembourg', 'Luxembourg'], ['Madagascar', 'Antananarivo'], ['Malawi', 'Lilongwe'],
    ['Malaysia', 'Kuala Lumpur'], ['Maldives', 'Male'], ['Mali', 'Bamako'], ['Malta', 'Valletta'],
    ['Marshall Islands', 'Majuro'], ['Mauritania', 'Nouakchott'], ['Mauritius', 'Port Louis'],
    ['Mexico', 'Mexico City'],
    ['Moldova', 'Chisinau'], ['Monaco', 'Monaco'], ['Mongolia', 'Ulaanbaatar'], ['Montenegro', 'Podgorica'],
    ['Morocco', 'Rabat'], ['Mozambique', 'Maputo'], ['Myanmar (Burma)', 'Nay Pyi Taw'], ['Namibia', 'Windhoek'],
    ['Nauru', 'No official capital'], ['Nepal', 'Kathmandu'], ['Netherlands', 'Amsterdam'],
    ['New Zealand', 'Wellington'],
    ['Nicaragua', 'Managua'], ['Niger', 'Niamey'], ['Nigeria', 'Abuja'], ['North Korea', 'Pyongyang'],
    ['North Macedonia (Macedonia)', 'Skopje'], ['Northern Ireland', 'Belfast'], ['Norway', 'Oslo'], ['Oman', 'Muscat'],
    ['Pakistan', 'Islamabad'], ['Palau', 'Melekeok'], ['Panama', 'Panama City'], ['Papua New Guinea', 'Port Moresby'],
    ['Paraguay', 'Asuncion'], ['Peru', 'Lima'], ['Philippines', 'Manila'], ['Poland', 'Warsaw'], ['Portugal', 'Lisbon'],
    ['Qatar', 'Doha'], ['Romania', 'Bucharest'], ['Russia', 'Moscow'], ['Rwanda', 'Kigali'],
    ['Saint Kitts and Nevis', 'Basseterre'], ['Saint Lucia', 'Castries'],
    ['Saint Vincent and the Grenadines', 'Kingstown'],
    ['Samoa', 'Apia'], ['San Marino', 'San Marino'], ['Sao Tome and Principe', 'Sao Tome'], ['Saudi Arabia', 'Riyadh'],
    ['Scotland', 'Edinburgh'], ['Senegal', 'Dakar'], ['Serbia', 'Belgrade'], ['Seychelles', 'Victoria'],
    ['Sierra Leone', 'Freetown'], ['Singapore', 'Singapore'], ['Slovakia', 'Bratislava'], ['Slovenia', 'Ljubljana'],
    ['Solomon Islands', 'Honiara'], ['Somalia', 'Mogadishu'], ['South Africa', 'Pretoria, Bloemfontein, Cape Town'],
    ['South Korea', 'Seoul'], ['South Sudan', 'Juba'], ['Spain', 'Madrid'], ['Sri Lanka', 'Colombo'],
    ['Sudan', 'Khartoum'],
    ['Suriname', 'Paramaribo'], ['Sweden', 'Stockholm'], ['Switzerland', 'Bern'], ['Syria', 'Damascus'],
    ['Taiwan', 'Taipei'], ['Tajikistan', 'Dushanbe'], ['Tanzania', 'Dodoma'], ['Thailand', 'Bangkok'], ['Togo', 'Lome'],
    ['Tonga', "Nuku'alofa"], ['Trinidad and Tobago', 'Port of Spain'], ['Tunisia', 'Tunis'], ['Turkey', 'Ankara'],
    ['Turkmenistan', 'Ashgabat'], ['Tuvalu', 'Funafuti'], ['Uganda', 'Kampala'], ['Ukraine', 'Kiev'],
    ['United Arab Emirates', 'Abu Dhabi'], ['United Kingdom', 'London'], ['United States', 'Washington D.C.'],
    ['Uruguay', 'Montevideo'], ['Uzbekistan', 'Tashkent'], ['Vanuatu', 'Port Vila'], ['Vatican City', 'Vatican City'],
    ['Venezuela', 'Caracas'], ['Vietnam', 'Hanoi'], ['Wales', 'Cardiff'], ['Yemen', "Sana'a"], ['Zambia', 'Lusaka'],
    ['Zimbabwe', 'Harare'])

#
# data of countries
#
# this is a tuple of strings. each element of the tuple is a string: the name of a country
#
countries = (
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
    'Australia',
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi',
    'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
    'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica',
    "Cote d'Ivoire (Ivory Coast)",
    'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic',
    'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Eritrea', 'Estonia',
    'Eswatini (Swaziland)', 'Ethiopia', 'Federated States of Micronesia', 'Fiji', 'Finland', 'France', 'Gabon',
    'Gambia',
    'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
    'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica',
    'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
    'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia',
    'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco',
    'Mongolia',
    'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
    'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia (Macedonia)', 'Northern Ireland', 'Norway', 'Oman',
    'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
    'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles',
    'Sierra Leone',
    'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
    'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
    'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
    'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia', 'Zimbabwe')

#
# data of capitals
#
# this is a tuple of strings. each element of the tuple is a string: the name of a capital city
#
capitals = (
    'Kabul', 'Tirana (Tirane)', 'Algiers', 'Andorra la Vella', 'Luanda', "Saint John's", 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto Novo',
    'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasilia', 'Bandar Seri Begawan', 'Sofia', 'Ouagadougou', 'Gitega',
    'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', "N'Djamena", 'Santiago', 'Beijing', 'Bogota', 'Moroni',
    'Kinshasa', 'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb', 'Havana', 'Nicosia', 'Prague', 'Copenhagen',
    'Djibouti', 'Roseau', 'Santo Domingo', 'Dili', 'Quito', 'Cairo', 'San Salvador', 'London', 'Malabo', 'Asmara',
    'Tallinn', 'Mbabana', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville', 'Banjul', 'Tbilisi',
    'Berlin', 'Accra', 'Athens', "Saint George's", 'Guatemala City', 'Conakry', 'Bissau', 'Georgetown',
    'Port au Prince',
    'Tegucigalpa', 'Budapest', 'Reykjavik', 'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Dublin', 'Jerusalem', 'Rome',
    'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa Atoll', 'Pristina', 'Kuwait City', 'Bishkek',
    'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo',
    'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako', 'Valletta', 'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City',
    'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo', 'Nay Pyi Taw', 'Windhoek',
    'No official capital',
    'Kathmandu', 'Amsterdam', 'Wellington', 'Managua', 'Niamey', 'Abuja', 'Pyongyang', 'Skopje', 'Belfast', 'Oslo',
    'Muscat', 'Islamabad', 'Melekeok', 'Panama City', 'Port Moresby', 'Asuncion', 'Lima', 'Manila', 'Warsaw', 'Lisbon',
    'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre', 'Castries', 'Kingstown', 'Apia', 'San Marino', 'Sao Tome',
    'Riyadh', 'Edinburgh', 'Dakar', 'Belgrade', 'Victoria', 'Freetown', 'Singapore', 'Bratislava', 'Ljubljana',
    'Honiara',
    'Mogadishu', 'Pretoria, Bloemfontein, Cape Town', 'Seoul', 'Juba', 'Madrid', 'Colombo', 'Khartoum', 'Paramaribo',
    'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangkok', 'Lome', "Nuku'alofa", 'Port of Spain',
    'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala', 'Kiev', 'Abu Dhabi', 'London', 'Washington D.C.',
    'Montevideo',
    'Tashkent', 'Port Vila', 'Vatican City', 'Caracas', 'Hanoi', 'Cardiff', "Sana'a", 'Lusaka', 'Harare')


def how_many_countries():
    """
    How many countries.

    Example output:
    200

    :return: The number of countries (integer)
    """
    #
    # count how many countries:
    # 1. check if the length of countries tuple is not 0
    # 2. if #1 is true, assign the length of countries tuple
    # 3. if #1 is false, print length of countries tuple cannot be 0
    #

    # assign None as a placeholder value to number_of_countries
    number_of_countries = None

    # if length of countries is not 0
    if len(countries) != 0:
        # assign length of countries tuple
        number_of_countries = len(countries)
    # otherwise, if the above conditions are not satisfied
    else:
        # print length of countries tuple cannot be 0
        print("length of countries tuple cannot be 0")

    # return the number of countries
    return number_of_countries


def get_name_of_longest_country():
    """
    Get name of longest country.

    Example output:
    Congo, Democratic Republic of the

    :return: The name of the longest country (string)
    """
    #
    # get name of longest country:
    # 1. iterate over countries tuple
    # 2. check if length of current country is greater than 0
    # 3. check if length of current country is greater than longest country size
    # 4. if #2 is true and index is 0, then assign the current country name and its length
    # 5. if #2 is false and index is 0, then assign 0
    # 6. if #3 is true and index is not 0, then assign the current country name and its length
    #

    # assign None as placeholder value for name_of_longest_country
    name_of_longest_country = None

    # assign None as placeholder value for longest_country_size
    longest_country_size = None

    # index variable for while loop
    i = 0

    # while loop with condition i < len(countries)
    while i < len(countries):
        # if index is 0 and length of current country is greater than 0
        if i == 0 and len(countries[i]) > 0:
            # assign length of current country to longest_country_size
            longest_country_size = len(countries[i])

            # assign current country name
            name_of_longest_country = countries[i]
        # if index is 0 and length of current country is not greater than 0
        elif i == 0 and not len(countries[i]) > 0:
            # assign 0 to longest_country_size
            longest_country_size = 0
        # if index is not 0 and length of current country is greater than longest country size
        elif i != 0 and len(countries[i]) > longest_country_size:
            # assign the length of the current country
            longest_country_size = len(countries[i])

            # assign the current country name
            name_of_longest_country = countries[i]
        # otherwise, if the above conditions are not satisfied
        else:
            # print length of country is smaller than longest country
            print("length of country is smaller than longest country")

        # increment index by 1
        i += 1

    # return the name of the longest country
    return name_of_longest_country


def get_number_of_capitals_containing(substring):
    """
    Get number of capitals containing substring.

    Example output:
    75

    :param substring: The substring to search for (string)
    :return: The number of capitals containing the substring (integer)
    """
    #
    # get number of capitals containing the substring:
    # 1. go through each index value in capitals tuple
    # 2. check the lowercase version of the substring against the lowercase version of the current index value
    # 3. if #2 is true and index is 0, then assign 1
    # 4. if #2 is false and index is 0, then assign 0
    # 5. if #2 is true and index is not 0, then add 1
    # 6. otherwise, if #3, #4, and #5 is false, print does not exist in current index value
    #

    # assign None as placeholder value for number_of_capitals
    number_of_capitals = None

    # index variable for while loop
    i = 0

    # while loop with condition i < len(capitals)
    while i < len(capitals):
        # if index is 0 and the substring exists in i'th index value of capitals (lowercase version check)
        if i == 0 and substring.lower() in capitals[i].lower():
            # assign 1 to number_of_capitals
            number_of_capitals = 1
        # if index is 0 and substring does not exist in the i'th index value of capitals (lowercase version check)
        elif i == 0 and not substring.lower() in capitals[i].lower():
            # assign 0 to number_of_capitals
            number_of_capitals = 0
        # if the substring exists in i'th index value of capitals (lowercase version check)
        elif i != 0 and substring.lower() in capitals[i].lower():
            # add 1 to number_of_capitals
            number_of_capitals += 1
        # otherwise, if the above conditions are not satisfied
        else:
            # print substring does not exist in current index value
            print("substring does not exist in current index value")

        # increment index by 1 every iteration
        i += 1

    # return the number of capitals
    return number_of_capitals


def get_countries_and_capitals_that_start_with_same_letter():
    """
    Get countries and capitals that start with same letter.

    Example output:
    ['Algiers - Algeria', 'Andorra la Vella - Andorra', 'Bridgetown - Barbados', 'Brussels - Belgium',
    'Belmopan - Belize', 'Brasilia - Brazil', 'Bandar Seri Begawan - Brunei', 'Djibouti - Djibouti',
    'Guatemala City - Guatemala', 'Georgetown - Guyana', 'Kuwait City - Kuwait', 'Luxembourg - Luxembourg',
    'Male - Maldives', 'Majuro - Marshall Islands', 'Mexico City - Mexico', 'Monaco - Monaco', 'Maputo - Mozambique',
    'No official capital - Nauru', 'Niamey - Niger', 'Panama City - Panama', 'Port Moresby - Papua New Guinea',
    'San Marino - San Marino', 'Sao Tome - Sao Tome and Principe', 'Singapore - Singapore', 'Seoul - South Korea',
    'Stockholm - Sweden', 'Taipei - Taiwan', 'Tunis - Tunisia', 'Vatican City - Vatican City']

    :return: The countries and capitals that start with the same letter (list of strings)
    """
    #
    # get countries and capitals that start with same letter:
    # 1. iterate over countries and capitals tuple based on rows
    # 2. store the countries and capitals based on the 0th and 1st indices of each row
    # 3. check the first character of each country and capital (lowercase version check)
    # 4. if #3 is true and index is 0, then assign a tuple based on a list that contains the capital followed
    # by the country that is separated by a hyphen
    # 5. if #3 is false and index is 0, then assign an empty tuple
    # 6. if #3 is true and index is not 0, then extend countries_and_capitals with a list containing the
    # capital and country separated by a hyphen
    # 7. if #4, #5 is false, then print capital and country do not start with the same letters
    #

    # assign None as placeholder value for countries_and_capitals_same_letter
    countries_and_capitals_same_letter = None

    # index variable for while loop
    i = 0

    # while loop with condition i < len(countries_and_capitals)
    while i < len(countries_and_capitals):
        # assign the current capital to curr_capitals_temp
        curr_capital_temp = countries_and_capitals[i][1]

        # assign the current country to curr_countries_temp
        curr_country_temp = countries_and_capitals[i][0]

        # if index is 0 and first letter of the current capital is equal to the first letter of the
        # current country (lowercase version check)
        if i == 0 and curr_capital_temp[0].lower() == curr_country_temp[0].lower():
            # assign a tuple based on a list containing the capital and country separated by a hyphen
            countries_and_capitals_same_letter = tuple([f"{curr_capital_temp} - {curr_country_temp}"])
        elif i == 0 and not curr_capital_temp[0].lower() == curr_country_temp[0].lower():
            # assign empty tuple to countries_and_capitals_same_letter
            countries_and_capitals_same_letter = ()
        # if the first character of curr_capital_temp and curr_country_temp are equal
        elif i != 0 and curr_capital_temp[0].lower() == curr_country_temp[0].lower():
            # extend countries and capitals with a hyphen separating them that start with the same letter:
            # 1. convert countries_and_capitals to list (open)
            # 2. extend countries_and_capitals_to_change with a list containing the capital and country separated
            # by a hyphen
            # 3. assign the tuple version of countries_and_capitals_to_change to original tuple variable (close)
            countries_and_capitals_to_change = list(countries_and_capitals_same_letter)
            countries_and_capitals_to_change.extend([f"{curr_capital_temp} - {curr_country_temp}"])
            countries_and_capitals_same_letter = tuple(countries_and_capitals_to_change)
        # otherwise, if the above conditions are not satisfied
        else:
            # print capital and country do not start with the same letter
            print("capital and country do not start with the same letter")

        # increment index by 1 every iteration
        i += 1

    # return the list of countries and capitals with the same letter
    return list(countries_and_capitals_same_letter)


def get_capital_of(country):
    """
    Get capital of country.

    Example output:
    Ottawa

    :param country: The country to search (string)
    :return: The capital of the country (string)
    """
    #
    # get the capital of a country:
    # 1. iterate over countries_and_capitals tuple
    # 2. check the country of each row (lowercase) is equal to the country passed in argument (lowercase)
    # 3. if #2 is true, then assign the corresponding capital of the country and early return
    # 4. if #2 is false, then assign "no such country" to capital_of_country and print doesn't match in tuple
    #

    # assign None as a placeholder value to capital_of_country
    capital_of_country = None

    # index variable for while loop
    i = 0

    # while loop with condition i < len(countries_and_capitals)
    while i < len(countries_and_capitals):
        # if the i'th row of the countries_and_capitals tuple is equal to the country argument value
        if countries_and_capitals[i][0].lower() == country.lower():
            # assign the corresponding capital of the i'th row
            capital_of_country = countries_and_capitals[i][1]

            # early return the matching capital of country
            return capital_of_country
        # otherwise, if the above condition is not satisfied
        else:
            # assign "no such country" to capital_of_country
            capital_of_country = "no such country"

            # print country does not match country in tuple
            print("country does not match country in tuple")

        # increment index by 1 every iteration
        i += 1

    # return capital of country
    return capital_of_country


def get_list_of_countries_with_this_many_letters_in_name(num_letters):
    """
    Get list of countries with amount of letters in the name.

    Example output:
    ['El Salvador', 'Netherlands', 'New Zealand', 'North Korea', 'Philippines', 'Saint Lucia', 'South Korea',
    'South Sudan', 'Switzerland']

    :param num_letters: The number of letters (string)
    :return: The list of countries (list of strings)
    """
    #
    # get list of countries with amount of letters in the name:
    # 1. iterate over countries tuple
    # 2. check the length of the i'th country containing the current country is equal to num_letters
    # 3. if #2 is true and index is 0, then assign a tuple based on the list containing the current country
    # 4. if #2 is false and index is 0, then assign an empty tuple
    # 5. if #2 is true and index is not 0, then extend countries_with_amount_of_letters with the i'th country
    #

    # assign None as a placeholder value to countries_with_amount_of_letters
    countries_with_amount_of_letters = None

    # index variable for while loop
    i = 0

    # while loop with condition i < len(countries)
    while i < len(countries):
        # if index is 0 and length of i'th country is equal to num_letters
        if i == 0 and len(countries[i]) == num_letters:
            # assign a tuple based on a list containing the current country
            countries_with_amount_of_letters = tuple([countries[i]])
        # if index is 0 and length of i'th country is not to num_letters
        elif i == 0 and not len(countries[i]) == num_letters:
            # assign empty tuple to countries_with_amount_of_letters
            countries_with_amount_of_letters = ()
        # if the length of the i'th country is equal to num_letters
        elif i != 0 and len(countries[i]) == num_letters:
            # extend countries_with_amount_of_letters with the i'th country
            # 1. convert countries_with_amount_of_letters to list (open)
            # 2. extend countries_with_amount_of_letters_to_change with the i'th country
            # 3. assign the tuple version of countries_with_amount_of_letters_to_change
            # to countries_with_amount_of_letters (close)
            countries_with_amount_of_letters_to_change = list(countries_with_amount_of_letters)
            countries_with_amount_of_letters_to_change.extend([countries[i]])
            countries_with_amount_of_letters = tuple(countries_with_amount_of_letters_to_change)
        # otherwise, if the above condition is not satisfied
        else:
            # print length of countries do not match with argument
            print("length of countries do not match with argument")

        # increment index by 1 every iteration
        i += 1

    # return the list version of list of countries
    return list(countries_with_amount_of_letters)


def get_capitals_and_countries_that_begin_and_end_with_same_letter():
    """
    Get capitals and countries that begin and end with same letter.

    Example output:
    ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
    'Central African Republic', 'Saint Kitts and Nevis', 'Saint Vincent and the Grenadines', 'Seychelles',
    'Solomon Islands', 'Andorra la Vella', "Saint John's", 'Asmara', 'Addis Ababa', 'Accra', "Saint George's",
    'Nur-Sultan', 'Abuja', 'Oslo', 'Warsaw', 'Apia', 'Ankara', 'Tashkent']
    :return: The capitals and countries that begin with the same letter (list of strings)
    """
    #
    # get capitals and countries that begin and end with same letter:
    # 1. iterate over countries and capitals tuple
    # 2. check the first character of the current country is equal to the last character
    # of the current country
    # 3. if #2 is true and index is 0, assign a tuple based on a list containing the current country
    # 4. if #2 is false and index is 0, assign an empty tuple to countries_and_capitals_begin_end_same_letter
    # 5. if #2 is true and index is not 0, extend countries_and_capitals_begin_end_same_letter with the current country
    #

    # assign None as placeholder value for countries_and_capitals_begin_end_same_letter
    countries_and_capitals_begin_end_same_letter = None

    # index variable for countries while loop
    i = 0

    # while loop with condition i < len(countries_and_capitals)
    while i < len(countries_and_capitals):
        # assign the current country to curr_country_temp
        curr_country_temp = countries_and_capitals[i][0]

        # if index is 0 and the first character of current country is equal to the last character of current country
        if i == 0 and curr_country_temp[0].lower() == curr_country_temp[-1].lower():
            # assign a tuple based on a list containing the current country
            countries_and_capitals_begin_end_same_letter = tuple([curr_country_temp])
        # if index is 0 and the first character of current country is not equal to the last character of current country
        elif i == 0 and not curr_country_temp[0].lower() == curr_country_temp[-1].lower():
            # assign an empty tuple to countries_and_capitals_begin_end_same_letter
            countries_and_capitals_begin_end_same_letter = ()
        # if index is not 0 and the first character of current country is equal to the last character of current country
        elif i != 0 and curr_country_temp[0].lower() == curr_country_temp[-1].lower():
            # extend countries_and_capitals_begin_end_same_letter with the current country
            # 1. convert countries_and_capitals_begin_end_same_letter to a list (open)
            # 2. extend the current country to countries_and_capitals_begin_end_same_letter_to_change
            # 3. assign the tuple version of countries_and_capitals_begin_end_same_letter_to_change
            # to countries_and_capitals_begin_end_same_letter (close)
            countries_and_capitals_begin_end_same_letter_to_change = list(
                countries_and_capitals_begin_end_same_letter)
            countries_and_capitals_begin_end_same_letter_to_change.extend([curr_country_temp])
            countries_and_capitals_begin_end_same_letter = tuple(
                countries_and_capitals_begin_end_same_letter_to_change)
        # otherwise, if the above conditions are not satisfied
        else:
            # print first and last letter of country are not equal
            print("first and last letter of country are not equal")

        # increment i index by 1
        i += 1

    # index variable for capitals while loop
    j = 0

    # while loop with condition j < len(countries_and_capitals)
    while j < len(countries_and_capitals):
        # assign the current capital to curr_capital_temp
        curr_capital_temp = countries_and_capitals[j][1]

        if curr_capital_temp[0].lower() == curr_capital_temp[-1].lower():
            # extend countries_and_capitals_begin_end_same_letter with the current country
            # 1. convert countries_and_capitals_begin_end_same_letter to a list (open)
            # 2. extend the current capital to countries_and_capitals_begin_end_same_letter_to_change
            # 3. assign the tuple version of countries_and_capitals_begin_end_same_letter_to_change
            # to countries_and_capitals_begin_end_same_letter (close)
            countries_and_capitals_begin_end_same_letter_to_change = list(
                countries_and_capitals_begin_end_same_letter)
            countries_and_capitals_begin_end_same_letter_to_change.extend([curr_capital_temp])
            countries_and_capitals_begin_end_same_letter = tuple(
                countries_and_capitals_begin_end_same_letter_to_change)
        # otherwise, if the above conditions are not satisfied
        else:
            # print first and last letter of capital are not equal
            print("first and last letter of capital are not equal")

        # increment j index by 1
        j += 1

    # return the list version of countries and capitals that begin and end with the same letter
    return list(countries_and_capitals_begin_end_same_letter)


def print_countries_in_reverse_alphabetical_order():
    """
    Print countries in reverse alphabetical order.

    Example output:
    ('Zimbabwe', 'Zambia', 'Yemen', 'Wales', 'Vietnam', 'Venezuela', 'Vatican City', 'Vanuatu', 'Uzbekistan', 'Uruguay',
     'United States', 'United Kingdom', 'United Arab Emirates', 'Ukraine', 'Uganda', 'Tuvalu', 'Turkmenistan', 'Turkey',
      'Tunisia', 'Trinidad and Tobago', 'Tonga', 'Togo', 'Thailand', 'Tanzania', 'Tajikistan', 'Taiwan', 'Syria',
      'Switzerland', 'Sweden', 'Suriname', 'Sudan', 'Sri Lanka', 'Spain', 'South Sudan', 'South Korea', 'South Africa',
      'Somalia', 'Solomon Islands', 'Slovenia', 'Slovakia', 'Singapore', 'Sierra Leone', 'Seychelles', 'Serbia',
      'Senegal', 'Scotland', 'Saudi Arabia', 'Sao Tome and Principe', 'San Marino', 'Samoa',
      'Saint Vincent and the Grenadines', 'Saint Lucia', 'Saint Kitts and Nevis', 'Rwanda', 'Russia', 'Romania',
      'Qatar', 'Portugal', 'Poland', 'Philippines', 'Peru', 'Paraguay', 'Papua New Guinea', 'Panama', 'Palau',
      'Pakistan', 'Oman', 'Norway', 'Northern Ireland', 'North Macedonia (Macedonia)', 'North Korea', 'Nigeria',
      'Niger', 'Nicaragua', 'New Zealand', 'Netherlands', 'Nepal', 'Nauru', 'Namibia', 'Myanmar (Burma)', 'Mozambique',
      'Morocco', 'Montenegro', 'Mongolia', 'Monaco', 'Moldova', 'Mexico', 'Mauritius', 'Mauritania', 'Marshall Islands',
      'Malta', 'Mali', 'Maldives', 'Malaysia', 'Malawi', 'Madagascar', 'Luxembourg', 'Lithuania', 'Liechtenstein',
      'Libya', 'Liberia', 'Lesotho', 'Lebanon', 'Latvia', 'Laos', 'Kyrgyzstan', 'Kuwait', 'Kosovo', 'Kiribati', 'Kenya',
      'Kazakhstan', 'Jordan', 'Japan', 'Jamaica', 'Italy', 'Israel', 'Ireland', 'Iraq', 'Iran', 'Indonesia', 'India',
      'Iceland', 'Hungary', 'Honduras', 'Haiti', 'Guyana', 'Guinea-Bissau', 'Guinea', 'Guatemala', 'Grenada', 'Greece',
      'Ghana', 'Germany', 'Georgia', 'Gambia', 'Gabon', 'France', 'Finland', 'Fiji', 'Federated States of Micronesia',
      'Ethiopia', 'Eswatini (Swaziland)', 'Estonia', 'Eritrea', 'Equatorial Guinea', 'England', 'El Salvador', 'Egypt',
      'Ecuador', 'East Timor', 'Dominican Republic', 'Dominica', 'Djibouti', 'Denmark', 'Czech Republic (Czechia)',
      'Cyprus', 'Cuba', 'Croatia', "Cote d'Ivoire (Ivory Coast)", 'Costa Rica', 'Congo, Republic of the',
      'Congo, Democratic Republic of the', 'Comoros', 'Colombia', 'China', 'Chile', 'Chad', 'Central African Republic',
      'Cape Verde', 'Canada', 'Cameroon', 'Cambodia', 'Burundi', 'Burkina Faso', 'Bulgaria', 'Brunei', 'Brazil',
      'Botswana', 'Bosnia and Herzegovina', 'Bolivia', 'Bhutan', 'Benin', 'Belize', 'Belgium', 'Belarus', 'Barbados',
      'Bangladesh', 'Bahrain', 'Bahamas', 'Azerbaijan', 'Austria', 'Australia', 'Armenia', 'Argentina',
      'Antigua and Barbuda', 'Angola', 'Andorra', 'Algeria', 'Albania', 'Afghanistan')
    :return: None
    """
    #
    # print countries in reverse alphabetical order:
    # 1. countries tuple is assumed to be alphabetical order
    # 2. create a new list using list comprehension
    # 3. reverse the new list using .reverse() method
    # 4. print the tuple of reverse alphabetical countries
    #

    # create new list using list comprehension and assign to reverse_alphabetical_countries
    # the condition is len(c) != 0 because if the countries tuple is empty, then it will throw an error, so we
    # want to make sure it is filled with a value
    reverse_alphabetical_countries = [c for c in countries if len(c) != 0]

    # reverse the list of alphabetical countries
    reverse_alphabetical_countries.reverse()

    # print the tuple of reverse alphabetical countries
    print(tuple(reverse_alphabetical_countries))


def main():
    """
    Print how many countries, name of longest country, number of capitals containing e, z, and ', an,
    get countries and capitals that start with same letter, get capital of canada, get capital of new zealand, get
    capital of xyz, get countries with length of 11, get countries with length of 15, get capitals and countries that
    end with same letter, and print countries in reverse alphabetical order.
    :return: None
    """
    # print the number of countries
    print(how_many_countries())

    # print the longest country name
    print(get_name_of_longest_country())

    # print number of capitals containing "e"
    print(get_number_of_capitals_containing("e"))

    # print number of capitals containing "z"
    print(get_number_of_capitals_containing("z"))

    # print number of capitals containing "'"
    print(get_number_of_capitals_containing("'"))

    # print number of capitals containing "an"
    print(get_number_of_capitals_containing("an"))

    # print countries and capitals that start with the same letter
    print(get_countries_and_capitals_that_start_with_same_letter())

    # print the capital of canada
    print(get_capital_of("canada"))

    # print the capital of nEW zeALAND
    print(get_capital_of("nEW zeALAND"))

    # print the capital of "zyz"
    print(get_capital_of("xyz"))

    # print list of countries with 11 letters in name
    print(get_list_of_countries_with_this_many_letters_in_name(11))

    # print list of countries with 15 letters in name
    print(get_list_of_countries_with_this_many_letters_in_name(15))

    # print capitals and countries that begin and end with same letter
    print(get_capitals_and_countries_that_begin_and_end_with_same_letter())

    # print countries in reverse alphabetical order
    print_countries_in_reverse_alphabetical_order()


if __name__ == "__main__":
    main()
