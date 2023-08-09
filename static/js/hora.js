function actualizarHora() {
    const divHora = document.querySelector('.msg-info-time');
    const fechaActual = new Date();
    const hora = fechaActual.getHours().toString().padStart(2, '0');
    const minutos = fechaActual.getMinutes().toString().padStart(2, '0');
    const horaActual = `${hora}:${minutos}`;
    divHora.textContent = horaActual;
}

// Llamar a la función al cargar la página y luego cada minuto
window.onload = function() {
    actualizarHora();
    setInterval(actualizarHora, 60000); // Actualizar cada minuto
};