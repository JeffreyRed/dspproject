import datetime
import os.path


def data_log(text):
    if os.path.isfile('myfile.txt'):
        f = open("myfile.txt", "a")
        x = datetime.datetime.now()
        f.write(str(x)+"  "+ text +"\r")
        f.close()
    else:
        f = open("myfile.txt", "w")
        x = datetime.datetime.now()
        f.write(str(x)+"  "+ text +"\r")
        f.close()