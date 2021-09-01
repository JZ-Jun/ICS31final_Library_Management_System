############ IMPORT HERE #############

import utilities
from utilities import datetime
from collections import deque

import sys
LINE_WIDTH = 60
VALID_PASS_CODE = {"Accio", "Protego"}

############## IMPLEMENT FUNCTIONS HERE ############
def printBooklist(listb):
    print("------------------------------------")
    print("Title: ", listb.title)
    print("Author: ", listb.author)
    print("Date: ", listb.year_published)
    print("Subject: ", listb.subject)
    print("Section: ", listb.section)


def command_pl(line):
    print(line[2:].strip())


def command_li(line):
    if not listbook:
        print("*********************LIBRARY INVENTORY**********************")
        print("Number of books available:  0")
        print("------------------------------------")
    else:
        print("*********************LIBRARY INVENTORY**********************")
        print("Number of books available:  ", len(listbook))
        for i in sorted(listbook, key=lambda x: x.title):
            printBooklist(i)
        print("------------------------------------")


def command_nb(line):
    # line="title=Curses and Counter-Curses,author=Vindictus Viridian,year_published=1703,subject=Curses,section=Restricted"
    # curses = Book("Curses and Counter-Curses", "Vindictus Viridian", 1703, "Curses", "Restricted")
    x = line[2:].strip().split(',')
    for i in x:
        if "title=" in i:
            title = i[6:]
        elif "author=" in i:
            author = i[7:]
        elif "year_published=" in i:
            year_published = int(i[15:])
        elif "subject=" in i:
            subject = i[8:]
        else:
            section = i[8:]
    book = utilities.Book(title, author, year_published, subject, section)
    if book in listbook:
        print(book.title, "already present.")
    else:
        utilities.book_collection[book.title] = book
        listbook.append(book)
    # print(utilities.book_collection)


def command_db(line):
    x = line[2:].strip()
    title_name = x[6:]
    flag = True
    for i in listbook:
        if i.title == title_name:
            listbook.remove(i)
            flag = False

    if title_name in utilities.book_collection:
        del utilities.book_collection[title_name]
        flag = False
    for j in list(utilities.checkouts.keys()):
        if j == title_name:
            del utilities.checkouts[j]
            flag = False
    if title_name in utilities.reservations:
        del utilities.reservations[title_name]
        flag=False
    if flag == True:
        print(title_name,"Not Found. Cannot be deleted.")

    # print(listbook)


def command_fb(line):
    x = line[2:].strip()
    # print (x)
    y = x.split(',')
    # string1=y[0][0:y[0].index('=')+1]+"'"+y[0][y[0].index('=')+1:]+"'"
    # print(string1)
    print("************************BOOK SEARCH*************************")
    if x == "":
        print("Number of books found:  ", len(listbook))
        for i in sorted(listbook, key=lambda x: x.title):
            printBooklist(i)
        print("------------------------------------")
    else:
        # print(listbook)
        # print(y)
        newlist = []
        for j in y:
            if "year_published=" in j:
                newlist.append(str(j))
            else:
                string1 = j[0:j.index('=') + 1] + "'" + j[j.index('=') + 1:] + "'"
                newlist.append(string1)
        # print(newlist)
        newlist2 = []
        for i in listbook:
            if all(x in str(i) for x in newlist):
                newlist2.append(i)
        if not newlist2:
            print("No Books Found")
        else:
            print("Number of books found:  ", len(newlist2))
            for i in newlist2:
                printBooklist(i)
        print("------------------------------------")


def command_as(line):
    # student_name = Draco Malfoy, house = Slytherin
    # harry_potter = Student("Harry Potter", [curses], "Gryffindor")
    x = line[2:].strip().split(',')
    for i in x:
        if "student_name=" in i:
            student_name = i[13:]
        elif "house=" in i:
            house = i[6:]
        else:
            checked_out_books = []
    student = utilities.Student(student_name, house, [])
    if student in liststudent:
        print(student.student_name, "is already present.")
    else:
        utilities.library_members[student.student_name] = student
        liststudent.append(student)


