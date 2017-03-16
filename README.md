# About
- Automatically create [blockonomics](https://www.blockonomics.co) bitcoin invoice.
- No need for approvals/API key/documentation. Use your own bitcoin address to
  receive funds.
- Invoices are peer to peer encrypted. Bitcoin amount adjusts dynamically
  according to [current price](https://medium.com/@blockonomics_co/peer-to-peer-no-signups-invoice-in-fiat-get-paid-in-bitcoin-f77772e4308b#.kayu1h1k0). Blockonomics supports almost all fiat currencies.
- Can to used to implement workflows like reccuring invoices, generate/mail
  invoices from website.
- If you need branding, custom logo/style in invoices you need to subscibe to [BitKart Plan](https://www.blockonomics.co/views/pricing.html) and mail blockonomics support to setup your branding.

# Examples
## Python

```
echo "20 hours of html/css work in January 2017" | python create_invoice.py --amount 10 -addr 1Cg6QbAnbY2XmEMiQhp6AQwfc36tTwTH7a
https://www.blockonomics.co/invoice/913/#/?key=sQm41g3y
```
Currency can changed (default is USD)
```
echo "20 hours of html/css work in January 2017" | python create_invoice.py --amount 20 --currency EUR -addr 1Cg6QbAnbY2XmEMiQhp6AQwfc36tTwTH7a
https://www.blockonomics.co/invoice/914/#/?key=zoLRxXKt

```
Invoice expiry can be specified in days (default is 7 days)
```
echo "20 hours of html/css work in January 2017" | python create_invoice.py --amount 20 --currency EUR -addr 1Cg6QbAnbY2XmEMiQhp6AQwfc36tTwTH7a --expiry 1
https://www.blockonomics.co/invoice/915/#/?key=q4mI3TSY
```
## Php
Coming soon
