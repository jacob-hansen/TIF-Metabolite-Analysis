from libraries import *
from functions import *

# Note: requirements!!!!!!
# Every excel document must have the pool number in it's name
# The standards 0, 0.1, 0.3, ect.. must have the word "pool" or "Pool" in them.
#

while(True):
    mPath, excelDocs, fileName = requestDocs()
    print("Loading documents (-13C columns)...")
    dfsResponse, dfsID, dfsFiles, docNames, cKeys, responseRead, IDRead, filesRead = readDocs(excelDocs)

    fcStatus, sortKeys = findCompoundStatus(mPath, dfsResponse, docNames, dfsFiles, dfsID, cKeys, fileName)

    print("Calculating concentrations....")

    standardList = ['0', '0.1', '0.3', '1', '3', '10', '30', '100', '500']

    for pool in dfsResponse:
        for compound in pool:
            test = True
            csList = []
            rValues = []
            try:
                if(fcStatus[compound] != 's'):
                    n = 0
                    for item in standardList:
                        if(pool[compound].at[item, 'Response Ratio'] != 'NF' and # noqa E501
                                pool[compound].at[item, 'Response Ratio'] != 'NaN'):
                            if(len(csList) == 0):
                                startVal = n
                            csList.append(float(item)*iStandards[compound]/500)
                            rValues.append(float(pool[compound].at[item, 'Response Ratio']))  # noqa E501 !!!!!!!!!!!!!!!!!!! I Just put in "Response Ratio", if it is changed earlier in the code, it will throw an error!!!!!!!!!!!!!!!!!!!!
                            n += 1
                    if(len(csList) == 0 or len(rValues) == 0):
                        pool[compound].slope, pool[compound].intercept, pool[compound].r_value, pool[compound].p_value, pool[compound].std_err = 0, 0, 0, 0, 0
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


                        if(fcStatus[compound] == 'e'): #pool[compound].at[item, 'Response Ratio']
                            getR = 0.98
                            pool[compound].slope, pool[compound].intercept, pool[compound].r_value, pool[compound].p_value, pool[compound].std_err = sp.stats.linregress([float(number) for number in csList], [number for number in rValues])
                            i = 0
                            while(True):
                                csList.pop()
                                rValues.pop()
                                islop, iintercept, ir_value, ip_value, istd_err = sp.stats.linregress([float(number) for number in csList], [float(number) for number in rValues])
                                if(ir_value > getR):
                                    pool[compound].slope, pool[compound].intercept, pool[compound].r_value, pool[compound].p_value, pool[compound].std_err = islop, iintercept, ir_value, ip_value, istd_err
                                    #print(pool[compound].r_value)
                                    break
                                elif(ir_value > pool[compound].r_value):
                                    pool[compound].slope, pool[compound].intercept, pool[compound].r_value, pool[compound].p_value, pool[compound].std_err = islop, iintercept, ir_value, ip_value, istd_err
                                if(i > 5):
                                    getR = 0.99
                                i += 1
                            print(str(compound)+" slope is "+str(pool[compound].slope))
                            print(str(compound)+" intercept is "+str(pool[compound].intercept))

                        elif(fcStatus[compound] == 'i'):
                            pool[compound].concentration = 0
                            endVal = len(csList)-4+startVal
                            cSTD = 100000000000000000
                            for n in range(max(0, 2-startVal), endVal):
                                if(rValues[n] !=0 and rValues[n+1] !=0 and rValues[n+2] !=0):
                                    tempSTD = st.stdev([csList[n]/rValues[n], csList[n+1]/rValues[n+1], csList[n+2]/rValues[n+2]])
                                    if (tempSTD < cSTD):
                                        pool[compound].concentration = 1000*(csList[n]/rValues[n]+csList[n+1]/rValues[n+1]+csList[n+2]/rValues[n+2])/3

                else:
                    print("Skipping over "+compound+" as directed.")
                    pool[compound].slope, pool[compound].intercept, pool[compound].r_value, pool[compound].p_value, pool[compound].std_err = 0, 0, 0, 0, 0

            except KeyError:
                print("Error, could not find "+compound+" in standard pool. Skipping over it ")
                fcStatus[compound] = 's'
                continue
            except ValueError:
                print("Error found with "+compound+", maybe the name was poorly formatted. Skipping over it ")
                fcStatus[compound] = 's'
                continue

    for pool in dfsResponse:
        for compound in pool:
            pool[compound].loc[:, responseRead] = pool[compound].apply(pd.to_numeric, args=('coerce',))
            if (fcStatus[compound] == 'e'):
                pool[compound]['Quantification'] = (pool[compound].loc[:, responseRead]-pool[compound].intercept)/(pool[compound].slope)*1000# multiplyV * pool[compound].loc[:, responseRead]#.apply(lambda row : row*multiplyV)#, axis = 1)
            elif(fcStatus[compound] == 'i'):
                multiplyV = pool[compound].concentration
                pool[compound]['Quantification'] = multiplyV * pool[compound].loc[:, responseRead]#, axis = 1)

    resultCompounds = [[] for item in range(len(dfsResponse))]
    for compound in fcStatus:
        for poolNum in range(len(dfsResponse)):
            if (compound in dfsResponse[poolNum] and (fcStatus[compound] == 'i' or fcStatus[compound] == 'e')):
                resultCompounds[poolNum].append(compound)

    filesNumIndex = []
    filesLetterIndex = []
    masterIndex = []
    filesIndex = []
    for poolNum in range(len(dfsResponse)):
        tempList = dfsID[poolNum][IDRead].values.tolist()
        for item in tempList:
            if (item[0] not in masterIndex and item not in standardList):
                masterIndex.append(item[0])
                value = dfsFiles[poolNum].at[item[0], filesRead[0]]
                if (type(value) == type('str')):
                    filesIndex.append(value)
                elif (type(value[0]) == type('str')):
                    filesIndex.append(value[0])
                number = [i for i in (filesIndex[-1].split('_')[-1]) if i.isnumeric()]
                number = int(''.join(number))
                if(number not in filesNumIndex):
                    filesNumIndex.append(number)
                else:
                    filesNumIndex.append(number+10000)

                # letter = [i for i in (filesIndex[-1].split('_')[-1]) if i.isalpha()]
                # letter = str(''.join(letter))
                filesLetterIndex.append(0)  # str(checkIsIn(item[0], sortKeys))

    filesNumIndex, filesIndex, masterIndex, filesLetterIndex = zip(
        *sorted(zip(filesNumIndex, filesIndex, masterIndex, filesLetterIndex)))

    sampleNames = [str(filesIndex[i]+'_'+masterIndex[i]) for i in range(
        len(masterIndex))]
    data = {'Sample': sampleNames}
    for pool in range(len(resultCompounds)):
        for compound in resultCompounds[pool]:
            tempList = []
            for set in masterIndex:
                if set in dfsResponse[pool][compound]['Quantification']:
                    tempList.append(dfsResponse[pool][compound][
                        'Quantification'][set])
                else:
                    tempList.append("NaN")
            data[compound] = tempList

    dfReturn = pd.DataFrame(data=data)
    append_df_to_excel(mPath, dfReturn, sheet_name='Output', startrow=1)
