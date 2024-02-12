# Converts the original markdown for the course in `orig-source` into
# lesson-builder formtted assignments

from pathlib import Path
import yaml
from textwrap import dedent

dst = Path(Path.cwd().joinpath('assignments'))

if not dst.exists():
    # Create if it does not exist
    dst.mkdir(parents=True)

import re


def extract(source: str, base_name: str):
    # Regex pattern to find python.run blocks with optional height and width
    pattern = re.compile(r"```python\.run(?:\:height='?(\d+)'?)?(?:,width='?(\d+)%?'?)?\n(.*?)```",
                         re.DOTALL)

    counter = [1]
    code = {}

    # Function to replace matched objects
    def replacer(match):
        m = match.group(0).strip('```')

        lines = m.split('\n')
        first = lines[0]
        py_code = '\n'.join(lines[1:])
        if ':' in first:
            _, spec = first.split(':')
            spec = spec.strip()
            _ , height = spec.split('=')
            height = int(height.strip("'"))
        else:
            height = 800

        prog_name = f"{base_name}_{counter[0]}.py"

        code[prog_name] = py_code
        # Construct the replacement string
        replacement = f"{{{{ trinket(\"{prog_name}\", width=\"100%\", height=\"{height}\", embed_type=\"python\") | safe }}}}"

        counter[0] += 1

        return replacement

    # Replace matched blocks in the source with the template string
    modified_source = pattern.sub(replacer, source)

    return modified_source, code

def convert(source_dir, dst_root):
    from collections import defaultdict

    def mklesson():
        return {
            'text': '',
            'resources': [],
            'assignments': []
        }

    lessons = defaultdict(mklesson)

    for f in source_dir.glob('**/*.md'):
        e = f.relative_to(source_dir)
        source = f.read_text()
        p = e.parent
        d = e.stem
        md, code = extract(source, d)

        lesson_path = p.joinpath(d)
        dest = dst_root.joinpath(lesson_path)

        if not dest.exists():
            dest.mkdir(parents=True)

        ack = dedent("""
        ---
        
        Thanks to Trinket.io for providing this assignment, 
        part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
        course.\n""").strip()

        (dest.joinpath('trinket.md')).write_text(md+"\n\n"+ack)

        for k, v in code.items():
              (dest.joinpath(k)).write_text(v)

        title =  d.replace('-',' ').title()
        asgn = {'title': title, 'description':title}

        (dest.joinpath('_assignment.yaml')).write_text(yaml.dump(asgn))

        l = lessons[str(p)]
        l['text'] = str(p.joinpath(str(p)+'.md'))

        lesson_title = str(p).replace('-',' ').title()
        lesson_text= dedent(f"""
        ---
        title: {lesson_title}
        ---
        
        # {lesson_title}
        
        """).strip()

        (dst.joinpath(p).joinpath(str(p)+'.md')).write_text(lesson_text)

        l['assignments'].append(str(lesson_path))

    plan = {
        'title': '',
        'description': '',
        'pages': [],
        'resources': [],
        'sidebar': [],
        'lessons': dict(lessons)
    }

    dst_root.joinpath('lesson-plan.yaml').write_text(yaml.dump(dict(plan)))


convert(Path.cwd().joinpath('orig-source'), dst)
