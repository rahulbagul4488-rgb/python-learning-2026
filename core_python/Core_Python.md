
# Python

## 1️⃣ What is Python?

🔹 Python is a high-level, interpreted, general-purpose programming language.

🔹 Python ही अशी programming language आहे ज्यात आपण computer ला instructions देतो आणि computer ते काम करतो.

Example:

```python

print("Hello, World!")

```

👉 Computer ला सांगितलं:

🔹 “Hello, World” print कर.


**🔍 Python चे मुख्य features (meaningful):**

**High-level:**

👉 Human-friendly (English सारखी syntax).

**Interpreted:**

👉 Code line-by-line execute होतो (compile step नाही).

**General-purpose:**

👉 Web, AI, ML, automation, data, scripting — सगळ्यासाठी वापरता येते.



## 2️⃣ Why Python?

**Python is preferred because of its simple syntax, rapid development capability, extensive libraries, and strong support for AI, data science, and automation.**


🔹 1️⃣ Easy to Learn & Read

```python

x = 10

```

C / Java पेक्षा:

🔹 syntax simple.

🔹 कमीत कमी boilerplate.

👉 Beginners + professionals दोघांसाठी योग्य.


🔹 2️⃣ Fast Development (MOST IMPORTANT)

🔹 कमी code

🔹 जास्त काम

👉 Time-to-market कमी.
👉 Startups + AI projects साठी best.



🔹 3️⃣ Huge Standard Library

 Python मध्ये आधीपासूनच खूप काही मिळतं:

🔹 file handling

🔹 math

🔹 date/time

🔹 OS work

👉 पुन्हा पुन्हा code लिहायची गरज नाही.


🔹 4️⃣ Massive Ecosystem (AI reason 🔥)

Python AI/ML मध्ये #1 आहे कारण:

🔹 NumPy

🔹 Pandas

🔹 TensorFlow

🔹 PyTorch

🔹 Scikit-learn

👉 Almost सगळे AI tools Python-first आहेत.


🔹 5️⃣ Cross-platform

🔹 Windows

🔹 Linux

🔹 macOS

👉 Same code, everywhere.


🔹 6️⃣ Strong Community

🔹 Millions of developers.

🔹 Answers सहज मिळतात.

🔹 Continuous improvement.

# Scripting

**What is Scripting?**

🔹 Scripting is a programming approach used to automate tasks and build applications

🔹 using interpreted languages with minimal code and fast execution.

🔹 Scripting = कमी code मध्ये, पटकन काम करणारा program.

👉 पण लक्षात ठेव:

**Python = programming language.**

**Scripting = Python चा use-case.**


**Key Features:**

- Interpreted (no manual compilation)
- Dynamically typed
- Less code
- Fast development

**Q) Why Scripting?**

- Rapid application development
- Automation
- Web, Cloud, AI, DevOps usage
- High industry demand

**Types of Scripting:**

1) Client-Side Scripting

   - Runs in the browser
   - JavaScript (main)

2) Server-Side Scripting

   - Runs on the server.
   - Python, PHP, Java, ASP.NET


# Source Code

Q) Source Code म्हणजे काय?

तू Python मध्ये जे लिहितोस ते म्हणजे Source Code!

🔹 Source Code = आपण लिहिलेला Python Code
🔹 हे .py extension च्या file मध्ये साठवलं जातं
🔹 उदा: hello.py, calculator.py

एक साधं उदाहरण 👇

'''python

name= "Rahul"
data= [12]

'''

Real Life उदाहरण 🏠

Source Code म्हणजे घराचा नकाशा आहे!

👷 Engineer → नकाशा बनवतो   (तू Code लिहितोस)
🏠 घर       → नकाशावरून बनतं (Computer Code Execute करतो)

नकाशा = Source Code
घर    = Output

📌 Source Code चे मुख्य Points

🔹 1️⃣ Human Readable असतो
       → माणसाला वाचता येतो

🔹 2️⃣ .py file मध्ये असतो
       → hello.py

🔹 3️⃣ Computer directly वाचू शकत नाही
       → म्हणून Interpreter लागतो

🔹 4️⃣ तूच लिहितोस
       → Variables, Functions, Logic


🔹 One Liner:
   "Programmer ने लिहिलेला Code 
    म्हणजे Source Code!"

📌 Source Code नंतर काय होतं?

Source Code (.py)
      ↓
Interpreter वाचतो
      ↓
Byte Code बनतो (.pyc)
      ↓
PVM Execute करतो
      ↓
Output Screen वर!

# Interpreter 

Q) Interpreter म्हणजे काय? 

