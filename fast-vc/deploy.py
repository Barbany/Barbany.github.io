import os


with open('list.txt', 'r') as f:
        lines = f.readlines()
with open('header.html', 'r') as f:
        head = f.read()
with open('footer.html', 'r') as f:
        foot = f.read()
with open('index.html', 'w') as f:
        f.write(head)
        f.write('<table>')
        
        # Header
        f.write('<thead>')
        f.write('<th>Description</th>')
        f.write('<th>Source speaker (content)</th>')
        f.write('<th>Target speaker (style)</th>')
        f.write('<th>Conversion</th>')
        f.write('<th></th>')
        f.write('</thead>')

        # Body
        f.write('<tbody>')
        f.write('<tr>')
        systems = sorted(os.listdir('conversion'))
        for line in lines:
            description, source, target, fname = line.split('\t')
            f.write(f'<td rowspan={len(systems)}>{description}</td>')
            f.write(f'<td rowspan={len(systems)}><audio align="middle" controls style="display: block;margin-left: auto;margin-right: auto;border-radius: 0%;"><source src="/fast-vc/source/{source}_{fname}" type="audio/wav">Your browser does not support the audio element.</audio></td>')
            f.write(f'<td rowspan={len(systems)}><audio align="middle" controls style="display: block;margin-left: auto;margin-right: auto;border-radius: 0%;"><source src="/fast-vc/target/{target}.wav" type="audio/wav">Your browser does not support the audio element.</audio></td>')
            for system in systems:
                f.write(f'<td>{system}</td>')
                f.write(f'<td><audio align="middle" controls style="display: block;margin-left: auto;margin-right: auto;border-radius: 0%;"><source src="/fast-vc/conversion/{system}/{source}_{target}_{fname}" type="audio/wav">Your browser does not support the audio element.</audio></td>')
                f.write('<tr>')

        f.write('<tbody>')
        f.write('</table>')
        f.write(foot)

