class DataFrame:
    def __init__(self, filename = None, column_types = [], column_names = []):
        if filename == None:
            ...
        else:
            import csv
            data = []
            f = open(filename, "r")
            for row in csv.reader(f):
                data.append(row)
            f.close()

            self.column_types = column_types
            self.column_names = column_names
            self.shape = [ len(data), len(column_names) ]
            self.columns = [ data[i] for i in range(self.shape[0]) ]

    def __repr__(self):
        out = ""
        length = [0] * len(self.columns[0])
        for j in range(len(self.columns[0])):
            for i in range(len(self.columns)):
                if len(str(self.columns[i][j])) > length[j]: length[j] = len(str(self.columns[i][j]))

        for i in range(len(self.columns)):
            for j in range(len(self.columns[0])):
                out += self.columns[i][j]
                out += " "
                out += (" " * (length[j] - len(str(self.columns[i][j]))))
            out += "\n"

        return out

Data = DataFrame("iris.csv", column_types=[float, float, float, float], column_names=["a", "b", "c", "d"])
print(Data)
