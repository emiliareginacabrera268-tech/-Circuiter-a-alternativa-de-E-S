import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ampliamos considerablemente la figura para dar espacio vertical y horizontal
fig, ax = plt.subplots(figsize=(16, 11))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Función auxiliar para dibujar cajas con control de tamaño y fuente
def draw_box(x, y, width, height, text, bg_color="#D4E6F1", text_color="#1B4F72", fontsize=8.5):
    box = patches.FancyBboxPatch((x, y), width, height, 
                                 boxstyle="round,pad=0.5", 
                                 facecolor=bg_color, 
                                 edgecolor=text_color, 
                                 linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, 
            horizontalalignment='center', 
            verticalalignment='center', 
            fontsize=fontsize, fontweight='bold', 
            color=text_color, wrap=True)

# Función para conectar nodos con flechas limpias
def draw_arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#566573", shrinkA=4, shrinkB=4))

# --- MAPA CONCEPTUAL AMPLIADO: CIRCUITERÍA ALTERNATIVA DE E/S ---

# 1. Nodo Principal (Raíz)
draw_box(30, 85, 40, 10, "CIRCUITERÍA ALTERNATIVA DE E/S\n(Entrada y Salida en Sistemas Embebidos)", bg_color="#AED6F1", text_color="#154360", fontsize=9.5)

# 2. Ramas Principales (Nivel 1) - Espaciadas equitativamente en X (de 3 a 78)
draw_box(3, 62, 21, 9, "1. Sensores y Transductores\n(Entrada)", bg_color="#A9DFBF", text_color="#145A32", fontsize=9)
draw_box(27, 62, 21, 9, "2. Actuadores de Control\n(Salida)", bg_color="#F9E79F", text_color="#7D6608", fontsize=9)
draw_box(51, 62, 21, 9, "3. Interfaces de Comunicación\n(Bus de Datos)", bg_color="#F5B7B1", text_color="#78281F", fontsize=9)
draw_box(75, 62, 22, 9, "4. Acondicionamiento\ny Conversión", bg_color="#D7BDE2", text_color="#512E5F", fontsize=9)

# Conexiones de Raíz a Nivel 1
draw_arrow(50, 85, 13.5, 71)
draw_arrow(50, 85, 37.5, 71)
draw_arrow(50, 85, 61.5, 71)
draw_arrow(50, 85, 86, 71)

# 3. Sub-nodos Detallados (Nivel 2) - Posicionados abajo con altura suficiente para evitar cruces
# 1. Sensores
draw_box(2, 22, 22.5, 36, 
         "• Sensores Analógicos:\n"
         "  - Fotorresistencias (LDR)\n"
         "  - Termistores (NTC/PTC)\n"
         "  - Potenciómetros\n"
         "• Sensores Digitales:\n"
         "  - Pulsadores y Switches\n"
         "  - Sensores Táctiles\n"
         "• Detección y Presencia:\n"
         "  - Infrarrojos (PIR / CNY70)\n"
         "  - Ultrasonido (HC-SR04)", 
         bg_color="#EAFAF1", text_color="#196F3D", fontsize=8)
draw_arrow(13.5, 62, 13.5, 58)

# 2. Actuadores
draw_box(26.2, 22, 22.5, 36, 
         "• Control de Movimiento:\n"
         "  - Motores DC y Servos\n"
         "  - Motores a Pasos (Stepper)\n"
         "• Potencia y Conmutación:\n"
         "  - Relés electromecánicos\n"
         "  - Transistores MOSFET\n"
         "• Interfaz Humano / Salida:\n"
         "  - Buzzers y Altavoces\n"
         "  - Displays LCD / OLED\n"
         "  - Matriz de LEDs", 
         bg_color="#FEF9E7", text_color="#7D6608", fontsize=8)
draw_arrow(37.5, 62, 37.5, 58)

# 3. Interfaces de Comunicación
draw_box(50.5, 22, 22.5, 36, 
         "• Protocolos Síncronos:\n"
         "  - I2C (2 hilos: SDA/SCL)\n"
         "  - SPI (Master / Slave)\n"
         "• Protocolos Asíncronos:\n"
         "  - UART (Tx / Rx)\n"
         "  - RS-232 / RS-485\n"
         "• Expansión de Puertos:\n"
         "  - Multiplexores (MUX/DEMUX)\n"
         "  - Expansores de pines I/O\n"
         "  - Protocolo 1-Wire", 
         bg_color="#FDEDEC", text_color="#78281F", fontsize=8)
draw_arrow(61.5, 62, 61.5, 58)

# 4. Acondicionamiento
draw_box(74.5, 22, 23.5, 36, 
         "• Conversión de Señales:\n"
         "  - ADC (Analógico a Digital)\n"
         "  - DAC (Digital a Analógico)\n"
         "• Procesamiento Analógico:\n"
         "  - Amplificadores Operacionales\n"
         "  - Filtros Activos y Pasivos\n"
         "• Protección y Aislamiento:\n"
         "  - Optoacopladores\n"
         "  - Diodos de libre circulación\n"
         "  - Control por PWM", 
         bg_color="#F4ECF7", text_color="#512E5F", fontsize=8)
draw_arrow(86, 62, 86, 58)

# Títulos del gráfico
plt.title("Mapa Conceptual: Circuitería Alternativa de E/S", fontsize=15, fontweight='bold', pad=25)
plt.suptitle("Arquitectura Avanzada de Entradas, Salidas, Interfaces y Acondicionamiento en Sistemas Electrónicos", fontsize=10, color='#566573', y=0.93)

plt.tight_layout()
plt.show()