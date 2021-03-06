// load the contents of the window, all listeners here
// https://www.w3schools.com/js/js_arrow_function.asp
window.addEventListener('load', ()=>{
    resize();
    document.addEventListener('mousedown', startPainting);
    document.addEventListener('mouseup', stopPainting);
    document.addEventListener('mousemove', sketch);
    window.addEventListener('resize', resize);
    document.getElementById("clear-canvas").addEventListener("click", clearCanvas);
    document.getElementById("submit").addEventListener("click", submitCanvas);
})

const canvas = document.querySelector('#canvas')

// a context helps to indentify what type of redering is required
// https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext
const ctx = canvas.getContext('2d')
ctx.strokeStyle="#FFF000";
ctx.canvas.width = 28;
ctx.canvas.height = 28;

// we can improve the resize with a box around
function resize() {
    ctx.strokeRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function clearCanvas() {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

// intialise
let coord = {x: 0, y: 0};
let paint = false;

// https://www.w3schools.com/jsref/obj_mouseevent.asp
function getPosition(event) {
    coord.x = event.clientX - canvas.offsetLeft;
    coord.y = event.clientY - canvas.offsetTop;
}

function startPainting(event) {
    paint = true;
    getPosition(event);
}

// param event can be supplied, however, it is not required/ used in this function thus not supplied
function stopPainting() {
    paint = false;
}

// triggered when event for mousemove is detected
function sketch(event) {
    if (!paint)
        return;

    ctx.beginPath();
    ctx.linewidth = 5;
    ctx.lineCap = 'round';

    // start from this coordinate
    ctx.moveTo(coord.x, coord.y);

    // get the new coordinate
    getPosition(event);

    // trace a line to the new coordinate (from the start coordinate)
    ctx.lineTo(coord.x, coord.y);

    // actually draw the line
    ctx.stroke();
}

function clearCanvas() {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    ctx.strokeRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    document.getElementById("result").innerText = "";
}

function submitCanvas() {
    let img = ctx.getImageData(0, 0, ctx.canvas.width, ctx.canvas.height);

    fetch('submitted_image', {
        method: 'POST',
        headers: new Headers({'content-type': 'application/json'}),
        body: JSON.stringify({"pixel_values": img})
    }).then(
        function(response) { return response.text(); }
    ).then(
        function(text) {
            console.log("Post request: ");
            console.log(text);
            document.getElementById("result").innerText = text;
        }
    )
}
