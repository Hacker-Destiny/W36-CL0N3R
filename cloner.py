print("######################################")
print("##	 	   	𝕎 𝟛𝟞-ℂ𝕝𝟘ℕ𝟛ℝ	  		    ##")
print("## 	Tool owner- Ayush Kumar Jha 	##")
print("##		Give credit.....	       	##")
print("######################################")
print("")

from pywebcopy import save_webpage
from os import system, name
from time import sleep

kwargs = {'project_name': 'site folder'}

save_webpage(

    # url pf the website
    url=input("enter the url to clone (copy & paste)//  "),

    # folder where the copy will be saved
    project_folder='F:/website/',
    **kwargs)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


sleep(2)

clear()

print("######################################")
sleep(2)
print("##	 	   	𝕎 𝟛𝟞-ℂ𝕝𝟘ℕ𝟛ℝ	  		    ##")
sleep(2)
print("######################################")
sleep(2)
print("")
sleep(2)
print("PLACE WHERE YOUR FILE SAVED IS : F:/website/")
sleep(2)
print("THANKS FOR USING THIS TOOL")
