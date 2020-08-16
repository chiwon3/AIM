// var tab_elements = document.querySelectorAll(".tab-bar ul li");
// var item_elements = document.querySelectorAll(".containers");
// for(var i = 0; i < tab_elements.length; i++){
//     tab_elements[i].addEventListener("click", function(){
//         tab_elements.forEach(function(li){
//             li.classList.remove("active");
//         })
//         this.classList.add("active");
//         var tab_value = this.getAttribute("data-li");
//         // console.log(item_elements[0].style.display="none")
//         item_elements.forEach(function(containers){
//             containers.style.display = "none";
//         })
//         if(tab_value == "tab1"){
//             document.getElementById(container1).style.display="flex";
//             console.log('why')
//         }
//         if(tab_value == "tab2"){
//             document.getElementById(container2).style.display="flex";
//                     }
//         if(tab_value == "tab3"){
//             document.getElementById(container3).style.display="flex";
//         }
//         else{
//             console.log("error");
//         }
//     })
// }


// function openTap(event, tab) {
//     var i, tabindex, tabcontents;
//     tabindex = document.getElementsByClassName('tab')
//     for (i = 0; i < tabindex.length; i++) {
//         tabindex[i].className = tabindex[i].className.replace(' active', '');
//     }
//     tabcontents = document.getElementsByClassName('containers');
//     for (i = 0; i < tabcontents.length; i++) {
//         tabcontents[i].style.display = 'none';
//     }

//     document.getElementById(tab).style.display = 'flex';
    
//     event.currentTarget.className += 'active';

// }


$(document).ready(function(){
	
	$('ul.tab li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tab li').removeClass('current');
		$('.containers').removeClass('active');

		$(this).addClass('current');
		$("#"+tab_id).addClass('active');
	})

})



