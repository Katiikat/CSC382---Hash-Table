class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for x in range(self.MAX)]

    def get_hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, val):
        hnum = self.get_hash(key)
        found = False
        for idx, item in enumerate(self.arr[hnum]):
            if len(item) == 2 and item[0] == key:
                self.arr[hnum][idx] = (key, val)
                found = True
        if not found:
            self.arr[hnum].append((key, val))

    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, kv in enumerate(self.arr[index]):
            if kv[0] == key:
                del self.arr[index][idx]

    def print_arr(self):
        print(self.arr)


# dictionary to hold our phone book data
phonebook = {}

with open("phonebook.txt", "r") as i:
    for line in i:
        info = line.split(',')
        name = info[0].strip()
        phone_num = info[1].strip()
        phonebook[name] = phone_num

    # for item in phonebook:
    #     print(item)
test = HashTable()

for names in phonebook:
    test.__setitem__(names, phonebook[names])

print("\n\n")
test.print_arr()
while True:
    choice = input("\n\nWhat would you like to do? Please type a number. \n1)Add a contact\n2)Retrieve a contact\n"
                   "3)Remove a contact\nChoice: ")

    if choice == "1":
        name = input("What is the first name of the contact you wish to add?\nFirst name: ")
        phone_num = input("What is the phone number of the contact you wish to add?\n"
                          "Use this format: 000-000-0000\nNumber: ")
        test.__setitem__(name, phone_num)
        test.print_arr()
    if choice == "2":
        name = input("What is the first name of the contact you would like to retrieve?\nFirst name: ")
        print(f"{name}'s number is {test.__getitem__(name)}")
    if choice == "3":
        name = input("What is the first name of the contact you would like to remove?\nFirst name: ")
        test.__delitem__(name)
        test.print_arr()

    answer = input("Would you like to do something else? Yes or No\n")
    answer = answer.upper()

    if answer == "NO" or answer == "N":
        break
