# noinspection SpellCheckingInspection
import time
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

    avg_lifespan = int(input("___________________________\nEnter average lifespan :"
                             "\n[Note: This ia an integer. ] \n"))
    mortality_rate = float(input("___________________________\nEnter infant mortality rate: "
                                 "[Note: This is a floating point integer that notes deaths per 1000 live births.] \n"))
    mortality_rate2 = 1.0 - (mortality_rate / (mortality_rate + 1000))

    year_of_interest = int(input("___________________________\n\
    Enter the year for which you would like population projection:"
                                 "\n[Note: THis is an integer value that should be greater than current year.]\n"))

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
        num_men2 = num_men
        num_women2 = num_women

        year = current_year
        birth_num = 0.000000000000000000
        first_doubling_flag = 0
        doubling_pop_ratio = 1
        doubling_time = 0
        will_double = True
        will_grow = "Randon"

        dummy_str = ""
        c = 0
        while year <= year_of_interest:
            birth_num = 0
            c = 0
            for i in range(len(conception_ages)):
                birth_num = birth_num + int(num_women[conception_ages[i]] * conception_number[i] * mortality_rate2)

            c = num_women.pop()
            c = c + num_men.pop()
            num_men.insert(0, round(birth_num / 2))
            num_women.insert(0, round(birth_num / 2))

            if year == current_year:
                if c >= birth_num:
                    will_double = False
                if c < birth_num:
                    will_grow = "Yes"

            year = year + 1
            dummy_str = "Year " + str(year) + " has population: " + str(int(summm(num_men) + summm(num_women))) + " with "+ str(num_men[0]+num_women[0]) + " births and " +str(c) + " deaths"+"\n"
            file.write(dummy_str)
            if first_doubling_flag == 0:
                doubling_pop_ratio = (summm(num_men) + summm(num_women)) / current_pop
                if doubling_pop_ratio >= 2:
                    first_doubling_flag = 1
                    doubling_time = year - current_year

        file.write("\n________________________________________________________\n\nConclusions:\n-----------\n\n")
        if will_grow == "Yes":
            print("Population count will not decline. Growth is expected.")
            file.write("Population count will not decline. Growth is expected.\n\n")

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
                                                                                           "initially.\n\n "
        w= "In the year " + str(year_of_interest) + ", the population will have become "\
           + str(round((summm(num_men) + summm(num_women))))
        print(w,"\n")
        file.write(p)
        file.write(w)

        if(will_grow == "Yes" and first_doubling_flag == 0):
            print("\nIt is known that population will grow."\
                  +"If you would like to calculate time taken for population to double, input 'Y': \n")
            wannadouble = ""
            wannadouble = str(input())
            wannadouble = wannadouble.lower()
            if(wannadouble == 'y'):
                print("", end = '')
                ij = 0
                summu=0
                num_men.clear()
                num_women.clear()
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
                print(summu) # 4545


                has_doubled_ratio = ((summm(num_men) + summm(num_women)) / current_pop)
                has_doubled = 'n'

                time_end = time.time() +60
                year_f=current_year
                while(time_end  >= time.time() and has_doubled_ratio < 2.00):
                    birth_num = 0
                    for ik in range(len(conception_ages)):
                        birth_num = birth_num + int(num_women[conception_ages[ik]] * conception_number[ik] * mortality_rate2)
                    num_women.pop()
                    num_men.pop()
                    num_men.insert(0, round(birth_num / 2))
                    num_women.insert(0, round(birth_num / 2))
                    year_f=year_f+1
                    has_doubled_ratio = ((summm(num_men) + summm(num_women)) / current_pop)
                if(has_doubled_ratio>=2.0000):
                    pop_dub = "Population count will double every "+ str(year_f-current_year) + " years."
                    file.write(pop_dub)
                    file.write("\n\n")
                    print(pop_dub)
                else:
                    pop_dub = "---"
                    pop_dub = "Population was computed till year " + str(year_f) + " in which it reaches " + str(summm(num_men) + summm(num_women)) + "\n"
                    pop_dub = pop_dub + "Though population will grow, it will not double even in the next " + str(year_f-current_year) + " years.\n"
                    pop_dub = pop_dub + "The only conclusion we can arrive is that" + " population will grow but slowly.\n\n"

                    print(pop_dub)
                    file.write(pop_dub)
            else:
                print("")

        print("A report has been stored in text file: Projection.txt in same folder as this file.")
