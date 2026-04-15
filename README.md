Project Overview
This project demonstrates a discrete-event simulation of Lamport’s Distributed Mutual
Exclusion Algorithm using SimPy and Streamlit.
The simulation models multiple distributed processes competing to access a shared Critical
Section (CS) while ensuring that only one process can access it at any time without using a
central coordinator.
The goal of the project is to understand how distributed systems maintain mutual exclusion
using message passing and logical clocks.
Technologies Used
• Python
• SimPy (Discrete Event Simulation)
• Streamlit (Interactive Visualization)
• GitHub (Version Control)
Lamport's Distributed Mutual Exclusion Algorithm
Lamport’s algorithm ensures mutual exclusion in distributed systems through logical clocks
and message passing.
Each process communicates with other processes using messages to coordinate access to the
Critical Section.
The algorithm works in three phases.
1. REQUEST Phase
When a process wants to enter the Critical Section:
1. The process increments its logical clock.
2. It sends a REQUEST message to all other processes.
3. The request is added to a request queue.
Example from simulation:
Time 1: Process 3 sends REQUEST
2. WAIT Phase
After sending the request, the process must wait until:
• It receives replies from all other processes.
• Its request has the highest priority in the queue.
Once these conditions are satisfied, the process enters the Critical Section.
Example:
Time 1: Process 3 ENTERS Critical Section
3. RELEASE Phase
After completing execution in the Critical Section:
1. The process exits the Critical Section.
2. It sends a RELEASE message to all other processes.
3. Other processes update their request queues.
Example:
Time 3: Process 3 EXITS Critical Section
Safety Property Verification
The most important property of mutual exclusion algorithms is safety.
Safety means:
No two processes are allowed to enter the Critical Section simultaneously.
From the simulation log:
Time 1: Process 3 ENTERS Critical Section
Time 3: Process 3 EXITS Critical Section
Time 3: Process 1 ENTERS Critical Section
We can see that a process enters the Critical Section only after the previous one exits,
ensuring mutual exclusion.
Lamport Clock Update Rule
Lamport introduced logical clocks to maintain ordering of events in distributed systems.
The update rule is:
Clock = max(local_clock, received_timestamp) + 1
Example:
Process P1 sends a request with timestamp 5.
Process P2 receives the message with local clock 3.
New clock value:
Clock = max(3,5) + 1 = 6
This ensures correct ordering of distributed events.
Message Complexity
For N processes, Lamport’s algorithm requires:
3(N−1) messages for each Critical Section request.
These messages include:
• REQUEST messages
• REPLY messages
• RELEASE messages
Example:
Number of Processes (N) Total Messages
3 6
5 12
10 27
Thus, message complexity grows linearly with the number of processes.
How to Run the Simulation
Install the required libraries:
pip install simpy streamlit
Run the application:
python3 -m streamlit run app.py
The browser will open automatically with the simulation interface.
Simulation Features
• Adjustable number of processes
• Visualization of request and critical section events
• Demonstration of mutual exclusion
• Event logs showing REQUEST, ENTER, and EXIT operations
Conclusion
This project successfully simulates Lamport’s Distributed Mutual Exclusion Algorithm
using discrete-event simulation.
The results demonstrate:
• Correct coordination between distributed processes
• Enforcement of mutual exclusion
• Proper ordering of events
The simulation helps understand how distributed systems manage shared resources without
centralized control.
