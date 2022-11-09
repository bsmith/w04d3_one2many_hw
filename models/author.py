class Author:
    def __init__(self, name, bio, id = None):
        self.name = name
        self.bio = bio
        self.id = id

    def __repr__(self):
        bio_abbrev = repr(self.bio)
        if len(self.bio) > 10:
            bio_abbrev = repr(self.bio[0:7]) + '...'
        return f"Author({self.name!r}, {bio_abbrev}, id={self.id!r})"
 