
def true_send_mail(email="toto@free.fr"):
    print(f"python_package_demo.module_demo.true_send_mail : Sending email to {email}")
    return True

def send_mail(email="toto@free.fr"):
    return true_send_mail(email)