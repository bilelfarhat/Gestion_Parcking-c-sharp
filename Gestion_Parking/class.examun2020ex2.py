class produit:
    def __init__(self,nom,prix,qte):
        self.nom=nom
        self.prix=prix
        self.qte=qte
    def disponible(self):
        if self.qte>0:
            return True
        else:
            return False        
    def reduction(self,p):
        s=p/100
        tot=self.prix - self.prix*s
        return tot
    def affiche(self):
        return ("le {0} est de prix {1} est {2}".format(self.nom,self.prix,self.qte))
c=produit('panadol',10,2)
print(c.disponible())
print(c.reduction(20))
print(c.affiche())                   
class medicament(produit):
    def __init__(self,ref,nom,prix, qte,etatord,cnam):
        
        super().__init__(nom, prix, qte)
        self.ref =ref
        self.etatord =etatord
        self.cnam = cnam
    def meddisponible(self,qte):
        produit.disponible(self,qte)
    def montant(self,qte):
        if self.qte== True :
            if self.cnam==True:
                montant = produit.reduction(30)*qte
                self.qte-=qte
            else:
                montant=qte*self.prix
                self.qte-=qte    
        else:
            print("qte non dispo")
        return (montant)
    def affichage(self):
        return("la qte {0} reste de medicament{1}".format(self.qte,self.nom))                        
class pharmacie:
    def __init__(self,lmed,lclient):
        self.lmed=lmed
        self.lclient=lclient


        