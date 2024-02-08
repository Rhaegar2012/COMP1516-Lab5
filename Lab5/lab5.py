# Author: Jose Tellez and Alex Kweung and Yu-shiuan Lin
import data

countries_and_capitals = data.countries_and_capitals
countries = data.countries
capitals = data.capitals


def main():
    """
    Main function , runs program
    :return:
    """
    # Returns the total number of countries in the tuple
    number_of_countries = how_many_countries()
    print(number_of_countries)
    # Returns the country with the longest name
    longest_country_name = get_name_of_longest_country()
    print(longest_country_name)
    # Returns the number of capitals containing the letter e
    number_of_capitals = get_number_of_capitals_containing('e')
    print(number_of_capitals)
    # Returns number of capitals containing the letter z
    number_of_capitals = get_number_of_capitals_containing("z")
    print(number_of_capitals)
    # Returns number of capitals containing an apostrophe symbol (')
    number_of_capitals = get_number_of_capitals_containing("an")
    print(number_of_capitals)
    # Returns a list of countries and capitals that start with the same letter
    capitals_and_countries_with_same_letter = get_capitals_and_countries_that_begin_and_end_with_same_letter()
    print(capitals_and_countries_with_same_letter)
    # Returns the capital of a given country- case insensitive
    capital = get_capital_of("Canada")
    print(capital)
    # Returns the capital of a given country- case insensitive
    capital = get_capital_of("nEW Zealand")
    print(capital)
    # Returns a list of countries with a given number of letters in the name
    countries_with_number_of_letters = get_list_of_countries_with_this_many_letters_in_name(11)
    print(countries_with_number_of_letters)


def how_many_countries():
    """
    Determines how many elements exist in the countries tuple
    :return: number of elements in tuple , as int
    """
    number_of_countries = len(countries)
    return number_of_countries


def get_name_of_longest_country():
    """
    Determines which is the country with the longest name (including spaces) and returns the country name
    :return: Country name with the longest name as string
    """
    country_with_longest_name = None
    number_of_countries = len(countries)
    index = 0
    max_name_length = 0
    while index < number_of_countries:
        country_name_length = len(countries[index])
        if country_name_length > max_name_length:
            max_name_length = country_name_length
            country_with_longest_name = countries[index]
        index += 1
    return country_with_longest_name


def get_number_of_capitals_containing(substring):
    """

    :param substring: sequence of characters to be found in capitals
    :return:number of capitals containing the substring as int
    """
    number_of_capitals_containing_substring = 0
    index = 0
    number_of_capitals = len(capitals)
    while index < number_of_capitals:
        capital = capitals[index]
        if substring in capital:
            number_of_capitals_containing_substring += 1
        index += 1
    return number_of_capitals_containing_substring


def get_capital_of(country):
    """
    Takes the name of a country as argument and returns the capital of that country
    :param country: country name as string
    :return: capital of the country as string
    """
    country = country.lower().capitalize()
    number_of_countries_and_capitals = len(countries_and_capitals)
    index = 0
    while index < number_of_countries_and_capitals:
        country_to_evaluate = countries_and_capitals[index][0].lower().capitalize()
        if country_to_evaluate == country:
            return countries_and_capitals[index][1]
        index += 1
    return None


def get_list_of_countries_with_this_many_letters_in_name(num_letters):
    """
    Takes a set number of letters and returns a list of countries that have the same number of letters
    :param num_letters: number of letters as int
    :return:list of countries that have the same number of letters , spaces removed
    """
    num_of_countries = len(countries)
    index = 0
    countries_with_same_number_of_letters = []
    while index < num_of_countries:
        country = countries[index].lower().replace(" ", "")
        if len(country) == num_letters:
            countries_with_same_number_of_letters.append(countries[index])
        index += 1
    return countries_with_same_number_of_letters


def get_capitals_and_countries_that_begin_and_end_with_same_letter():
    """
    Determines if a country and its capital start with the same letter and adds them to a list
    then returns the list
    :return:list of countries that share the same first name with their capitals
    """
    index = 0
    number_of_country_capital_pairs = len(countries_and_capitals)
    capitals_countries_with_same_letter = []
    while index < number_of_country_capital_pairs:
        country_letter = countries_and_capitals[index][0][0].lower()
        capital_letter = countries_and_capitals[index][1][0].lower()
        if country_letter == capital_letter:
            capitals_countries_with_same_letter.append(countries_and_capitals[index][0]+"-"
                                                       + countries_and_capitals[index][1])
        index += 1
    return capitals_countries_with_same_letter


def print_countries_in_reverse_alphabetical_order():
    """
    Reverses lists of countries in alphabetical order and returns it
    :return: reversed list of countries
    """
    reverse_list = countries.reverse()
    return reverse_list


if __name__ == "__main__":
    main()