Interpreter म्हणजे एक Translator आहे जो तुझा Code Line by Line वाचतो आणि Computer ला समजेल अशा भाषेत Convert करतो!

Real Life उदाहरण 🌍

समजा तू Marathi बोलतोस
पण समोरचा माणूस फक्त English समजतो

मग एक Translator लागतो जो:
🔹 तुझं Marathi ऐकतो
🔹 English मध्ये सांगतो

Translator = Interpreter
तुझं Marathi = Source Code
समोरचा माणूस = Computer

Interpreter काय करतो? 👇

Source Code
name = "Rahul"     ← Line 1 वाचली → Convert केली → Run केली
print("Hello")     ← Line 2 वाचली → Convert केली → Run केली
age = 20           ← Line 3 वाचली → Convert केली → Run केली

→ एक एक Line असं करत जातो!

📌 Interpreter चे मुख्य Points

🔹 1️⃣ Line by Line काम करतो
       → एक Line वाचतो
       → Convert करतो
       → Run करतो
       → मग पुढची Line

🔹 2️⃣ Error लगेच सांगतो
       → चुकीची Line आली
       → तिथेच थांबतो
       → Error दाखवतो

🔹 3️⃣ Byte Code बनवतो
       → Source Code → Byte Code
       → .py → .pyc

🔹 4️⃣ Python मध्ये असतो
       → Java मध्ये Compiler असतो
       → Python मध्ये Interpreter असतो

📌 Error आली तर काय होतं?

name = "Rahul"      # ✅ Line 1 → OK → Run
print("Hello")      # ✅ Line 2 → OK → Run
prnt("World")       # ❌ Line 3 → Error! → थांबलो!
age = 20            # ⏸️ Line 4 → Run होणारच नाही!

→ Interpreter Line 3 वर थांबला
→ Line 4 कधीच Run होणार नाही
→ Error Fix केल्याशिवाय पुढे जाणार नाही!

→ हेच Interpreter चं वैशिष्ट्य आहे! 🔥


# Byte Code

Byte Code म्हणजे Source Code आणि Machine Code मधला एक Middle Step आहे!

Real Life उदाहरण 🌍

समजा तू Marathi मध्ये बोलतोस
पण समोरचा माणूस फक्त Chinese समजतो

Direct Marathi → Chinese कठीण आहे!
मग आधी Marathi → Hindi (Middle Step)
मग Hindi → Chinese

Marathi = Source Code
Hindi   = Byte Code   ← हा Middle Step!
Chinese = Machine Code

Byte Code काय असतो? 👇

Source Code (तू लिहिलेला)
name = "Rahul"
print("Hello")
      ↓
Interpreter Convert करतो
      ↓
Byte Code (Middle Language)
\x47\x65\x74\x49\x74\x65...
      ↓
PVM Execute करतो
      ↓
Output!

📌 Byte Code चे मुख्य Points

🔹 1️⃣ Middle Step आहे
       → Source Code नाही
       → Machine Code पण नाही
       → दोघांच्या मध्ये आहे!

🔹 2️⃣ .pyc file मध्ये साठवतो
       → hello.py  → Source Code
       → hello.pyc → Byte Code

🔹 3️⃣ PVM ला समजतो
       → Byte Code फक्त PVM वाचतो
       → माणसाला वाचता येत नाही

🔹 4️⃣ Cross Platform आहे
       → Windows चा Byte Code
       → Mac वर पण चालतो! ✅

📌 Byte Code कुठे साठवतो?

तुझ्या Project Folder मध्ये:

📁 MyProject
   ├── hello.py        ← Source Code (तू लिहिलेला)
   └── __pycache__
         └── hello.pyc ← Byte Code (Interpreter बनवतो)

→ Python आपोआप .pyc file बनवतो!
→ तुला manually करायची गरज नाही!

📌 Byte Code चा फायदा काय?

🔹 फायदा 1️⃣ → Speed!
   
   पहिल्यांदा Run केलं:
   Source Code → Byte Code → PVM → Output
   
   दुसऱ्यांदा Run केलं:
   Byte Code → PVM → Output  ← जलद! 🚀
   (Source Code परत Convert करायची गरज नाही!)

🔹 फायदा 2️⃣ → Cross Platform!

   Windows वर Byte Code बनवला
         ↓
   Mac वर पण चालतो!
   Linux वर पण चालतो!


   📌 Source Code vs Byte Code vs Machine Code

