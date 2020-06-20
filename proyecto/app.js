(function(){

const imagenes = [
    'img/img1.jpg',
    'img/img2.jpg',
    'img/img3.jpg',
    'img/img4.jpg',
    'img/img5.jpg',
]

let recuadros = document.querySelectorAll('.rect');
let container = document.querySelector('.container')

recuadros.forEach((ele, key) => {
    ele.addEventListener('mouseover', function(){
        container.classList.remove('visible_image')
        container.classList.add('opacity_image')
        container.style.backgroundImage = `url(${imagenes[key]})`
    })
    ele.addEventListener('mouseleave', function(){
        container.classList.add('visible_image')
    })
});




})();