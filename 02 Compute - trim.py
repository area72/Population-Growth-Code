# noinspection SpellCheckingInspection
def summm(listt):
    summ = 0
    for boots in listt:
        summ = summ + boots
    return summ


if __name__ == '__main__':

    input("Press Enter to begin...")

    current_year = int(input("___________________________\nEnter current year:"
                             "\n[Note: This should be an positive integer]\n"))
    current_pop = int(input("___________________________\nEnter Current Population:"
                            "\n[Note:  This should be an positive integer] "
                            "\n[Note: This calculator assumes the population \
                            pyramid to be a rectangle i.e, equal popupaltion"
                            "\n        distribution across all ages and equal male and female population] \n"))
    fertility_rate = float(input("___________________________\nNow enter fertility rate(average children per mother):"
                                 "\n[Note: This can be a float value]\n"))

    i = 0
    conception_ages = []
    conception_number = []
    while i <= fertility_rate:
        string = "Enter age of mother at her conception number " + str(i + 1) + ":\n"
        conception_ages.append(int(input(string)))
        i = i + 1
    cpm = fertility_rate
    while cpm > 0:
        jam = 0
        if cpm >= 1.0:
            jam = 1
        else:
            jam = cpm
        conception_number.append(jam)
        cpm = cpm - jam


    if year_of_interest <= current_year:
        print("We could not go ahead. Year of interest isnt after the current year.")
    else:
        print("\n___________________________________________________\nAll inputs taken. Calculating.....\n")
        file = open('Projection.txt', 'w')
        num_men = []
        num_women = []
        i = 0
        summu = 0
        initial = "Here is the population report for given inputs:\n\n"
        initial = initial + "Current year is: " + str(current_year) + ".\n\n"
        initial = initial + "Population is: " + str(current_pop) + ".\n\n"
        initial = initial + "Fertility rate is: " + str(fertility_rate) + "."

        for ij in range(len(conception_ages)):
            initial = initial + "\n\tAge of mother at childbirth number " + str(ij + 1) + \
                      " will be " + str(conception_ages[ij]) + "."

        initial = initial + "\n\nMortality Rate is:" + str(mortality_rate) + \
                  ".  (Infant deaths per 1000 live births)\n\n"

        initial = initial + "Average lifespan for both males and females will be: " + str(avg_lifespan) + " years.\n\n"

        initial = initial + "And finally, you have asked for population during year :" + str(year_of_interest) + "\n\n"
        initial + initial + "\n______________________________________________________________________________\n\n"

        initial = initial + "Findings:\n---------\n\n"
        file.write(initial)


        ij = 0
        rdiff = current_pop - ((int(current_pop / 2 / (avg_lifespan + 1))) * 2 * (avg_lifespan + 1))
        while ij <= avg_lifespan:
            num_men.append(int(current_pop / 2 / (avg_lifespan + 1)))
            if rdiff:
                num_men[-1] = num_men[-1] + 1
                rdiff = rdiff - 1
            num_women.append(int(current_pop / 2 / (avg_lifespan + 1)))
            if rdiff:
                num_women[-1] = num_women[-1] + 1
                rdiff = rdiff - 1
            summu = summu + num_men[ij] + num_women[ij]
            ij = ij + 1

        year = current_year
        birth_num = 0.000000000000000000
        first_doubling_flag = 0
        doubling_pop_ratio = 1
        doubling_time = 0
        will_double = True

        dummy_str = ""
        c = 0
        while year <= year_of_interest:
            birth_num = 0
            c = 0
            for i in range(len(conception_ages)):
                birth_num = birth_num + num_women[conception_ages[i]] * conception_number[i] * mortality_rate2

            c = num_women.pop()
            c = c + num_men.pop()
            num_men.insert(0, birth_num / 2)
            num_women.insert(0, birth_num / 2)
            
            if year == current_year:
                if c >= birth_num:
                    will_double = False

            year = year + 1
            dummy_str = "Year " + str(year) + " has population: " + str(int(summm(num_men) + summm(num_women))) + "\n"
            file.write(dummy_str)
            if first_doubling_flag == 0:
                doubling_pop_ratio = (summm(num_men) + summm(num_women)) / current_pop
                if doubling_pop_ratio >= 2:
                    first_doubling_flag = 1
                    doubling_time = year - current_year

        file.write("\n________________________________________________________\n\nConclusions:\n-----------\n\n")
        if not will_double:
            print("Population is headed for decline or stagnation.")
            file.write("Population is headed for decline or stagnation.\n\n")
        else:
            if first_doubling_flag == 1:
                print("Population will double every", doubling_time, "years.")
                dummy_strr = "Population will double every " + str(doubling_time) + " years.\n\n"
                file.write(dummy_strr)

        p = ((summm(num_men) + summm(num_women)) / current_pop)
        p = str("%.4f" % p)
        print("Over the next", year_of_interest - current_year, "years population will have become ", p,
              "of what is was initially")
        p = "Over the next " + str(
            year_of_interest - current_year) + " years population will have become " + p + "of what it was " \
                                                                                           "initially.\n "
        file.write(p)
        print("A report has been stored in text file: Projection.txt in same folder as this project.")
