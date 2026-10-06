import streamlit as st
from datetime import datetime, timedelta

# Configuración estética de la aplicación móvil
st.set_page_config(page_title="SUPER LIMPIAS S.A.S.", page_icon="🏢", layout="centered")

st.markdown("""
    <style>
    .report-box {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28A745;
        margin-bottom: 15px;
    }
    .title-box {
        color: #1E3A8A;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏢 SUPER LIMPIAS S.A.S.")
st.subheader("Programa de Conservación 5 Años (60 Meses)")
st.markdown("---")

# Sección 1: Parámetros de Entrada
st.markdown("### 📋 Parámetros de Inspección")
nombre_edificio = st.text_input("Nombre de la Copropiedad:", "Edificio Cayena")

col1, col2 = st.columns(2)
with col1:
    perimetro = st.number_input("Perímetro (Metros):", min_value=1.0, value=50.0, step=1.0)
with col2:
    altura = st.number_input("Altura / Pisos (Metros):", min_value=1.0, value=15.0, step=1.0)

tipo_fachada = st.selectbox(
    "Componente Constructivo Dominante:", 
    ["Mixta (Ladrillo/Pintura)", "Tecnológica (Vidrio/Alucobond)"]
)

# Lógica matemática y financiera
area_bruta = perimetro * altura
tarifa_m2 = 35000 if tipo_fachada == "Mixta (Ladrillo/Pintura)" else 14000
mes_lavado_ciclo = 18 if tipo_fachada == "Mixta (Ladrillo/Pintura)" else 12

costo_restauracion = area_bruta * tarifa_m2
fee_mensual = (costo_restauracion * 0.05) / 12

# Resultados en pantalla
st.markdown("---")
st.markdown("### 📊 Viabilidad Económica")
st.success(f"### 💰 FEE RECURRENTE: $ {fee_mensual:,.2f} COP / mes")
st.caption("Contrato a término de 60 meses. Valores netos sin AIU.")

# Sección 2: Cronograma Visual de 5 Años
st.markdown("---")
st.markdown("### 📅 Cronograma Maestro Corporativo (60 Meses)")
st.markdown("Despliegue cada año para revisar las actividades programadas frente al cliente:")

fecha_inicio = datetime.now()

# Ciclo de años
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
            <h5 class="title-box">🧗 DISPONIBILIDAD DE DESCUELGUES (Anual)</h5>
            <p>• <b>Bolsa de Horas Técnicas:</b> Cuadrilla certificada en alturas disponible para intervenciones puntuales de sellamiento de fisuras o juntas críticas reportadas por el dron o por emergencias de filtración.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Lógica de lavados recurrentes cada 18 meses (para mixtas) o 12 meses (tecnológicas)
        meses_totales_anio = list(range((anio-1)*12 + 1, anio*12 + 1))
        for m in meses_totales_anio:
            if m % mes_lavado_ciclo == 0:
                f_lavado = fecha_inicio + timedelta(days=m * 30)
                st.markdown(f"""
                <div class="report-box" style="border-left-color: #28A745;">
                    <h5 class="title-box">🧼 MES {m} — {f_lavado.strftime('%B %Y').upper()} | Hito Estético</h5>
                    <p>• <b>Lavado Parcial Programado:</b> Limpieza mecánica a presión con detergentes neutros en las zonas con mayor exposición a la contaminación, polución y humedad.</p>
                </div>
                """, unsafe_allow_html=True)

# Sección 3: Generación del Documento para Descarga
cronograma_completo_txt = f"""====================================================================
   PLAN DE CONSERVACIÓN PREVENTIVA A 5 AÑOS (60 MESES)
   SUPER LIMPIAS S.A.S. - PROPIEDAD HORIZONTAL COLOMBIA
====================================================================

COPROPIEDAD: {nombre_edificio}
ÁREA DE FACHADA BRUTA: {area_bruta:,.2f} m2
FEE MENSUAL ACORDADO: $ {fee_mensual:,.2f} COP / mes
DURACIÓN CONTRACTUAL: 60 Meses (5 Años)

--------------------------------------------------------------------
MATRIZ RECURRENTE DE ALCANCES Y HITOS TÉCNICOS:
--------------------------------------------------------------------
1. MONITOREO AVANZADO (Cada 12 meses): Inspección visual gráfica con Dron 
   y entrega de Reporte de Salud al Consejo de Administración.
2. CONTROL HIDRÁULICO (Cada 12 meses): Sondeo, limpieza y desatasco técnico 
   de bajantes de aguas lluvias.
3. BOLSA DE DESCUELGUES EN DISPONIBILIDAD: Acceso prioritario a cuadrillas 
   en alturas para sellado puntual de fisuras ante reportes o emergencias.
4. LAVADO PARCIAL PROGRAMADO (Cada {mes_lavado_ciclo} meses): Limpieza mecánica focalizada 
   de las zonas de alta exposición a hollín y hongos (Zonas críticas).

--------------------------------------------------------------------
DOCUMENTO EMITIDO POR SUPER LIMPIAS S.A.S. — BOGOTÁ, COLOMBIA
"""

st.markdown("---")
st.download_button(
    label="📥 Guardar Reporte Maestro 60 Meses en el Celular",
    data=cronograma_completo_txt,
    file_name=f"Plan_60_Meses_{nombre_edificio.replace(' ', '_')}.txt",
    mime="text/plain",
    use_container_width=True
)

