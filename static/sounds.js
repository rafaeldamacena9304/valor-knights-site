document.addEventListener('DOMContentLoaded', () => {
    const hoverElement = document.querySelector('.hover-element');
    const hoverSound = document.getElementById('hover-sound');

    hoverElement.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const hoverElement = document.querySelector('.hover-element2');
    const hoverSound = document.getElementById('hover-sound2');

    hoverElement.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const hoverElement = document.querySelector('.hover-element2');
    const hoverSound = document.getElementById('hover-sound2');

    hoverElement.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const hoverElement = document.querySelector('.hover-element22');
    const hoverSound = document.getElementById('hover-sound22');

    hoverElement.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const hoverElement = document.querySelector('.hover-element22');
    const hoverSound = document.getElementById('hover-sound22');

    hoverElement.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const hoverElement = document.querySelector('.hover-element3');
    const hoverSound = document.getElementById('hover-sound3');

    hoverElement.addEventListener('mouseenter', () => {
        hoverSound.currentTime = 0;
        hoverSound.play();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const popup = document.getElementById('cookie-popup');
    const popupOkButton = document.getElementById('popup-ok');

    // Show the popup when the page loads
    popup.style.display = 'flex';

    // Hide the popup when the OK button is clicked
    popupOkButton.addEventListener('click', () => {
        popup.style.display = 'none';
    });
});

const clickElement = document.querySelector('.click-element');
const clickSound = document.getElementById('click-sound');
clickElement.addEventListener('click', () => {
    clickSound.currentTime = 0; // Rewind to the start
    clickSound.play();
});

const clickElement1 = document.querySelector('.click-element1');
const clickSound1 = document.getElementById('click-sound1');
clickElement1.addEventListener('click', () => {
    clickSound1.currentTime = 0; // Rewind to the start
    clickSound1.play();
});

document.getElementById('copyIP').addEventListener('click', async function() {
    // A string que será copiada
    const textToCopy = 'jogar.valorknight.com.br';

    try {
        // Usando a Clipboard API para copiar o texto
        await navigator.clipboard.writeText(textToCopy);
        
        // Exibe uma mensagem de sucesso (opcional)
        alert('IP copiado com sucesso!!');
    } catch (err) {
        console.error('Falha ao copiar o texto: ', err);
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var audioElements = document.querySelectorAll('audio');
    audioElements.forEach(function(audio) {
        audio.volume = 0.2; // Define o volume para 50%
    });
});
