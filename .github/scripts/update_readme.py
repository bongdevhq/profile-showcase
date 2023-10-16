import os
from PIL import Image

profiles_dir = "content/profiles"
readme_path = "README.md"
profiles = []

for filename in os.listdir(profiles_dir):
    if filename.endswith(".md"):
        with open(os.path.join(profiles_dir, filename), 'r') as f:
            lines = f.readlines()
            if len(lines) < 4:  # Check if the file has at least 4 lines
                print(f"Warning: File {filename} has fewer lines than expected. Skipping...")
                continue
            if len(lines[0]) > 9:
                print(f"Warning: File {filename} doesn't match the expected format. Skipping...")
                continue
            try:
                name = lines[1].split(":")[1].strip().replace("'", "")
                image = lines[2].split(":")[1].strip().replace("'", "")
                
                #Resizing the image to specified format
                im = Image.open(f"static/images/{image}")
                im.thumbnail((250,250))
                im.save(f"static/images/{image}","JPEG")
                
                bio = lines[4].split(":")[1].strip().replace("'", "")
                
                #Don't more profile info it's causing unpack error
                profiles.append((name, image, bio))
                
            except IndexError:
                print(f"Warning: File {filename} doesn't match the expected format. Skipping...")
            except Exception as e:
                print(f'Image {image} is corrupted')

with open(readme_path, 'r') as f:
    readme_content = f.read()

start_placeholder = "## Contributors:\n\n"
end_placeholder = "## Happy Hacking! 🚀\n"
profile_strings = []

for name, image, bio in profiles:
    profile_md = f"![{name}](static/images/{image})\n\n**{name}**\n\n{bio}\n\n---\n\n"
    profile_strings.append(profile_md)

new_content = readme_content.split(start_placeholder)[0] + start_placeholder + "\n".join(profile_strings) + end_placeholder

with open(readme_path, 'w', encoding="utf-8") as f:
    f.write(new_content)
