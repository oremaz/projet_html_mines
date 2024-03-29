// tournaments.js

// Fonction pour récupérer et afficher les données du JSON
function displayTournaments() {
    fetch('chemin/vers/votre/fichier.json')
        .then(response => response.json())
        .then(data => {
            var atp250Data = data.atp250;
            var mymap = L.map('map-container').setView([46.6031, 1.7192], 5);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(mymap);

            atp250Data.forEach(tournament => {
                var coordinates = tournament.coordinates;
                var date = tournament.date_debut + " - " + tournament.date_fin;
                L.marker(coordinates).addTo(mymap).bindPopup('ATP 250 Tournoi - Dates : ' + date);
            });

            var masters1000Coordinates = data.masters1000.coordinates;
            var masters1000Date = data.masters1000.date;
            var masters1000 = L.marker(masters1000Coordinates).addTo(mymap).bindPopup('Masters 1000 - Rolex Paris Masters<br>Dates : ' + masters1000Date);

            var grandSlamCoordinates = data.grandSlam.coordinates;
            var grandSlamDate = data.grandSlam.date;
            var grandSlam = L.marker(grandSlamCoordinates).addTo(mymap).bindPopup('Grand Chelem - Roland Garros<br>Dates : ' + grandSlamDate);
        })
        .catch(error => console.error('Erreur lors de la récupération des données JSON :', error));
}

// Appel de la fonction pour afficher les tournois
displayTournaments();
