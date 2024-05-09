// api.js
export const enviarDatosCategorias = async (datos) => {
  try {
    const respuesta = await fetch('http://127.0.0.1:5000/crear_categoria', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(datos)
    });

    if (!respuesta.ok) {
      throw new Error('Error al enviar los datos');
    }

    const datosRespuesta = await respuesta.json();
    return datosRespuesta;
  } catch (error) {
    console.error('Hubo un error:', error);
  }
};
