var logdiv = $('#moodlog');

var actions;

var moods;

console.log(logdiv);

$('#btn-moods').on("click", function(){

$.ajax({

	method: 'GET',
	url: 'http://127.0.0.1:8000/api/logs/',

	success: function(response){

		moods = response;

		for (let moodl of response){
			
			$('#moods').append(`
				
				<h4 >${moodl.mood.emoji} ${moodl.mood.title}</h4>

				`);

		}
		$('#btn-moods').remove();

		}

});
});


$('#btn-actions').on("click", function(){

$.ajax({

	method: 'GET',
	url: 'http://127.0.0.1:8000/api/logs/',

	success: function(response){

		actions = response;
		for (let moodl of response){
			
			$('#actions').append(`
				
				<h4>${moodl.action.emoji} ${moodl.action.title}</h4>
				`);

		}
		$('#btn-actions').remove();

		}

});
});




$.ajax({

	method: 'GET',
	url: 'http://127.0.0.1:8000/api/logs/',

	success: function(response){

		for (let moodl of response){
			
			logdiv.append(`
				<h3>${moodl.note}</h3>

				<span class='tag'>Mood: ${moodl.mood.emoji} ${moodl.mood.title}</span>
				<span class='tag'>Action: ${moodl.action.emoji} ${moodl.action.title}</span>
				<hr>
				`);

		}

		}


});