def command_lm(line):
    print("**********************LIBRARY MEMBERS***********************")
    flaghouse = True
    # print(liststudent)
    print("Gryffindor:")
    for i in sorted(liststudent, key=lambda x: x.student_name):
        if i.house == "Gryffindor":
            flaghouse = False
            print(i.student_name)
    if flaghouse == True:
        print("No Registered Members")
    flaghouse = True
    print("Hufflepuff:")
    for i in sorted(liststudent, key=lambda x: x.student_name):
        if i.house == "Hufflepuff":
            flaghouse = False
            print(i.student_name)
    if flaghouse == True:
        print("No Registered Members")
    flaghouse = True
    print("Ravenclaw:")
    for i in sorted(liststudent, key=lambda x: x.student_name):
        if i.house == "Ravenclaw":
            flaghouse = False
            print(i.student_name)
    if flaghouse == True:
        print("No Registered Members")
    flaghouse = True
    print("Slytherin:")
    for i in sorted(liststudent, key=lambda x: x.student_name):
        if i.house == "Slytherin":
            flaghouse = False
            print(i.student_name)
    if flaghouse == True:
        print("No Registered Members")


def command_sd(line):
    sentence = line[2:].strip()
    sentence = ''.join(sentence.split())
    utilities.start_date = sentence
    print("*************HOGWARTS LIBRARY MANAGEMENT SYSTEM*************")
    var1 = convertdate(utilities.start_date)
    var2 = var1.strftime('%A %d, %B %Y')
    len1 = int((60 - len(var2)) / 2)
    print('*' * len1 + var2 + (60 - len1 - len(var2)) * '*')


def convertdate(line):
    x = line.split('/')
    date1 = datetime.date(int(x[2]), int(x[0]), int(x[1]))
    return date1


def convertdatetostr(line):
    x = line.split('-')
    str1 = str(x[1]) + '/' + str(x[2]) + '/' + str(x[0])
    return str1


def command_cb(line):
    x = line[2:].strip().split(',')
    number_of_days = 0
    pass_code = None
    for i in x:
        if "title=" in i:
            title = i[6:]
        elif "student_name=" in i:
            student_name = i[13:]
        elif "number_of_days=" in i:
            number_of_days = i[15:]
        elif "pass_code=" in i:
            pass_code = i[10:]
    if number_of_days == 0:
        number_of_days = 14
    star_date = convertdate(utilities.start_date)
    end_date = star_date + datetime.timedelta(days=int(number_of_days))

    if not student_name in utilities.library_members:
        print(student_name, "is not a registered library member.")
        return

    if title in utilities.checkouts:
        print(title, "is currently unavailable to be checked out.")
        return

    if title not in utilities.book_collection:
        print(title, "not in inventory.")
        return

    book = utilities.book_collection[title]

    if book.section == 'Restricted' and pass_code == None:
        print(title, "is a Restricted book, and requires a pass code to be checked out.")
        #print("NoAccess is not a valid pass code.")
        return
    if book.section == 'Restricted' and not pass_code in VALID_PASS_CODE:
        print("{0} is not a valid pass code.".format(pass_code))
        return
    temp_checkout = utilities.Checkout(utilities.book_collection[title],
                                       utilities.library_members[student_name], end_date)
    utilities.checkouts[title] = temp_checkout
    del utilities.book_collection[title]
    '''
    x = line[2:].strip().split(',')
    number_of_days = 0
    pass_code = None
    for i in x:
        if "title=" in i:
            title = i[6:]
        elif "student_name=" in i:
            student_name = i[13:]
        elif "number_of_days=" in i:
            number_of_days = i[15:]
        elif "pass_code=" in i:
            pass_code = i[10:]
    if number_of_days == 0:
        number_of_days = 14
    star_date = convertdate(utilities.start_date)
    end_date = star_date + datetime.timedelta(days=int(number_of_days))

    if any(title == i for i in list(utilities.checkouts.keys())):
        print(title, "is currently unavailable to be checked out.")
    elif all(title != i for i in list(utilities.book_collection.keys())):
        print(title, "not in inventory.")
    for i in list(utilities.book_collection.keys()):
        if i == title:
            if utilities.book_collection[i][4] == 'Restricted':
                if (pass_code == None):
                    print(i, "is a Restricted book, and requires a pass code to be checked out.")
                elif (pass_code != None and (pass_code == 'Accio' or pass_code == 'Protego')):
                    if all(student_name != i.student_name for i in list(utilities.library_members.values())):
                        print(student_name, "is not a registered library member.")
                        break
                    temp_checkout = utilities.Checkout(utilities.book_collection[i],
                                                       utilities.library_members[student_name], end_date)
                    utilities.checkouts[title] = temp_checkout
                    del utilities.book_collection[i]
            else:
                if all(student_name != i.student_name for i in list(utilities.library_members.values())):
                    print(student_name, "is not a registered library member.")
                    break
                temp_checkout = utilities.Checkout(utilities.book_collection[i],
                                                   utilities.library_members[student_name], end_date)
                utilities.checkouts[title] = temp_checkout
                del utilities.book_collection[i]

    # print(utilities.book_collection)
    '''

