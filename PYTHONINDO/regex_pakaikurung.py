import re

no_telp_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d\d\d\d\d)')
mo = no_telp_regex.search('Nomor telpon saya (021) 8273467')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

