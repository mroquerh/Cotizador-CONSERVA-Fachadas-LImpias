import streamlit as st
from datetime import datetime, timedelta

# 1. Configuración estética de la pestaña del navegador
st.set_page_config(page_title="FACHADAS LIMPIAS CONSERVA", page_icon="🛡️", layout="centered")

# 2. Inyección de estilos visuales y etiquetas para el celular
LOGOTIPO_EMPRESA_URL = "https://i.postimg.cc/CK75HXjy/Logo-circular-de-Fachadas-Limpiasak_r.png"

st.markdown(f"""
    <head>
        <link rel="apple-touch-icon" href="{LOGOTIPO_EMPRESA_URL}">
        <link rel="icon" type="image/png" href="{LOGOTIPO_EMPRESA_URL}">
        <meta name="apple-mobile-web-app-image" content="{LOGOTIPO_EMPRESA_URL}">
    </head>
    <style>
    .report-box {{
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28A745;
        margin-bottom: 15px;
    }}
    .title-box {{
        color: #1E3A8A;
        font-weight: bold;
    }}
    .subbrand-text {{
        color: #555555;
        font-size: 14px;
        font-style: italic;
        margin-top: -15px;
        margin-bottom: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# 3. Encabezado con tu nueva estructura de marca solicitada
st.title("🏢 FACHADAS LIMPIAS CONSERVA")
st.markdown('<p class="subbrand-text">SUPER LIMPIAS SAS / NIT 900.533.282-2</p>', unsafe_allow_html=True)
st.subheader("Programa de Conservación 5 Años (60 Meses)")
st.markdown("---")

# Inicialización de variables de sesión para el reinicio limpio
if "edificio" not in st.session_state:
    st.session_state.edificio = ""
if "perimetro" not in st.session_state:
    st.session_state.perimetro = 50.0
if "altura" not in st.session_state:
    st.session_state.altura = 15.0

# Botón técnico para limpiar la simulación anterior
if st.button("🧹 Limpiar y Nueva Cotización", use_container_width=True):
    st.session_state.edificio = ""
    st.session_state.perimetro = 50.0
    st.session_state.altura = 15.0
    st.rerun()

st.markdown("---")

# Sección 1: Parámetros de Entrada
st.markdown("### 📋 Parámetros de Inspección")
nombre_edificio = st.text_input("Nombre de la Copropiedad:", key="edificio")

col1, col2 = st.columns(2)
with col1:
    perimetro = st.number_input("Perímetro (Metros):", min_value=1.0, step=1.0, key="perimetro")
with col2:
    altura = st.number_input("Altura / Pisos (Metros):", min_value=1.0, step=1.0, key="altura")

tipo_fachada = st.selectbox(
    "Componente Constructivo Dominante:", 
    ["Mixta (Ladrillo/Pintura)", "Tecnológica (Vidrio/Alucobond)"]
)

# CONSTANTE DE PISO FINANCIERO ESTABLECIDA EN $140.000 COP
BASE_MINIMA_FEE = 140000.0

# Ingeniería matemática y financiera
area_bruta = perimetro * altura
tarifa_m2 = 35000 if tipo_fachada == "Mixta (Ladrillo/Pintura)" else 14000
mes_lavado_ciclo = 18 if tipo_fachada == "Mixta (Ladrillo/Pintura)" else 12

costo_restauracion = area_bruta * tarifa_m2
fee_calculado = (costo_restauracion * 0.05) / 12

# Aplicación automática de la Base Mínima
es_tarifa_minima = False
if fee_calculado < BASE_MINIMA_FEE:
    fee_final = BASE_MINIMA_FEE
    es_tarifa_minima = True
else:
    fee_final = fee_calculado

# Resultados en pantalla
st.markdown("---")
st.markdown("### 📊 Viabilidad Económica")

if es_tarifa_minima:
    st.warning(f"### 💰 FEE RECURRENTE: $ {fee_final:,.2f} COP / mes")
    st.caption("⚠️ *Nota: Se está aplicando la Tarifa Mínima Base de \$140.000 COP para estructuras pequeñas.*")
else:
    st.success(f"### 💰 FEE RECURRENTE: $ {fee_final:,.2f} COP / mes")
    st.caption("Tarifa estándar calculada bajo el modelo del 5% anualizado.")

st.caption("Contrato a término de 60 meses. Valores netos sin AIU. Reajustable con el IPC anual.")

# Sección 2: Cronograma Visual de 5 Años
st.markdown("---")
st.markdown("### 📅 Cronograma Maestro Corporativo (60 Meses)")

fecha_inicio = datetime.now()

for anio in range(1, 6):
    with st.expander(f"📅 AÑO {anio} (Meses {(anio-1)*12 + 1} al {anio*12})"):
        f_dron = fecha_inicio + timedelta(days=365 * (anio - 1) + 90)
        f_bajantes = fecha_inicio + timedelta(days=365 * (anio - 1) + 180)
        
        st.markdown(f"""
        <div class="report-box" style="border-left-color: #4285F4;">
            <h5 class="title-box">📸 MES {(anio-1)*12 + 3} — {f_dron.strftime('%B %Y').upper()}</h5>
            <p>• <b>Monitoreo con Dron:</b> Mapeo fotográfico de alta resolución para detección temprana de fisuras y fallas en sellos.</p>
            <p>• <b>Entregable:</b> Reporte de Salud de Fachada para el Consejo de Administración.</p>
        </div>
        
        <div class="report-box" style="border-left-color: #FFBB00;">
            <h5 class="title-box">💧 MES {(anio-1)*12 + 6} — {f_bajantes.strftime('%B %Y').upper()}</h5>
            <p>• <b>Control Hidráulico:</b> Sondeo mecánico, limpieza profunda y desatasco de bajantes críticas de aguas lluvias.</p>
        </div>
        
        <div class="report-box" style="border-left-color: #EA4335;">
            <h5 class="title-box">🧗 BOLSA DE DESCUELGUES (2 por Semestre)</h5>
            <p>• <b>Disponibilidad Controlada:</b> Acceso a un máximo de dos (2) descuelgues técnicos puntuales por semestre para sellado de fisuras críticas o emergencias.</p>
            <p>• <b>Condición Contractual:</b> Cupos semestrales estrictamente <u>no acumulables</u> para garantizar la ejecución preventiva continua.</p>
        </div>
        """, unsafe_allow_html=True)
        
        meses_totales_anio = list(range((anio-1)*12 + 1, anio*12 + 1))
        for m in meses_totales_anio:
            if m % mes_lavado_ciclo == 0:
                f_lavado = fecha_inicio + timedelta(days=m * 30)
                st.markdown(f"""
                <div class="report-box" style="border-left-color: #28A745;">
                    <h5 class="title-box">🧼 MES {m} — {f_lavado.strftime('%B %Y').upper()} | Hito Estético</h5>
                    <p>• <b>Lavado Parcial Programado:</b> Limpieza mecánica a presión con detergentes neutros en las zonas con mayor exposición a la contaminación.</p>
                </div>
                """, unsafe_allow_html=True)

# Sección 3: Generación del Documento para Descarga
nombre_seguro = nombre_edificio if nombre_edificio else "Nueva_Copropiedad"
cronograma_completo_txt = f"""====================================================================
   PLAN DE CONSERVACIÓN PREVENTIVA A 5 AÑOS (60 MESES)
   FACHADAS LIMPIAS CONSERVA — PROPIEDAD HORIZONTAL COLOMBIA
   Soporte Corporativo: SUPER LIMPIAS SAS / NIT 900.533.282-2
====================================================================

COPROPIEDAD: {nombre_seguro}
ÁREA DE FACHADA BRUTA: {area_bruta:,.2f} m2
FEE MENSUAL ACORDADO: $ {fee_final:,.2f} COP / mes {"(Tarifa Minima Base)" if es_tarifa_minima else ""}
DURACIÓN CONTRACTUAL: 60 Meses (5 Años)

--------------------------------------------------------------------
MATRIZ RECURRENTE DE ALCANCES Y HITOS TÉCNICOS:
--------------------------------------------------------------------
1. MONITOREO AVANZADO (Cada 12 meses): Inspección visual gráfica con Dron.
2. CONTROL HIDRÁULICO (Cada 12 meses): Sondeo, limpieza y desatasco de bajantes.
3. BOLSA DE DESCUELGUES DE MITIGACIÓN: Disponibilidad de hasta dos (2) descuelgues 
   técnicos por semestre. Cupos NO acumulables entre periodos.
4. LAVADO PARCIAL PROGRAMADO (Cada {mes_lavado_ciclo} meses): Limpieza mecánica focalizada 
   de zonas críticas de alta exposición.

--------------------------------------------------------------------
DOCUMENTO EMITIDO POR SUPER LIMPIAS S.A.S. — BOGOTÁ, COLOMBIA
"""

st.markdown("---")
st.download_button(
    label="📥 Guardar Reporte Maestro 60 Meses en el Celular",
    data=cronograma_completo_txt,
    file_name=f"Plan_60_Meses_{nombre_seguro.replace(' ', '_')}.txt",
    mime="text/plain",
    use_container_width=True
)

