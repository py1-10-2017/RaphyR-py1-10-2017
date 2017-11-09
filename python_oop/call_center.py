from datetime import datetime

class Call(object):
    def __init__(self, uniqueid, caller_name, caller_phonenumber, time, call_reason):
        self.uniqueid = uniqueid
        self.caller_name = caller_name
        self.caller_phonenumber = caller_phonenumber
        self.time_of_call = time
        self.call_reason = call_reason
    def display(self):
        print self.uniqueid
        print self.caller_name
        print self.caller_phonenumber
        print self.time_of_call
        print self.call_reason


class CallCenter(Call):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
    def remove(self, call):
        self.calls.pop[0]
        self.queue_size -= 1
        return self
    def info(self):
        for i in self.calls:
            print i.caller_name + " " + str(i.caller_phonenumber)
        return self

harry = Call(1, 'Harry', '7863551188', datetime.now(), 'return')
jess = Call(2, 'Jessica', '1234567890', datetime.now(), 'order')

today = CallCenter()
today.add(harry).add(jess).info()
