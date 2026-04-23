Classroom IT Support & Monitoring System

# Overview  
The Classroom IT Support & Monitoring System is a Python-based application designed to simulate real-world IT support operations within academic environments such as computer labs, HyFlex classrooms, and e-learning spaces.  
This system enables users to log, track, manage, and escalate classroom technology issues, closely reflecting the workflows used by institutional IT departments.

# Key Features  
- Log classroom IT issues (room, device, description, priority)  
- Track issue lifecycle (Open → In Progress → Resolved → Escalated)  
- Assign and manage priority levels (Low, Medium, High)  
- Escalate unresolved issues to simulate Technical Support workflows  
- Persistent storage using JSON (simulates ticketing systems)  
- Command-Line Interface (CLI) for easy interaction  
- Modular architecture (Models, Services, Utilities)

---

# Technologies Used  
- Python 3  
- JSON (for data persistence)  
- Tabulate (optional CLI formatting)

---

# Installation & Setup  

## 1. Clone the Repository  
```bash
git clone https://github.com/your-username/classroom_it_support.git
cd classroom_it_support
```

## 2. Create Virtual Environment
python -m venv venv

## 3. Activate Virtual Environment
# Windows
venv\Scripts\activate
# Mac/ Linux
source venv/bin/activate

## 4. Install Dependencies
pip install -r requirements.txt

## 5. Run
python main.py

---

# Sample Menu:-
--- Classroom IT Support System ---
1. Log Issue
2. View Issues
3. Update Issue Status
4. Escalate Issue
5. Exit

Log Issue: Input room number, device (projector, microphone, etc.), description, and priority.
View Issues: Displays all logged issues with current status
Update Status: Change issue state (e.g., In Progress, Resolved)
Escalate Issue: Mark the issue as escalated for higher-level support

---

# Future Enhancements:-
Web- based Interface
Ticket ID tracking system with timestamps
Real- time notifications

---

# Author
Ekjot Kaur
Honours Bachelor's of Technology (BSD) student
Seneca Polytechnic
