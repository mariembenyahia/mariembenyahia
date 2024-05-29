
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-id');
            if (confirm('Êtes-vous sûr de vouloir supprimer cet utilisateur ?')) {
                fetch(`/delete-user/${userId}`, {
                    method: 'DELETE',
                })
                .then(response => {
                    if (response.ok) {
                        location.reload(); // Recharger la page après la suppression
                    } else {
                        alert('Erreur lors de la suppression de l\'utilisateur.');
                    }
                });
            }
        });
    });
});

