## Python Project


### Install Local

udo systemctl restart gunicorn

```sh

// Crea un entorno virtual:

python3 -m venv myenv
source myenv/bin/activate

// Instala Flask:
pip install Flask

// Prueba la aplicación: Ejecuta el archivo app.py para probarlo localmente.
// Run server
python app.py



//****** Export by server requeriments
//--- Create file Requerimets (local)
pip freeze > requirements.txt

//--- Para el Server (Plesk)
pip3 install -r requirements.txt

```




## Install Server (Servidor Plesk)

```sh

// Instala los requirimientos:
pip install -r requirements.txt

// Luego:
pip install Flask
pip install gunicorn



// PLESK Servidor - WSGI (es el que tengo que buscar)
// Configurar en Dominio -> Apache & nginx Settings -> Additional directives for HTTPS. El servicio se ejecutará con Apache y escribir:

...
<Location "/">
	ProxyPass http://localhost:8000/
	ProxyPassReverse http://localhost:8000/
</Location>
...


// Luego para iniciar el servidor (solo para probar)
gunicorn app:app


// importate: se agrego Gunicorn como un servicio con systemd

sudo nano /etc/systemd/system/gunicorn.service
...
[Unit]
Description=Gunicorn instance to serve python.splytin.com
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/vhosts/splytin.com/python.splytin.com
ExecStart=/var/www/vhosts/splytin.com/python.splytin.com/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
...


sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn

// y para los cambios
sudo systemctl restart gunicorn


```