┌─────────────────────────────────────────┐
│ Source Code  → name = "Rahul"           │
│               माणसाला समजतं ✅          │
│               Computer ला समजत नाही ❌  │
├─────────────────────────────────────────┤
│ Byte Code    → \x47\x65\x74...          │
│               माणसाला समजत नाही ❌      │
│               PVM ला समजतं ✅           │
├─────────────────────────────────────────┤
│ Machine Code → 01001000 01100101...     │
│               फक्त Processor समजतो ✅   │
└─────────────────────────────────────────┘


# PVM (Python Virtual Machine)

Q) PVM (Python Virtual Machine) म्हणजे काय?

PVM म्हणजे एक Virtual Engine आहे जो Byte Code वाचतो आणि Execute करतो!

Real Life उदाहरण 🌍

समजा तुझ्याकडे एक Recipe आहे
पण ती Recipe Special Language मध्ये आहे

ती Recipe वाचायला आणि 
जेवण बनवायला एक Special Chef लागतो

Special Chef = PVM
Recipe       = Byte Code
जेवण         = Output

PVM काय करतो? 👇

Byte Code (.pyc)
\x47\x65\x74\x49...
      ↓
PVM वाचतो
      ↓
Line by Line Execute करतो
      ↓
Output Screen वर!
"Hello Rahul"

📌 PVM चे मुख्य Points

🔹 1️⃣ Byte Code Execute करतो
       → Byte Code Input घेतो
       → Output देतो

🔹 2️⃣ Virtual आहे म्हणजे काय?
       → Real Machine नाही
       → Software मध्ये बनवलेलं
       → Engine आहे फक्त!

🔹 3️⃣ Platform नुसार काम करतो
       → Windows वर → Windows PVM
       → Mac वर     → Mac PVM
       → Linux वर   → Linux PVM

🔹 4️⃣ Python Install केलं की
       PVM आपोआप येतो!
       → वेगळं Install करायची 
         गरज नाही!


📌 PVM Virtual का आहे?

Real Machine (Computer):
🔹 Hardware आहे
🔹 Touch करता येतं
🔹 Machine Code समजतो

Virtual Machine (PVM):
🔹 Software आहे
🔹 Touch करता येत नाही
🔹 Byte Code समजतो

→ PVM एक Software Engine आहे
  जो Byte Code Execute करतो!

📌 PVM Cross Platform कसा?

Without PVM:
Windows Code → फक्त Windows वर चालेल ❌
Mac Code     → फक्त Mac वर चालेल ❌

With PVM:
Code एकदा लिही
      ↓
Byte Code बनतो
      ↓
Windows PVM → Windows वर चालतो ✅
Mac PVM     → Mac वर चालतो ✅
Linux PVM   → Linux वर चालतो ✅

→ "Write Once, Run Anywhere!" 🔥

📌 PVM चा Process कसा असतो?

Step 1 → Byte Code घेतो
         \x47\x65\x74...

Step 2 → एक एक Instruction वाचतो
         Instruction 1 → Execute
         Instruction 2 → Execute
         Instruction 3 → Execute

Step 3 → Output देतो
         Screen वर दाखवतो


आता पूर्ण Process एकत्र बघ 👇

Source Code (.py)
name = "Rahul"
print("Hello")
      ↓
Interpreter
Line by Line वाचतो
      ↓
Byte Code (.pyc)
\x47\x65\x74...
      ↓
PVM
Execute करतो
      ↓
Output
"Hello Rahul" 🎉


# Compiler vs Interpreter vs PVM

अगदी Simple भाषेत 👇

Compiler    = एकत्र सगळं काम करणारा
Interpreter = एक एक करून काम करणारा
PVM         = Execute करणारा Engine

Real Life उदाहरण 🌍

समजा तुला एक Marathi Book 
English मध्ये Convert करायची आहे

Compiler:
🔹 पूर्ण Book आधी वाचतो
🔹 मग एकत्र Convert करतो
🔹 शेवटी English Book देतो

Interpreter:
🔹 एक Page वाचतो
🔹 लगेच Convert करतो
🔹 लगेच देतो
🔹 मग पुढचा Page

PVM:
🔹 Convert झालेलं वाचतो
🔹 Execute करतो
🔹 Output देतो

📌 Compiler म्हणजे काय?

🔹 पूर्ण Code एकत्र वाचतो
🔹 एकत्र Convert करतो
🔹 मग Execute करतो
🔹 Java, C, C++ मध्ये असतो

Process:
Source Code
(पूर्ण Code)
      ↓
Compiler
(सगळं एकत्र वाचतो)
      ↓
Machine Code
      ↓
Execute
      ↓
Output

Error कधी कळतो?
❌ सगळ्यात शेवटी कळतो!


📌 तिघांमधला मुख्य फरक

