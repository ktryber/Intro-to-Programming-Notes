for note in concepts_1_1 and concepts_1_2:
			new_note = Notes_db(lesson_number = note[0])
			new_note.put()

			for note in your_notes:
    new_note = Notes_db(lesson_number = notes[0], title = notes[1], content = notes[2])
    new_note.put()


    <div class="stage">
	<h1>Stage 4: Allow Users to Comment</h1>
		{% for concept in concepts_1_1 %}
  		<div class="lesson-title-box">
  			<h2></h2>
	  				<div class="concept">
	  					<h3></h3>		
	  						<div class="content">
	  							<p>
	  								
	  							</p>
	  						</div>
	  				</div>
	  			{% endfor %}
	 	 </div>