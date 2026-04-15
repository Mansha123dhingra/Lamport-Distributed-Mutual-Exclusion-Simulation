import simpy
import random

class Process: 
  def __init__(self, env, pid, processes):
    self.env = env
    self.pid = pid
    self.processes = processes
    self.clock = 0
    self.request_queue = []
    self.reply_count = 0
    self.message_count = 0
 def broadcast_request(self):
   self.clock += 1
   timestamp = self.clock
   self.request_queue.append((timestamp, self.pid))
   print(f"{self.env.now}: Process {self.pid} sends REQUEST ({timestamp})")
   for p in self.processes:
     if p.pid != self.pid:
       p.receive_request(timestamp, self.pid)
       self.message_count += 1
 def receive_request(self, timestamp, pid):
   self.clock = max(self.clock, timestamp) + 1
   self.request_queue.append((timestamp, pid))
    self.send_reply(pid)
 def send_reply(self, pid):
   for p in self.processes:
     if p.pid == pid:
       p.receive_reply()
       self.message_count += 1
 def receive_reply(self):
     self.reply_count += 1
 def broadcast_release(self):
     print(f"{self.env.now}: Process {self.pid} sends RELEASE")
     self.request_queue = [
       req for req in self.request_queue if req[1] != self.pid]
     for p in self.processes:
       if p.pid != self.pid:
           p.receive_release(self.pid)
           self.message_count += 1
 def receive_release(self, pid):
     self.request_queue = [
       req for req in self.request_queue if req[1] != pid]
 def run(self):
     while True:
       yield self.env.timeout(random.randint(1,5))
       self.broadcast_request()
       yield self.env.timeout(1)
       if self.reply_count == len(self.processes) - 1:
          print(f"{self.env.now}: Process {self.pid} ENTERS Critical   Section")
          yield self.env.timeout(2)
          print(f"{self.env.now}: Process {self.pid} EXITS Critical Section")
         self.broadcast_release()
         self.reply_count = 0

   
