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
        print ("[ 1 ] windows/DDoS/payload")
        print ("-------------------------------------------------------")
        wellcome()
    if text == 1:
        option = input("lina >> type the ip: ")
        option2 = input("Lina >> type the port: ")
        
        wellcome()
        
wellcome()