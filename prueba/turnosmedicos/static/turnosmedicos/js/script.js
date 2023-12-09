const $d = document;
const $selectprovincias = $d.getElementById("selectprovincias");
const $selectmunicipios = $d.getElementById("selectmunicipios");
const $selectlocalidades = $d.getElementById("selectlocalidades");

function provincia() {
    fetch("https://apis.datos.gob.ar/georef/api/provincias")
    .then(res => res.ok ? res.json() : Promise.reject(res))
    .then(json => {
        let $options = `<option value="Elige una provincia">Elige una provincia</option>`;
        json.provincias.forEach(el => $options += `<option value="${el.nombre}">${el.nombre}</option>`);
        $selectprovincias.innerHTML = $options;
    })
    .catch( error => {
        let message = error.statusText || "Ocurrió un error al conectar";
        $selectprovincias.nextElementSibling.innerHTML = 'Error: ${error.status}: ${message}';
    })
}
$d.addEventListener("DOMContentLoaded", provincia)

function municipio(provincia) {
   
   fetch(`https://apis.datos.gob.ar/georef/api/municipios?provincia=${provincia}`)
        .then(res => res.ok ? res.json() : Promise.reject(res))
        .then(json => {
            let $options = `<option value="Elige un municipio">Elige un municipio</option>`;
            json.municipios.forEach(el => $options += `<option value="${el.id}">${el.nombre}</option>`);
            $selectmunicipios.innerHTML = $options;

        })
        .catch( error => {
            let message = error.statusText || "Ocurrió un error al conectar";
            $selectmunicipios.nextElementSibling.innerHTML = 'Error: ${error.status}: ${message}';
    })
}
$selectprovincias.addEventListener("change", e =>{
    municipio(e.target.value);
    console.log(e.target.value)
})
function localidad(municipio) {
    fetch(`https://apis.datos.gob.ar/georef/api/localidades?municipio=${municipio}`)
        .then(res => res.ok ? res.json() : Promise.reject(res))
        .then(json => {
            let $options = `<option value="Elige una ciudad">Elige una ciudad</option>`;
            json.localidades.forEach(el => $options += `<option value="${el.id}">${el.nombre}</option>`);
            $selectlocalidades.innerHTML = $options;

        })
        .catch( error => {
            let message = error.statusText || "Ocurrió un error al conectar";
            $selectlocalidades.nextElementSibling.innerHTML = 'Error: ${error.status}: ${message}';
    })
}
$selectmunicipios.addEventListener("change", e =>{
    localidad(e.target.value);
    console.log(e.target.value)
})