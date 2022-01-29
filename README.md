# **Minimal Base MHRise Database with Python**

## **Description**

I wanted to make this project to learn OOP with Python and, when I finish it, try to replicate to use a database python library to improve this project with a database and to even use it with a discord bot so that it can give info to people who need it without going on [Kiranico](https://mhrise.kiranico.com/ "MHRise Kiranico") (I'd recommend to use this though) every time (it's even useful when you don't have connection)

---

## FAQ and some questions that will surely be asked

**Will you Update the database when [Monster Hunter Rise: Sunbreak](https://www.monsterhunter.com/rise-sunbreak "Link to the MHR:S Official Page") will be released, in Summer 2022?**  
It's written in the title: **Base Rise** but if I have time and will I'll do it

![Monster Hunter Rise Sunbreak](assets/mhr_sunbreak_banner.jpg)

---

## Changelogs

## ALPHA (0.0)

`0.0.2`

* Added the \_\_init__ files for importing
* Made some arguments in `skills.py`
  
* Importing the database will activate the \_\_init__ file and, if you look closely, you see that it will return nothing (or at least I tried to, if it doesn't work just open an issue and tell everything you need to tell what you  **e x p e r i e n c e d** while trying that so I can ~~steal some code from StackOverflow~~ fix that, or at least I hope so since I think there is so much spaghetti code and I guess that `0.0.3` - or maybe `0.0.2 ß` and this becomes `0.0.2 α` - will just be code reordering).
That means that if you want to copy something you will have to copy the files directly

* Made so that the type of the classes (in this case template) of the data is now static and not dynamic (it's not ```int(x)``` but ```def __init__(self, x: int)```)

* this update becomes 0.0.2 and the previous 0.0.2 becomes `0.0.1 ß`, the first one becomes `0.0.1 α`

* Fixed some "UI mistakes" in this file
  
`0.0.1 ß`

* Started making the classes used for making an object of each object for its category (armors, items, monsters, skills)
* Made so that the program occupies less memory and takes less to be used and coded
* Fixed some errors in this file

`0.0.1 α`

* Started the Project
* Initialized the repo
* Imagine starting to code and then writing the README.md file when you can just start writing and then coding and release it in the `0.0.1 ß`