def command_cr():
    print('***CURRENT CHECKOUT REPORT**************' + utilities.start_date + '**********')
    # print(len(list(utilities.checkouts.values())))
    if len(list(utilities.checkouts.values())) == 0:
        print("No Books Checked Out.")
    print('Book Title                        Student Name      Due Date')
    print('------------------------------------------------------------')

    for i in sorted(list(utilities.checkouts.values()),
                    key=lambda kv: (kv.student.house, kv.student.student_name, kv.book.title)):
        print(utilities.checkout_report_format_string.format(title=i[0].title[0:30], name=i[1].student_name[0:20],
                                                             due_date=convertdatetostr(str(i[2]))[0:10]))


def command_la():
    # print(utilities.book_collection)
    print("Number of books in available: " + str(len(utilities.book_collection)))
    for i in sorted(list(utilities.book_collection.values()),
                    key=lambda kv: (kv.title)):
        print("------------------------------------")
        print("Title: ", i.title)
        print("Author: ", i.author)
        print("Date: ", i.year_published)
        print("Subject: ", i.subject)
        print("Section: ", i.section)
    print("------------------------------------")


def command_dt():
    print("*******BOOKS DUE TODAY******************" + utilities.start_date + (20 - len(utilities.start_date)) * '*')
    # print(utilities.checkouts)
    var1 = convertdate(utilities.start_date)
    # print(var1)
    if all(var1 != i.due_date for i in list(utilities.checkouts.values())):
        print("No books due today.")
    for i in sorted(list(utilities.checkouts.values()),
                    key=lambda kv: (kv.due_date)):
        if var1 == i.due_date:
            print(utilities.due_today_format_string.format(title=i[0].title[0:35], name=i[1].student_name[0:25]))


def command_ad():
    print("*************HOGWARTS LIBRARY MANAGEMENT SYSTEM*************")
    var1 = convertdate(utilities.start_date)
    var2 = var1 + datetime.timedelta(days=1)
    var3 = var2.strftime('%A %d, %B %Y')
    len1 = int((60 - len(var3)) / 2)
    print('*' * len1 + var3 + (60 - len1 - len(var3)) * '*')

    utilities.start_date = convertdatetostr(str(var2))
    # print(var1)
    # print(var2)
    # print(utilities.start_date)
    #add_penalties()


