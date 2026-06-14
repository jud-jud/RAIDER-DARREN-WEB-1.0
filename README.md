🛠️ RAIDER DARREN WEB 1.0 🛠️

🛠️ GUÍA MAESTRA DE CONFIGURACIÓN

🧱 1. PYTHON: Preparación del Entorno
Para que la interfaz web y la lógica del bot se ejecuten, necesitas instalar y preparar Python correctamente en tu sistema.

Descarga e Instalación:

Entra a la página oficial de Python.

Descarga Python 3.10 (o superior) asegurándote de elegir la versión de 64 bits (x86-64).

CRÍTICO: Al abrir el instalador, marca la casilla de abajo que dice "Add Python to PATH" antes de darle a Install Now. Si no haces esto, los comandos no funcionarán en tu consola.

Instalación de Librerías:

Abre la terminal de tu computadora (Escribe cmd en la barra de inicio de Windows y presiona Enter).

Escribe el siguiente comando para instalar todo lo necesario de golpe:

pip install -r requirements.txt

   * Deja la consola abierta para los siguientes pasos.

---

### 🌐 2. NGROK: Abriendo la Web a Internet
Herramienta necesaria para que tus amigos (por ejemplo, desde España) puedan entrar a tu panel de control local.

> 🌐 **PD: Debes tener el archivo `Page.py` iniciado para que esto funcione correctamente.**

1. **Creación de Cuenta:**
   * Regístrate gratis en la página oficial de [Ngrok](https://ngrok.com/).
   * Ve a tu panel de control (Dashboard) y copia tu **Authtoken** personal.
2. **Configuración en la Consola:**
   * Abre una ventana de comandos (CMD) y vincula tu cuenta ejecutando tu token limpio:
     ```bash
     ngrok config add-authtoken $AUTH_TOKEN
     ( **LO CONSIGUERAS EN "Your AuthToken" En ngrok** )
Lanzar el Túnel Público:

Una vez que tengas tu script Page.py corriendo en el puerto por defecto (8501), abre otra ventana de CMD diferente y arranca el túnel con el siguiente comando:

Bash
ngrok http 8501
   * En la pantalla aparecerá una línea llamada `Forwarding` con un enlace que termina en `.ngrok-free.dev`. **Ese es el enlace que debes pasarle a tu amigo.**

---

### 🤖 3. DISCORD: Configuración del Bot de Destrucción
El bot necesita los permisos de desarrollador adecuados para poder ejecutar acciones masivas en milisegundos sin ser rechazado de inmediato por la API.

1. **Crear la Aplicación:**
   * Ve al [Discord Developer Portal](https://discord.com/developers/applications).
   * Haz clic en **New Application**, ponle un nombre fachero y dale a crear.
2. **Activar los Privileged Gateway Intents (OBLIGATORIO):**
   * En el menú izquierdo, ve a la pestaña **Bot**.
   * Baja hasta encontrar la sección **Privileged Gateway Intents**.
   * **Activa las 3 casillas obligatoriamente:**
     * `Presence Intent`
     * `Server Members Intent`
     * `Message Content Intent`
   * Haz clic en **Save Changes** (Guardar Cambios).
3. **Obtener el Token:**
   * En esa misma pestaña de *Bot*, arriba del todo, haz clic en **Reset Token** y copia el código alfanumérico largo que te dará. *Ese es el Token que pegarás en la página web.*
4. **Invitar al Bot con Permisos:**
   * Ve a **OAuth2** -> **URL Generator**.
   * En la cuadrícula de *Scopes*, marca las casillas `bot` y `applications.commands`.
   * Abajo, en *Bot Permissions*, marca únicamente **Administrator** (Administrador).
   * Copia el enlace generado al final de la página, pégalo en tu navegador e invita al bot al servidor que vayas a usar para las pruebas.

---

### ⚡ 4. EXTRA: Reglas de Oro de Sincronización
Para asegurar el éxito total de la operación y evitar errores de conexión o pantallas congeladas, memoriza estas dos reglas fundamentales:

* **El Bot debe estar físicamente dentro del servidor objetivo:** El panel web es solo un control remoto; no hace magia. Si configuras la ID de un servidor en la web pero el bot no fue invitado previamente a ese servidor mediante el enlace de OAuth2, la herramienta lanzará un error en los logs diciendo que no se encontró el objetivo.
* **El orden de encendido con Ngrok es estricto:** Si planeas trabajar con tu amigo a distancia mediante Ngrok, el orden de ejecución debe ser siempre el siguiente:
  1. Abres y ejecutas tu archivo `Page.py` en tu computadora (con `python Page.py`).
  2. Una vez que veas que tu navegador local cargó la interfaz, abres la otra consola y ejecutas `ngrok http 8501`. 
  3. Si cierras la pestaña o la consola de `Page.py`, el enlace de Ngrok de tu amigo dejará de funcionar al instante dando un error `502 Bad Gateway`.
