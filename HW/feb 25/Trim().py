def Trim(Name):
    Dots = "..."
    Space = ""
    NameLen = len(Name)

    if NameLen < 17:
        return Name

    while NameLen > 13:
        Name = Name[:-1]
        if Name[NameLen] == Space:
            break

    Name += Dots
    return Name


print(Trim("Bohemian Symphony"))
