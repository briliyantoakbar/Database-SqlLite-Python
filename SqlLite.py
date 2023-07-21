# import sqlite3
# data={"aku":"DODIO"}
# nama=data["aku"]
# kontak=data["aku"]
# conn=sqlite3.connect("databast.db")
# cursor=conn.cursor()
# put='DODIO'
# put1="DIOU"
# i=0

# cursor.execute("DELETE FROM KONTAK WHERE NAMA='DODO'")
#cursor.execute("UPDATE KONTAK SET NAMA=?,NOMOR=? WHERE NOMOR=?",(put1,put1,put))
# cursor.execute("UPDATE KONTAK SET NAMA ="+ put+"WHERE NAMA = DODIO")
# cursor.execute("INSERT INTO KONTAK VALUES(nama,kontak)")
# conn.commit()
# conn.close()
#UPDATE KONTAK SET NAMA='JONO' WHERE ID="1"
# INSERT INTO KONTAK (NAMA,NOMOR) VALUES ("NANA", "555-777");



from fastapi import Body, FastAPI,UploadFile, File, Request, Form
from fastapi.responses import FileResponse
from secrets import token_hex
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import sqlite3
app = FastAPI()
import sqlite3
# data={"aku":"DODO"}
# nama=data["aku"]
# kontak=data["aku"]
conn=sqlite3.connect("databast.db",check_same_thread=False)
cursor=conn.cursor()
# data={"aku":"koe"}

# print(data["aku"])
@app.post("/tambah")
def tambaH(payload: dict=Body(...)):
    return{"sukses"}
@app.post("/tambahkontak")
def tambah_post(payload: dict=Body(...)):
    print(type(payload))
    nama=payload['NAMA']
    nomor=payload['NOMOR']
    lis=[]
    conn=sqlite3.connect("databast.db",check_same_thread=False)
    cursor=conn.cursor()
    cursor.execute("INSERT INTO KONTAK VALUES (?,?)",(nama,nomor))
    conn.commit()
    # conn.close()
    data=conn.execute('SELECT * FROM KONTAK')
    for i in data:
            print(i[1])
            dicenery={"username":i[0],"nomor":i[1]}
            lis.append(dicenery)
    return {"status":"sukses","kontak":lis}

@app.post("/hapuskontak")
def hapus_post(payload: dict=Body(...)):
    conn=sqlite3.connect("databast.db",check_same_thread=False)
    cursor=conn.cursor()
    nama=payload['NAMA']
    lis=[]
    cursor=conn.cursor()
    cursor.execute("DELETE FROM KONTAK WHERE NAMA=?",(nama,))
    conn.commit()
    data=conn.execute('SELECT * FROM KONTAK')
    for i in data:
            print(i[1])
            dicenery={"username":i[0],"nomor":i[1]}
            lis.append(dicenery)
    return {"status":"sukses","kontak":lis}

@app.post("/editkontak")
def edit_post(payload: dict=Body(...)):
    conn=sqlite3.connect("databast.db",check_same_thread=False)
    cursor=conn.cursor()
    namalama=payload['NAMALama']
    namabaru=payload['NAMABaru']
    kontakbaru=payload['KONTAKBaru']
    cursor.execute("UPDATE KONTAK SET NAMA=?,NOMOR=? WHERE NAMA=?",(namabaru,kontakbaru,namalama))
    conn.commit()
    lis=[]
    data=conn.execute('SELECT * FROM KONTAK')
    for i in data:
            print(i[1])
            dicenery={"username":i[0],"nomor":i[1]}
            lis.append(dicenery)
    return {"status":"sukses","kontak":lis}

@app.post("/tampilkontak")
def tampil_post(payload: dict=Body(...)):
    lis=[]
    conn=sqlite3.connect("databast.db",check_same_thread=False)
    cursor=conn.cursor()
    getkontak=payload['getkontak']
    if(getkontak=="cekdata"):
        data=conn.execute('SELECT * FROM KONTAK')
        for i in data:
            print(i[1])
            dicenery={"username":i[0],"nomor":i[1]}
            lis.append(dicenery)
        print(lis)
     #conn.close()
    return {"status":"sukses","kontak":lis}
