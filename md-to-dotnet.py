import sys
import markdown

def convert_markdown_to_html(markdown_path):
    """Converts a markdown file to HTML."""
    with open(markdown_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    html_content = markdown.markdown(md_content)
    return html_content

def insert_html_at_placeholder(html_file_path, html_content, new_html_file_path):
    """Inserts HTML content into an existing HTML file at the placeholder location, then writes to a new file."""
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_file_content = file.read()
    
    updated_html_content = html_file_content.replace("<!-- MARKDOWN_CONTENT -->", html_content)
    
    with open(new_html_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_html_content)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py markdown_path html_file_path new_html_file_path")
        sys.exit(1)
    
    markdown_path = sys.argv[1]
    html_file_path = sys.argv[2]
    new_html_file_path = sys.argv[3]
    
    html_content = convert_markdown_to_html(markdown_path)
    insert_html_at_placeholder(html_file_path, html_content, new_html_file_path)

