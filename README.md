# Python-based-Process-Scheduler-simulation
🖥️ Simulates a Priority-Based Round-Robin Operating System Scheduler in Python | Supports process creation, blocking, forking, termination, and file-based program replacement with interactive command execution (Q, U, P, T). Ideal for OS education and systems programming demos.


Here's a professional and clear `README.md` for your **Operating System Process Scheduler Simulation** project:

---

````markdown
# 🖥️ Operating System Process Scheduler Simulation

This project is a Python-based simulation of an **Operating System Process Scheduler** designed to mimic core concepts of process management in a multitasking OS. It demonstrates process creation, scheduling, blocking, termination, and context switching using priority-based round-robin scheduling.

---

## 📂 Features

- ✅ Simulated Process Control Blocks (PCBs)
- ✅ Priority-based round-robin scheduling (4 levels)
- ✅ Time slicing based on priority:
  - Level 0: 1 unit
  - Level 1: 2 units
  - Level 2: 4 units
  - Level 3: 8 units
- ✅ Process instructions: `S` (Set), `A` (Add), `D` (Subtract), `B` (Block), `E` (Exit), `F` (Fork), `R` (Replace program)
- ✅ State transitions: READY, RUNNING, BLOCKED, TERMINATED
- ✅ Interactive CLI for issuing OS-level commands

---

## 🚀 How It Works

Each process is defined by a list of instructions. The `ProcessManager` handles process execution, scheduling, and transitions based on commands:

### 🛠 Supported Commands:
| Command | Action                                |
|---------|----------------------------------------|
| `Q`     | Execute the next instruction (quantum) |
| `U`     | Unblock a process                      |
| `P`     | Print current system state             |
| `T`     | Terminate simulation                   |

---

## ▶️ Example

### Sample Process:
```python
["S 1000", "A 19", "A 20", "D 53", "A 55", "F 1", "R file_a", "E"]
````

### Sample Run:

```bash
Enter command (Q/U/P/T): Q
Enter command (Q/U/P/T): P
...
```

---

## 📁 File Structure

```
Final_version_OS_project.py       # Main simulation script
file_a, file_b, file_c...         # Optional: Sample instruction files (used in R command)
```

---

## 💡 Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/os-process-scheduler.git
   cd os-process-scheduler
   ```

2. Run the simulation:

   ```bash
   python Final_version_OS_project.py
   ```

3. Enter commands interactively (`Q`, `U`, `P`, `T`).

---

## 📌 Requirements

* Python 3.6+
* No external dependencies

---

## 📚 Educational Value

This project is ideal for:

* Operating Systems coursework
* Understanding process states and scheduling
* Learning how real OS schedulers work behind the scenes

---

## 👨‍💻 Author

Md Julfiker Ali Jewel
Graduate Researcher & Software Programmer
West Virginia Department of Health and Human Resources
[Portfolio](https://mdjulfikeralijewel.com) | [Email](mailto:jewelsheikh2013@gmail.com)

---

## 📜 License

This project is open-source and free to use for educational or research purposes.

```

---

Would you like me to generate this as a downloadable `README.md` file now?
```

