var logdiv = $('#moodlog');

console.log(logdiv);

$('btn').click(function(){



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