┌─────────────────────────────────────────────────────┐
│              Compiler                               │
│  ✅ पूर्ण Code एकत्र Convert करतो                  │
│  ✅ जलद Execute होतो                               │
│  ❌ Error शेवटी कळतो                               │
│  ❌ Platform specific असतो                          │
│  📌 Use: Java, C, C++                               │
├─────────────────────────────────────────────────────┤
│              Interpreter                            │
│  ✅ Line by Line Convert करतो                      │
│  ✅ Error लगेच कळतो                                │
│  ✅ Beginners साठी सोपं                              │
│  ❌ थोडा हळू असतो                                   │
│  📌 Use: Python                                     │
├─────────────────────────────────────────────────────┤
│              PVM                                    │
│  ✅ Byte Code Execute करतो                         │
│  ✅ Cross Platform आहे                             │
│  ✅ Python Install केलं की येतो                       │
│  📌 Use: फक्त Python मध्ये                            │
└─────────────────────────────────────────────────────┘

📌 तिघांचं काम वेगळं आहे!

Compiler    → Convert करतो (Java, C)
Interpreter → Convert करतो (Python)
PVM         → Execute करतो (Python)

→ Compiler आणि Interpreter एकच काम करतात
  पण वेगळ्या पद्धतीने!

→ PVM चं काम वेगळंच आहे —
  तो फक्त Execute करतो!

📌 Error कधी कळतो?

# Code उदाहरण
name = "Rahul"      # Line 1
print("Hello")      # Line 2
prnt("World")       # Line 3 → Error!
age = 20            # Line 4

Compiler असता तर:
→ Line 1, 2, 3, 4 सगळं वाचलं
→ शेवटी Error सांगितला ❌
→ वेळ जास्त लागला

Interpreter (Python):
→ Line 1 → OK ✅
→ Line 2 → OK ✅
→ Line 3 → Error! लगेच थांबलो ✅
→ Line 4 → Run झालाच नाही ⏸️

→ Python मध्ये Error लगेच कळतो — हाच मोठा फायदा! 🔥

📌 Python मध्ये दोन्ही असतात!

Python मध्ये:

Interpreter ✅  +  PVM ✅
     ↓                ↓
Byte Code         Execute
बनवतो             करतो

→ Compiler नाही Python मध्ये!
→ Interpreter + PVM मिळून
  Python चालवतात!

📌 Real World मध्ये कुठे काय?

Language    | काय वापरतं
────────────|─────────────────
Python      | Interpreter + PVM
Java        | Compiler + JVM
C           | Compiler
C++         | Compiler
JavaScript  | Interpreter
Ruby        | Interpreter


# Phase 1: Naming & Basics

## Identifier

**Q) 🧠 Identifier म्हणजे काय?**

🔹 Identifier = program मधल्या गोष्टींचं नाव.

Python मध्ये तू ज्या गोष्टींना नाव देतोस, ते नाव म्हणजे Identifier.

उदा:
```python

a = 10
name = "Rahul"
total_sum = 50

``` 

👉 इथे:

🔹 a → identifier

🔹 name → identifier

🔹 total_sum → identifier


## Q) Python मध्ये Identifier कुठे वापरतो?

Identifiers वापरले जातात:

🔹 Variables

🔹 Functions

🔹 Classes

🔹 Modules

Examples:

```python

age = 25          # variable identifier
def add():        # function identifier
class Student:   # class identifier

```


## 📏 Identifier साठी Python चे RULES (खूप important):


✅ **Rule 1: Letter किंवा _ ने सुरू व्हायला पाहिजे.**

✔️ **valid:**

🔹 name

🔹 _age

🔹 total1


**❌ invalid:**

🔹 1name   # number ने सुरू.

🔹 @age    # special character.


✅ **Rule 2: Letters, numbers, underscore चालतात.**

✔️ **valid:**

🔹 student_name

🔹 marks2025

**❌ invalid:**

🔹 student-name   # dash (-) allowed नाही.


✅ **Rule 3: Python keywords वापरू शकत नाही.**

**❌ invalid:**

🔹 if = 10

🔹 class = "A"

✔️ **valid:**


🔹 if_value = 10

🔹 class_name = "A"


✅ **Rule 4: Case-sensitive असतात.**

🔹 age = 10

🔹 Age = 20

👉 age आणि Age वेगवेगळे identifiers आहेत.


✅ **Rule 5: Space allowed नाही.**

**❌ invalid:**

🔹 total marks = 50

✔️ **valid:**

🔹 total_marks = 50


## 🧠 Naming Convention (Good Practice – real world)

## 🔹 Variables

```python

student_name
total_marks

```

## 🔹 Constants (by convention)

