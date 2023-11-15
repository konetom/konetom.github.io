# Bioinformatics
### What is bioinformatics?
> Bioinformatics is like a bridge that connects the world of biology with the world of computer science. It’s a field that develops methods and software tools for understanding biological data.

> *For example, imagine a scientist who has just sequenced a new gene. With bioinformatics, they can compare this gene to databases of known genes, predict the structure of the protein it codes for, and begin to hypothesize its function.*
<br>

### Who is a bioinformatician?
> A bioinformatician is like a detective in the world of biology. They use computational tools to gather and analyze data from biological experiments, and then use this data to solve problems or make new discoveries.

> *For instance, a bioinformatician might analyze the genetic sequences of a population of fruit flies to understand how genetic variation contributes to differences in wing color.*
<br>

# Linux
### What is Linux?
> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/300px-Tux.svg.png" height="100px">  **GNU/Linux** is an operating system, just like Windows or MacOS, but it’s open-source. It means that anyone can look at and modify its code. This has led to a huge variety of different versions, or “distributions”, of Linux, each tailored to different needs.

> (image from wikimedia.org)
<br>

### Who is using Linux?
> Linux is used by many companies and organizations, including Google and Facebook. Linux is a part of govermental systems in France, China, South Africa. Linux is currently the worldwide leading operation system on all servers and nearly all supercomputers.
<br>

### Who is Linus?
> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Lc3_2018_%28263682303%29_%28cropped%29.jpeg/440px-Lc3_2018_%28263682303%29_%28cropped%29.jpeg" height="100px">  **Linus Benedict Torvalds** is a Finnish software engineer, creator of Linux, and lead developer of the Linux kernel used by several Linux distributions, like Debian, Arch, or Android. He started developing Linux as a student at the University of Helsinki in Finland. The story goes that he wasn’t happy with the operating systems available at the time, so he decided to create his own.

> (image from wikimedia.org)
<br>

### Who is Richard Stallman and what is copyleft?
> <img src="https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2019/09/3240px-Richard_Stallman_by_Anders_Brenna_01-Cropped.jpg" height="100px"> **Richard Stallman** campaigns for software to be distributed in such a manner that its users have the freedom to use, study, distribute, and modify that software. Stallman pioneered the concept of copyleft, which uses the principles of copyright law to preserve the right to use, modify, and distribute free software. The exact definition of copyleft varies based on jurisdiction, but the essence is that the author of a work has a limited monopoly on the copying, performance, etc. of the work.

> (image from cdn0.tnwcdn.com)
<br>

# Bash
### What is bash?
> Bash, or the Bourne Again SHell, is a command language interpreter for the Linux operating system. It’s like the text-based version of clicking and dragging in a graphical user interface.

> *For example, instead of clicking on a folder to open it, you would type* `cd <foldername>` in bash.
<br>


### Why to use bash?
> Bash is incredibly powerful. With it, you can automate repetitive tasks, manage files and directories, and even access network resources. Plus, since it’s text-based, you can use bash over a network connection, which isn’t possible with a graphical interface.
<br>

### When to use bash?
> Bash is used when you need to interact with your system, automate tasks, manipulate files and directories, and much more. It’s especially useful when working with large amounts of data or performing repetitive tasks.
<br>

# Git
### What is Git?
> Git is a version control system. It’s like a time machine for your code. You can save versions of your code at different points in time, and then jump back to any saved version whenever you want. This is incredibly useful for tracking changes and collaborating with others.
<br>

### Why should we talk about Linus again?
> Because Linus Torvalds, the creator of Linux, is also the creator of Git. He developed it to help manage the development of the Linux kernel.
<br>

### When to use Git?
> Git is used when you need to manage and track versions of your project. It’s especially useful in collaboration, version control, backup and restore, tracking changes, exerimentation, and more.

> *For example, whenever you are working on a project (especially in a team) where you need to track changes, collaborate efficiently, and have the flexibility to experiment without fear of losing or overwriting work, Git is the best friend.*
<br>

# Programming
### What is programming?
> Programming is the process of creating a set of instructions (= algorithms) that tell a computer what to do. It’s like writing a recipe for a computer to follow.

> *For example, a simple program might tell the computer to take a number, multiply it by two, and then print the result.*
<br>

### What is low-level programming and do bioinformaticians need to use it?
> Low-level programming refers to a programming style that is closer to machine code than to human language. Programs written in low-level languages can run very quickly, but they are considered difficult to use. In most cases, bioinformaticians do not necessarily need to use low-level programming.
<br>

### Why bioinformaticians do not need to know low-level programming?
> While low-level programming languages like C++ or Java can be useful in certain situations, most bioinformatics tasks can be accomplished with high-level scripting languages like Python or R. These languages are easier to learn and faster to write code in, which makes them a great choice for bioinformaticians.

