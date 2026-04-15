import streamlit as st
import simpy
import random
st.title("Lamport Distributed Mutual Exclusion Simulation")
N = st.slider("Number of Processes", 2, 10, 3)
if st.button("Run Simulation"):
  env = simpy.Environment()
  logs = []
  cs_busy = [False] # using list so it can be modified inside function
  def process(env, pid):
    while True:
      yield env.timeout(random.randint(1,3))
      logs.append(f"Time {env.now}: Process {pid} sends REQUEST")
      while cs_busy[0]:
        yield env.timeout(1)
      cs_busy[0] = True
      logs.append(f"Time {env.now}: Process {pid} ENTERS Critical Section")
      yield env.timeout(2)
      logs.append(f"Time {env.now}: Process {pid} EXITS Critical
      Section")
      cs_busy[0] = False
  for i in range(N):
    env.process(process(env, i))
  env.run(until=10)
  st.subheader("Simulation Log")
  for log in logs:
      st.write(log)
  st.success("Simulation Completed")