```python

PI = 3.14
MAX_LIMIT = 100

```
## 🔹 Functions

```python

def calculate_total():

```
## 🔹 Classes


```python

class StudentDetails:

```


**“An identifier is the name used to identify variables, functions, classes, or other objects in a program.”**


## Constant

**🧠 Constant in Python म्हणजे काय?**

🔹 Constant = अशी value जी program चालू असताना बदलायची नसते.

उदा:

🔹 PI ची value बदलत नाही.

🔹 Maximum limit fix असते.

🔹 Configuration values fix असतात.


**❗ Python मधली खरी गोष्ट (IMPORTANT TRUTH)**

🔴 Python मध्ये real “constant” असा keyword नाही.

म्हणजे:

🔹 Python मध्ये const नाही.

🔹 Python enforce करत नाही की value बदलू नये.

**🟢 मग Python मध्ये Constant कसा बनवतो?**

👉 Convention (नियम) वापरून.

Rule:

🔹 Constant variables UPPERCASE नावाने लिहायचे.


🔍 Example (standard practice)

```python

PI = 3.14
MAX_USERS = 100
TAX_RATE = 0.18

```
👉 हे technically variables आहेत.
👉 पण नावामुळे सगळ्यांना कळतं:

**“हे बदलू नये”**

**🧠 Real-world use cases**

## 1️⃣ Mathematical constants

```python

PI = 3.14159

```
## 2️⃣ Configuration values

```python

DB_HOST = "localhost"
DB_PORT = 5432

```
## 3️⃣ Limits

```python

MAX_RETRIES = 3

```

**Python does not have true constants; instead, it uses naming conventions to indicate values that should not be changed.**


## Variables


**🧠 Variable म्हणजे काय? (Simple definition).**

🔹 Variable = नाव दिलेली गोष्ट जी value store करते.

म्हणजे:

🔹 Value memory मध्ये ठेवली जाते.

🔹 त्या value ला नाव (identifier) दिलं जातं.

🔹 ते नाव वापरून आपण value वापरतो / बदलतो.


## 🔍 Basic example:

```python

age = 25

```

इथे:

🔹 age → variable name (identifier).

🔹 = → assignment operator.

🔹 25 → value.

👉 याचा अर्थ:

🔹 “25 ही value age नावाने memory मध्ये ठेव”.


## 🎯 Interview-ready answer

**“A variable in Python is a name that refers to an object stored in memory.”**


**✅ Summary (one page view):**

🔹 Variable = name + value.

🔹 Python = dynamically typed.

🔹 Variable points to object.

🔹 Value बदलली की variable नवीन object कडे point करतो.


## 📏 Python Variable Writing Rules:

**✅ Rule 1: Variable नाव letter किंवा _ ने सुरू व्हायला पाहिजे.**

✔️ Valid:

```python

age = 25
_name = "Rahul"


```

❌ Invalid:

```python

1age = 25
@name = "Rahul"

```

**✅ Rule 2: Letters, numbers आणि underscore (_) allowed.**

✔️ Valid:

```python

student_name = "Rahul"
marks2026 = 90

```

❌ Invalid:


```python

student-name = "Rahul"   # dash allowed नाही

```

**✅ Rule 3: Python keywords वापरू शकत नाही.**

❌ Invalid:

```python

if = 10
class = "A"

```

✔️ Valid:

```python

if_value = 10
class_name = "A"

```

**✅ Rule 4: Variable names case-sensitive असतात.**

```python

age = 10
Age = 20

```

👉 age आणि Age वेगवेगळे variables आहेत.


**✅ Rule 5: Variable नावात space allowed नाही.**

❌ Invalid:

```python

total marks = 50

```

✔️ Valid:

```python

total_marks = 50

```


**✅ Rule 6: Meaningful नाव ठेवा (BEST PRACTICE).**

❌ Poor:

```python

x = 90
a = "Rahul"

```

✔️ Good:

```python

total_marks = 90
student_name = "Rahul"

```

**✅ Rule 7: Constants साठी UPPERCASE वापरा (by convention):**

```python

PI = 3.14
MAX_LIMIT = 100

```

⚠️ Python enforce करत नाही, पण humans साठी signal आहे.


**❌ Common beginner mistakes (avoid कर):**

```python

print = 10       # built-in overwrite (bad)
sum = 5          # built-in overwrite (bad)

```

✔️ Better:

```python

total_sum = 5

```

## 🧠 Quick Cheat Sheet

| Rule                | Example          |
| ------------------- | ---------------- |
| Start with letter/_ | `name`, `_count` |
| No keyword          | `if_value`       |
| Case-sensitive      | `age ≠ Age`      |
| No space            | `total_marks`    |
| Meaningful name     | `student_score`  |
| Constant            | `MAX_SIZE`       |



