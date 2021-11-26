def yesOrNo(question, default=None):
    """
    Yes or no question
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    sys.stdout.write(f"{question}{prompt}")  
    choice = input().lower()
    if default is not None and choice == '':
        return valid[default]
    elif choice in valid:
        return valid[choice]
    else:
        print("\nPlease respond with 'yes' or 'no' (or 'y' or 'n')")
        
"""
credit to GitHub Copilot (and to the man/woman, who made the code, that GitHub Copilot learned) for making the original program, that I changed
"""
