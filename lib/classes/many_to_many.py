class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)
        if self not in author.articles():
            author.articles().append(self)

        if self not in magazine.articles():
            magazine.add_article(self)
        

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author.")
        if self not in value.articles():
            value._articles.append(self)
        self._author = value

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if self not in value.articles():
            value._articles.append(self)
        self._magazine = value

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def magazines(self):
        magazines = {article.magazine for article in self._articles}
        return list(magazines)

    def topic_areas(self):
        if not self._articles:
            return None
        topic_areas = {magazine.category for magazine in self.magazines()}
        return list(topic_areas)

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def contributors(self):
        contributors = {article.author for article in self._articles}
        return list(contributors)

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        max_articles = 0
        top_publisher = None

        for magazine in cls.all:
            num_articles = len(magazine.articles())
            if num_articles > max_articles:
                max_articles = num_articles
                top_publisher = magazine

        return top_publisher