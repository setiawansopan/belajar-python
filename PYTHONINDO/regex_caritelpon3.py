import re
no_texp_regex = re.compile(r'(\d\d\d) (\d\d\d\d\d\d\d)')
mo = no_texp_regex.search('Nomor telpon saya 021 8273467')
print(mo.group())