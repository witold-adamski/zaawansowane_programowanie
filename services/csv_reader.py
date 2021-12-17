from csv import reader


def read_csv(path, class_name):
    objects_list = []
    with open(path, 'r', errors="ignore") as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header is not None:
            for row in csv_reader:
                obj = class_name(*row)
                objects_list.append(obj.api())
    return objects_list
