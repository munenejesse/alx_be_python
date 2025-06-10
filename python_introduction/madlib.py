noun = str(input("noun: "))
verb = str(input("verb: "))
adjective = str(input("adjective: "))
verb2 = str(input("verb2: "))

class madlibs():
    def first_method():
        madlib = f"On a beautiful ({adjective} day, I went to the zoo. I saw a funny {adjective} monkey swinging from the trees. Then, I spotted a majestic {adjective} lion lounging in the sun.  What a wild and {adjective} experience!"
        print(madlib)

print(madlibs())