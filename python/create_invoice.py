#!/usr/bin/env python
import argparse
import sys
import time
import requests
import json
from util import generate_passphrase, encrypt
BLOCKONOMICS_URL="https://www.blockonomics.co"
API_ENDPOINT="/api/invoice"

def create_invoice(amount, currency, description, address, expiry):
  passphrase = generate_passphrase(8)
  invoice = dict(desc=description, timestamp=int(time.time()), addr=address,
                 amount=amount, currency=currency, expiry=expiry*86400)
  encrypted_invoice = encrypt(json.dumps(invoice), passphrase)
  r = requests.post(BLOCKONOMICS_URL + API_ENDPOINT,
                    json=dict(content=encrypted_invoice))
  r.raise_for_status()
  invoice_id =  r.json().get('number')
  if (not invoice_id):
    raise Exception("Server didn't return invoice number")

  return "{}/invoice/{}/#/?key={}".format(BLOCKONOMICS_URL, invoice_id,
                                          passphrase)


def main():
  parser = argparse.ArgumentParser(description="Creates blockonomics invoice") 
  parser.add_argument('infile', type=argparse.FileType('r'),
                      default=sys.stdin, nargs="?", help="File containing invoice description"
                      "(Default read from stdin)")
  parser.add_argument("-a", "--amount", dest="amount", action="store", 
                      required=True, type=float, help="Invoice Amount")
  parser.add_argument("-addr", "--address", dest="address", action="store", 
                      required=True, help="Receiving Bitcoin Address")
  parser.add_argument("-c", "--currency", dest="cur", action="store", 
                      required=False, default="USD", help="Invoice Currency(Default USD)")
  parser.add_argument("-e", "--expiry", dest="expiry", action="store", 
                      required=False, type=int, default=7, help="Invoice expiry in days(Default 7)")
  args = parser.parse_args() 
  description = args.infile.read()
  print create_invoice(amount=args.amount, currency=args.cur,
                 description=description, address=args.address, 
                 expiry=args.expiry)
if __name__ == "__main__":
  main()
