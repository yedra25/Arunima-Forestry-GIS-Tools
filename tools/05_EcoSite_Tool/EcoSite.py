fc = arcpy.GetParameterAsText(0)
ECOField = arcpy.GetParameterAsText(1)
BeginWith = ECOField[0:3]
import arcpy

# re is a built in python module which search specific text
import re
NewField = [BeginWith+"Geo", BeginWith+"EcoNu",BeginWith+"Vege",BeginWith+"Depth",BeginWith+"Moist",BeginWith+"Chem",BeginWith+"Class",BeginWith+"EcoKey"]
depValue = ["R","S","VS","M","D","MD"]
moisValue = ["d","f","h","m","s","v","w","x"]
chemValue = ["a","b","k","n","z"]
classValue = ["Tt","cTt","oTt","sTt","Tl","sTl","St","sSt","Sl","sSl","H","sH","Nv","X"]
for field in NewField:
    arcpy.AddField_management(fc, field, "TEXT")
NewField.append(ECOField)

# fixed print brackets
print(NewField)
cursor = arcpy.da.UpdateCursor(fc,NewField)

error_count = 0
for row in cursor:
    if (row[8] is not None) and (row[8] != '') and (row[8].isspace() == False):
        row[0] = row[8][0]

        # searches for a pattern at the start of the text, looks for alphabetsand one or more numbers, row[8] has the originl ECO code so from B127 it picks' 127 and converts into an integer for calculations
        match = re.match(r"[A-Za-z](\d+)", row[8])
        if match:
            if len(match.group(1)) != 3:
                error_count = error_count + 1
                arcpy.AddWarning("Invalid Ecosite value: %s"%row[8])
            row[1] = match.group(1)
            
            # changed int(row[1]) to eco_num as assigned below for all the if and elif statements
            eco_num = int(row[1])
            row[7] = "2"
            
        # changed the bottom two lines from elif to if as if this finds a match then it will not run the other elif statments afterwads
        
            if eco_num <= 28:
                row[7] = "3"
                 
                
            elif eco_num <= 43:
                row[7] = "4"
            elif eco_num <= 59:
                row[7] = "5"
            elif eco_num <= 76:
                row[7] = "6"
            elif eco_num <= 92:
                row[7] = "7"
            elif eco_num <= 108:
                row[7] = "8"
            elif eco_num <= 125:
                row[7] = "9"
            elif eco_num <= 156:
                row[7] = "10"
            elif eco_num <= 188:
                row[7] = "11"
            elif eco_num <= 200:
                row[7] = "12a"
            elif eco_num <= 221:
                row[7] = "13"
            elif eco_num <= 224:
                row[7] = "10"
            else: 
                row[7] = "12b"
            if len(row[8]) > 4: 
                if row[8][4:] == "X":
                    row[2] = row[8][4:]
                else:
                    row[2] = row[8][4:6]
                    if len(row[8]) > 6:
                        for i in depValue:
                            if i in row[8][6:]:
                                row[3] = i
                        for i in moisValue:
                            if i in row[8][6:]:
                                row[4] = i
                        for i in chemValue:
                            if i in row[8][6:]:
                                row[5] = i
                        for i in classValue:
                            if i in row[8][6:]:
                                row[6] = i
            cursor.updateRow(row)

if error_count > 0:
    arcpy.AddWarning("Number of records with incorrect ecosite value: %s "%error_count)
del row
del cursor 
