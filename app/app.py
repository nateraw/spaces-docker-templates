import gradio as gr


def name_to_hf_markdown(name):
    return f"[{name}](https://huggingface.co/{name})"


def show_template(name, description, authors, url, image_url, more_info=None):
    if isinstance(authors, str):
        authors = [authors]
    authors_md = ", ".join([name_to_hf_markdown(author) for author in authors])
    with gr.Box():
        with gr.Row():
            with gr.Column(scale=1):
                gr.HTML(f"""<img src="{image_url}" alt="{name}-thumbnail" height=256 width=256>""")
            with gr.Column(scale=4):
                gr.Markdown(
                    f"""
                ## {name}
                [![Open In Colab](https://img.shields.io/badge/-Duplicate%20Space-blue?labelColor=white&amp;style=flat&amp;logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAP5JREFUOE+lk7FqAkEURY+ltunEgFXS2sZGIbXfEPdLlnxJyDdYB62sbbUKpLbVNhyYFzbrrA74YJlh9r079973psed0cvUD4A+4HoCjsA85X0Dfn/RBLBgBDxnQPfAEJgBY+A9gALA4tcbamSzS4xq4FOQAJgCDwV2CPKV8tZAJcAjMMkUe1vX+U+SMhfAJEHasQIWmXNN3abzDwHUrgcRGmYcgKe0bxrblHEB4E/pndMazNpSZGcsZdBlYJcEL9Afo75molJyM2FxmPgmgPqlWNLGfwZGG6UiyEvLzHYDmoPkDDiNm9JR9uboiONcBXrpY1qmgs21x1QwyZcpvxt9NS09PlsPAAAAAElFTkSuQmCC&amp;logoWidth=14)]({url})

                #### {description}

                **Author(s):** {authors_md}
            """
                )
                if more_info:
                    with gr.Row():
                        with gr.Accordion("👀 More Details", open=False):
                            gr.Markdown(more_info)


title_and_description = """
# Spaces Templates

<div align="center">
  <a src="https://img.shields.io/github/stars/nateraw/spaces-docker-templates?style=social" href="https://github.com/nateraw/spaces-docker-templates" target="_blank">
    <img src="https://img.shields.io/github/stars/nateraw/spaces-docker-templates?label=Contribute&style=social" alt="GitHub Stars">
  </a>

  <h4>🚀 A collection of templates for <a href="https://huggingface.co/spaces">Hugging Face Spaces</a></h4>

  The templates below are designed to help you get started with Docker Spaces. Duplicate them to get started with your own project. 🤗
</div>
"""

with gr.Blocks(css="style.css") as demo:
    gr.Markdown(title_and_description)
    show_template(
        name="JupyterLab",
        description="Spin up a JupyterLab instance with just a couple clicks. This template is great for data exploration, model training, and more. Works on CPU and GPU hardware.",
        authors=["camenduru", "nateraw"],
        url="https://huggingface.co/spaces/DockerTemplates/jupyterlab?duplicate=true",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1767px-Jupyter_logo.svg.png",
        more_info="""
        ### Configuration
        - You can add dependencies to your JupyterLab instance by editing the `requirements.txt` file.
        - You can add linux packages to your JupyterLab instance by editing the `packages.txt` file.
        - You can add custom startup commands to your JupyterLab instance by editing the `on_startup.sh` file. These run with the root user.
        """,
    )
    show_template(
        name="VSCode",
        description="Spin up a VSCode instance with just a couple clicks. This template is great for data exploration, model training, and more. Works on CPU and GPU hardware.",
        authors=["camenduru", "nateraw"],
        url="https://huggingface.co/spaces/DockerTemplates/vscode?duplicate=true",
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1200px-Visual_Studio_Code_1.35_icon.svg.png",
        more_info="""
        ### Configuration
        - You can add dependencies to your VSCode instance by editing the `requirements.txt` file.
        - You can add linux packages to your VSCode instance by editing the `packages.txt` file.
        - You can add custom startup commands to your VSCode instance by editing the `on_startup.sh` file. These run with the root user.
        """,
    )


if __name__ == "__main__":
    demo.launch()
