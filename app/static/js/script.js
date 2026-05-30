// Proyecto Maní - Sistema IoT
console.log("Proyecto Maní iniciado");

async function cargarDatos() {

    try {

        const response = await fetch("/api/datos");

        const datos = await response.json();

        const menuToggle = document.getElementById("menu-toggle");

        const menu = document.getElementById("menu");

        menuToggle.addEventListener("click", () => {

            menu.classList.toggle("active");

        });

        document.querySelectorAll("#menu a").forEach(link => {

            link.addEventListener("click", () => {

                menu.classList.remove("active");

            });

        });

        document.getElementById("temp").innerText =
            datos.temperatura + " °C";

        document.getElementById("temp_horno").innerText =
            datos.temperatura_horno + " °C";

        document.getElementById("humedad").innerText =
            datos.humedad_grano + " %";

        document.getElementById("extractor").innerText =
            datos.extractor;

        document.getElementById("calefactor").innerText =
            datos.calefactor;

    } catch (error) {

        console.error(error);
    }
}

setInterval(cargarDatos, 2000);

cargarDatos();