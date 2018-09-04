# importation des librairies 
from selenium import webdriver as wd
import sys, os

# choix et encapsulation du navigateur
options = wd.ChromeOptions() 
options.add_argument("download.default_directory=Users\Taoufik\Documents\Project")
Navigateur = wd.Chrome(chrome_options=options)
 

# Inputs 
Villes=['RABAT','CASABLANCA','SETTAT','SALE','KENTRA','Wialaya de Casablanca Anfa','Wilaya de Rabat','Province de Boulemane','Province de Settat','MAROC RABAT','BOULEMANE','MAROC CASABLANCA']
section=['Fournitures']



# Recuperation de la liste des appels d'offres ainsi que les CPS

Navigateur.get ('https://www.marchespublics.gov.ma/')
Navigateur.find_element_by_xpath("//ul[@class='tabs-nav']/li[2]/a").click()
Navigateur.find_element_by_xpath('//*[@id="fragment-2"]/div/table/tbody/tr[7]/td[1]/a').click()
Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]').click()
Nbr_offre= Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_resultSearch_nombreElement"]').text
Nbr_offre=int(Nbr_offre)
for i in range (1,Nbr_offre):
    Type = Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl'+str(i)+'_panelBlocCategorie"]').text
    Ville = Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl'+str(i)+'_panelBlocLieuxExec"]').text
    if( Type in  section) and (Ville in Villes):
        Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl"+str(i)+"_panelAction\"]/a[1]").click()
        Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_linkDownloadDce\"]").click()
        Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_accepterConditions\"]").click()
        Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_nom"]').send_keys ('a')
        Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_prenom"]').send_keys ('a')
        Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_email"]').send_keys ('a@gmail.com')
        Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_validateButton\"]").click()
        Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_EntrepriseDownloadDce_completeDownload\"]").click()
        Navigateur.back()
        Navigateur.back()
        Navigateur.back()
        Navigateur.back()

        
        
# decompression et Analyse appels d'offres  


#move to directory that containes archives
os.chdir("C:\\Users\Taoufik\Downloads")

#decoumpresse files
for filename in os.listdir("C:\\Users\Taoufik\Downloads\\test"):
    name = str(filename)
    if name.endswith('.zip'):
        x =  len(name)
        directory = name[:(x-4)]
        os.system("unzip -o \""+name+"\" -d \""+directory+"\"")


            
      
     
            
        
            
        
            


   

        

   
    
  



       








