from csv import reader


def read_csv(path, class_name):
    objects_list = []
    with open(path, 'r', errors="ignore") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                obj = object()
                #obj = class_name(row[0], row[1], row[2])
                obj = class_name(**)
                objects_list.append(obj.api())
    return objects_list
