class Record(object):
    def __init__(self, line):
        timestamp, uf_time, serial, state = line[:-1].split(',')
        self.timestamp = int(timestamp)
        self.uf_time = uf_time
        self.serial = serial
        self.state = int(state)

input_file = open('question.in')
input_data = input_file.readlines()

serial_on_times = {}

for each_row in input_data:
    record_obj = Record(each_row)
    print(record_obj.__dict__)
    if record_obj.state:
        serial_on_times.setdefault(record_obj.serial, [0, None])
        if not serial_on_times[record_obj.serial][1]:
            serial_on_times[record_obj.serial][1] = record_obj.timestamp
    else:
        serial_info = serial_on_times.get(record_obj.serial)
        if serial_info:
            serial_on_times[record_obj.serial][0] += (
                record_obj.timestamp-serial_on_times[record_obj.serial][1])
            serial_on_times[record_obj.serial][1] = None
print(serial_on_times)
