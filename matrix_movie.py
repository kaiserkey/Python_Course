import time, os

text = "*****************************************************"
text_space = " "

os.system("mpg123 sound.mp3")
print(f"\n\n{text_space*30}\033[1;32mMATRIX\033[0m".center(45))
time.sleep(2)
print(f"\n\033[1;32m{text_space*5}{text}\033[0m".center(45))
time.sleep(2)
print(f"\n\n{text_space*10}\033[1;34mNeo: ¿Qué es la Matrix? ¿Control?\n\033[0m".center(45))
time.sleep(3)
print(f"{text_space*10}\033[1;31mMorpheus:La Matrix es una simulación virtual de la realidad, \n{text_space*10}un vasto programa informático que controla el pensamiento \n{text_space*10}y las acciones de cada uno de nosotros.\n\033[0m".center(45))
time.sleep(5)
print(f"{text_space*10}\033[1;34mNeo: ¿Quién la controla?\n\033[0m".center(45))
time.sleep(5)
print(f"{text_space*10}\033[1;31mMorpheus: Las máquinas. A lo largo de los años se han \n{text_space*10}desarrollado inteligencias artificiales más complejas \n{text_space*10}y poderosas que los humanos...\n\033[0m".center(45))
time.sleep(5)
print(f"{text_space*10}\033[1;34mNeo: ¿Y para qué?\n\033[0m".center(40))
time.sleep(4)
print(f"{text_space*10}\033[1;31mMorpheus: Para controlar nuestra realidad. \n{text_space*10}Para mantenernos en un estado de inconsciencia \n{text_space*10}y así poder explotarnos como fuente de energía.\n\033[0m".center(45))
time.sleep(4)
print(f"\n\033[1;32m{text_space*5}{text}\033[0m".center(45))
time.sleep(2)
print(f"\n\n{text_space*20}\033[1;32mFin de la película.\n\033[0m".center(40))
os.system("mpg123 sound.mp3")