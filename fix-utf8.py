import re

with open(r'c:\Users\himan\OneDrive\Desktop\SAPXG\register.html', 'rb') as f:
    content = f.read()

content = re.sub(b'<a class="register-back" href="index.html#training">.*?</a>', b'<a class="register-back" href="index.html#training">&larr; Back to Training</a>', content)

with open(r'c:\Users\himan\OneDrive\Desktop\SAPXG\register.html', 'wb') as f:
    f.write(content)
