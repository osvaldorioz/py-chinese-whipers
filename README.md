### **Algoritmo Chinese Whispers**

**Chinese Whispers** es un algoritmo de **clustering no supervisado basado en grafos**, que se utiliza para detectar comunidades o grupos dentro de datos estructurados en forma de red.

### **¿Cómo funciona?**
1. **Inicialización:**  
   - Se asigna una etiqueta única a cada nodo del grafo.

2. **Iteraciones (Propagación de etiquetas):**  
   - Se recorren los nodos en orden aleatorio.
   - Cada nodo adopta la etiqueta más frecuente entre sus vecinos.
   - Se repite este proceso durante varias iteraciones hasta que la estructura se estabiliza.

3. **Finalización:**  
   - Los nodos que comparten la misma etiqueta forman un cluster.

### **¿Para qué se usa?**
- **Procesamiento de lenguaje natural (PLN):** Agrupación de entidades similares en textos.  
- **Redes sociales:** Detección de comunidades en grafos de relaciones.  
- **Análisis de fraude:** Identificación de grupos sospechosos en transacciones.  
- **Biología y genética:** Agrupación de proteínas o genes similares.  

El método es rápido y escalable, ya que funciona en tiempo cercano a **O(n log n)**. 🚀
