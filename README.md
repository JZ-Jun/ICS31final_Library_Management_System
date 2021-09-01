# Library_Management_System
Paperwork:
Establishing library rules, regulations, policies and procedures.
Preparing the library due date sheets and maintaining overdue records.
Prepare and manage the library budgets, circulation files, statistics and inventories. Classify, and catalogue library books in order to properly making them ready for checkout.
Practical work:
Monitoring the Library, as well as keeping it organized, clean and neat.
Assisting students and staff members in fnding the desired reading material. Implementing and enforcing library rules, regulations, policies and procedures.
Placing spells on the books aimed at protecting them from mistreatment or theft. Checking the authenticity of the written permissions slips for the Restricted Section. Making sure all students have left the library by 8:00 pm, at which time the library closes. Overseeing the Study Hall and helping students with academic research and/or homework.
Undertaking any other reasonable duty at the request of the Headmaster/Headmistress of Hogwarts.
The program will keep track of the library's inventory.

Technical Details
1. Everything in Stage I goes into main.py
2. Take a command line argument which is the filename, which is the command script, in
your main statement. Do NOT take input! Read the file with the given filename.
3. Create a function called hogwarts_library() which takes one input argument which is a
string representing all the contents of command script.
4. Process the string line-by-line (Hint: split by newline character)
5. Create a variable (in modular scope) named "book_collection", as a dictionary with the key being a string, book_title, and the value a Book nametuple instance.
6. Create a function command_nb() which takes in one single line of command (a string) starting with "NB" and process accordingly
7. Create a function command_li() which takes in one single line of command (a string) starting with "LI" and process accordingly
8. Create a function command_db() which takes in one single line of command (a string) starting with "DB" and process accordingly
9. Create a function command_fb() which takes in one single line of command (a string) starting with "FB" and process accordingly
10. Create a function command_as() which takes in one single line of command (a string) starting with "AS" and process accordingly
11. Create a function command_lm() which takes in one single line of command (a string) starting with "LM" and process accordingly
12. Create a function command_pl() which takes in one single line of command (a string) starting with "PL" and process accordingly
13. In hogwarts_library(), call one of the command_* functions whenever a newline in command script is stepped onto
14. Add functions using the format/pattern above for other commands as needed in each stage
