#precision hawk'in urettigi datanin pix4d'nin istedigi formata getirilmesi
#5 tane resmin adinin tek bir resmin adi haline getirmektedir.

x = raw_input("Please enter output file name :")

file = open("telemetry.dat","r")
lines =file.readlines()
file.close()

count = 0
content = []

fo = open(x+".txt","wb")
fo.write("image name;longitude;lattude;altitude"+"\n")

for line in lines:
    count = count + 1
    if count >=3:
        begin = line.find("IMG_")
        end = line.find("_1.tif")
        image_name = line[begin:end]+".tif"
        #print image_name
        appendList =[]
        line = line.replace('\t',';')
        line = line.replace(';;',';')
        line = line.replace(' ',';')
        
        new_list = line.split(";")
        appendList.append(image_name)
        appendList.append(new_list[3])
        appendList.append(new_list[4])
        appendList.append(new_list[5])
        data_line = ";".join(appendList)
        fo.write(data_line+"\n")
fo.close()
