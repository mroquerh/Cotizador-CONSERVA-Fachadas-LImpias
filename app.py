import streamlit as st
from datetime import datetime, timedelta

# Configuración de la página móvil
st.set_page_config(page_title="SUPER LIMPIAS S.A.S.", page_icon="🚀", layout="centered")

# Encabezado corporativo
st.title("🚀 SUPER LIMPIAS S.A.S.")
st.subheader("Sistema Móvil de Cotización y Conservación")
st.markdown("---")

st.markdown("### 📋 Datos del Edificio")

# Inputs diseñados para tocar fácil desde la pantalla del celular
nombre_edificio = st.text_input("Nombre del Edificio / Cliente:", "Edificio Cayena")
perimetro = st.number_input("Perímetro del Edificio (Metros lineales):", min_value=1.0, value=50.0, step=1.0)
altura = st.number_input("Altura / Pisos (Metros totales):", min_value=1.0, value=15.0, step=1.0)
tipo_fachada = st.selectbox("Tipo de Estructura Constructiva:", ["Mixta (Ladrillo/Pintura)", "Tecnológica (Vidrio/Alucobond)"])

# Ingeniería matemática comercial de tu modelo de negocio
area_bruta = perimetro * altura

if tipo_fachada == "Mixta (Ladrillo/Pintura)":
    tarifa_m2 = 35000
    mes_lavado = 18  # Frecuencia optimizada para ladrillo/pintura
else:
    tarifa_m2 = 14000
    mes_lavado = 12  # Fachada tecnológica se lava más seguido (vidrio/aluminio)

costo_restauracion = area_bruta * tarifa_m2
fee_mensual = (costo_restauracion * 0.05) / 12

st.markdown("---")
st.markdown("### 📊 Proyección Económica")

# Cuadros de resultados visuales en el celular
st.info(f"**Área de Fachada Calculada:** {area_bruta:,.2f} m²")
st.warning(f"**Costo Restauración de Referencia:** $ {costo_restauracion:,.2f} COP")
st.success(f"**💰 FEE MENSUAL SUGERIDO: $ {fee_mensual:,.2f} COP / mes**")

# Automatización del cronograma con fechas reales de calendario (Colombia)
fecha_inicio = datetime.now()
fecha_dron = fecha_inicio + timedelta(days=90)      # Mes 3
fecha_bajantes = fecha_inicio + timedelta(days=180)  # Mes 6
fecha_mitigacion = fecha_inicio + timedelta(days=365) # Mes 12
fecha_lavado = fecha_inicio + timedelta(days=mes_lavado * 30)

# Construcción limpia del texto para el archivo final
cronograma_texto = f"""====================================================================
   CRONOGRAMA DE OPERACIONES PREVENTIVAS - SUPER LIMPIAS S.A.S.     
====================================================================

EDIFICIO / COPROPIEDAD: {nombre_edificio}
TIPO DE FACHADA: {tipo_fachada}
ÁREA EXPUESTA CALCULADA: {area_bruta:,.2f} m2
FEE MENSUAL ACORDADO (Sujeto a IPC): $ {fee_mensual:,.2f} COP / mes
FECHA DE ACTIVACIÓN DE SUSCRIPCIÓN: {fecha_inicio.strftime('%d/%m/%Y')}

--------------------------------------------------------------------
PROGRAMACIÓN AUTOMÁTICA DE HITOS TÉCNICOS (SLA INCLUIDO):
--------------------------------------------------------------------

[*] MES 3 - {fecha_dron.strftime('%m/%Y')}:
    -> Primer monitoreo avanzado con Dron y mapeo fotográfico de fisuras.
    -> Entrega del Reporte Digital de Salud de Fachada a la Administración.

[*] MES 6 - {fecha_bajantes.strftime('%m/%Y')}:
    -> Sondeo mecánico, limpieza profunda y desatasco de bajantes críticas.
    -> Inspección preventiva de sellos en perfiles de ventanas.

[*] MES 12 (Anual) - {fecha_mitigacion.strftime('%m/%Y')}:
    -> Descuelgue técnico puntual enfocado en zonas de alto riesgo.
    -> Sellado y emboquillado inmediato de microfisuras detectadas.

[*] HITO DE RENOVACIÓN ESTÉTICA - {fecha_lavado.strftime('%m/%Y')}:
    -> Ejecución del Lavado General Mecánico de toda la superficie (Mes {mes_lavado}).
    -> Remoción de hollín, hongos y carga contaminante sin uso de ácidos.

--------------------------------------------------------------------
NOTA: Este cronograma es el entregable formal que el administrador
puede anexar a sus informes de gestión para el Consejo y la Asamblea.
"""

st.markdown("---")
# Botón nativo para descargar el archivo de texto directo en la carpeta "Descargas" del celular
st.download_button(
    label="📥 Descargar Cronograma .TXT en Celular",
    data=cronograma_texto,
    file_name=f"Cronograma_{nombre_edificio.replace(' ', '_')}.txt",
    mime="text/plain",
    use_container_width=True
)
