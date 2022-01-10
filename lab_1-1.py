# Author: IBN (AMDG) 1/10/22

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
blank = []
for row in rows:
    for name in row:
        if name[-1] == "s":
            blank.append(name + "'")
        else:
            blank.append(name + "'s")
 
print(blank)
