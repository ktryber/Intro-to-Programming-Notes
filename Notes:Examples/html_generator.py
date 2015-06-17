example_concept_list = [ ['Python', 'Python is a Programming Language'],
                 ['For Loop', 'For Loops allow you to iterate over lists'],
                 ['Lists', 'Lists are sequences of data'] ]

def generate_concept_html(concept_title, concept_description):
	html1 = """
	<div class="concept">
		<div class="concept-title">
			<h3>""" + concept_title
	html2 = """</h3>
		</div>
		<div class="content">
			<p>""" + concept_description
	html3 = """</p>
		</div>
	</div>"""
	full_html = html1 + html2 + html3
	return full_html



def HTML_content(concept_list):
	concept_title = concept_list[0]
	concept_description = concept_list[1]
	return generate_concept_html(concept_title, concept_description)




def combine_concept_and_HTML(list_of_concepts):
	HTML = ""
	for item1 in list_of_concepts:
		item1_HTML = HTML_content(item1)
		HTML = HTML + item1_HTML
	return HTML

print combine_concept_and_HTML(example_concept_list)