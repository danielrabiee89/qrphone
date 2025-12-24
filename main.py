from fastapi import FastAPI,Response
from Model import Phone
import qrcode
from io import BytesIO

app=FastAPI()


@app.post("/add")
def add(number:int):
    pish=0
    p=Phone.create(Phone_number=number)
    data=f"tel:{pish}{number}".strip()
    img=qrcode.make(data)
    img.save("qrphone.png")

    im=BytesIO
    img.save(im,format="PNG")
    im.seek(0)

    return Response(content=im.read(),media_type="img/png")




