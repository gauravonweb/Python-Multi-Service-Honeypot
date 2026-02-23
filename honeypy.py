# honeypy.py

import argparse
from ssh_honeypot import honeypot
from web_honeypot import run_web_honeypot


def main():
    parser = argparse.ArgumentParser(description="Honeypot Launcher")

    # Common arguments
    parser.add_argument(
        "-a", "--address",
        type=str,
        default="0.0.0.0",
        help="IP address to bind (default: 0.0.0.0)"
    )

    parser.add_argument(
        "-p", "--port",
        type=int,
        required=True,
        help="Port number to listen on"
    )

    parser.add_argument(
        "-u", "--username",
        type=str,
        help="Username for honeypot login"
    )

    parser.add_argument(
        "-pw", "--password",
        type=str,
        help="Password for honeypot login"
    )

    parser.add_argument(
        "-s", "--ssh",
        action="store_true",
        help="Run SSH honeypot"
    )

    parser.add_argument(
        "-w", "--http",
        action="store_true",
        help="Run HTTP honeypot"
    )

    args = parser.parse_args()

    # Ensure only one mode is selected
    if not args.ssh and not args.http:
        print("[!] Please choose a honeypot type:")
        print("    -s  for SSH")
        print("    -w  for HTTP")
        return

    try:
        if args.ssh:
            print(f"[-] Starting SSH Honeypot on {args.address}:{args.port}")
            honeypot(args.address, args.port, args.username, args.password)

        elif args.http:
            print(f"[-] Starting HTTP Honeypot on port {args.port}")

            # Default credentials for HTTP if not provided
            if not args.username:
                args.username = "admin"
            if not args.password:
                args.password = "password"

            print(f"[+] Using credentials -> Username: {args.username} | Password: {args.password}")

            run_web_honeypot(args.port, args.username, args.password)

    except Exception as e:
        print("\n[ERROR] Honeypot crashed:")
        print(e)


if __name__ == "__main__":
    main()