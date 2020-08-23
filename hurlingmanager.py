#hello world
#why am i doing this
#woah this source code is cool
import cmd
import textwrap
import sys
import random
import time
#tactic and variables
#title screen and beginning shit
print ("GAELIC GAMES MANAGER 2020: FOOTBALL by Murray Man")
answer = input("What team would you like to be?")
if answer == "London":
    confirm = input("Are you sure you would like to be London? (y/n)")
    if confirm == "y":
        print ("MAIN MENU")
        print("---------")
        print ("simulate")
        menu = input("TYPE IN A COMMAND TO PERFORM IT")
        if menu == "simulate":
            print("CONNACHT FOOTBALL TOURNAMENT 2020 QF London vs Roscommon")
            rcomn20 = input("WHAT TACTICS WOULD YOU LIKE TO USE? (man mark/swarm)")
            if rcomn20 == "man mark":
                    print("YOU WON")
                    time.sleep(5)
                    print("MAIN MENU")
                    print("---------")
                    print("simulate")
                    menuw1 = input("TYPE IN A COMMAND TO PERFORM IT")
                    if menuw1 == "simulate":
                        print("CONNACHT FOOTBALL TOURNAMENT 2020 SF London vs Mayo")
                        mayo20 = input("WHAT TEAM TALK WOULD YOU LIKE TO GIVE? (passionate/aggressive/underdog mentality)")
                        if mayo20 == "passionate":
                            print("YOU WON")
                            time.sleep(5)
                            print("MAIN MENU")
                            print("---------")
                            print("simulate")
                            print("train")
                            train = input ("YOU CAN TRAIN YOUR TEAM WITH THE 'train' command")
                            #lowkeythowhydid i do this, its very unoptimised and not good code lol help me
                            if train == "train":
                                print("YOUR TEAM'S OVERALL HAS INCREASED BY 5")
                                time.sleep(2)
                                print("---------")
                                print("MAIN MENU")
                                print("---------")
                                print("simulate")
                                print("----------")
                                sligo20 = input("TYPE IN A COMMAND TO PERFORM IT")
                                if sligo20 == "simulate":
                                    print("CONNACHT FOOTBALL TOURNAMENT 2020 FINAL")
                                    final20 = input("WHAT TACTICS DO YOU WANT TO IMPLEMENT? (constant pressure/zonal marking")
                                    f20 = input("WHAT TEAM TALK WOULD YOU LIKE TO GIVE? passionate (proud and slightly aggressive)/aggressive (screaming at the lads)")
                                    tips20 = input("ANY LAST MINUTE POINTERS? have fun/full throttle")
                                    if tips20 == "full throttle":
                                        print("YOU WON. COMHGHAIRDEAS! YOU ARE NOW IN THE IRISH CUP SEMI FINALS")
                                        time.sleep(5)
                                        print("MAIN MENU")
                                        print("---------")
                                        print("simulate")
                                        print("----------")
                                        kerry20 = input("TYPE IN A COMMAND TO PERFORM IT")
                                        if kerry20 == "simulate":
                                            print("IRISH CUP 2020 SEMI FINAL")
                                            sf20 = input("WHAT TACTICS DO YOU WANT TO IMPLEMENT (attack)? conservative/fast/aggressive")
                                            if sf20 == "conservative":
                                                print("YOU WON, YOU ADVANCE ONTO THE IRISH CUP FINAL!")
                                                time.sleep(0.5)
                                                print("YOUR TEAM'S OVERALL HAS INCREASED BY 10 OVERALL AS A RESULT OF THE PAST GAME AND TRAINING SESSION")
                                                time.sleep(5)
                                                print("MAIN MENU")
                                                print("---------")
                                                print("simulate")
                                                print("----------")
                                                dub20 = input("TYPE IN A COMMAND TO PERFORM IT")
                                                if dub20 == "simulate":
                                                    print("IRISH CUP 2020 FINAL")
                                                    aif20 = input("WHAT ATTACKING TACTICS WOULD YOU LIKE TO IMPLETENT? conservative/fast")
                                                    if aif20 == "conservative":
                                                        aifdef20 = input("WHAT DEFENDING TACTICS WOULD YOU LIKE TO IMPLETENT? conservative/aggressive")
                                                        if aifdef20 == "aggressive":
                                                            aiftalkx = input("WHAT TYPE OF TEAM TALK WOULD YOU LIKE TO GIVE? passionate/aggressive")
                                                            if aiftalkx == "passionate":
                                                                print("COMHGHAIRDEAS! YOU HAVE WON THE IRISH CUP!")
                                                            else:
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")
                                                        else:
                                                            aiftalk = input("WHAT TYPE OF TEAM TALK WOULD YOU LIKE TO GIVE? passionate/aggressive")
                                                            if aiftalk == "passionate":
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")
                                                            else:
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")

                                                    else:
                                                        aifdefx20 = input("WHAT DEFENDING TACTICS WOULD YOU LIKE TO IMPLETENT? conservative/aggressive")
                                                        if aifdefx20 == "aggressive":
                                                            aiftalkxx = input("WHAT TYPE OF TEAM TALK WOULD YOU LIKE TO GIVE? passionate/aggressive")
                                                            if aiftalkxx == "passionate":
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")
                                                            else:
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")
                                                        else:
                                                            aiftalkxxx = input(
                                                                "WHAT TYPE OF TEAM TALK WOULD YOU LIKE TO GIVE? passionate/aggressive")
                                                            if aiftalkxxx == "passionate":
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")
                                                            else:
                                                                print("COMMISERATIONS, YOU HAVE LOST THE IRISH CUP FINAL")

                                            else:
                                                print("YOU HAVE LOST THE IRISH CUP SEMI FINAL")

                                        else:
                                            print("Unlucky, You Lost! Restart the Game and Try Again.")

                                    else:
                                        print("UNLUCKY, YOU LOST. GOOD LUCK NEXT YEAR")
                                        nextyear21 = input("WOULD YOU LIKE TO CONTINUE UNTIL NEXT YEAR (y/n)")
                                        if nextyear21 == "y":
                                            print("WOAH, WELL AREN'T YOU FAST? OR ELSE YOU GOT KNOCKED OUT IN THE 1ST ROUND. WHATEVER IT MAY BE, THE 2ND SEASON ISN'T FINISHED QUITE JUST YET. FEEL FREE TO RESTART THE GAME. SLÁN GO FOILL AND GOOD LUCK!")




                        else:
                            print("YOU LOST. RESTART AND TRY AGAIN UNTIL WE ADD MORE SEASONS")
                            #m20loss = input("WOULD YOU LIKE TO SIMULATE TO NEXT SEASON? (y/n)")
                            #if m20loss == "y":
                             #   print("MAIN MENU")
                            #print("simulate")
                    #else:
                     #   print("Your time as the manager of London is over. You can now exit and close the game")

            else:
                print ("YOU LOST. RESTART AND TRY AGAIN UNTIL WE ADD MORE SEASONS")
                #rcomloss = input("WOULD YOU LIKE TO SIMULATE TO NEXT SEASON? (y/n)")
                #if rcomloss == "y":
                    #print("MAIN MENU")
                    #print("simulate")
                #else:
                    #print("Your time as the manager of London is over. You can now exit and close the game")

    else:
        print ("Restart game and pick another team")


else:
    print ("Team Invalid")