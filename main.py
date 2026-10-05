# Macros plugin for MkDocs
# See https://mkdocs-macros-plugin.readthedocs.io/en/latest/#full-example

# Here you can define your own macros, which can be used in your markdown files.

def define_env(env):
    "Hook function"

    # Example
    # This macro will be available in your markdown files as {{ mymacro(" world") }}
    @env.macro
    def mymacro(s):
        return "hello" + s

    def replaceSpaces(s):
        return s.replace(" ", "-")

    @env.macro
    def linkCard(name, description):
        # Replace the placeholders with name
        clean_name = replaceSpaces(name)
        return f"""<div class="link-card">
            <a href="../{clean_name.lower()}">
            <img src="../{clean_name.lower()}/index.jpg" alt="{name}">
            <div>{name}</div>
            <p>{description}</p>
            </a>
        </div>"""   
 