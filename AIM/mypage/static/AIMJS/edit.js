$(document).ready(function(){
	
	$('ul.tab li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tab li').removeClass('current');
		$('.containers').removeClass('active');

		$(this).addClass('current');
		$("#"+tab_id).addClass('active');
	})

})
