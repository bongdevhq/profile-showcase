import os

profiles_dir = "content/profiles"
readme_path = "README.md"

profiles = []

for filename in os.listdir(profiles_dir):
    if filename.endswith(".md"):
        with open(os.path.join(profiles_dir, filename), 'r') as f:
            lines = f.readlines()
            name = lines[1].split(":")[1].strip().replace("'", "")
            image = lines[2].split(":")[1].strip().replace("'", "")
            bio = lines[3].split(":")[1].strip().replace("'", "")
            profiles.append((name, image, bio))

with open(readme_path, 'r') as f:
    readme_content = f.readlines()

start_index = readme_content.index("## Contributors:\n")
end_index = readme_content.index("## Happy Hacking! 🚀\n")

del readme_content[start_index + 1:end_index]

for name, image, bio in profiles:
    profile_md = f"![{name}](static/images/{image})\n\n**{name}**\n\n{bio}\n\n---\n\n"
    readme_content.insert(start_index + 1, profile_md)

with open(readme_path, 'w') as f:
    f.writelines(readme_content)
