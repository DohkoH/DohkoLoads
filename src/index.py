from flask import Flask,render_template,request,send_file
import You2be
import os,shutil

app=Flask(__name__)

PATH_FILE_AUDIO=os.getcwd()+"/Descarga/Musica/"
PATH_FILE_VIDEO=os.getcwd()+"/Descarga/Video/"
file_extension="mp4"

@app.route("/")
def home():
    if os.path.isdir(PATH_FILE_AUDIO):
        shutil.rmtree(PATH_FILE_AUDIO)
    if os.path.isdir(PATH_FILE_VIDEO):
        shutil.rmtree(PATH_FILE_VIDEO)
    return render_template("index.html")
   
@app.route("/Descargar")
def descargar_al_servidor():
    url=request.args.get('urlVideo')
    tipo=request.args.get('tipo_input').lower()
    if tipo=="audio":
        PATH_FILE=PATH_FILE_AUDIO
    elif tipo=="video":
        PATH_FILE=PATH_FILE_VIDEO
    multimedia=You2be.youtube(path=PATH_FILE,link=url,file_extension=file_extension,type=tipo)
    multimedia.Descarga()
    nombre=multimedia.titulo()+"."+file_extension

    return send_file(PATH_FILE+nombre,as_attachment=True)
    
if __name__=="__main__":
    app.run(debug=True)