import sys
import operator

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

matrix_all_hall = dict()


def creating_hall(take_command):
    hall_name = []
    row_column = []

    if (len(take_command) == 2):
        hall_name = str(take_command[0])
        row_column = take_command[1].split("x")



    sayac = 0
    while (sayac < 1):
        if (len(take_command) < 2):
            print("Error: Not enough parameters for creating a hall!", file=output_file)
            print("Error: Not enough parameters for creating a hall!")
            break
        elif (len(take_command) > 2):
            print("Error: Too much parameters for creating a hall!", file=output_file)
            print("Error: Too much parameters for creating a hall!")
            break
        elif (int(row_column[1]) > 26):
            break
        else:
            print("The hall '{}' having".format(hall_name), (int(row_column[0]) * int(row_column[1])),
                  "seats has been created", file=output_file)
            print("The hall '{}' having".format(hall_name), (int(row_column[0]) * int(row_column[1])),
                  "seats has been created")

        sayac += 1

        matrix_list = []
        for i in range(int(row_column[0])):
            row = []
            for i in range(int(row_column[1])):
                row.append("X")
            matrix_list.append(row)

        # matrix_dict =  dict()
        # matrix_dict[hall_name] = matrix_list
        # matrix_all_hall.append(matrix_dict)
        matrix_all_hall[hall_name] = {}
        for k in range(int(row_column[0])):
            matrix_all_hall[hall_name][alphabet[k]] = []

            for j in range(int(row_column[1])):
                matrix_all_hall[hall_name][alphabet[k]].append("X")


def selling_ticket(take_command):
    if len(take_command) >= 4 :



        audience_name = take_command[0]
        fare_type = take_command[1]
        which_hall = take_command[2]
        ticket_place = take_command[3:]

        column = len(matrix_all_hall[which_hall]["A"])

        for i in ticket_place:

            if not "-" in i:
                if int(i[1:]) > column-1:
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!",
                          file=output_file)
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!")
                    continue

                if matrix_all_hall[which_hall][str(i[0])][int(i[1])] == "X":

                    if fare_type == "full":
                        matrix_all_hall[which_hall][str(i[0])][int(i[1])] = "F"
                        print("Success: " + audience_name + " has bought " + i + " at " + which_hall, file=output_file)
                        print("Success: " + audience_name + " has bought " + i + " at " + which_hall)

                    elif fare_type == "student":
                        matrix_all_hall[which_hall][str(i[0])][int(i[1])] = "S"
                        print("Success: " + audience_name + " has bought " + i + " at " + which_hall, file=output_file)
                        print("Success: " + audience_name + " has bought " + i + " at " + which_hall)

                else:
                    print("Warning: The seat " + i + " cannot be sold to " + audience_name + " since it was already sold!")
                    print("Warning: The seat " + i + " cannot be sold to " + audience_name + " since it was already sold!",
                          file=output_file)
                    continue
            else:

                j = i.split("-")
                hypen_list = []
                number = 0
                if int(j[1]) <= column-1:
                    for k in range(int(j[0][1:]), int(j[1])):
                        l = j[0][0] + str(k)
                        hypen_list.append(l)
                    for x in range(int(j[0][1:]), int(j[1])):
                        if matrix_all_hall[which_hall][i[0]][x] == "X":
                            number += 1

                    if number == len(hypen_list):
                        for k in range(int(j[0][1:]), int(j[1])):

                            if fare_type == "full":
                                matrix_all_hall[which_hall][str(i[0])][k] = "F"
                            elif fare_type == "student":
                                matrix_all_hall[which_hall][str(i[0])][k] = "S"

                        print("Success: " + audience_name + " has bought " + i + " at " + which_hall, file=output_file)
                        print("Success: " + audience_name + " has bought " + i + " at " + which_hall)
                    else:
                        print(
                            "Warning: The seat " + i + " cannot be sold to " + audience_name + " due some of them have already been sold!",
                            file=output_file)
                        print(
                            "Warning: The seat " + i + " cannot be sold to " + audience_name + " due some of them have already been sold!")
                        continue
                else:
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!",
                          file=output_file)
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!")
                    continue
    else:
        print("Error: Not enough parameters for selling ticket!",file=output_file)
        print("Error: Not enough parameters for selling ticket!")





