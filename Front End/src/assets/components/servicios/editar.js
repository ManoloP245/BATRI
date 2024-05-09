export const enviarDatosCategorias = async (datos, id_categoria) => {
    try {
      const respuesta = await fetch(`http://127.0.0.1:5000/editar_categoria/${id_categoria}`, {
        method: 'PUT',
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
