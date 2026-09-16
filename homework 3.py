def dashify_substring(s, sub):
    new = s.replace(sub, f'-{sub}-', 1)
    return new
print(dashify_substring('foo', 'o'))