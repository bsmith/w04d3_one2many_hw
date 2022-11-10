# Little Books Database

## Diagrams

![diagram.jpg](diagram.jpg)

# Class diagram

```mermaid
classDiagram
Author : int id
Author : str name
Author : str bio
Book : int id
Book : str title
Book : int page_count
Book : bool has_read
Book : int author_id
Author o-- Book
```

## Screenshots

![allbooks.png](allbooks.png)

![deletebook.png](deletebook.png)