## 🎯 Interview-ready one-liner:

**“A variable name in Python must start with a letter or underscore, can contain letters, digits, underscores, cannot be a keyword, and is case-sensitive.”**



**❓ तुझा प्रश्न (simple शब्दात)**

तू म्हणतोयस:

a = 10
तेव्हा 10 ला memory address मिळतो,
a ला नाही
a फक्त tag / label असतो

❓ Python असं का करतो?

❓ याचे फायदे काय?

❓ तोटे काय?

उत्तर: हो, तू अगदी बरोबर समजला आहेस.

आता का ते बघू.


**🧠 Python मध्ये a = 10 झाल्यावर काय होतं?**

Step-by-step internally:

```python

a = 10

```

Python काय करतो:

1️⃣ Memory मध्ये 10 नावाचा object तयार करतो.

2️⃣ त्या object ला address देतो (उदा: 0x100).

3️⃣ a नावाचा label/reference तयार करतो.

4️⃣ a → त्या 10 object कडे point करतो.

```python

Memory:
0x100  ──>  10

Variable:
a  ────────┘

```

👉 Address object ला असतो, variable ला नाही.

👉 Variable = reference / label.


## ❓ Python असं design का केलं?

**कारण 1️⃣: Memory efficiency (खूप मोठा फायदा)**

```python
a = 10
b = 10

```

**Python असं करत नाही:**

```python

a → 10 (new)
b → 10 (new)

```

**Python असं करतो:**

```python

      ┌── a
10 ───┤
      └── b

```

👉 एकच 10 object
👉 दोन variables त्याच object कडे point करतात

✔️ Memory वाचते
✔️ Performance सुधारते


**❓ जर variable ला address दिला असता तर?**

मग असं झालं असतं:

🔹 प्रत्येक variable = वेगळं memory block.

🔹 Value copy करावी लागली असती.

🔹 Memory जास्त वापरली गेली असती.

👉 Python high-level, efficient भाषा आहे.

🔹 म्हणून हा model निवडला.


**🧠 कारण 2️⃣: Dynamic typing possible होतं.**

```python

a = 10
a = "Rahul"

```

**Python मध्ये हे valid आहे कारण:**

🔹 a fix memory नाही.

🔹 a फक्त label आहे.

🔹 तो कुठल्याही object कडे point करू शकतो.

👉 जर a ला fixed address असता तर:

🔹 type बदलता आला नसता.

🔹 Python C सारखी झाली असती.


**🧠 कारण 3️⃣: Object sharing & immutability.**

Python मध्ये:

🔹 int, str, tuple → immutable.

```python

x = 10
y = x
x = 20

```

Internally:

```python

10 ← y
20 ← x

```

👉 y बदलत नाही
👉 x फक्त नवीन object कडे point करतो

✔️ Bugs कमी
✔️ Predictable behavior


## 🎯 याचे फायदे (BENEFITS)

**✅ 1️⃣ Memory efficient**

🔹 Same value reuse.

🔹 Less duplication.

**✅ 2️⃣ Flexible typing**

🔹 Variable कोणत्याही type कडे point करू शकतो.

**✅ 3️⃣ Safe behavior (immutables)**

🔹 Accidental changes टळतात.

**✅ 4️⃣ Simple language for humans**

🔹 Programmer ला memory manage करावी लागत नाही.


## ⚠️ याचे तोटे (TRADE-OFFS):

**❌ 1️⃣ Beginners ला confusion.**

“Variable box आहे” असा गैरसमज

**❌ 2️⃣ Mutable objects मध्ये surprise.**

```python

a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]

```
👉 कारण:

🔹 a आणि b एकाच list कडे point करतात.


**🧠 Real-life analogy (best one):**

📦 Object = घर
🏷️ Variable = घराचं नावपट्ट

🔹 नावपट्ट बदलली.
🔹 घर तेच राहू शकतं.
🔹 किंवा नवीन घराला नावपट्ट लागू शकते.


## 🎯 Interview-ready one-liner

**“In Python, variables are references to objects; memory is allocated to objects, not variables.”**


## ✅ Final summary (crystal clear)

✔️ Address object ला असतो.

✔️ Variable फक्त reference आहे.

✔️ Python ने efficiency + flexibility साठी हे design केलं.

⚠️ Mutable objects मध्ये careful राहावं लागतं.



# Data Types:


**🧠 Data Type म्हणजे काय? (ZERO LEVEL):**

🔹 Data Type = value कशा प्रकारची आहे ते सांगणारा प्रकार.

