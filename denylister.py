import itertools


def banner():
    print(
        """
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗██╗     ██╗███████╗████████╗███████╗██████╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██║     ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██████╔╝██║     ███████║██║     █████╔╝ ██║     ██║███████╗   ██║   █████╗  ██████╔╝
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██║     ██║╚════██║   ██║   ██╔══╝  ██╔══██╗
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗███████╗██║███████║   ██║   ███████╗██║  ██║
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
               A wordlist generator for denylisting common password strings
                                        v1.0
                          Another tool created by TheMayor
    """
    )


def leetspeak_generator(word):
    # years = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
    leet_dict = {
        "a": [
            "4",
            "@",
        ],
        "b": ["8"],
        "c": ["<", "("],
        "e": ["3"],
        "g": ["9", "6"],
        "h": ["#"],
        "i": ["1", "!", "|"],
        "l": ["|", "1", "7"],
        "o": ["0"],
        "s": ["$", "5"],
        "t": ["+", "7"],
        "z": ["2"],
    }

    leet_combinations = []
    for char in word:
        if char.lower() in leet_dict:
            leet_combinations.append(leet_dict[char.lower()] + [char.upper()])
        else:
            leet_combinations.append([char])

    return [
        "".join(combination) for combination in itertools.product(*leet_combinations)
    ]


def generate_leetspeak_combinations(word_list):
    leetspeak_combinations = []

    for word in word_list:
        leetspeak_combinations.append(word)

        leet_plain = "".join(word)
        leetspeak_combinations.extend(leetspeak_generator(leet_plain))

    return leetspeak_combinations


if __name__ == "__main__":
    banner()
    # Get the file name from the user
    try:
        file_name = input("Enter the file name containing the list of words: ")

        with open(file_name, "r") as file:
            word_list = [line.strip() for line in file.readlines()]
        output_file_name = "denylisted_passwords.txt"
        leetspeak_combinations = generate_leetspeak_combinations(word_list)
        print(f"\nNumber of words generated: {len(leetspeak_combinations)}\n")
        with open(output_file_name, "w") as output_file:
            output_file.write("\n".join(leetspeak_combinations))
        # Generate leetspeak combinations
        leetspeak_combinations = generate_leetspeak_combinations(word_list)
        print(f"Leetspeak combinations saved to '{output_file_name}'\n")
        output_list = input("[!] Do you want to output combinations to terminal? (y/n)? ")
        if output_list.lower() == "y":
            # Print leetspeak combinations
            print("\nLeetspeak List:")
            print("\n".join(leetspeak_combinations))
        else:
            print('\nQuitting!')
            quit()
    except KeyboardInterrupt:
        print('\n\nYou either fat fingered this, or something else. Either way, Quitting!')
    except FileNotFoundError:
        print(f"\n[-] Error: File '{file_name}' not found. Retry with a valid file.\n")
        exit()
