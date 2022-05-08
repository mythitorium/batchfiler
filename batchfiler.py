# Mythitorium
# v1.0

import pyperclip, os, re, time

# Set values are script defaults
cfg = {
    "prefix" : "",
    "suffix" : "",
    "filter" : "",
    "output_name" : "output.txt",
    "output_path" : ""
}

value_pattern_list = [r"^prefix:",r"^suffix:",r"^filter:",
                    r"^output_file_name:",r"^output_file_path:"]


def main():
    # Creating the config file
    try:
        config = open("config.ini", "x")
        content = ["[config]\n",
            "prefix:\n","suffix:\n","filter:\n",
            "output_name:\n","output_path:\n"]
        config.writelines(content)
        config.close()
        print("Creating config file...")
    except:
        print("Config found")

    # Reading the config file
    config = open("config.ini", "r")
    config_values = config.readlines()
    config.close()
    # Applying settings
    cfg_keys = list(cfg.keys())
    for value in config_values:
        for index in range(0,len(value_pattern_list)):
            if re.match(value_pattern_list[index], value):
                cfg[cfg_keys[index]] = value.split(":", 1)[1].strip()

    # Print results
    print("--------")
    print("Prefix set to '" + cfg["prefix"] + "'")
    print("Suffix set to '" + cfg["suffix"] + "'")
    print("Filter set to '" + cfg["filter"] + "'")
    print("Output file name set to '" + cfg["output_name"] + "'")
    print("Output file path set to '" + cfg["output_path"] + "'")
    print("--------")
    print("Ready to archive clipboard contents")
    print("Press ctrl + c to exit")
    print("--------")
    monitor_clipboard()


# Checks the clipboard for changes. Attempts to save those changes
def monitor_clipboard():
    old_clipboard = pyperclip.paste()
    repeat = True

    while repeat:
        try:
            time.sleep(0.05) # Wait (just don't copy to your clipboard faster than 20 times a second)
            clipboard = pyperclip.paste()
            if not clipboard == old_clipboard:
                save_clipboard(clipboard)
                old_clipboard = clipboard
        except KeyboardInterrupt:
            print("Script killed")
            repeat = False


# Takes a string and appends it to the output file
def save_clipboard(input):
    try:
        output = open(cfg["output_path"] + cfg["output_name"], "x")
    except FileExistsError:
        output = open(cfg["output_path"] + cfg["output_name"], "a")
    
    final = (cfg["prefix"]+" "+input+" "+cfg["suffix"]).strip()
    if cfg["filter"] in input: 
        output.write(final+"\n")
    output.close()
    print("- Saved: '" + final + "'")


if __name__ == "__main__":
    main()