Simple words मध्ये:

🔹 Python ला समजायला हवं:

🔹 हा नंबर आहे का?

🔹 हा text आहे का?

🔹 हा collection आहे का?

🔹 हा True/False आहे का?


👉 Data type Python ला सांगतो:

🔹 किती memory घ्यायची.

🔹 value वर काय operations करता येतील.

🔹 Value कशी behave करेल.


**Example:**

```python

x = 10

```

🔹 value = 10

🔹 data type = int (integer)


```python

name = "Rahul"

```

🔹 value = "Rahul"

🔹 data type = str (string)





## There are two main types of data types in Python:

**1) Built-in Data Types**

**2) User-Defined Data Types**


## Python Built-in Data Types (Clean Hierarchy)

**I. NUMERIC Data  TYPES:**

   - int

   - float

   - complex

**II. SEQUENCE Data TYPES:**

   A. Immutable Sequences

      - str

      - tuple

      - range

      - bytes
   
   B. Mutable Sequences

      - list

      - bytearray

**III. SET Data TYPES:**

   - set (Mutable)

   - frozenset (Immutable)

**IV. MAPPING Data TYPE:**

   - dict (Mutable)

**V. BOOLEAN Data TYPE:**

   - bool

**VI. BINARY / BUFFER Data TYPES:**

   - memoryview (view on binary data)

**VII. NONE Data TYPE:**

   - NoneType (None)


## Python User-Defined Data Types:

   1) Class
   2) Object
   3) Function
   4) Module


#  Operators 

🔹 Operators in Python are symbols or keywords used to perform operations on operands.
🔹 Such as arithmetic, comparison, logical, assignment, bitwise, membership, and identity operations.

# 🔥 Types of Operators

1️⃣ Arithmetic Operators

## 1) +   # addition
## 2) -   # subtraction
## 3) *   # multiplication
## 4) /   # division
## 5) %   # modulus (remainder)
## 6) / / # floor division
## 7) **  # power



2️⃣ Comparison Operators

# 1) ==  # equal
# 2) !=  # not equal
# 3) >   # greater
# 4) <   # less
# 5) >=  # greater equal
# 6) <=  # less equal


3️⃣ Logical Operators

# 1) and
# 2) or
# 3) not

4️⃣ Assignment Operators

# 1) = 
# 2) +=
# 3) -=
# 4) *=
# 5) /=
# 6) %=
# 7) **=

5️⃣ Bitwise Operators

# 1) &   # AND
# 2) |   # OR
# 3) ^   # XOR
# 4) ~   # NOT
# 5) <<  # left shift
# 6) >>  # right shift


6️⃣ Membership Operators

# 1) in
# 2) not in


7️⃣ Identity Operators

# 1) is
# 2) is not



















# 🔒 Python Reserved Words म्हणजे काय?

🔹 Reserved Words (Keywords) = Python ने आधीच वापरलेले शब्द.

👉 हे variable / function / class नाव म्हणून वापरता येत नाहीत.


## 📋 Python Keywords – COMPLETE LIST (Python 3.x)

| Category | Keywords |
|---|---|
| Boolean / Constants | `True`, `False`, `None` |
| Conditions | `if`, `elif`, `else` |
| Loops | `for`, `while`, `break`, `continue` |
| Functions | `def`, `return`, `lambda` |
| Exception Handling | `try`, `except`, `finally`, `raise` |

📌 Total Keywords in Python 3.x: `35`

**❌ Reserved words वापरले तर काय होतं?**

## 💻 Example

```python
if = 10
```

❌ Error येईल:

🔹 SyntaxError: invalid syntax


**✅ Correct way (safe identifiers)**

Reserved word ला suffix / prefix लावा:

🔹 if_value = 10

🔹 class_name = "A"

🔹 is_valid = True


**1. Keywords ची Properties**

🔹 Keywords case-sensitive असतात (True ≠ true).

🔹 Python मध्ये keywords ची संख्या version नुसार बदलते (Python 2.x vs 3.x).

🔹 keyword module वापरून keywords list मिळवता येते:

```python
import keyword

print(keyword.kwlist)
```
**2. Version Differences**

🔹 Python 3.7 पासून keywords stable झाले आहेत.

🔹 Python 3.5 मध्ये async आणि await add झाले.

🔹 Python 2.x मध्ये print keyword होता, पण Python 3.x मध्ये तो function आहे.

## ❓ Difference Between Keywords and Identifiers

🔹 Keywords = predefined.

🔹 identifiers = user-defined.

🔹 Keywords ला variable नाव म्हणून वापरता येत नाही.

