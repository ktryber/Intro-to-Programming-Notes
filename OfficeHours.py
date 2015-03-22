list_of_concepts = [['Python', 'Python is a language.'],
					['HTML', 'Stands for Hypertext Markup Language']]


def make_HTML_for_many_concepts(concept_list):
	HTML = ""
	for concept in concept_list:
		HTML = HTML + make_HTML_for_many_concepts(concept)
	return HTML


def make_html_for_concept(concept):
	title = concept[0]
	description = concept[1]
	concept_HTML = """
<div class="concept>
	<div class="concept-title">
		""" + title + """
	</div>
	<div class="concept-description">
		""" + description + """
	</div>
</div>"""
	return concept_HTML

make_HTML_for_many_concepts(list_of_concepts)