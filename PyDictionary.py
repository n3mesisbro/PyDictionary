#!/usr/bin/env python3

import os 
import sys
import time
import signal
from itertools import permutations


"""
All rights reserved.

MIT License

Copyright (c) 2024 N3mesis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Colors
red = "\033[0;31m"
cyan = "\033[0;36m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
green = "\033[0;32m"
nc = "\033[00m"  # Reset color

# Global variables
version = "1.0"
creator = "ne0mesys"

logo = f"""
    {red}_______          _____  ___          ___  ___
    {cyan}|  _   \        |     \ |_|  _____ __| |__|_| _____  __     _   ______ _______
    {yellow}|  ¬   / _    _ |  _   | _  /____/|__  __| _ |  _  ||   \  | | /  _   || ____/_    _
    {green}|   __/ | |__| || |_|  || || |       | |  | || | | || |  \ | ||  / |  || |   | |__| |
    {red}|  |    |____  ||      || || |____   | |  | || |_| || |   \  ||  \_|  || |   |____  |
    {yellow}|__|         | ||____ / |_||_____/   |_|  |_||_____||_|    \_| \______||_|        | |
    {green}           _/ /                                                                 _/ /
    {cyan}          |__/                                                                 |__/
                                                                {" "*19}{red}[v{version}]
                                                                 {" "*11} {green}[By {creator}]

{red}[+] {nc}Welcome to PyDictionary, I hope you enjoy it :)

