// tournaments.js

// Fonction pour afficher les tournois sur la carte
function displayTournaments() {
    // Définition de la carte et de son centre
    var mymap = L.map('map').setView([46.6031, 1.7192], 5);

    // Ajout de la couche de tuiles OpenStreetMap à la carte
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(mymap);


    // Masters 1000 - Rolex Paris Masters
    var masters1000Coordinates = [48.8566, 2.3509]; // Exemple de coordonnées (Paris, France)
    var masters1000Date = "2024-10-28 - 2024-11-03"; // Exemple de dates
    var masters1000 = L.marker(masters1000Coordinates).addTo(mymap).bindPopup('Masters 1000 - Rolex Paris Masters<br>Dates : ' + masters1000Date);

    // Grand Chelem - Roland Garros
    var grandSlamCoordinates = [48.8398, 2.2519]; // Exemple de coordonnées (Paris, France)
    var grandSlamDate = "2024-05-26 - 2024-06-09"; // Exemple de dates
    var grandSlam = L.marker(grandSlamCoordinates).addTo(mymap).bindPopup('Grand Chelem - Roland Garros<br>Dates : ' + grandSlamDate);
}

// Appel de la fonction pour afficher les tournois
displayTournaments();

