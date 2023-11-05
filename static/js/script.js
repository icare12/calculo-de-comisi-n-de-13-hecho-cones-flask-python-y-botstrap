document.getElementById('commissionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var nombre = document.getElementById('nombre').value;
    var ventas = document.getElementById('ventas').value;
    var comision = Math.round(ventas * 13 / 100 * 100) / 100;
    document.getElementById('result').textContent = `Hola ${nombre}, tus comisiones de este mes son de $${comision}`;
});
