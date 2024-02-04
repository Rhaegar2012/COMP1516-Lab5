# Author: Jose Tellez
import data

countries_and_capitals = data.countries_and_capitals
countries = data.countries
capitals = data.capitals


def main():
    """
    Main function , runs program
    :return:
    """
    pass


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
    while index<number_of_countries:
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
        country_to_evaluate = countries_and_capitals[index][0]
        if country_to_evaluate == country :
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
        country = countries_and_capitals[index][0].lower()
        capital = countries_and_capitals[index][1].lower()
        if country == capital:
            capitals_countries_with_same_letter.append(country)
        index += 1
    return capitals_countries_with_same_letter


def print_countries_in_reverse_alphabetical_order():
    """
    Reverses lists of countries in alphabetical order and returns it
    :return: reversed list of countries
    """
    reverse_list = countries.reverse()
    return reverse_list


if __name__ == "main":
    main()