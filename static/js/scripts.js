/**
 * Created by RMac on 28/02/2017.
 */

function menuContraction(){
	var mq = window.matchMedia( "(min-width: 992px)" );
	if (mq.matches) {
  		if(window.scrollY > '20'){
  			document.getElementById("menu-bar").style.padding = '0px';
  		}
  		else {
  			document.getElementById("menu-bar").style.padding = '20px 0px';
  		}
	}

}

window.onload = menuContraction;
window.addEventListener("scroll", menuContraction);