import os
import shutil
import install_fish

def install(*args, **kwargs):
    current_directory = os.getcwd()
    awesome_fish_directory = os.path.join(current_directory, "awesome-fish")
    fish_config_location = os.path.expanduser("~/.config/fish")
    print(f"Fish config location: {fish_config_location}")

    # Change to the current working directory
    os.chdir(fish_config_location)
    
    # List all files and directories in the current directory
    items = os.listdir(fish_config_location)
    
    if os.path.exists(f"{fish_config_location}/functions"):
        print("The functions directory exists")
        items = os.listdir(f"{fish_config_location}/functions")
        print("Items in the functions directory:")
        for item in items:
            print(item)

        shutil.move(awesome_fish_directory, f"{fish_config_location}/functions")
        print("Awesome Fish has been moved to the functions directory")

    else:
        print("Please ensure that the Friendly Interactive Shell is installed.")
        result = input("Do you want to install it? (y/n): ")
        if result == "y":
            install_fish.fish_install(*args, **kwargs)
        else:
            print("Exiting...")
            exit()


