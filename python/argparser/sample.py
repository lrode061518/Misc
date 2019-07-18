#!/usr/bin/env python
from argparse import ArgumentParser, FileType

DEFAULT_PROFILE = 10
DEFAULT_API_PORT = 4432
DEFAULT_SITE_ID = 1
DEFAULT_CUSTOMER_ID = 'aasdfasdf'
DEFAULT_PRIORITY = 50
DEFAULT_THRESHOLD = 30

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("filename", help="Files to process", nargs='+')
    parser.add_argument("-p", "--port", help="api server port", required=False, default=DEFAULT_API_PORT)
    parser.add_argument("--customer-id", help="customer id", dest="customer", required=False, default=DEFAULT_CUSTOMER_ID)
    parser.add_argument("--site-id", help="site id for host", dest="site_id", required=False, default=DEFAULT_SITE_ID)
    parser.add_argument("-P", "--profile-id", help="profile id", dest="profile", required=False, default=DEFAULT_PROFILE) # 1100 dynamic-only
    parser.add_argument("--passthrough", help="Paththrough string", required=False, default="ococococ")
    parser.add_argument("-o", "--output", help="Path for output result, result filename as '${scanned_file}-${timestamp}'", required=False, default="")
    parser.add_argument("--priority", help="priority value, default is (%d)"%DEFAULT_PRIORITY, required=False, default=DEFAULT_PRIORITY)
    parser.add_argument("--delete-src", help="purge source file", dest="delete", action="store_true")
    parser.add_argument("--no-delete-src", dest="delete", action="store_false")
    parser.add_argument("--rescan", help="Disable this value to use cache result", dest="rescan", action="store_true")
    parser.add_argument("--no-rescan", dest="rescan", action="store_false")
    parser.add_argument("--is-on-demand", help="This value will affect internal logic", dest="on_demand", action="store_true")
    parser.add_argument("--not-on-demand", dest="on_demand",  action="store_false")
    parser.add_argument("--send-alert-confidence", help="threshold for sending(%d)"%DEFAULT_THRESHOLD, dest="threshold", default=DEFAULT_THRESHOLD)
    parser.add_argument("--push-result", help="Run a simple server and wait for scan result, default is True", dest="push_result", action="store_true")
    parser.add_argument("--no-push-result", dest="push_result", action="store_false")

    parser.set_defaults(push_result=True, on_demand=False, rescan=True, delete=False)

    parser.add_argument("--debug", help="Print request on console without sending it.", action="store_true", default=False)
    return parser.parse_args()

def main():
    args = parse_arguments()
    print(args)

if __name__ == "__main__":
    main()
