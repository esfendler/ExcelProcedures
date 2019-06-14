import re
import sys, os

d = {}
output = []
originaltext = r"C:\\Users\esf\Desktop\ExcelviaPython\AsReceived.txt"
codes = r"C:\\Users\esf\Desktop\ExcelviaPython\FinalizedCodes.txt"

with open("C:\\Users\esf\Desktop\ExcelviaPython\Crosswalk.txt") as f:
    for line in f:
       (key, val) = line.split("\t")
       d[key] = val.strip()


with open (originaltext) as OT:
    counter = 0
    for line in OT:
        finalline = []
        counter += 1
        if line == '\n':
            finalline = ""
            output.append(finalline)
        else:
            Originallinelist = line.split(";")
            for Originalline_element in Originallinelist:
                if Originalline_element == '':
                    continue
                else:

                    element = d.get(Originalline_element.strip())
                    if element != "":
                        finalline.append(element)
            try:
                finalline = ";".join(finalline)
                output.append(finalline)
            except Exception as e:
                print("error on line", counter,"\n", line)




with open(codes, "a") as out_file:
    for finalline in output:
        #finalline = "; ".join(finalline)
        #record_fields = record.split()

        out_file.write('%s\n' % finalline)
