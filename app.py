import streamlit as st

# 1. Configuración de la página web
st.set_page_config(page_title="Capturador de Datos", page_icon="📊")
st.title("📋 Sistema Web de Captura de Datos")
st.write("Introduce la información en el formulario y descárgala en formato CSV.")

# 2. Inicializar la base de datos en la memoria de la página web
if "lista_usuarios" not in st.session_state:
    st.session_state.lista_usuarios = []

# 3. Crear el formulario web de captura
with st.form("formulario_registro", clear_on_submit=True):
    nombre = st.text_input("Nombre completo:")
    correo = st.text_input("Correo electrónico:")
    ciudad = st.text_input("Ciudad:")
    escuela = st.text_input("Escuela:")
    
    boton_guardar = st.form_submit_button("Registrar Usuario")

# 4. Lógica al presionar el botón
if boton_guardar:
    if nombre and correo and ciudad and escuela:  # Validamos que ninguno esté vacío
        nuevo_usuario = {"Nombre": nombre, "Correo": correo, "Ciudad": ciudad, "Escuela": escuela}
        st.session_state.lista_usuarios.append(nuevo_usuario)
        st.success(f"¡{nombre} ha sido registrado con éxito!")
    else:
        st.error("⚠️ Por favor, rellena todos los campos antes de guardar.")

# 5. MOSTRAR DATOS Y DESCARGAR (Versión Ultra-Segura sin Numpy)
if st.session_state.lista_usuarios:
    st.subheader("👥 Usuarios Registrados Temporalmente")
    
    # En lugar de usar st.write() con la lista entera (que activa Numpy),
    # mostramos cada usuario de forma individual usando texto simple en pantalla
    for idx, u in enumerate(st.session_state.lista_usuarios, start=1):
        st.text(f"👤 Usuario #{idx} -> Nombre: {u['Nombre']} | Correo: {u['Correo']} | Ciudad: {u['Ciudad']} | Escuela: {u['Escuela']}")
    
    # Construimos el archivo CSV manualmente línea por línea
    csv_lineas = ["Nombre,Correo,Ciudad,Escuela"]  # Encabezados
    for u in st.session_state.lista_usuarios:
        n = u["Nombre"].replace(",", " ")
        c = u["Correo"].replace(",", " ")
        ci = u["Ciudad"].replace(",", " ")
        e = u["Escuela"].replace(",", " ")
        csv_lineas.append(f"{n},{c},{ci},{e}")
        
    csv_final = "\n".join(csv_lineas).encode('utf-8')
    
    st.markdown("---") # Una línea divisoria visual
    # Botón web de descarga
    st.download_button(
        label="📥 Descargar datos en formato CSV (Excel)",
        data=csv_final,
        file_name="usuarios_web.csv",
        mime="text/csv"
    )
