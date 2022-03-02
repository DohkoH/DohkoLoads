import pytube
import os

class youtube():

    def __init__(self,link,path="",file_extension="mp4",type="audio"):
        if path=="":
            self.path=os.getcwd()
        else:
            self.path=path
        self.extension=file_extension
        self.type=type
        try:
            self.videoyt=pytube.YouTube(link)
        except:
            print("Falta el url del video o direccion incompleta.")
            
    def Descarga(self):
        if self.type=="audio":
            progressive=False
        else:
            progressive=True
        try:
            lista=self.videoyt.streams.filter(progressive=progressive,type=self.type,file_extension=self.extension)
        except:
            return
        stream=lista[-1]
        stream.download(self.path)
        print("Descarga Terminada.")
    
    def titulo(self):
        try:
            return str(self.videoyt.title)
        except:
            print("No hay objeto creado.")

