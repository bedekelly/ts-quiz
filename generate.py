from pprint import pprint
import re
import lzstring

lz = lzstring.LZString()

code_block_pattern = re.compile("```(?s:.)*?```")
code_inline_pattern = re.compile("`(.*?)`")

_unsafe = re.compile("[^A-Za-z0-9]+")


def slugify(s):
    return re.sub(_unsafe, "-", s).lower().strip("-")


def format(s):
    s = re.sub("\*\*(.*?)\*\*", "<strong>\\1</strong>", s)
    s = re.sub("\*(.*?)\*", "<em>\\1</em>", s)
    s = re.sub(
        "<pre>(.*?)</pre>",
        lambda m: "<pre>"
        + m.group(1).replace("<", "&lt;").replace(">", "&gt;")
        + "</pre>",
        s,
    )
    s = s.strip()
    return s


print(
    """
    <html lang="en">
    <meta charset="UTF-8">
    <title>TypeScript Questions</title>
    <head>
        <link rel="stylesheet" href="style.css">   
    </head>
    <body>
    <h1>TypeScript Questions</h1>
    <ol>"""
)


with open("data.md") as f:
    question_no = 0
    sections = f.read().split("\n---\n")
    for section_no, section in enumerate(sections):
        print(f'<hr id="section-{section_no+1}" />')

        if section.startswith("##") or section.startswith("\n##"):
            title = section.strip().split("\n")[0]
            section = section.replace(title + "\n", "")
            title = title.replace("##", "").strip()
            print(
                f"<h2 id={slugify(title)}>{title} <a class=anchor href='#{slugify(title)}'>§</a> </h2>"
            )

        questions = section.split("\n\n")

        for q in questions:
            if not q.strip():
                continue
            question_no += 1
            without_code_block = re.sub(code_block_pattern, "", q).strip()
            with_pres = re.sub(
                code_inline_pattern,
                lambda match: f"<pre>{format(match.group(1))}</pre>",
                without_code_block,
            )
            code_block = None

            code_block_with_tags = re.search(code_block_pattern, q)
            if code_block_with_tags:
                code_block = re.sub(
                    "```(typescript)?", "", code_block_with_tags.group(0)
                ).strip()

            # print(repr(with_pres))
            question, answer = with_pres.split("--")
            question = format(question)
            question = question[0].upper() + question[1:]

            answer = format(answer)
            answer = answer[0].upper() + answer[1:]

            # pprint({
            #     "question_text": question,
            #     "code_block": code_block,
            #     "answer_text": answer
            # })

            print(
                f"""
        <li id="question-{question_no}">
            <details>
                <summary>
                    {question}"""
                + (
                    """<pre class="code-block">{}</pre>""".format(
                        code_block.replace("<", "&lt;").replace(">", "&gt;"),
                    )
                    if code_block
                    else ""
                )
                + f"""
                </summary>
                <div class="details-content">
                    {answer}{' <a target="_blank" class="ts-playground" href="https://www.typescriptlang.org/play/?#code/{}">Try it online 🡒</a>'.format(lz.compressToEncodedURIComponent(code_block))if code_block else ''}
                </div>
            </details>
        </li>"""
            )

print("</ol>\n</body>")
