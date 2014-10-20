import subprocess


def get_user_name_from_git():
    try:
        git_process = subprocess.Popen(
            ['git', 'config', 'user.name'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        user_name, _ = git_process.communicate()
        return user_name.rstrip()
    except OSError:
        return None


def get_user_email_from_git():
    try:
        git_process = subprocess.Popen(
            ['git', 'config', 'user.email'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        user_email, _ = git_process.communicate()
        return user_email.rstrip()
    except OSError:
        return None
