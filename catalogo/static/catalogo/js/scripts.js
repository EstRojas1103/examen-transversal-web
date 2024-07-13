document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is working!');

    // Validación de formularios
    $('#searchForm').on('submit', function(event) {
        if (!this.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
            alert('Por favor, completa el campo de búsqueda.');
        }
        this.classList.add('was-validated');
    });

    // Funcion "Ver más"
    $('.ver-mas').on('click', function() {
        // Mostrar alerta 
        Swal.fire({
            title: 'No hay información por el momento',
            text: 'Vuelve a intentarlo más tarde.',
            icon: 'info'
        });
    });
});
