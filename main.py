import __displaytable__
import numpy, csv
from rich import print


class LList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self, data=[]):
        self.head = None
        self.tail = None
        self.size = 0

        for i in range(len(data)):
            self.insert(data[i])

    def insert(self, val):
        new = LList.Node(val)
        if (self.head == None):
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.size += 1

    def remove(self, index):
        if(index == 0):
            self.head = self.head.next
            return
        cur = self.head
        i = 0
        while(index-1 != i):
            cur = cur.next
            i += 1
        cur.next = cur.next.next
        
    def __getitem__(self, index):
        if (index >= self.size):
            raise IndexError("list index out of range")
        cur = self.head
        while (index - 1 != -1):
            cur = cur.next
            index -= 1
        return cur.val

    def __len__(self):
        return self.size

    def print(self):
        cur = self.head
        while (cur != None):
            print(cur.val)
            cur = cur.next

filename = "test.csv"


def load(cols, skip_rows):
    return numpy.loadtxt(open(filename, "rb"),
                         delimiter=",",
                         usecols=cols,
                         skiprows=skip_rows)


with open(filename) as f:
    reader = csv.reader(f)
    column_names = next(reader)

input_variables = list(filter(lambda i: i[0] != "Y", column_names))
output_variables = list(filter(lambda i: i[0] == "Y", column_names))

input = load(tuple(range(len(input_variables))), 1)
otable = load(tuple(range(len(input_variables), len(column_names))), 1)

table = LList(numpy.array(list(input)).astype("int"))
outputs = LList(numpy.array(list(otable)).astype("int").T)

canonical_form_list = []


def solve(y):
    term_idx = 0
    for j in range(len(outputs[y])):
        flag = 0
        if (outputs[y][j] == 0):
            continue
        for input_idx in range(len(table[j])):
            flag = 1
            if (table[j][input_idx] == 0):
                canonical_form_list[y][
                    term_idx] += input_variables[input_idx] + "'"
                continue
            canonical_form_list[y][term_idx] += input_variables[input_idx]
        if (flag):
            canonical_form_list[y].append("+")
            canonical_form_list[y].append("")
            term_idx += 2
    del canonical_form_list[y][-2:]


for y in range(len(outputs)):
    canonical_form_list.append([""])
    solve(y)

for i in range(len(canonical_form_list)):
    print("\n[bold red]%s" % (output_variables[i]), end=": ")
    for j in range(len(canonical_form_list[i])):
        print("[bold green]{}".format(canonical_form_list[i][j]), end=" ")
print()
