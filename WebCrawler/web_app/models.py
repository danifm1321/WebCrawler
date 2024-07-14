class NewsEntry():
    """
    Represents a news entry with the attributes number, title, points, and number of comments.
    """

    number = 0
    title = ''
    points = 0
    number_of_comments = 0

    def __init__(self, number, title, points, number_of_comments):
        """
        Initializes a NewsEntry instance with specified attributes.

        Args:
            number (int): The number of the news entry.
            title (str): The title of the news entry.
            points (int): The points of the news entry.
            number_of_comments (int): The number of comments on the news entry.
        """
        self.number = int(number)
        self.title = title
        self.points = int(points)
        self.number_of_comments = int(number_of_comments)

    @classmethod
    def from_dict(cls, data):
        """
        Creates a NewsEntry instance from a dictionary.

        Args:
            data (dict): A dictionary containing 'number', 'title', 'points', and 'number_of_comments' keys.

        Returns:
            NewsEntry: An instance of NewsEntry initialized with data from the dictionary.
        """
        return cls(
            number=int(data['number']),
            title=data['title'],
            points=int(data['points']),
            number_of_comments=int(data['number_of_comments'])
        )
    
    def __eq__(self, other):
        """
        Compares two NewsEntry objects for equality.

        Args:
            other (NewsEntry): The other NewsEntry object to compare against.

        Returns:
            bool: True if both objects have the same attributes (number, title, points, number_of_comments), False otherwise.
        """
        if not isinstance(other, NewsEntry):
            return NotImplemented
        
        return (
            self.number == other.number and
            self.title == other.title and
            self.points == other.points and
            self.number_of_comments == other.number_of_comments
        )