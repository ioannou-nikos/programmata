# -*- coding:utf-8 -*-

__author__ = 'urban'

#Ορισμοί Δομών Δεδομένων απαραίτητων για την ανάλυση
#Οι τίτλοι των φορέων ως προς τη σημασία τους
foreis_dict={'071':'PDE',
             '151':'_IDRIMATA,NEFROPATHEIS',
             '153':'_KATASKINOSEIS',
             '191':'_METAFORA MATHITON',
             '192':'_METAFORA MATHITON',
             '291':'_AGROTIKI OIKONOMIA',
             '292':'_KTINIATRIKI',
             '293':'_ALIEIA',
             '294':'_EGGEIES VELTIOSEIS',
             '390':'METAFORON IDIA ESODA',
             '721':'LEITOYRGIKA,IDIOI POROI, EKLOGES, OLATH ',
             '722':'TEO',
             '723':'ANTAPODOTIKA',
             '724':'ERGA KAP',
             '725':'ERGA KAP PKM',
}
#Οι τίτλοι των χιλιάδων από τους ΚΑΕ
xiliades_dict={'0':'PLIROMES GIA YPIRESIES',
        '1':'PROMITHIES AGATHWN KAI KEFALAIAKOY EXOPLISMOU',
        '2':'PLIROMES METABIBASTIKES',
        '3':'PLIROMES POU ANTIKRIZONTAI APO PRAGMATOPOIOUMENA ESODA',
        '4':'DAPANES NATO APO KRATOI MELH',
        '5':'DAPANES POU DEN ENTASSONTAI SE ALLES KATIGORIES',
        '6':'PLIROMES GIA THN EXYPHRETHSH THS DHMOSIAS PISTIS',
        '7':'APALOTRIOSEIS, AGORES, ANEGERSEIS ...',
        '8':'PLIROMES GIA ERGA P.D.E',
        '9':'PLIROMES GIA EPENDISEIS'}

#Set the columns names for exoda
exnames = ['logar','perigrafi','proteinomenos','eggekrimenos','anamorfoseis',
           'diamorfomenos','desmefthenta','entalthenta','proplirothenta','plirothenta']

#Set the columns names for esoda
esnames = ['logar','perigrafi','proteinomenos','eggekrimenos','anamorfoseis',
           'diamorfomenos']
           
enotites = { '00':'EDRA',
            '01':'THESSALONIKI',
            '02':'IMATHIA',
            '03':'KILKIS',
            '04':'PIERIA',
            '05':'PELLA',
            '06':'SERRES',
            '07':'CHALKIDIKI'
            }
