from flask import Flask, request, render_template
from itertools import pairwise
from textwrap import wrap
from os import environ, path
from questions import questions
import pydot as pyd
import json
current_path = environ.get("PATH")
environ["PATH"] = current_path + ";C:\\Program Files (x86)\\Graphviz\\bin"

app = Flask(__name__)

@app.route('/')
def form():
    if path.exists('answers.json'):
        with open('answers.json') as a:
            answer_list = json.load(a)
    else:
        answer_list = None
    
    return render_template('form.html', questions=questions, answers=answer_list)


@app.route('/', methods=['POST'])
def form_post():
    # Save the users answers to answers.json file if they want to revisit their answers
    answers = request.form.to_dict(flat=False)
    with open('answers.json', 'w') as a:
        json.dump(answers, a, ensure_ascii=False, indent=4)
    
    diagram = create_diagram(answers)
    diagram.write_png('static/img/output.png')
    diagram.write_svg('static/img/output.svg')
    diagram.write_raw('static/script/output.dot')
    return render_template('diagram.html')

def create_diagram(answers: dict):
    toc_components = ["Inputs","Activities","Outputs","Outcomes","Impacts"]
    toc_colors = ['lightblue', 'lightyellow', 'lavenderblush', 'lightgreen', 'lightcoral']
    charity_name = answers[questions[0]['question']][0]

    # Used to decide number of nodes via sliders, replace this with 'num_of_nodes = 5' in the second iteration if you remove the slider question from the previous one
    num_of_nodes = answers[questions[1]['question']]

    # Regular label, doesnt do anything at the moment
    charity_type = (answers[questions[2]['question']][0] if 'Other' not in answers[questions[2]['question']] else answers[questions[2]['question']][1])

    # Currently gets the value of the input itself if the question has toc_component, value should be changed based on what option you choose
    node_labels = {answers.get(key)[1]: answers.get(key)[0].split('\r\n') for key in list(answers) if answers.get(key)[1] in toc_components}
    
    # Initialize the graph
    graph = pyd.Dot(
        'toc', 
        graph_type='digraph', 
        fontname='Helvetica', 
        labelloc='t', 
        label=f'{charity_name} - Theory of Change Diagram for {charity_type}', 
        rankdir='LR', 
        compound=True
    )
    graph.set_node_defaults(shape='box', width=1.5, style='filled', color='black', fontname='Helvetica')
    graph.set_graph_defaults(style='filled', color='transparent', fillcolor='lightgrey')

    dummy_nodes = []
    clusters = []

    # Create clusters and dummy nodes
    for idx, (label, color, num) in enumerate(zip(toc_components, toc_colors, num_of_nodes)):
        cluster = pyd.Cluster(f'{idx}', label=label)
        cluster.set_node_defaults(fillcolor=color, clusterrank='global')
        graph.add_subgraph(cluster)
        clusters.append(cluster)

        dummy = pyd.Node(f'DUMMY_{idx}', shape='point', style='invis', height=0)
        dummy_nodes.append(dummy)
        cluster.add_node(dummy)
        
        # Add nodes to clusters based on slider input + appropriate labels
        for n in range(int(num)):
            formatted_labels = '\n'.join(wrap(node_labels[toc_components[idx]][n], 20))
            node_name = f'{toc_components[idx]}{n}'
            clusters[idx].add_node(pyd.Node(node_name, label=formatted_labels))

    # Link dummy nodes invisibly to force layout to look like a toc diagram
    for dummy1, dummy2 in pairwise(dummy_nodes):
        graph.add_edge(pyd.Edge(dummy1, dummy2, style='invis'))

    return graph
    
if __name__ == '__main__':
            
    app.run(debug=True)