txt = 'what.was.that.txt'
def last_dot_kept(s):
    new = s.replace('.', '-dot-', count = s.count('.') - 1)
    return new

print(last_dot_kept(txt))