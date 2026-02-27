'''What is this?

data is a list

Each element inside the list is a dictionary

Each dictionary has two key-value pairs:

"name"

"age"

So internally it looks like this:

List
 ├── Dictionary 1 → {"name": "A", "age": 25}
 └── Dictionary 2 → {"name": "B", "age": 20}

This is called a list of dictionaries.
----------------------------------------------------------------
Step 2: The sorted() Function
sorted_data = sorted(data, key=lambda x: x["age"])
What does sorted() do?

It sorts any iterable (list, tuple, etc.)

It returns a new sorted list

It does NOT modify the original list

Syntax:

sorted(iterable, key=..., reverse=...)
-------------------------------------------------
Step 3: Understanding the key Parameter
key=lambda x: x["age"]

This is the most important part.

What is lambda?

A lambda is an anonymous function (a function without a name).

This:

lambda x: x["age"]

is equivalent to:

def get_age(x):
    return x["age"]
    
 ------------------------------------------
Step 4: What Happens Internally?

When Python executes:

sorted(data, key=lambda x: x["age"])

Python does this internally:

Takes first dictionary → {"name": "A", "age": 25}

Calls lambda → x["age"]

Returns 25

Takes second dictionary → {"name": "B", "age": 20}

Calls lambda → x["age"]

Returns 20

So Python compares:

25 and 20

Then sorts in ascending order (default behavior).
-----------------------
Step 5: Final Output

Since 20 < 25, order becomes:

[
    {"name": "B", "age": 20},
    {"name": "A", "age": 25}
]

And this gets printed:

[{'name': 'B', 'age': 20}, {'name': 'A', 'age': 25}]

-------------================================
Important Concepts for Interview

Since you're preparing for automation/SDET roles, interviewers often test:

1️⃣ Sorting list of dictionaries

Very common question.

2️⃣ Lambda understanding

They may ask:

What is lambda?

Difference between lambda and normal function?

Why use lambda inside sorted?

3️⃣ Sorting in Descending Order

You can reverse it like this:

sorted_data = sorted(data, key=lambda x: x["age"], reverse=True)

Now output becomes:

[
    {"name": "A", "age": 25},
    {"name": "B", "age": 20}
]
🔹 Visual Flow of Execution
data
 ↓
sorted()
 ↓
lambda extracts age
 ↓
Python compares ages
 ↓
Returns new sorted list
🔹 One More Important Point

sorted() → returns new list
list.sort() → modifies original list

Example:

data.sort(key=lambda x: x["age"])

This changes data directly.

'''




data = [
    {"name": "A", "age": 25},
    {"name": "B", "age": 20},
    {"name": "C", "age": 99},
    {"name": "D", "age": 92},
    {"name": "E", "age": 999}
]
new_sort= sorted(data, key = lambda y: y["age"])
print(new_sort)
    
Rever= new_sort.reverse()
print(Rever)