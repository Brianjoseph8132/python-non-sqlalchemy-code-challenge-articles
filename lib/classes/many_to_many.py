class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self,"title"):ArithmeticError("Title can't be changed after creation")
        else:
            if isinstance(title,str):
                if 5 <= len(title) <= 50:
                    self._title = title
                else:ValueError("Must be 5 to 50 characters")
            else:TypeError("Must be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be of type Magazine")


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) and len(name) <= 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, '_name'):
            return AttributeError("Name cannot be changed after the author is instantiated.")
        
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Author name must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles())) if self.articles() else None


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                return ValueError("Name must be a string between 2 and 16 characters")
        
        else:
            return TypeError("Name must be a string") 
            

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category.strip()) > 0:
                self._category = new_category
            else:
                return ValueError("Category must be longer than 0 characters")
        else:
            return TypeError("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        authors = [author for author, count in author_counts.items() if count > 2]
        return authors if authors else None


author1 = Author("Brian Joseph")
author2 = Author("Irene Joseph")

magazine1 = Magazine("Tech Digest", "Technology")
magazine2 = Magazine("Health is wealth", "Health")

article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine1, "Quantum Computing Basics")
article3 = author2.add_article(magazine2, "Healthy Living Tips")
article4 = author1.add_article(magazine2, "Nutrition Myths Debunked")

print(f"Articles by {author1.name}: {[article.title for article in author1.articles()]}")
print(f"Articles by {author2.name}: {[article.title for article in author2.articles()]}")
print(f"Magazines by {author1.name}: {[magazine.name for magazine in author1.magazines()]}")
print(f"Contributors to {magazine1.name}: {[author.name for author in magazine1.contributors()]}")
print(f"Titles in {magazine2.name}: {magazine2.article_titles()}")
