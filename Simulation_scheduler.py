#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import time
from collections import deque

# Define process states
RUNNING = "RUNNING"
READY = "READY"
BLOCKED = "BLOCKED"
TERMINATED = "TERMINATED"

# Define priority levels and time slices
PRIORITY_LEVELS = 4
TIME_SLICES = [1, 2, 4, 8]  # Quantum size for each priority level

class SimulatedProcess:
    def __init__(self, pid, ppid, program, priority=0):
        self.pid = pid
        self.ppid = ppid
        self.program = program
        self.priority = priority
        self.state = READY
        self.value = 0
        self.start_time = 0
        self.cpu_time_used = 0
        self.program_counter = 0

class ProcessManager:
    def __init__(self):
        self.time = 0
        self.cpu = None
        self.pcb_table = {}
        self.ready_state = [[] for _ in range(PRIORITY_LEVELS)]
        self.blocked_state = deque()
        self.running_state = None

    def create_process(self, ppid, program, priority=0):
        pid = len(self.pcb_table)
        process = SimulatedProcess(pid, ppid, program, priority)
        self.pcb_table[pid] = process
        self.ready_state[priority].append(pid)

    def execute_next_instruction(self):
        if self.running_state is not None:
            process = self.pcb_table[self.running_state]
            instruction = process.program[process.program_counter]
            opcode, *args = instruction.split()
            if opcode == "S":
                process.value = int(args[0])
            elif opcode == "A":
                process.value += int(args[0])
            elif opcode == "D":
                process.value -= int(args[0])
            elif opcode == "B":
                self.block_process(process.pid)
            elif opcode == "E":
                self.terminate_process(process.pid)
            elif opcode == "F":
                self.create_process(process.pid, process.program[process.program_counter + 1])
            elif opcode == "R":
                # Replace program with contents of file
                filename = args[0]
                with open(filename, 'r') as file:
                    new_program = file.readlines()
                process.program = new_program
                process.program_counter = 0
            process.program_counter += 1

    def block_process(self, pid):
        process = self.pcb_table[pid]
        process.state = BLOCKED
        self.blocked_state.append(pid)
        self.schedule()

    def terminate_process(self, pid):
        process = self.pcb_table[pid]
        process.state = TERMINATED
        del self.pcb_table[pid]
        self.schedule()

    def schedule(self):
        # Perform scheduling and context switching
        # Algorithm based on priority levels and time slices
        if self.running_state is not None:
            running_process = self.pcb_table[self.running_state]
            priority = running_process.priority
            time_slice = TIME_SLICES[priority]
            running_process.cpu_time_used += 1
            if running_process.cpu_time_used >= time_slice:
                # Preempt process if it has used up its time slice
                self.ready_state[priority].append(self.running_state)
                self.running_state = None

        for priority in range(PRIORITY_LEVELS):
            if self.ready_state[priority]:
                self.running_state = self.ready_state[priority].pop(0)
                self.pcb_table[self.running_state].state = RUNNING
                break

    def process_command(self, command):
        if command == "Q":
            self.execute_next_instruction()
            self.time += 1
            self.schedule()
        elif command == "U":
            if self.blocked_state:
                pid = self.blocked_state.popleft()
                process = self.pcb_table[pid]
                process.state = READY
                self.ready_state[process.priority].append(pid)
                self.schedule()
        elif command == "P":
            self.print_system_state()
        elif command == "T":
            self.print_system_state()
            sys.exit(0)

    def print_system_state(self):
        print("****************************************************************")
        print("The current system state is as follows:")
        print("****************************************************************")
        print("CURRENT TIME:", self.time)
        if self.running_state is not None:
            print("RUNNING PROCESS:")
            self.print_process_info(self.running_state)
        if self.blocked_state:
            print("BLOCKED PROCESSES:")
            for pid in self.blocked_state:
                self.print_process_info(pid)
        print("PROCESSES READY TO EXECUTE:")
        for priority, queue in enumerate(self.ready_state):
            print("Queue of processes with priority", priority, ":")
            for pid in queue:
                self.print_process_info(pid)
        print("****************************************************************")

    def print_process_info(self, pid):
        process = self.pcb_table[pid]
        print(pid, process.ppid, process.priority, process.value, process.start_time, process.cpu_time_used)


if __name__ == "__main__":
    # Main simulation logic
    process_manager = ProcessManager()
    process_manager.create_process(0, ["S 1000", "A 19", "A 20", "D 53", "A 55", "F 1", "R file_a", "F 1", "R file_b", "F 1", "R file_c", "F 1", "R file_d", "F 1", "R file_e", "E"])

    while True:
        command = input("Enter command (Q/U/P/T): ").strip()
        if command not in ["Q", "U", "P", "T"]:
            print("Invalid command. Please enter Q, U, P, or T.")
            continue
        process_manager.process_command(command)


# In[ ]:




