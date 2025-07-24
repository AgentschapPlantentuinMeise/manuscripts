import yaml
from pathlib import Path

# Load author info from AUTHORS.md
authors_md = Path("manuscript/AUTHORS.md").read_text()

# Convert Markdown to YAML-style author list (simplified)
authors_yaml = [
    {
        "name": "Christophe [YourLastName]",
        "affiliation": "Your Institution",
        "orcid": "https://orcid.org/0000-0000-0000-0000"
    },
    {
        "name": "Co-author Name",
        "affiliation": "Co-author Institution",
        "orcid": "https://orcid.org/0000-0000-0000-0001"
    }
]

# Load paper.md and inject authors
paper = Path("manuscript/paper.md").read_text()
lines = paper.splitlines()
for i, line in enumerate(lines):
    if line.strip() == "---":
        start = i
        break
for j in range(start + 1, len(lines)):
    if lines[j].strip() == "---":
        end = j
        break

yaml_block = yaml.safe_load("\n".join(lines[start + 1:end]))
yaml_block["author"] = authors_yaml
new_yaml = yaml.dump(yaml_block, sort_keys=False)

# Rebuild paper.md with injected authors
new_paper = ["---", new_yaml.strip(), "---"] + lines[end + 1:]
Path("manuscript/paper.injected.md").write_text("\n".join(new_paper))
