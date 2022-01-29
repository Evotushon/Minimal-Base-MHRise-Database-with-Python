# I hate adding everytime this file, but I gotta do this unless there is a better method to import other things

# made so that no one can use this directory because
# when the __init__ function (called whenever the file is imported) from the __init__ file (called whenever someone imports this)
# it returns nothing
# or at least that's what I tried to do here
def __init__(self) -> None:
    if __name__ != "__main__":
        return