> *Bioinformaticians typically work with large datasets and use existing tools and libraries to analyze data. While they do need to write code to manipulate data and glue different tools together, they usually don’t need to write complex algorithms or data structures from scratch. That’s why a high-level language like Python or R, which has many built-in functions and libraries, is often sufficient.*

```
# Here is a simple “Hello, World!” program written in Assembly language \
for machine with an x86 processor and Linux operating system:

section .data
    hello db 'Hello, World!',0

section .text
    global _start

_start:
    ; write hello to stdout
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    mov edx, 13
    int 0x80

    ; exit
    mov eax, 1
    xor ebx, ebx
    int 0x80
```
<br>

# R
### What is R?
> R is a high-level programming language that was specifically designed for data analysis and visualization. It’s like the Swiss Army knife of data science. It has a huge number of packages for everything from statistical tests to plots.

> *For example, a bioinformatician might use R to analyze the gene expression of a population of fruit flies to understand how genetic variation contributes to differences in wing color.*
<br>

### Why many bioinformaticians use R?
> R is particularly popular in bioinformatics because it makes it easy to perform complex data analyses and create visualizations. Because it’s open-source, there’s a huge community of users who contribute with new packages and help answering questions.
<br>

# Python
### What is Python?
> Python is an interpreted, dynamically typed, garbage-collected, high-level, general-purpose, cross-platform, object-oriented, functional programming language that is both easy to learn and robust enough for large-scale projects.

> Whether you’re new to programming or an experienced developer, Python is a fantastic language to learn and use. It is used for a variety of applications, including automation, data analytics, databases, documentation, GUI, image processing, machine learning, mobile apps, multimedia (libraries for audiovisual processing), networking (cybersecurity and hacking), scientific computing (numpy, pandas, scipy, scikit-learn, etc.), system administration, frameworks, text processing (ChatGPT), web scaping, web development, and more.
<br>

* Python 1 (released in 1994) introduced new features like lambda, map, and filter.
* Python 2 (released in 2000) had new features, including a cycle-detecting garbage collector for memory management and support for Unicode (last version was 2.7 released in 2020).
* Python 3, (released in 2008) was a backwards-incompatible release with many new features.
<br>

> Modern programming languages like Go, JavaScript, Julia, Ruby, Swift, and F#, were inspired or are at least partly written in Python.

> Python has been succesfully implemented in other programming languages. List of famous cross-compilers: Cython, Brython, Jython, PyJL, Nuitka, RPython, ...

> Who is using Python? Google, Facebook, Amazon, NASA, Spotify, Netflix, Dropbox, and many more.

> Nowadays, Python is widely used in a variety of industries and many applications. In 2022, Python was the most commonly used programming language for web development and data analysis. Significant number of companies (from small to large-sized) use Python in any way every day...
<br>

### Who is Guido van Rossum?
> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Guido-portrait-2014-drc.jpg/440px-Guido-portrait-2014-drc.jpg" height="100px"> **Guido van Rossum** (born in Netherland) is the creator of Python. He started developing Python in the late 1980s as a hobby project. The first version (Python 0.9.0) was published in 1991. Since the time it has grown into one of the most popular programming languages in the world.

> According to Guido van Rossum, Python 4 will probably never come. The transition from Python 2 to Python 3 created compatibility problems and was a slow and painful process for many developers. Instead of releasing a new major version, the Python developer team continues to focus on improving Python 3. So, while Python continues to evolve and improve, the major version number will likely stay at number 3. First released version of Python3 was 3.6, and currently the newest stable version is 3.12.0 released on October 2, 2023.

> (image from wikimedia.org)

<br>

### *Try to follow "Python Enhancement Proposals (PEPs)", especially `PEP20: Zen of Python`*

<br>

### Why to follow Zen of Python?
*The Zen of Python is a collection of “guiding principles” for writing computer programs that influence the design of the Python programming language.*
<br>


#### Beautiful is better than ugly.
```
# Beautiful
def greet(name):
    return f"Hello, {name}. how are you?"


# Ugly
def greet(name): return "Hello, " + name + ". how are you?"
```
<br>

#### Explicit is better than implicit.
```
# Explicit
def calculate_rectangle_area(length, width):
    return length * width


# Implicit
def calculate_area(x, y):
    return x * y
```
<br>

#### Simple is better than complex.
```
# Simple
def is_even(num):
    return num % 2 == 0


# Complex
def is_even(num):
    if ((num / 2) * 2) == num:
        return True
    else:
        return False
```
<br>

#### Complex is better than complicated.
```
# Complex
def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)


# Complicated
def factorial(num):
    if num == 0:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact
```
<br>

#### Readability counts.
```
# Less readable
def s(l):
    return list(map(lambda x: x**2, l))


# More readable
def exponentiate(numbers, exponent):
    results = []
    for element in numbers:
        results.append(element ** exponent)
    return results

<br>

## vitisSOM - An implementation of Python and Bash into an existing R project

> To be continued...