def canceling_ticket(take_command):
    if len(take_command) >= 2:

        which_hall = take_command[0]
        ticket_place = take_command[1:]
        column = len(matrix_all_hall[which_hall]["A"])

        for i in ticket_place:

            if not "-" in i:
                if int(i[1:]) > column:
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!",
                          file=output_file)
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!")
                    continue

                if matrix_all_hall[which_hall][str(i[0])][int(i[1])] != "X":

                    matrix_all_hall[which_hall][str(i[0])][int(i[1])] = "X"
                    print(
                        "Success: The seat " + i + " at '" + which_hall + "' has been canceled and now ready to be sell again",
                        file=output_file)
                    print(
                        "Success: The seat " + i + " at '" + which_hall + "' has been canceled and now ready to be sell again")

                else:
                    print("Error: The seat " + i + " at '" + which_hall + "' has already been free! Nothing to cancel")
                    print("Error: The seat " + i + " at '" + which_hall + "' has already been free! Nothing to cancel",
                          file=output_file)
                    continue

            else:
                j = i.split("-")
                hypen_list = []
                number = 0
                if int(j[1]) <= column:
                    for k in range(int(j[0][1:]), int(j[1])):
                        l = j[0][0] + str(k)
                        hypen_list.append(l)

                    for k in hypen_list:
                        if matrix_all_hall[which_hall][str(k[0])][int(k[1:])] == "X":
                            number += 1

                    if number == len(hypen_list):
                        print("Success: The seats " + i + " at '" + which_hall + "' have been canceled and now ready to be sell again",file=output_file)
                        print("Success: The seats " + i + " at '" + which_hall + "' have been canceled and now ready to be sell again")

                    else:
                        for k in hypen_list:
                            if matrix_all_hall[which_hall][str(k[0])][int(k[1:])] == "X":
                                print("Error: The seat "+k+" at '"+which_hall+"' has already been free! Nothing to cancel",file=output_file)
                                print("Error: The seat "+k+" at '"+which_hall+"' has already been free! Nothing to cancel")
                            else:
                                matrix_all_hall[which_hall][str(k[0])][int(k[1:])] = "X"
                                print("Success: The seat "+k+" at '"+which_hall+"'has been canceled and now ready to sell again",file=output_file)
                                print("Success: The seat "+k+" at '"+which_hall+"'has been canceled and now ready to sell again")


                else:
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!",file=output_file)
                    print("Error: The hall '" + which_hall + "' has less column than the specified index " + i + "!")
                    continue
    else :
        print("Error: Not enough parameters for canceling ticket!",file=output_file)
        print("Error: Not enough parameters for canceling ticket!")


def balance(take_command):
    if len(take_command) >= 1 :


        which_hall = take_command

        for i in which_hall:
            number_student = 0
            number_full = 0

            for j in matrix_all_hall[i].values():

                for k in j:
                    if k == "S":
                        number_student += 1
                    elif k == "F":
                        number_full += 1
                    else:
                        None

            print("Hall report of '" + i + "'")
            print("-------------------------")
            print("Sum of students = " + str(number_student) + ", Sum of full fares = " + str(
                number_full) + ", Overall = " + str(number_full + number_student))
            print("Hall report of '" + i + "'",file=output_file)
            print("-------------------------",file=output_file)
            print("Sum of students = " + str(number_student) + ", Sum of full fares = " + str(
                number_full) + ", Overall = " + str(number_full + number_student),file=output_file)
    else :
        print("Error: There is no hall to show balance!")
        print("Error: There is no hall to show balance!",file=output_file)


def showing_hall(take_command):

    which_halls = take_command

    for i in which_halls:
        lenght = len(matrix_all_hall[i]["A"])

        sorted_matrix = sorted(matrix_all_hall[i].items(), key=operator.itemgetter(0), reverse=True)

        numbers=[]
        for i in range(0,lenght,1):
            numbers.append(i)

        for i in sorted_matrix:
            print(i[0], " ", "  ".join(i[1]))
            print(i[0], " ", "  ".join(i[1]),file=output_file)

        print("    ",end="")
        print("    ",end="",file=output_file)
        for i in  numbers:

            if i<=8:
                print(numbers[i],end="  ")
                print(numbers[i],end="  ",file=output_file)
            else:
                print(numbers[i],end=" ")
                print(numbers[i],end=" ",file=output_file)
    print("\n")
    print("\n",file=output_file)


input_file = open(sys.argv[1], "r")
output_file = open("out.txt", "w")

commands_list = []
for line in input_file:
    commands_list.append(line.split())

hall_names = []
for command in commands_list:
    if command[0] == "CREATEHALL":
        if command[1] in hall_names:
            print("Warning: Cannot create the hall for the second time. The cinema has already {}".format(command[1]),
                  file=output_file)
            print("Warning: Cannot create the hall for the second time. The cinema has already {}".format(command[1]))
            continue
        else:
            hall_names.append(command[1])
            creating_hall(command[1:])
    elif command[0] == "SELLTICKET":
        selling_ticket(command[1:])
    elif command[0] == "CANCELTICKET":
        canceling_ticket(command[1:])
    elif command[0] == "BALANCE":
        balance(command[1:])
    elif command[0] == "SHOWHALL":
        showing_hall(command[1:])

input_file.close()
