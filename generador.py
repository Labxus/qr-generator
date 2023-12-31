import qrcode

def generar_codigo_qr(data, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="none")
    img.save(nombre_archivo)


if __name__ == "__main__":
    # Datos que deseas codificar en el QR
    datos = "https://linkcapriccio.netlify.app/"

    # Nombre del archivo donde se guardará el código QR (debe tener extensión .png)
    nombre_archivo = "codigo_qr.png"

    # Llamada a la función para generar el código QR
    generar_codigo_qr(datos, nombre_archivo)