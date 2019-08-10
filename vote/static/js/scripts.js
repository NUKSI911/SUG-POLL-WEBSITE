/*function appender(caller,list){
	for (var i = 0; i < list.length; i++){
		caller.appendChild(list[i]);
	}
}
function create(element){
	return document.createElement(element);
}*/
/*img.src =src*/ /*{{ url_for('static', filename='img/pic.jpg') }}*/ 
/*function carousels(src){
	carousel_container = document.getElementById('carousel_content');
	carousel_item = create("DIV");
	carousel_item.className = "carousel-item"
	//add an active class to carousel
	carousel = create("DIV");
	img_tag = create("IMG");
	img_tag.className = "d-block";
	img_tag.alt = "Slide";
	img_tag.classList.add("w-100");
	
	p_tag = create("P");
	p_tag.innerHTML = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmo tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
	for (var k = 0; k < src.length; k++){
		img_tag.src = src[k];
		if (k == 0){
			carousel_item.classList.add("active");
		}
		appender(carousel, [img_tag,p_tag]);
		appender(carousel_item, [carousel]);
		appender(carousel_container, [carousel_item])
	}

}
$.ajax({
	url: "/api/requested",
	type: 'GET',
	success: function(res) {
	    carousels(res)
	}
});

to get the file name you just have to filter it

use cms to control the html file
*/

function clicks(val){
	document.getElementById(val).click()
}
//console.log('hola');
//console.log(document.getElementsByClassName("count").length);