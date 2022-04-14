class Book:
	def __init__(this, link, rating, date):
		this.link = link
		this.rating = rating
		this.id = link[link.rfind("/")+1:]
		this.full_link = link
		this.date = date
		this.name = None
		this.ISBN = None
		this.cover = ""
		this.author = ""
	
	def __str__(this):
		try:
			return 'id="%s", link="%s", rating="%s", name="%s", isbn="%s"' % (this.id, this.link, this.rating, this.date, this.name, this.ISBN)
		except:
			print("oops")
		return 'id=%s' % (this.id)	

	def add_isbn(this, isbn):
		this.ISBN = isbn

	def add_name(this, name):
		this.name = name

	def add_cover(this, cover):
		this.cover = cover
	
	def add_author(this, author):
		this.author = author