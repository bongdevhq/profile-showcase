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
    readme_content = f.read()

start_placeholder = "## Contributors:\n"
end_placeholder = "## Happy Hacking! 🚀\n"
profile_strings = []

for name, image, bio in profiles:
    profile_md = f"![{name}](static/images/{image})\n\n**{name}**\n\n{bio}\n\n---\n\n"
    profile_strings.append(profile_md)

new_content = readme_content.split(start_placeholder)[0] + start_placeholder + "\n".join(profile_strings) + end_placeholder + readme_content.split(end_placeholder)[1]

with open(readme_path, 'w') as f:
    f.write(new_content)
