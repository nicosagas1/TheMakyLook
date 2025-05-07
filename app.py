from flask import Flask, render_template, url_for, request
from mail_config import enviar_correo
import os
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import quote
load_dotenv()

app = Flask(__name__)
app.secret_key = '7772428b-01cf-4d05-9c3e-cea510398586'

@app.route("/")
@app.route("/inicio")
def inicio():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("index.html")

@app.route("/nosotros")
def nosotros():
    return render_template("index.html")

@app.route("/galeria")
def galeria():
    return render_template("index.html")

@app.route("/testimonios")
def testimonios():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    return render_template("index.html")

@app.route("/reservar-cita", methods=['POST'])
def reservarCita():
    print("llego Reservar cita")

    if request.method == 'POST':
        nombre_original = request.form.get('nombre', '')
        email = request.form.get('correo', '')
        telefono = request.form.get('telefono', '')
        servicio_original = request.form.get('servicio', '')
        fecha_str = request.form.get('fecha', '')  # formato esperado: 'YYYY-MM-DD'
        hora = request.form.get('hora', '')
        asunto = "Cita solicitada ❗❗"
        
        destinatario = os.getenv('CORREO_ORIGEN') 

        # Reemplazo de espacios por %
        nombre_encoded = quote(nombre_original)
        servicio_encoded = quote(servicio_original)
        

        # Conversión de fecha al formato Día % MesNombre
        try:
            fecha_dt = datetime.strptime(fecha_str, '%Y-%m-%d')
            dia = fecha_dt.day
            mes_nombre = fecha_dt.strftime('%B')  # mes en inglés
            # Si lo quieres en español, puedes mapearlo manualmente:
            meses_es = {
                'January': 'enero', 'February': 'febrero', 'March': 'marzo',
                'April': 'abril', 'May': 'mayo', 'June': 'junio',
                'July': 'julio', 'August': 'agosto', 'September': 'septiembre',
                'October': 'octubre', 'November': 'noviembre', 'December': 'diciembre'
            }
            mes_nombre_es = meses_es[mes_nombre]
            fecha_formateada = f"{dia}%{mes_nombre_es}"
            fecha_encoded = quote(fecha_formateada)
        except ValueError:
            fecha_formateada = fecha_str  # si falla el parseo, deja la fecha original

        # Construcción del mensaje
        mensaje = f"Correo Electrónico: {email}\n"
        mensaje += f"Nombre y Apellido: {nombre_original}\n"
        
        whatsapp_directo = f"https://wa.me/{telefono}?text=Hola%20{nombre_encoded}%20me%20ha%20llegado%20una%20solicitud%20de%20cita%20para%20el%20servicio%20de%20{servicio_encoded}%20el%20dia%20{fecha_encoded}%20a%20las%20{hora}"

        
        mensaje += f"Enviar mensaje al cliente: {whatsapp_directo}\n"
        mensaje += f"Servicio solicitado: {servicio_original}\n"
        mensaje += f"Fecha: {fecha_str}\n"
        mensaje += f"Hora: {hora}\n"

        #print(mensaje)
        enviar_correo(destinatario, asunto, mensaje, None)
        aviso = "Nos ha llegado tu mensaje ✔, ya nos comunicaremos con usted."
        return render_template("index.html", aviso=aviso)
 

if __name__ == '__main__':
    app.run()