def command_rh(line):

    x = line[2:].strip().split(',')
    number_of_days = 0
    pass_code = None
    for i in x:
        if "title=" in i:
            title = i[6:]
        elif "student_name=" in i:
            student_name = i[13:]
        elif "number_of_days=" in i:
            number_of_days = i[15:]
    if number_of_days == 0:
        number_of_days = 14
    star_date = convertdate(utilities.start_date)
    end_date = star_date + datetime.timedelta(days=int(number_of_days))
    flag = False
    if title not in list(utilities.checkouts.keys()) and title not in list(utilities.book_collection.keys()):
        flag = True
    if flag == True:
        print(title, "not in inventory.")
        return
    if title in utilities.checkouts:
        checkout = utilities.checkouts[title]
        if checkout.student.student_name == student_name:
           print("{0} currently has checked out {1}.".format(checkout.student.student_name, title))
           return
    if all(student_name != i.student_name for i in list(utilities.library_members.values())):
        print(student_name, "is not a registered library member.")
        return
    if any(title == i for i in list(utilities.book_collection.keys())):
        print(title, "is available to be checked out. Use command to checkout book.")
        return
    else:
        if len(utilities.reservations) == 0 or title not in list(utilities.reservations.keys()):
            templist = deque()
            temp_reservations = (student_name, star_date, end_date)
            templist.append(temp_reservations)
            utilities.reservations[title] = templist
        elif title in list(utilities.reservations.keys()):
            templist = utilities.reservations[title]
            for student_reserve in templist:
                if student_name == student_reserve[0]:
                    print("{0} has already requested a hold for {1}.".format(student_name, title))
                    return

            temp_reservations = (student_name, star_date, end_date)
            templist.append(temp_reservations)
            utilities.reservations[title] = templist
    # print(utilities.reservations)


def command_hr():
    # print(utilities.reservations.keys())
    # print(list(utilities.reservations.values()))
    print('*****HOLD REQUEST REPORT****************' + utilities.start_date + '**********')
    print('Student Name                        # of Days Requested')
    print('------------------------------------------------------------')
    if not list(utilities.reservations.items()):
        print("No Holds Requested.")
        return
    for i in sorted(list(utilities.reservations.items()),
                    key=lambda kv: kv[0]):
        print(i[0])
        for j in i[1]:
            # print(j[0][0])
            print(utilities.hold_report_format_string.format(name=j[0], number_of_days=str((j[2] - j[1]).days)))
        print('------------------------------------------------------------')


def command_rb(line):
    x = line[2:].strip().split('=')
    title = x[1]
    if title not in utilities.checkouts:
        #print(title, "not in inventory.")
        print("Invalid Return Request for {0}.".format(title))
        return
    if title in utilities.reservations and utilities.checkouts:
        checkout = utilities.checkouts[title]
        oldstudent = checkout.student
        reservation = utilities.reservations[title].popleft()
        newstudentname = reservation[0]
        newstudent = utilities.library_members[newstudentname]
        timedelta = reservation[2] - reservation[1]
        newdate = convertdate(utilities.start_date) + timedelta
        newcheckout = utilities.Checkout(checkout.book, newstudent, newdate)
        utilities.checkouts[title] = newcheckout
        return
    utilities.book_collection[title] = utilities.checkouts[title].book
    del utilities.checkouts[title]

def find_penalties():
    student_penalty={}
    for i in utilities.checkouts.values():
        if i.due_date < convertdate(utilities.start_date):
            days1 = (convertdate(utilities.start_date) - i.due_date).days
            penalty_index=days1
            if days1>5:
                penalty_index=5
            student_penalty[i.student.student_name]=utilities.penalties[penalty_index]
    return student_penalty
def command_or():
    # print(utilities.checkouts)
    print("********OVERDUE REPORT*************" + utilities.start_date + "*******# Days**")
    flag = False
    due_report_format_string = "{title:<33}{name:^19.15}{days:<8}"
    for i in sorted(list(utilities.checkouts.values()),
                    key=lambda kv: (kv.book.title), reverse=False):
        if i.due_date < convertdate(utilities.start_date):
            # print (i.due_date)
            # print("{0:<30}".format(i.book.title), "{0:^20}".format(i.student.student_name),
            #       (convertdate(utilities.start_date) - i.due_date).days)
            days = (convertdate(utilities.start_date) - i.due_date).days
            print(due_report_format_string.format(title=i.book.title, name=i.student.student_name, days=days))
            #newstudent = utilities.Student(i.student.student_name, i.student.house,
            #                              utilities.penalties[(convertdate(utilities.start_date) - i.due_date).days])
            # print(newstudent)
            #utilities.library_members[i.student.student_name] = newstudent
            flag = True
    if flag == False:
        print("No books overdue today.".center(60))

