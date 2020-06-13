import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, parameter_list):
        list.append(self, parameter_list)
        Loggable.log(self, parameter_list)

list_test = LoggableList()
list_test.append(3)