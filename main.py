from youtube.search import Youtube

try:
    with Youtube() as bot:
        bot.search_vid(vid_title=input("1st vid? "))

        print("This video has " + bot.getviews() + " views.")


except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise