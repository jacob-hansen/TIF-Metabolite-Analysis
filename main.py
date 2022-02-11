from libraries import *
from functions import *

# Note: requirements!!!!!!
# The standards 0, 0.1, 0.3, ect.. must have the word "pool" or "Pool" in them.
#

mPath, excelDocs, fileName = requestDocs()
print("Loading documents (-13C columns)...")
fileFinal = readDocs(excelDocs)
columns = list(fileFinal.columns)
values = fileFinal.copy()
values.drop(columns[0], axis=1, inplace=True)
values.drop(columns[1], axis=1, inplace=True)

fcStatus, sortKeys = findCompoundStatus(mPath, fileName, values)


print("Calculating concentrations....")

standardList = ['0', '0.1', '0.3', '1', '3', '10', '30', '100', '500']
quantDict = {}

for compound in values:
    test = True
    csList = []
    rValues = []
    testList = []

    if(fcStatus[compound] != 's'):
        n = 0
        for item in standardList:
            if(fileFinal.at[item, compound] != 'NF' and # noqa E501
                    fileFinal.at[item, compound] != 'NaN' and not math.isnan(fileFinal.at[item, compound])):
                if(len(csList) == 0):
                    startVal = n
                testList.append(round(float(item), 1))
                csList.append(float(item)*iStandards[compound]/500)
                rValues.append(float(fileFinal.at[item, compound]))  # noqa E501 !!!!!!!!!!!!!!!!!!! I Just put in "Response Ratio", if it is changed earlier in the code, it will throw an error!!!!!!!!!!!!!!!!!!!!
                n += 1
        if(len(csList) == 0 or len(rValues) == 0):
            fileFinal[compound].slope, fileFinal[compound].intercept, fileFinal[compound].r_value, fileFinal[compound].p_value, fileFinal[compound].std_err = 0, 0, 0, 0, 0
            test = False
            fcStatus[compound] = 's'

        if(test == True):
            check = ['e', 'i', 's']
            if(fcStatus[compound] not in check):
                newStatus = input("Did not understand command for "+compound+". Please enter 'i' for Internal, 'e' for external, or 's' for skip: ")
                while(True):
                    if(newStatus in check):
                        fcStatus[compound] = newStatus
                        break
                    else:
                        newStatus = input("Still did not understand the command. Enter i, e, or s only: ")

            # => calculating concentrations for external standard compounds
            if(fcStatus[compound] == 'e'):
                getR = 0.98
                fileFinal[compound].slope, fileFinal[compound].intercept, fileFinal[compound].r_value, fileFinal[compound].p_value, fileFinal[compound].std_err = sp.stats.linregress([float(number) for number in csList], [number for number in rValues])
                i = 0
                if (len(csList) == 0 and len(rValues) == 0):
                    fcStatus[compound] = 's'
                while(len(csList) > 3 and len(rValues) > 3):
                    csList.pop()
                    rValues.pop()
                    islop, iintercept, ir_value, ip_value, istd_err = sp.stats.linregress([float(number) for number in csList], [float(number) for number in rValues])
                    if(ir_value > getR):
                        fileFinal[compound].slope, fileFinal[compound].intercept, fileFinal[compound].r_value, fileFinal[compound].p_value, fileFinal[compound].std_err = islop, iintercept, ir_value, ip_value, istd_err
                        break
                    elif(ir_value > fileFinal[compound].r_value):
                        fileFinal[compound].slope, fileFinal[compound].intercept, fileFinal[compound].r_value, fileFinal[compound].p_value, fileFinal[compound].std_err = islop, iintercept, ir_value, ip_value, istd_err
                    if(i > 5):
                        getR = 0.99
                    i += 1

                # => Calculating final concentration!!
                quantDict[compound] = []
                for val in fileFinal[compound]:
                    quantDict[compound].append((val-fileFinal[compound].intercept)/(fileFinal[compound].slope)*1000)



            # => calculating concentrations for internal standard compounds
            elif(fcStatus[compound] == 'i'):
                fileFinal[compound].concentration = 0
                endVal = len(csList)-4+startVal
                cSTD = 100000000000000000 #Some value greater than it could be in the code. sys.max????
                finalPos = max(0, 2-startVal)
                for n in range(max(0, 2-startVal), endVal):
                    if(rValues[n] !=0 and rValues[n+1] !=0 and rValues[n+2] !=0):
                        tempSTD = st.stdev([csList[n]/rValues[n], csList[n+1]/rValues[n+1], csList[n+2]/rValues[n+2]])
                        if (tempSTD < cSTD):
                            fileFinal[compound].concentration = 1000*(csList[n]/rValues[n]+csList[n+1]/rValues[n+1]+csList[n+2]/rValues[n+2])/3
                            finalPos = (testList[n], testList[n+1], testList[n+2])



                # => Calculating final concentration!!
                quantDict[compound] = []
                multiplyV = fileFinal[compound].concentration
                for val in fileFinal[compound]:
                    quantDict[compound].append(multiplyV * val)



                # => This if statement checks to make sure the concentration value includes the "100" standard value if it is over 100.
                # If it is over 100, and it doesn't already include it, then it averages the old and a new value including it.
                if(sum(quantDict[compound][0:10])/10 > 100 and 100.0 not in finalPos):
                    if (100.0 not in testList):
                        print("Compound "+compound+" value might be slightly off because the pool standards were not great in the high range.")
                    else:
                        print("Recalculating concentration for "+compound+". It was "+str(fileFinal[compound].concentration))
                        try:
                            n = testList.index(100.0) # => End value is now set to where the 100 is.
                            fileFinal[compound].concentration = (fileFinal[compound].concentration+1000*(csList[n]/rValues[n]+csList[n-1]/rValues[n-1]+csList[n-2]/rValues[n-2])/3)/2
                            #print((testList[n], testList[n-1], testList[n-2]))
                            print("New value is "+str(fileFinal[compound].concentration))
                            quantDict[compound] = []
                            multiplyV = fileFinal[compound].concentration
                            for val in fileFinal[compound]:
                                quantDict[compound].append(multiplyV * val)

                        except IndexError:
                            print("Unable to update concentration with better values for compound "+compound)
                            pass


    else:
        print("Skipping over "+compound+" as directed.")
        fileFinal[compound].slope, fileFinal[compound].intercept, fileFinal[compound].r_value, fileFinal[compound].p_value, fileFinal[compound].std_err = 0, 0, 0, 0, 0



dfReturn = pd.DataFrame(data=quantDict, index = fileFinal.index.tolist())
append_df_to_excel(mPath, dfReturn, sheet_name='Output', startrow=1)
