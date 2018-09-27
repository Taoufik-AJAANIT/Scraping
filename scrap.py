from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mongo import Mongo

#Navigator set up
Navigateur = webdriver.Chrome(
    executable_path='/home/taoufik/Documents/TTProject/chromedriver')
Navigateur.get('https://www.marchespublics.gov.ma/')


#wait until element exist
def wait(xpath):
      WebDriverWait(Navigateur, 90).until(
          EC.presence_of_element_located((By.XPATH, xpath)))


# Inputs
Villes = ['RABAT', 'CASABLANCA', 'SETTAT', 'SALE', 'KENTRA', 'Wialaya de Casablanca Anfa', 'Wilaya de Rabat',
          'Province de Boulemane', 'Province de Settat', 'MAROC RABAT', 'BOULEMANE', 'MAROC CASABLANCA']
section = ['Fournitures']


#set up database
mydb = Mongo('TTProject',['offres-info','offres-text'])

#file to store references
f = open("references.txt", "a")


#scraping

wait("//ul[@class='tabs-nav']/li[2]/a")
Navigateur.find_element_by_xpath(
    "//ul[@class='tabs-nav']/li[2]/a").click()


wait('//*[@id="fragment-2"]/div/table/tbody/tr[7]/td[1]/a')
Navigateur.find_element_by_xpath(
    '//*[@id="fragment-2"]/div/table/tbody/tr[7]/td[1]/a').click()

wait('//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]')
Navigateur.find_element_by_xpath(
    '//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]').click()



wait('//*[@id="ctl0_CONTENU_PAGE_resultSearch_nombreElement"]')
Nbr_offre = Navigateur.find_element_by_xpath(
    '//*[@id="ctl0_CONTENU_PAGE_resultSearch_nombreElement"]').text


Nbr_offre = int(Nbr_offre)
for i in range(1, Nbr_offre):
    wait('//*[@id="ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl' +
         str(i)+'_panelBlocCategorie"]')
    Type = Navigateur.find_element_by_xpath(
        '//*[@id="ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl'+str(i)+'_panelBlocCategorie"]').text
    Ville = Navigateur.find_element_by_xpath(
        '//*[@id="ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl'+str(i)+'_panelBlocLieuxExec"]').text
    if(Type in section) and (Ville in Villes):
        wait("//*[@id=\"ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl" +
             str(i)+"_panelAction\"]/a[1]")
        Navigateur.find_element_by_xpath(
            "//*[@id=\"ctl0_CONTENU_PAGE_resultSearch_tableauResultSearch_ctl"+str(i)+"_panelAction\"]/a[1]").click()


        #check if exist in mongo
        wait('//*[@id="ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_reference"]')
        reference = Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_idEntrepriseConsultationSummary_reference"]').text
        result = mydb.find('offres-info', '_id', reference)
        if  result.count() == 0:   #if not exist insert to db & continue

            #collect elements to insert
            lien = Navigateur.current_url
            offre = {'_id' : reference , 'lien' : lien  } 

            #add reference to .txt file
            f.write(str(reference+" "))
            #inserting
            mydb.insert(offre, 'offres-info')
        
            #continue action
            wait("//*[@id=\"ctl0_CONTENU_PAGE_linkDownloadDce\"]")
            Navigateur.find_element_by_xpath(
                "//*[@id=\"ctl0_CONTENU_PAGE_linkDownloadDce\"]").click()
    
            wait(
                "//*[@id=\"ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_accepterConditions\"]")
            Navigateur.find_element_by_xpath(
                "//*[@id=\"ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_accepterConditions\"]").click()
    
            wait('//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_nom"]')
            Navigateur.find_element_by_xpath(
                '//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_nom"]').send_keys('a')
            Navigateur.find_element_by_xpath(
                '//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_prenom"]').send_keys('a')
            Navigateur.find_element_by_xpath('//*[@id="ctl0_CONTENU_PAGE_EntrepriseFormulaireDemande_email"]').send_keys('a@gmail.com')
            Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_validateButton\"]").click()
            Navigateur.find_element_by_xpath("//*[@id = \"ctl0_CONTENU_PAGE_EntrepriseDownloadDce_completeDownload\"]").click()
    
            #retour
            Navigateur.find_element_by_xpath("//*[@id = \"ctl0_CONTENU_PAGE_panelEntrepriseDownloadDce\"]/a[1]").click()
            wait("//*[@id=\"ctl0_CONTENU_PAGE_linkRetourBas2\"]")
            Navigateur.find_element_by_xpath("//*[@id=\"ctl0_CONTENU_PAGE_linkRetourBas2\"]").click()
            wait('//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]')
            Navigateur.find_element_by_xpath(
        '//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]').click()

        #if exist :  return to home page :
        else :
            Navigateur.find_element_by_xpath(
                '//*[@id = \"ctl0_CONTENU_PAGE_linkRetourBas2\"]').click()
            wait('//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]')
            Navigateur.find_element_by_xpath(
                '//*[@id="ctl0_CONTENU_PAGE_resultSearch_listePageSizeTop"]/option[5]').click()
            
        

	    
	
