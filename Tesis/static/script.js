const $canvas = document.querySelector("#canvas");
const $btnGuardar = document.querySelector("#btnGuardar");
const imgConverted = document.querySelector("#imgConverted");
const $btnLimpiar = document.querySelector("#btnLimpiar");
    

const contexto = $canvas.getContext("2d");
const COLOR_PINCEL = "black";
const COLOR_FONDO = "#D5D4D8";
const GROSOR = 2;
let xAnterior = 0, yAnterior = 0, xActual = 0, yActual = 0;
const obtenerXReal = (clientX) => clientX - $canvas.getBoundingClientRect().left;
const obtenerYReal = (clientY) => clientY - $canvas.getBoundingClientRect().top;
let haComenzadoDibujo = false;


$canvas.addEventListener("mousedown", evento => {
    // En este evento solo se ha iniciado el clic, así que dibujamos un punto
    xAnterior = xActual;
    yAnterior = yActual;
    xActual = obtenerXReal(evento.clientX);
    yActual = obtenerYReal(evento.clientY);
    contexto.beginPath();
    contexto.fillStyle = COLOR_PINCEL;
    contexto.fillRect(xActual, yActual, GROSOR, GROSOR);
    contexto.closePath();
    // Y establecemos la bandera
    haComenzadoDibujo = true;
});

$canvas.addEventListener("mousemove", (evento) => {
    if (!haComenzadoDibujo) {
        return;
    }
    // El mouse se está moviendo y el usuario está presionando el botón, así que dibujamos todo

    xAnterior = xActual;
    yAnterior = yActual;
    xActual = obtenerXReal(evento.clientX);
    yActual = obtenerYReal(evento.clientY);
    contexto.beginPath();
    contexto.moveTo(xAnterior, yAnterior);
    contexto.lineTo(xActual, yActual);
    contexto.strokeStyle = COLOR_PINCEL;
    contexto.lineWidth = GROSOR;
    contexto.stroke();
    contexto.closePath();
});
["mouseup", "mouseout"].forEach(nombreDeEvento => {
    $canvas.addEventListener(nombreDeEvento, () => {
        haComenzadoDibujo = false;
    });
});

const limpiarCanvas = () => {
    // Colocar color blanco en fondo de canvas
    contexto.fillStyle = COLOR_FONDO;
    contexto.fillRect(0, 0, $canvas.width, $canvas.height);
};
limpiarCanvas();
$btnLimpiar.onclick = limpiarCanvas;

$btnGuardar.onclick = async () => {
    // Convertir la imagen a Base64 y ponerlo en el enlace
    const data = $canvas.toDataURL("image/png");
    const fd = new FormData();
    fd.append("imagen", data); // Se llama "imagen", en PHP lo recuperamos con $_POST["imagen"]
    const respuestaHttp = await fetch("views.py", {
        method: "POST",
        body: fd,
    });
    const nombreImagenSubida = await respuestaHttp.json();
    console.log("La imagen ha sido enviada y tiene el nombre de: " + nombreImagenSubida);
};


// empieza segunda firma

const $canvas2 = document.querySelector("#canvas2"),
    $btnLimpiar2 = document.querySelector("#btnLimpiar2");

const contexto2 = $canvas2.getContext("2d");
const COLOR_PINCEL2 = "black";
const COLOR_FONDO2 = "#D5D4D8";
const GROSOR2 = 2;
let xAnterior2 = 0, yAnterior2 = 0, xActual2 = 0, yActual2 = 0;
const obtenerXReal2 = (clientX) => clientX - $canvas2.getBoundingClientRect().left;
const obtenerYReal2 = (clientY) => clientY - $canvas2.getBoundingClientRect().top;
let haComenzadoDibujo2 = false;

$canvas2.addEventListener("mousedown", evento => {
    // En este evento solo se ha iniciado el clic, así que dibujamos un punto
    xAnterior2 = xActual2;
    yAnterior2 = yActual2;
    xActual2 = obtenerXReal2(evento.clientX);
    yActual2 = obtenerYReal2(evento.clientY);
    contexto2.beginPath();
    contexto2.fillStyle = COLOR_PINCEL2;
    contexto2.fillRect(xActual2, yActual2, GROSOR2, GROSOR2);
    contexto2.closePath();
    // Y establecemos la bandera
    haComenzadoDibujo2 = true;
});

$canvas2.addEventListener("mousemove", (evento) => {
    if (!haComenzadoDibujo2) {
        return;
    }
    // El mouse se está moviendo y el usuario está presionando el botón, así que dibujamos todo

    xAnterior2 = xActual2;
    yAnterior2 = yActual2;
    xActual2 = obtenerXReal2(evento.clientX);
    yActual2 = obtenerYReal2(evento.clientY);
    contexto2.beginPath();
    contexto2.moveTo(xAnterior2, yAnterior2);
    contexto2.lineTo(xActual2, yActual2);
    contexto2.strokeStyle = COLOR_PINCEL2;
    contexto2.lineWidth = GROSOR2;
    contexto2.stroke();
    contexto2.closePath();
});
["mouseup", "mouseout"].forEach(nombreDeEvento => {
    $canvas2.addEventListener(nombreDeEvento, () => {
        haComenzadoDibujo2 = false;
    });
});

const limpiarCanvas2 = () => {
    // Colocar color blanco en fondo de canvas
    contexto2.fillStyle = COLOR_FONDO2;
    contexto2.fillRect(0, 0, $canvas2.width, $canvas2.height);
};
limpiarCanvas2();
$btnLimpiar2.onclick = limpiarCanvas2;