def command_ur(line):
    x = line[2:].strip().split('=')
    student_name = x[1]
    if not student_name in utilities.library_members:
        print(student_name, "is not a registered member of the library.")
        return
    #print(utilities.checkouts)
    #print(utilities.library_members)
    len1=44-len(student_name)
    print('*'*int(len1/2)+"USER REPORT for "+student_name+(len1-int(len1/2))*'*')
    student_penalty=find_penalties()
    if student_name in student_penalty:
        print(student_name, "Curse:",
                       student_penalty[student_name].curse)
    flag = True
    for i in sorted(utilities.checkouts.values()):
        if i.student.student_name==student_name:
            if flag==True:
                print("-------------------------CHECKOUTS--------------------------")
                flag=False
            print(utilities.user_report_format_string.format(title=i.book.title,due_date=convertdatetostr(str(i.due_date))))
    if flag == True:
        print("-------------------------CHECKOUTS--------------------------")
        print("No checkouts.")
    flag1=True
    flag2=True
    for i in utilities.reservations.items():
        for j in range(len(i[1])):
            if i[1][j][0]==student_name:
                if flag1 == True:
                    print("---------------------------HOLDS----------------------------")
                    flag1 = False
                print(utilities.hold_report_format_string.format(
                    name=i[0],
                    number_of_days=str((i[1][j][2]-i[1][j][1]).days)))
                flag2=False
    if flag2==True:
        print("---------------------------HOLDS----------------------------")
        print("No holds.")


    #print()
def command_dr(line):
    x = line[2:].strip().split(',')
    start_date=convertdate((x[0].split('='))[1])
    end_date= convertdate((x[1].split('='))[1])
    print("***BOOKS DUE BETWEEN********{0} to {1}********".format((x[0].split('='))[1],(x[1].split('='))[1]))
    flag=True
    for i in sorted(list(utilities.checkouts.values()),
                    key=lambda kv: (kv.book.title)):
        #print(i.due_date)
        if i.due_date>=start_date and i.due_date<=end_date:
            #print(i)
            print(utilities.due_report_format_string.format(
                title=i.book.title,name=i.student.student_name))
            flag=False
    if flag==True:
        print("No books due for the given dates.")

if __name__ == "__main__":
    list1 = []
    filename = "Stage4Commands.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    listbook = []
    liststudent = []
    with open(filename) as f:
        list1 = f.read().splitlines()

    for i in list1:
        stripi = i.strip()
        check = stripi[0:2].upper()
        if check == "PL":
            command_pl(stripi)
        elif check == "LI":
            command_li(stripi)
        elif check == "NB":
            command_nb(stripi)
        elif check == "DB":
            command_db(stripi)
        elif check == "FB":
            command_fb(stripi)
        elif check == "AS":
            command_as(stripi)
        elif check == "LM":
            command_lm(stripi)
        elif check == "SD":
            command_sd(stripi)
        elif check == "CB":
            command_cb(stripi)
        elif check == "CR":
            command_cr()
        elif check == "LA":
            command_la()
        elif check == "DT":
            command_dt()
        elif check == "AD":
            command_ad()
        elif check == "RH":
            command_rh(stripi)
        elif check == "HR":
            command_hr()
        elif check == "RB":
            command_rb(stripi)
        elif check == "OR":
            command_or()
        elif check == "UR":
            command_ur(stripi)
        elif check == "DR":
            command_dr(stripi)
