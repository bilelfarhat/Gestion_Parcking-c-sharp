def saisie():
    etudients={}
    while 1:
        
        etu=input("donner le nom de l'etudients:")
        moyenne=int(input("donner le moyenne:"))
        if moyenne <=20 and moyenne>0:
            etudients[etu]=moyenne
        else:
            break 
    return etudients
admis={}
refu={}    
                
for kyes ,values in saisie().items():
    if values>=10:
        admis[kyes]=values
    else :
        refu[kyes]=values



print(admis)
print(refu)    