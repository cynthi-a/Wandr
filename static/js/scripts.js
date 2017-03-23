/**
 * Created by RMac on 28/02/2017.
 */

function menuContraction(){
	var mq = window.matchMedia( "(min-width: 992px)" );
	if (mq.matches) {
  		if(window.scrollY > '20'){
  			document.getElementById("menu-bar").style.padding = '0px';
  			document.getElementById("menu-bar").style.opacity = 0.85;
  		}
  		else {
  			document.getElementById("menu-bar").style.padding = '20px 0px';
  			document.getElementById("menu-bar").style.opacity = 1;
  		}
	}

}

window.onload = menuContraction;
window.addEventListener("scroll", menuContraction);