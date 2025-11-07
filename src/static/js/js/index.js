document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("calc-form");
    if (!form) return;

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const peso = parseFloat(document.getElementById("peso").value);
        const alturaCm = parseFloat(document.getElementById("altura").value);

        if (isNaN(peso) || isNaN(alturaCm)) return;

        const altura = alturaCm / 100;
        const imc = peso / (altura * altura);
        const imcFixado = imc.toFixed(2);

        document.getElementById("valor-imc").textContent = imcFixado;
        document.getElementById("peso-val").textContent = peso;
        document.getElementById("altura-val").textContent = alturaCm;

        const classificacao = document.getElementById("classificacao");
        let classe = "";
        let texto = "";

        if (imc < 18.5) {
            classe = "magreza";
            texto = "Magreza";
        } else if (imc < 24.9) {
            classe = "normal";
            texto = "Normal";
        } else if (imc < 29.9) {
            classe = "sobrepeso";
            texto = "Sobrepeso";
        } else {
            classe = "obesidade";
            texto = "Obesidade";
        }

        classificacao.className = "status " + classe;
        classificacao.textContent = texto;

        // Peso ideal
        const pesoIdeal = 22 * (altura * altura);
        document.getElementById("peso-ideal").textContent = pesoIdeal.toFixed(2);

        // Mover o marcador
        const marcador = document.getElementById("marcador");
        let pos = 0;

        if (imc < 18.5) pos = (imc / 18.5) * 25;
        else if (imc < 25) pos = 25 + ((imc - 18.5) / 6.4) * 25;
        else if (imc < 30) pos = 50 + ((imc - 25) / 5) * 25;
        else pos = 75 + ((imc - 30) / 10) * 25;

        marcador.style.left = `${Math.min(95, Math.max(0, pos))}%`;
    });
});




    