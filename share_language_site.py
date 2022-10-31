import json

with open("language_codes.json", "r") as infile:
    lang_dict = json.load(infile)

while True:
    infile = open("index.txt", "r")
    language = infile.readline()

    if language and len(language) < 20:
        infile.close()
        language.strip().capitalize()

        if language in lang_dict:
            result = "https://glottolog.org/resource/languoid/id/" + lang_dict[language]
            with open("index.txt", "w") as outfile:
                outfile.write(f"Click here to learn more about {language}: {result}")
        else:
            potential = [f"{lang}: " + "https://glottolog.org/resource/languoid/id/" + lang_dict[lang] + "\n"
                         for lang in lang_dict if language in lang]
            if potential:
                with open("index.txt", "w") as outfile:
                    outfile.write(f"We couldn't find an exact match for {language}. Check out the following links:\n")
                    outfile.writelines(potential)
            else:
                with open("index.txt", "w") as outfile:
                    outfile.write(f"Sorry, we couldn't find any more info about {language} on Glottolog")

    else:
        infile.close()


