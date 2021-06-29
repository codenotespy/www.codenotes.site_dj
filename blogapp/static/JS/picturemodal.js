const modal = document.querySelector('.modalxz')
const modalImage = document.querySelector('.modalImagexz')
const thumbnails = document.querySelectorAll('.thumbnailxz');

thumbnails.forEach(thumbnail => {
	thumbnail.addEventListener('click', evt => {
  	modal.classList.remove('hiddenxz');
    modalImage.setAttribute('src', evt.target.getAttribute('src'));
  })
});

modal.addEventListener('click', evt => {
	modal.classList.add('hiddenxz');
});