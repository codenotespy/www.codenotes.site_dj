const navbtn = document.getElementById("navbtn");
const navcontainer = document.getElementById("navcontainer")

// TO DRAW NAVIGATION BUTTON:
navbtn.addEventListener("click", function() {
////    navcontainer.classList.toggle("hidden");
//    navcontainer.style.display = navcontainer.style.display === 'none' ? '' : 'none';
    this.style.left = this.style.left === '320px' ? '0' : '320px';
});


// TO HIDE NAVIGATION:
navbtn.addEventListener('click', function () {
  
  if (navcontainer.classList.contains('hidden')) {
    navcontainer.classList.remove('hidden');
    setTimeout(function () {
      navcontainer.classList.remove('visuallyhidden');
    }, 20);
  } else {
    navcontainer.classList.add('visuallyhidden');    
    navcontainer.addEventListener('transitionend', function(e) {
      navcontainer.classList.add('hidden');
    }, {
      capture: false,
      once: true,
      passive: false
    });
  }
}, false);



// TO HIDE NAVIGATION WHEN WINDOW WIDTH IS SMALLER 991PX:
window.addEventListener("resize", function(event) {
    if (document.body.clientWidth > 991){
        navcontainer.classList.remove('hidden');
    }
    else {
        navcontainer.classList.add('hidden');
        navbtn.style.left = '0'
    }


//    console.log(document.body.clientWidth + ' wide by ' + document.body.clientHeight+' high');
});

//if (document.body.clientWidth < 991) {
 // navcontainer.classList.remove('hidden');
//}
  














// FOR HOVER EFFECT ON NAVIGATION MENU OPTIONS: (I ADD BELOW FUNTION IN CSS BUT BELOW WORKS AS WELL)
//    const navli = document.querySelectorAll('.navli')

//    for (var i, i=0; i<navli.length; i++) {
//        navli[i].addEventListener("mouseover", function() {
//            var current = document.getElementsByClassName("active");
//            current[0].classList.remove('active');  
//            this.classList.add('active');
//        });
//    };