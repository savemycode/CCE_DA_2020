import threading

class TSThread(threading.Thread):

   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      msg = '$$RUN Time Series Analysis Thread : ' + self.name
      print(msg)