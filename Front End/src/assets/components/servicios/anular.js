export const anular = (urlBase, id_categoria) => {
    const url = `${urlBase}${id_categoria}`;
    return fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ estado: 0 }), // Aquí es donde pasas el estado a 0
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
