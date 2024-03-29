// script.js

document.addEventListener("DOMContentLoaded", function () {
    const projectsList = document.getElementById("projects-list");

    fetch("https://api.github.com/orgs/ue12-p23/repos?per_page=all")
        .then(response => response.json())
        .then(data => {
            data.forEach(project => {
                const listItem = document.createElement("li");
                listItem.innerHTML = `
                    <h3>${project.name}</h3>
                    <p>Langage: ${project.language}</p>
                    <p>Description: ${project.description}</p>
                    <a href="${project.html_url}" target="_blank">Lien vers le projet</a>
                `;
                projectsList.appendChild(listItem);
            });
        })
        .catch(error => console.error(error));
});
