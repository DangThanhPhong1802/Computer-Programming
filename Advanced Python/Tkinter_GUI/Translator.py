import googletrans
from googletrans import Translator
t=Translator()
a= t.translate("Bạn rất đẹp", src="vi", dest="en")
print(a.text)