🔹 identifiers ला वापरता येतं.


## 🧠 Keywords category-wise (समजायला सोपं):

**1️⃣ Boolean / Constants**

True, False, None

**1️⃣ True**

✅ Boolean constant → logical value "true" दर्शवतो.

👉 Type: bool

## 💻 Example

```python
x = True

print(type(x))   # <class 'bool'>

if x:
    print("Yes")   # Output: Yes
```

🧠 Internally: True म्हणजे integer 1 सारखं वागतो, पण semantic meaning वेगळं आहे.


**2️⃣ False**

❌ Boolean constant → logical value "false" दर्शवतो.

👉 Type: `bool`

## 💻 Example

```python
y = False

print(type(y))   # <class 'bool'>

if y:
    print("Yes")
else:
    print("No")   # Output: No
```

🧠 Internally: False म्हणजे integer 0 सारखं वागतो.


## 3️⃣ None

🚫 Special constant → "no value" किंवा "null" represent करतो.

👉 Type: `NoneType`

## 💻 Example

```python
z = None

print(type(z))   # <class 'NoneType'>

if z is None:
    print("Empty")   # Output: Empty
```

## 🧠 Usage

🔹 Functions मध्ये default return value (return नसेल तर None मिळतो).

🔹 Optional variables initialize करण्यासाठी.

🔹 "no data" किंवा "missing value" represent करण्यासाठी.

> ⚠️ Important: `None` falsy आहे, पण `False` नाही.

🎯 Summary

🔹 True → Boolean constant (logical 1).

🔹 False → Boolean constant (logical 0).

🔹 None → Special constant (absence of value).

# 🧠 Advanced Concepts of None / Boolean in Python

---

## 1️⃣ Truthiness Concept

Python मध्ये काही values **truthy** तर काही **falsy** असतात.

## ❌ Falsy Values

- `False`
- `None`
- `0`
- `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)
- `set()`

बाकी जवळपास सगळ्या values **truthy** असतात.

💡 म्हणजे `None` logical check मध्ये `False` सारखं वागतो, पण तो `False` नाही.

## 💻 Example

```python
x = None

if x:
    print("Truthy")
else:
    print("Falsy")
```

### ✅ Output

```python
Falsy
```

---

## 2️⃣ Identity vs Equality

`None` check करण्यासाठी नेहमी `is None` वापरतात.

## ✅ Correct Way

```python
x = None

if x is None:
    print("Empty")
```

## ❌ Avoid

```python
if x == None:
    print("Empty")
```

⚠ `is` identity check करतो, तर `==` equality check करतो.

💡 Python community मध्ये `is None` ही best practice मानली जाते.

---

## 3️⃣ Memory Internals

`True` आणि `False` हे singleton objects आहेत.

👉 Python internally त्यांना reuse करतो.

`None` सुद्धा singleton object आहे.

💡 म्हणजे संपूर्ण Python program मध्ये फक्त एकच `None` object असतो.

## 💻 Example

```python
x = None
y = None

print(x is y)
```

### ✅ Output

```python
True
```

---

## 🎯 Summary

🔹 `None` falsy आहे, पण `False` नाही.

🔹 `is None` वापरणे best practice आहे.

🔹 `True`, `False`, आणि `None` हे singleton objects आहेत.

🔹 `None` म्हणजे absence of value.

---

## 📌 Final Understanding

✅ Boolean (True/False): हे लॉजिकल निर्णय घेण्यासाठी वापरतात. पायथनमध्ये True म्हणजे 1 आणि False म्हणजे 0 असते.

📌 None ला Boolean category मध्ये technically ठेवता येत नाही, कारण तो logical True/False नाही. पण Python keywords grouping मध्ये आपण त्याला Constants मध्ये ठेवतो.

💡 False म्हणजे "नाही" — None म्हणजे "माहीतच नाही / अस्तित्वच नाही"

**2️⃣  Conditions**

if, elif, else


**3️⃣ Loops**

for, while, break, continue

**4️⃣ Functions / Classes**

def, return, class, yield, lambda


**5️⃣ Exceptions**

try, except, finally, raise, assert


**6️⃣ Logic Operators**

and, or, not, is, in


**7️⃣ Scope / Context**

global, nonlocal, with, as


**8️⃣ Imports**

import, from

**9️⃣ Async Programming**

async, await


**“Reserved words are predefined keywords in Python that have special meaning and cannot be used as identifiers.”**

**🎯 Summary Line**

*“Python keywords म्हणजे reserved words ज्यांना special meaning आहे. ते identifiers म्हणून वापरता येत नाहीत, आणि Python चं grammar define करतात.”*