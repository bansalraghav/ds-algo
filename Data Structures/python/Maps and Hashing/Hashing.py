#Hash value is calculated by from the first 2 letters of the word by the following formula:
#Hash Value = ( (ASCII value of first letter * 100) + ASCII value of the second letter)



class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
            else:
                return -1

    def calculate_hash_value(self, string):
        hvalue = (ord(string[0])*100) + ord(string[1])
        return hvalue