{red}[+]{yellow} Press Enter after each input. Leave blank and press Enter to stop.{nc}
"""

# Functions
def exit_message(signum, frame): 
    print(f"{red}\n\n\n[!] Terminating program...{nc}\n")
    print(f"{green}By {creator}{red} [v{version}]{nc}\n\n")
    sys.exit(0)

# Register the handler for the SIGINT sign (Ctrl+C)
signal.signal(signal.SIGINT, exit_message)

def clear_console():
    """Clears the console based on the operating system."""
    os.system("clear" if os.name == 'posix' else 'cls')

def validated_input(prompt, color, input_type=str, optional=True, min_value=None, max_value=None):
    """Validates user input with optional constraints."""
    while True:
        user_input = input(f"{red}[+] {color}{prompt}{nc} ").strip()
        if optional and not user_input:
            return None
        try:
            value = input_type(user_input)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"{red}Invalid input. Please enter a value between {min_value} and {max_value}.{nc}")
                continue
            return value
        except ValueError:
            print(f"{red}Invalid input. Please enter a valid {input_type.__name__}.{nc}")

def typewriter_with_cursor(text, delay=0):
    """Simulates typewriter effect when printing text."""
    clear_console()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def collect_data():
    """Collects user data in a loop, displaying input dynamically."""
    collected_data = []
    fields = ["Name", "Surname", "Second_Surname", "Nickname", "Second_Nickname", "Day_of_Birth", "Month_of_Birth", "Year_of_Birth"]
    
    for field in fields:
        while True:
            clear_console()
            current_line = "; ".join([item.split(": ")[1] for item in collected_data])
            print(f"\n{nc}{current_line}{'; ' if current_line else ''}{nc}", end="", flush=True)

            print(f"\n\n{yellow}[+] {cyan}Type 'none' when there is no data. Leave blank and press Enter to stop.{nc}")
            print(f"\n{yellow}[+] {nc}Input for {yellow}{field}{nc} = ", end="", flush=True)
            user_input = input().strip()

            if not user_input:  # Stop when input is blank
                print(f"{red}\n[!] Error: {field} cannot be empty.{nc}")
                time.sleep(1)
                continue
            
            if user_input.lower() == "none":
                collected_data.append(f"{field}: None")
                break

            if " " in user_input:
                print(f"{red}\n[!] Error: Spaces are not allowed in the input for {field}.{nc}")
                time.sleep(1)
                continue

            if field == "Day_of_Birth":
                try:
                    day = int(user_input)
                    if day < 1 or day > 31:
                        print(f"{red}\n[!] Error: Day of birth must be between 1 and 31.{nc}")
                        time.sleep(1)
                        continue
                except ValueError:
                    print(f"{red}\n[!] Error: Please enter a valid number for Day of Birth.{nc}")
                    time.sleep(1)
                    continue

            if field == "Month_of_Birth":
                try:
                    month = int(user_input)
                    if month < 1 or month > 12:
                        print(f"{red}\n[!] Error: Month of birth must be between 1 and 12.{nc}")
                        time.sleep(1)
                        continue
                except ValueError:
                    print(f"{red}\n[!] Error: Please enter a valid number for Month of Birth.{nc}")
                    time.sleep(1)
                    continue

            if field == "Year_of_Birth":
                try: 
                    year = int(user_input)
                    if year < 1950 or year > 2050:
                        print(f"{red}\n[!] Error: Year of Birth must be between 1 and 2050.{nc}")
                        time.sleep(1)
                        continue
                except ValueError:
                    print(f"{red}\n[!] Error: Please enter a valid number for Year of Birth.{nc}")
                    time.sleep(1)
                    continue

            collected_data.append(f"{field}: {user_input}")
            break
    return collected_data

def add_variant(variant, combinations, seen_combinations):
    if "none" not in variant.lower() and variant not in seen_combinations:
        combinations.append(variant)
        seen_combinations.add(variant)
        print(f"{yellow}\r[+]{nc} Combinations generated: {yellow}{len(combinations)}{nc}", end="")
        
# Function to generate both, lowercase, uppercase, and capitalized variants
def both_variants(value):
    return [value.lower(), value.upper(), value.capitalize()]

#Function to extract initials
def extract_initials(full_name):
    if isinstance(full_name, list):
        full_name = " ".join(full_name)  

    if not isinstance(full_name, str) or full_name.lower() == "none" or not full_name.strip():
        return ""

    return "".join(part[0].upper() for part in full_name.split() if part)

# Permutations of dates
def generate_date_combinations(base, date_parts, combinations, seen_combinations): 
    valid_parts = [str(p) for p in date_parts if str(p).isdigit()]
    for r in range(1, len(valid_parts) + 1): 
        for date_combo in permutations(valid_parts, r): 
            joined = ''.join(date_combo)
            add_variant(f"{base}{joined}", combinations, seen_combinations)
            add_variant(f"{base}_{joined}", combinations, seen_combinations)

def combinations_initials(name, surname, second_surname, day, month, year, seen_combinations, combinations):
    initials_name = extract_initials(name)
    initials_surname = extract_initials(surname)
    initials_second_surname = extract_initials(second_surname)

    if initials_name and initials_surname and initials_second_surname:
        new_combination = f"{initials_name}{initials_surname}{initials_second_surname}"

        for variant in both_variants(new_combination):
            add_variant(variant, combinations, seen_combinations)

        for value in [day, month, year]:
            if value.lower() != "none":
                for variant in (
                    both_variants(f"{new_combination}{value}") +
                    both_variants(f"{new_combination}_{value}")
                ):
                    add_variant(variant, combinations, seen_combinations)

        generate_date_combinations(new_combination, [day, month, year], combinations, seen_combinations)

def generate_combinations_with_dates(
    name, nickname, second_nickname, surname, second_surname, day, month, year, combinations, seen_combinations):
    def is_valid(value):
        return value and value.lower() != "none"

    def is_number(value):
        try:
            int(value)
            return True
        except:
            return False

    def add_date_combinations(base, day, month, year):
      last_two_digits = str(year)[-2:]

      date_parts = [
          (day,), (month,), (year,), (last_two_digits,),
          (day, month), (month, day),
          (day, year), (year, day),
          (day, last_two_digits), (last_two_digits, day),
          (month, year), (year, month),
          (month, last_two_digits), (last_two_digits, month),
      ]

      for parts in date_parts:
          joined = ''.join(parts)
          add_all_permutations([base, joined], combinations, seen_combinations)
          add_all_permutations([base, "_", joined], combinations, seen_combinations)

    valid_inputs = []

    if is_valid(name) and is_valid(surname):
        valid_inputs.append(name + surname)
    if is_valid(name) and is_valid(surname) and is_valid(second_surname):
        valid_inputs.append(name + surname + second_surname)
    if is_valid(nickname) and is_valid(surname):
        valid_inputs.append(nickname + surname)
    if is_valid(nickname) and is_valid(surname) and is_valid(second_surname):
        valid_inputs.append(nickname + surname + second_surname)
    if is_valid(second_nickname) and is_valid(surname):
        valid_inputs.append(second_nickname + surname)
    if is_valid(second_nickname) and is_valid(surname) and is_valid(second_surname):
        valid_inputs.append(second_nickname + surname + second_surname)

    # Validating dates
    day_valid = is_number(day)
    month_valid = is_number(month)
    year_valid = is_number(year)

    for base in valid_inputs:
        # Combinations without dates
        add_all_permutations(base, combinations, seen_combinations)

        # Combinations with dates
        if day_valid and month_valid and year_valid:
            add_date_combinations(base, day, month, str(year))
        else:
            if day_valid:
                add_all_permutations([base, day], combinations, seen_combinations)
                add_all_permutations([base, "_", day], combinations, seen_combinations)
            if month_valid:
                add_all_permutations([base, month], combinations, seen_combinations)
                add_all_permutations([base, "_", month], combinations, seen_combinations)
            if year_valid:
                last_two = str(year)[-2:]
                for y in (last_two, str(year)):
                    add_all_permutations([base, y], combinations, seen_combinations)
                    add_all_permutations([base, "_", y], combinations, seen_combinations)

def add_all_permutations(parts, combinations, seen_combinations):
    if isinstance(parts, str):
        parts = [parts]
    for perm in permutations(parts):
        combined = ''.join(str(p) for p in perm)
        add_variant(combined, combinations, seen_combinations)

def generate_combinations(data, fruits, verdura, numbers, cities, words, colores, special_characters):  
    combinations = []
    seen_combinations = set() # Track seen combinations for each key

    # Initialize relevant variables
    name = next((item.split(": ")[1] for item in data if item.startswith("Name")), "")
    surname = next((item.split(": ")[1] for item in data if item.startswith("Surname")), "")
    second_surname = next((item.split(": ")[1] for item in data if item.startswith("Second_Surname")), "")
    nickname = next((item.split(": ")[1] for item in data if item.startswith("Nickname")), "")
    second_nickname = next((item.split(": ")[1] for item in data if item.startswith("Second_Nickname")), "")
    day = next((item.split(": ")[1] for item in data if item.startswith("Day_of_Birth")), "")
    month = next((item.split(": ")[1] for item in data if item.startswith("Month_of_Birth")), "")
    year = next((item.split(": ")[1] for item in data if item.startswith("Year_of_Birth")), "")

    names = [name, surname, second_surname]
    time = [day, month, year]
    surnames = [surname, second_surname]

    # Add combinations for name, nickname, nickname, etc. only if there is not "none"
    for _, value in [
        ("name", name), 
        ("nickname", nickname), 
        ("second_nickname", second_nickname), 
        ("surname", surname), 
        ("second_surname", second_surname),
    ]:
        if value and value.lower() != "none": 
            variants = both_variants(value)
            for variant in variants:
                add_variant(variant, combinations, seen_combinations)

    combinations_initials(name, surname, second_surname, day, month, year, seen_combinations, combinations)

    # Add combinations with the lists (fruits, verdura, etc.)
    for related_list in [fruits, verdura, numbers, cities, words, colores, special_characters]:
        for element in related_list:
            for current_name in names:
                if current_name.lower() != "none":
                    for variant in both_variants(current_name):
                        add_all_permutations([variant, element], combinations, seen_combinations)
                        add_all_permutations([variant, f"_{element}"], combinations, seen_combinations)

    # Articles + names
    for element in articulos:
        for current_name in names:
            if current_name.lower() != "none":
                for variant in both_variants(current_name):
                    add_all_permutations([element, variant], combinations, seen_combinations)
                    add_all_permutations([element, f"_{variant}"], combinations, seen_combinations)
    
    # Names + surname + numbers
    for element in numbers: 
        for current_name in names:
            if current_name.lower() != "none":
                if surname.lower() != "none":
                    for variant in both_variants(current_name):
                        add_all_permutations([variant, surname, element], combinations, seen_combinations)
                        add_all_permutations([variant, surname, f"_{element}"], combinations, seen_combinations)

        # Surname + numbers
        if surname.lower() != "none":
            for variant in both_variants(surname):
                add_all_permutations([variant, element], combinations, seen_combinations)
                add_all_permutations([variant, f"_{element}"], combinations, seen_combinations)

        # Names + numbers
        for current_name in names:
            if current_name.lower() != "none":
                for variant in both_variants(current_name):
                    add_all_permutations([variant, element], combinations, seen_combinations)
                    add_all_permutations([variant, f"_{element}"], combinations, seen_combinations)

    # Articles + names + surnames
    for element in articulos:
        for current_name in names:
            if current_name.lower() != "none":
                for current_surname in surnames:
                    if current_surname.lower() != "none":
                        for variant_name in both_variants(current_name):
                            for variant_surname in both_variants(current_surname):
                                add_all_permutations([element, variant_name, variant_surname], combinations, seen_combinations)
                                add_all_permutations([element, f"_{variant_name}", variant_surname], combinations, seen_combinations)

    # Articles + names + surname 
    for element in articulos:
        for current_name in names:
            if current_name.lower() != "none" and surname.lower() != "none":
                for variant_name in both_variants(current_name):
                    for variant_surname in both_variants(surname):
                        add_all_permutations([element, variant_name, surname], combinations, seen_combinations)
                        add_all_permutations([element, f"_{variant_name}", surname], combinations, seen_combinations)

    # Articles + names + surnames + second_surnames
    for element in articulos:
        for current_name in names:
            if current_name.lower() != "none" and surname.lower() != "none" and second_surname.lower() != "none":
                for variant_name in both_variants(current_name):
                    for variant_surname in both_variants(surname):
                        for variant_second_surname in both_variants(second_surname):
                            add_all_permutations(
                                [element, variant_name, variant_surname, variant_second_surname], combinations, seen_combinations)
                            add_all_permutations(
                                [element, f"_{variant_name}", variant_surname, variant_second_surname], combinations, seen_combinations)

    # Articles + names + day/month/year                                   
    date_parts = [str(d) for d in time if str(d).isdigit()]

    for article in articulos: 
        for current_name in names: 
            if current_name.lower() == "none": 
                continue
            for variant_name in both_variants(current_name): 
                # Individual date_parts
                for part in date_parts: 
                    add_all_permutations([article, variant_name, part], combinations, seen_combinations)
                    add_all_permutations([article, f"_{variant_name}", part], combinations, seen_combinations)

                # Permutaciones de 2 partes de date_parts
                for combo in permutations(date_parts, 2):
                    joined = ''.join(combo) 
                    add_all_permutations([article, variant_name, joined], combinations, seen_combinations)
                    add_all_permutations([article, f"_{variant_name}", joined], combinations, seen_combinations)

                # Permutaciones de 3 partes de date_parts
                for combo in permutations(date_parts, 3): 
                    joined = ''.join(combo)
                    add_all_permutations([article, variant_name, joined], combinations, seen_combinations)
                    add_all_permutations([article, f"_{variant_name}", joined], combinations, seen_combinations)

        # Names + team 
        for element in teams:
            for current_name in names:
                if current_name.lower() != "none":
                    for variant_name in both_variants(current_name):
                        add_all_permutations([variant_name, element], combinations, seen_combinations)
                        add_all_permutations([variant_name, f"_{element}"], combinations, seen_combinations)

            # Names + team + numbers
            for number in teams_numbers:
                if current_name.lower() != "none":
                    for variant_name in both_variants(current_name):
                        add_all_permutations([variant_name, element, number], combinations, seen_combinations)
                        add_all_permutations([variant_name, f"_{element}", number], combinations, seen_combinations)


    def add_name_variant_date_permutations(base_name: str, day: str, month: str, year: str, combinations, seen_combinations):
        if not base_name:
            return

        variants = both_variants(base_name)

        valid_day = day.isdigit() and 1 <= int(day) <= 31
        valid_month = month.isdigit() and 1 <= int(month) <= 12
        valid_year = year.isdigit() and len(year) == 4

        if valid_day or valid_month or valid_year:
            for variant in variants:
                if valid_day and valid_month and valid_year:
                    add_all_permutations([variant, day, month, year], combinations, seen_combinations)
                    add_all_permutations([variant, day, year, month], combinations, seen_combinations)
                    add_all_permutations([variant, month, day, year], combinations, seen_combinations)
                    add_all_permutations([variant, month, year, day], combinations, seen_combinations)
                    add_all_permutations([variant, year, day, month], combinations, seen_combinations)
                    add_all_permutations([variant, year, month, day], combinations, seen_combinations)

                if valid_day and valid_month:
                    add_all_permutations([variant, day, month], combinations, seen_combinations)
                    add_all_permutations([variant, month, day], combinations, seen_combinations)

                if valid_day and valid_year:
                    add_all_permutations([variant, day, year], combinations, seen_combinations)
                    add_all_permutations([variant, year, day], combinations, seen_combinations)

                if valid_month and valid_year:
                    add_all_permutations([variant, month, year], combinations, seen_combinations)
                    add_all_permutations([variant, year, month], combinations, seen_combinations)

                if valid_day:
                    add_all_permutations([variant, day], combinations, seen_combinations)
                if valid_month:
                    add_all_permutations([variant, month], combinations, seen_combinations)
                if valid_year:
                    add_all_permutations([variant, year], combinations, seen_combinations)

                if valid_day and valid_month and valid_year:
                    add_all_permutations([variant, day, month, year[2:]], combinations, seen_combinations)
                    add_all_permutations([variant, day, year[2:], month], combinations, seen_combinations)
                    add_all_permutations([variant, month, day, year[2:]], combinations, seen_combinations)
                    add_all_permutations([variant, month, year[2:], day], combinations, seen_combinations)
                    add_all_permutations([variant, year[2:], day, month], combinations, seen_combinations)
                    add_all_permutations([variant, year[2:], month, day], combinations, seen_combinations)

                if valid_day and valid_year:
                    add_all_permutations([variant, day, year[2:]], combinations, seen_combinations)
                    add_all_permutations([variant, year[2:], day], combinations, seen_combinations)

                if valid_month and valid_year:
                    add_all_permutations([variant, month, year[2:]], combinations, seen_combinations)
                    add_all_permutations([variant, year[2:], month], combinations, seen_combinations)

                if valid_year:
                    add_all_permutations([variant, year[2:]], combinations, seen_combinations)
                
    generate_combinations_with_dates(name, nickname, second_nickname, surname, second_surname, day, month, year, combinations, seen_combinations)

    add_name_variant_date_permutations(name, day, month, year, combinations, seen_combinations)    

    if name:
        filename = f"{name}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            for combination in combinations:
                file.write(f"{combination}\n")
        print()
        print()
        print(f"{yellow}[+] {nc}Dictionary stored in {cyan}{filename}{nc}")
        print()
    else:
        filename = "none.txt"
        with open(filename, "w", encoding="utf-8") as file: 
            for combination in combinations: 
                file.write(f"{combination}\n")
        print()
        print()        
        print(f"{yellow}[+] {nc}Dictionary stored in{cyan} {filename}{nc}")
        print()

    return combinations


# Main script
if __name__ == "__main__":
    # Display the logo with typewriter effect
    typewriter_with_cursor(logo, delay=0.005)
    input(f"\n{red}[+] {cyan}Press Enter to continue...{nc}")

    # Collect data from the user
    data = collect_data()
    clear_console()
    print()
    print(
        f"""
    {red}_______          _____  ___          ___  ___
    {cyan}|  _   \        |     \ |_|  _____ __| |__|_| _____  __     _   ______ _______
    {yellow}|  ¬   / _    _ |  _   | _  /____/|__  __| _ |  _  ||   \  | | /  _   || ____/_    _
    {green}|   __/ | |__| || |_|  || || |       | |  | || | | || |  \ | ||  / |  || |   | |__| |
    {red}|  |    |____  ||      || || |____   | |  | || |_| || |   \  ||  \_|  || |   |____  |
    {yellow}|__|         | ||____ / |_||_____/   |_|  |_||_____||_|    \_| \______||_|        | |
    {green}           _/ /                                                                 _/ /
    {cyan}          |__/                                                                 |__/
                                                                {" "*19}{red}[v{version}]
                                                                {" "*11} {green}[By {creator}]
        """
    )
    print()

    # Format and display the final data
    formatted_data = "; ".join(f'"{item.split(": ")[1]}"' for item in data)
    
    #Lists of possible ingredients
    fruits = {"fruta", "123", "44", "33", "22", "11", "55", "66", "77", "88", "99", "100","banana", "apple", "pear", "watermelon", "melon", "strawberry", "cherry", "blueberry", "orange", "lemon", "tangerine", "tomato", "cherry", "peach", 
            "nectarine", "pineapple", "mango", "coconut", "kiwi", "papaya", "lime", "fruits", "plátano", "platano", "manzana", "pera", "sandía", "sandia", "fresa", "arandano", "naranja", "limón", "limon", "mandarina", "tomate",
            "cereza", "melocotón", "melocoton", "nectarina", "piña", "mango", "coco", "kiwi", "papaya", "lima"}

    verdura = {"cebolla", "lechuga", "brocoli", "berenjena", "zanahoria", "hortalizas", "puerros", "porros", "cigalas", "cigarro", "maiz", "queso", "aceite", "vinagre", "cilantro",
                "perejil", "aguacate", "onion", "lettuce", "broccoli", "eggplant", "carrot", "vegetables", "leeks", "joints", "crayfish", "cigar", "corn", "cheese", "oil", "vinegar", "coriander",
                "parsley", "avocado"}

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 123, 234, 345, 456, 567, 678, 789, 12345, 321]

    cities = {"madrid", "barcelona", "ibiza", "tenerife", "cataluña", "berlin", "münich", "munich", "freiburg", "konstanz", "zürich", "zurich", "bern", "lussane", "newyork", "nyc", 
            "washington", "dallas", "LA", "paris", "valencia", "boston", "new mexico", "london", "nj", "newjersey"}

    words = {"hello", "hi", "bye", "goodbye", "hola", "adiós", "adios", "el", "la", "los", "the", "pretty", "boy", "girl", "chico", "chica", "amigos", "amigas", "friends", "by", "coc", "shooter", "twitch", "yt", "mama", "papa"}

    articulos = {"hello", "hi", "bye", "goodbye", "hola", "adiós", "adios", "el", "la", "los", "by", "the", "a"}

    colores = {"rojo", "azul", "amarillo", "marron", "verde", "rosa", "morado", "lila", "purpura", "cian", "vino", "red", "blue", "yellow", "brown", "green", "pink", "purple", "cyan", "wine"}
    special_characters = {"_", "#", "and"}
    
    teams = {"yankees", "barcelona", "barca", "realmadrid", "madridista", "cule", "manutd", "reddevils", "chelsea", "liverpool", "ynwa", "arsenal", "gunners", "bayern", "bayernmunich", "lakers", "kobebryant", "gsw", "warriors", "bulls", "mj",
            "celtics", "heatnation", "cowboys", "dc4life", "patriots12", "brady", "packers", "gopackgo", "nyy27rings", "dodgers", "ladodgers", "mpaleleafs", "tm4life", "blackhawks", "hawks", "atleti", "atletico", "atleti77"}

    teams_numbers = [7, 10, 9, 11, 12, 14, 13, 29, 19, 23, 22, 1999, 2008, 21, 24]

    #Generate combinations
    dictionary = generate_combinations(data, fruits, verdura, numbers, cities, words, colores, special_characters)
