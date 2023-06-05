##### Criss-Cross Studying: Your own income tax simulator
#The aim of this is to create a working tax calculator that will tell you an estimation of your income taxes
# based on the Tarifs set in DBG 36

print("Wilkommen beim Steuerschätzer!")
print("Sind sie verheiratet/ein einer eingetragenen Partnerschaft?(Ja/Nein/It's complicated)")
marr = input()

if marr == "It's complicated":
    print("This isn't your Facebook status.Come back once you have figured it out")
    exit()

print("Wieviele Kinder haben sie? (in ganzen Zahlen bitte)")
kid0 = float(input())
kid1 = int(kid0)
kid2 = float(kid1)
if kid2 - kid0 != 0:
    print("Ihre Koordinaten wurden der Polizei weitergeleitet. Sie Monster.")
    exit()
else: kid = int(kid0)
kid_ded = 6500 * kid

if marr == "Nein":
# We will now list the different Tax thresholds into tiers, and their corresponding tax added values per 100CHF
    taxs = {9:[755200,86848, 11.50], 8: [176000,10393.60, 13.20], 7: [134600,5839.60,11.00],\
            6:[103600,3111.60 ,8.80], 5:[78100,1248.60, 6.60], 4:[72500,1096, 5.94], 3: [55200,582.20,2.97],\
            2:[41400,217.90,2.64], 1:[31600,131.65, 0.88], 0:[14500,0.00,0.77]}         
    
    print("Zahlen sie Beiträge an die AHV/Altersvorsorge in Totalaufwand von > 1700? Ja/Nein")
    ahv = input()
    if ahv == "Ja":
        ahv_ded = 1700 #deduction for single people
    elif ahv == "Nein":
        print("Wieviel haben sie einbezahlt?")
        ahv_ded = int(input())
    
    print("Bitte geben sie ihr jährliches Einkommen ein, auf hundert CHF gerundet:")
    a0 = int(input())
    a = a0 - ahv_ded - kid_ded 
    
elif marr == "Ja":
    taxs = {13:[895900,103028.50,11.50], 12:[145000,5412,13], 11:[143100,5184,12], 10:[141200,4975,11], \
            9:[137300,4585,10],8:[131700,4081,9], 7:[124200,3481,8], 6:[114700,2816,6], 5:[103400,2138,6], \
            4:[90300,1483,5], 3:[75300,883,4], 2:[58400,376,3], 1:[50900,226,2], 0:[28300,0.00,1.00]}
    ##Fix the deduction for the lower income: Max. 13'400 CHF, min 8'100, in all cases 50% of the lower income!!
    #Regulated in DBG
    marr_ded = 2600
    kid_extra_ded = kid * 251
    
    print("Zahlen sie Beiträge an die AHV/Altersvorsorge in Totalaufwand von > 3500? Ja/Nein")
    ahv = input()
    if ahv == "Ja":
        ahv_ded = 3500 #deduction for married couples
    elif ahv == "Nein":
        print("Wieviel haben sie einbezahlt?")
        ahv_ded = int(input())
        
    print("Bitte geben sie das höhere Einkommen in der Ehe ein:")
    a1 = int(input())
    print("Bitte geben sie das niedrigere Einkommen in der Ehe ein:")
    a2 = int(input())
    a2_ded = a2 / 2
    if a2_ded >= 13400:
        a2_ded = 13400
    elif a2_ded <= 8100:
        a2_ded = 8100
    else: a2_ded = a2_ded
    
    a0 = a1 + (a2 - a2_ded) #calculating the final taxeable sum 
    a = a0 - (marr_ded + ahv_ded + kid_ded + kid_extra_ded)

for i in taxs: #iterate over dictionary
    if a >= taxs[i][0]:#see if a falls into the tax bracket
        b = a - taxs[i][0]  # create b to see the remaining difference
        c =  b / 100  
        res = taxs[i][1] + c * taxs[i][2] # calculating final value based on base tax + added tax per 100CHF
        print("Sie fallen in die Steuerkategorie " + str(i) + ", mit einer Steuerschwelle von: " + str(taxs[i][0]))
        print("Und zahlen somit voraussichtlich:")
        print(str(res) + " " + "CHF")
        break   
    elif a <= taxs[0][0]:
        print("Sie fallen tiefer als die Steuerkategorie 0, mit einer Steuerschwelle von: 14500 CHF resp. 28300 CHF für Ehepaare")
        print("Und zahlen somit voraussichtlich:")
        print("Keine Einkommenssteuern")
        break
